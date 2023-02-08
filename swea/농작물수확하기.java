/* TITLE: 농작물 수확하기 (2805)
** LEVEL: D3
** TAG: implementation
** DATE: 20230208
*/

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

class Solution {
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for(int test_case = 1; test_case <= T; test_case++)
		{
			int N = Integer.parseInt(br.readLine());
			int[][] arr = new int[N][N];
			int answer = 0;
			
			for (int i=0; i<N; i++) {
				String s = br.readLine();
				for (int j=0; j<N; j++) {
					arr[i][j] =  s.charAt(j) - '0';
				}
			}
			
			int mid = N / 2;
			for (int i = mid, t = 0; i >= 0; i--, t++) {
				for (int j = t; j < N-t; j++) {
					answer += arr[i][j];
				}
			}
			
			for (int i = mid+1, t = 1; i < N; i++, t++) {
				for (int j = t; j < N-t; j++) {
					answer += arr[i][j];
				}
			}
			
			System.out.printf("#%d %d\n", test_case, answer);
		}
	}

}
