/* TITLE: Ladder1 (1210)
** LEVEL: D4
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
		int T = 10;
		for(int test_case = 1; test_case <= T; test_case++)
		{
			br.readLine();
			int[][] map = new int[100][100];
			
			StringTokenizer st;
			for (int i=0; i<100; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j=0; j<100; j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
			int[][] dir = {{0, 1}, {0, -1}, {-1, 0}}; //오른쪽, 왼쪽, 위 (위로 가는 우선순위가 제일 낮게 해야함)
			
			// 뒤에서 부터 올라옴
			int r = 99;
			int c = 0;
			int d = 0;
			for (int i=0; i<100; i++) {
				if (map[99][i] == 2) {
					c = i;
					break;
				}
			}
			
			
			while (true) {
				if (r == 0) {
					break;
				}
				
				for (int i=0; i<3; i++) {
					int nr = r + dir[i][0];
					int nc = c + dir[i][1];
					
					if (nr < 0 || nr >= 100 || nc < 0 || nc >= 100)
						continue;
					
					if (map[nr][nc] == 1) {
						map[nr][nc] = 3;
						r = nr;
						c = nc;
					}
				}
			}
			
			System.out.printf("#%d %d\n", test_case, c);
		}
	}

}
