/**
 * TITLE: 색종이 만들기
 * LEVEL: Silver 2
 * TAG: divide_and_conquer
 * DATE: 20230209
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_2630 {

	static int N, white, blue;
	static int[][] arr;
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		arr = new int[N][N];
		for (int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int j=0; j<N; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		cut(0, 0, N);
		System.out.println(white);
		System.out.println(blue);
	}

	private static void cut(int r, int c, int size) {
		
		int sum = 0;
		for (int i=r, rEnd = r+size; i<rEnd; i++) {
			for (int j=c, cEnd = c+size; j<cEnd; j++) {
				sum += arr[i][j];
			}
		}
		
		if (sum == size*size) {
			blue++;
		} else if(sum == 0) {
			white++;
		} else {
			int half = size / 2;
			cut(r, c, half);
			cut(r, c+half, half);
			cut(r+half, c, half);
			cut(r+half, c+half, half);
		}
		
	}

}
