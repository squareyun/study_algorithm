/* TITLE: 백설 공주와 일곱 난쟁이
** LEVEL: Bronze 2
** TAG: combination, recursion
** DATE: 20230208
*/

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int[] arr = new int[9];
		
		int total = 0;
		for (int i=0; i<9; i++) {
			arr[i] = Integer.parseInt(br.readLine());
			total += arr[i];
		}
		
		for (int i=0; i<9; i++) {
			for (int j=i+1; j<9; j++) {
				int result = total - (arr[i] + arr[j]);
				if (result == 100) {
					for (int k=0; k<9; k++) {
						if (k == i || k == j)
							continue;
						System.out.println(arr[k]);
					}
					break;
				}
			}
		}
		
	}
}
