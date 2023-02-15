/**
 * TITLE: 색종이
 * LEVEL: Silver 5
 * TAG: implementation
 * DATE: 20230215
 */

import java.util.Scanner;

public class BOJ_2563 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[][] arr = new int[101][101];
		
		for (int tc=0; tc<N; tc++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			for (int i=b; i<b+10; i++) {
				for (int j=a; j<a+10; j++) {
					if (arr[i][j] != 1)
						arr[i][j] = 1;
				}
			}
		}
		
		int res = 0;
		for (int i=0; i<101; i++) {
			for (int j=0; j<101; j++) {
				res += arr[i][j];
			}
		}
		System.out.println(res);
	}

}
