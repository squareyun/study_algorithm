/**
 * TITLE: Z
 * LEVEL: Silver 1
 * TAG: divide_and_conquer
 * DATE: 20230221
 */

import java.util.Scanner;

public class BOJ_1074 {

	static int N, tr, tc, cnt;
	static boolean flag;
	
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		
		N = sc.nextInt();
		tr = sc.nextInt();
		tc = sc.nextInt();
		int N2N = (int)Math.pow(2, N);
		solve(0, 0, N2N);
		System.out.println(cnt);
	}
	
	private static void solve(int r, int c, int size) {
		if (r == tr && c == tc) {
			flag = true;
			return;
		}
		
		if (size == 1) {
			cnt += 1;
			return;
		}
		
		if (!(r <= tr && tr <= r+size) || !(c <= tc && tc <= c+size)) {
			cnt += size * size;
			return;
		}
		
		int half = size / 2;
		if(!flag) solve(r, c, half);
		if(!flag) solve(r, c+half, half);
		if(!flag) solve(r+half, c, half);
		if(!flag) solve(r+half, c+half, half);
	}

}
