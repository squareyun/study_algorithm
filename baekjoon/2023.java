/**
 * TITLE: 신가한 소수
 * LEVEL: Gold 5
 * TAG: backtracking, prime, math
 * DATE: 20230209
 */

import java.util.Scanner;

public class BOJ_2023 {

	static int N;
	static String num ;
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		

		int[] bases = {2,3,5,7};
		for (int base : bases) {
			num = String.valueOf(base);
			dfs(1);
		}
		System.out.println(sb.toString());
	}
	
	private static void dfs(int cnt) {
		if (!isPrime(Integer.valueOf(num))) {
			return;
		}
		
		if (cnt == N) {
			if (isPrime(Integer.valueOf(num))) {
				sb.append(num).append("\n");
			}
			return;
		}
		
		for (int i=0; i<10; i++) {
			num += String.valueOf(i);
			dfs(cnt + 1);
			num = num.substring(0, num.length()-1);
		}
	}

	private static boolean isPrime(int num) {
		for (int i=2; i*i <= num; i++)
			if (num % i == 0)
				return false;
		return true;
	}
}
