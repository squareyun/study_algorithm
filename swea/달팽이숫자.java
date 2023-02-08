/* TITLE: 달팽이 숫자 (1954)
** LEVEL: D2
** TAG: implementation
** DATE: 20230208
*/

import java.util.Scanner;

class Solution {
	
	public static void main(String[] args) throws Exception {
		
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int test_case=1; test_case<=T; test_case++) {
			System.out.printf("#%d\n", test_case);
			
			int N = sc.nextInt();
			int[][] arr = new int[N][N];
			int cnt = 1;
			int cntMax = N*N;
			
			int[][] dir = {{0,1},{1,0}, {0,-1},{-1,0}}; // 오른쪽, 왼쪽, 아래쪽, 위쪽
			int r = 0;
			int c = 0;
			int d = 0;
			while (true) {
				if (arr[r][c] == 0)
					arr[r][c] = cnt;
				
				if (cnt == cntMax)
					break;
				
				int nr = r + dir[d][0];
				int nc = c + dir[d][1];
				
				if (nr < 0 || nr >= N || nc < 0 || nc >= N || arr[nr][nc] != 0) {
					d = (d + 1) % 4;
					continue;
				}
				
				r = nr;
				c = nc;
				cnt += 1;
			}
			
			StringBuilder sb = new StringBuilder();
			for (int i=0; i<N; i++) {
				for (int j=0; j<N; j++) {
					sb.append(arr[i][j] + " ");
				}
				if (i != N-1)
					sb.append("\n");
			}
			System.out.println(sb.toString());
		}
	}

}
