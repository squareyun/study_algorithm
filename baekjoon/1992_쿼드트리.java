/**
 * TITLE: 쿼드트리
 * LEVEL: Silver 1
 * TAG: divide_and_conquer
 * DATE: 20230221
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class BOJ_1992 {

	static int N;
	static int[][] arr;
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		arr = new int[N][N];
		for (int i=0; i<N; i++) {
			String input = br.readLine();
			for (int j=0; j<N; j++) {
				arr[i][j] = input.charAt(j) == '0' ? 0 : 1;
			}
		}
		// 입력끝
		
		solve(0, 0, N);
		System.out.println(sb);
	}

	private static void solve(int r, int c, int size) {
		int cnt = 0;
		for (int i=r, rEnd=r+size; i<rEnd; i++) {
			for (int j=c, cEnd=c+size; j<cEnd; j++) {
				cnt += arr[i][j];
			}
		}
		
		if (cnt == size*size) {
			sb.append(1);
		} else if (cnt == 0) {
			sb.append(0);
		} else {
			int half = size / 2;
			sb.append('(');
			solve(r, c, half);
			solve(r, c+half, half);
			solve(r+half, c, half);
			solve(r+half, c+half, half);
			sb.append(')');
		}
		
	}

}
