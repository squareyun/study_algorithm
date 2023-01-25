/* TITLE: 퇴사 2
** LEVEL: Bronze 1
** TAG: implementation
** DATE: 20230125
*/

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		String input = sc.next();
		char[] answer = new char[n];
		boolean isSuccess = true;
		
		for (int i=0; i<n; i++) {
			String stub = input.substring(i*6, i*6+6);
			char ret = solve(stub);
			
			if (ret == 'Z') {
				System.out.println(i+1);
				isSuccess = false;
				break;	
			}
			
			answer[i] = ret;
		}
		
		if (isSuccess) {
			System.out.println(String.valueOf(answer));
		}
		
		sc.close();
	}
	
	static char solve(String stub) {
		String[] code = {"000000", "001111", "010011", "011100", "100110", "101001", "110101", "111010"};
		
		for (int i=0; i<8; i++) {
			int diff = 0;
			for (int j=0; j<6; j++) {
				if (stub.charAt(j) != code[i].charAt(j)) {
					diff++;
				}
			}
			
			if (diff == 0 || diff == 1) { // 일치하거나, 하나만 틀리는 경우
				return (char) ('A' + i);
			}
		}
		return 'Z'; // error code
	}
	
}