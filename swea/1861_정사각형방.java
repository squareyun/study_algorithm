/**
 * LEVEL: D4
 * TAG: bfs
 * DATE: 20230215
 */

import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Scanner;

public class SWEA_1861 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		int[] dx = new int[]{1, 0, -1, 0};
		int[] dy = new int[] {0, 1, 0, -1};
		
		for (int tc=1; tc<=T; tc++) {
			int res_num = 0;
			int res_cnt = 0;
			
			int N = sc.nextInt();
			int[][] graph = new int[N+2][N+2];
			for (int i=1; i<N+1; i++) {
				for (int j=1; j<N+1; j++) {
					graph[i][j] = sc.nextInt();
				}
			}
			
			for (int i=1; i<N+1; i++) {
				for (int j=1; j<N+1; j++) {
					int t_res_num = graph[i][j];
					int t_res_cnt = 1;
				
					Queue<Pos> q = new ArrayDeque<>();
					q.offer(new Pos(i, j));
					
					while (!q.isEmpty()) {
						Pos cur = q.poll();
						for (int d=0; d<4; d++) {
							int nx = cur.x + dx[d];
							int ny = cur.y + dy[d];
							if (graph[nx][ny] == graph[cur.x][cur.y]+1) {
								q.offer(new Pos(nx, ny));
								t_res_cnt += 1;
							}
						}
					}
					
					if (t_res_cnt > res_cnt) {
						res_num = t_res_num;
						res_cnt = t_res_cnt;
					} else if (t_res_cnt == res_cnt) {
						res_num = Math.min(res_num, t_res_num);
					}
				}
			}
			
			System.out.printf("#%d %d %d\n", tc, res_num, res_cnt);
		}
	}

}

class Pos {
	int x, y;
	public Pos(int x, int y) {
		this.x=x;
		this.y=y;
	}
}
