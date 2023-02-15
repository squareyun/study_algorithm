/**
 * TITLE: 섬의 개수
 * LEVEL: Silver 2
 * TAG: bfs
 * DATE: 20230215
 */

import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Scanner;

public class BOJ_4963 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		
		int[] dx = {-1,-1,0,1,1,1,0,-1};
		int[] dy = {0,1,1,1,0,-1,-1,-1};
		
		int w, h;
		while( (w = sc.nextInt()) != 0 && (h = sc.nextInt()) != 0 ) {
			int[][] graph = new int[h+2][w+2];
			boolean[][] visited = new boolean[h+2][w+2];
			
			Queue<Integer[]> q = new ArrayDeque<>();
			for (int i=1; i<=h; i++) {
				for (int j=1; j<=w; j++) {
					graph[i][j] = sc.nextInt();
				}
			}
			
			int cnt = 0;
			for (int i=1; i<=h; i++) {
				for (int j=1; j<=w; j++) {
					if (graph[i][j] == 1 && !visited[i][j]) {
						q.offer(new Integer[] {i, j});
						visited[i][j] = true;
						cnt += 1;
						while (!q.isEmpty()) {
							Integer[] a = q.poll();
							int x = a[0], y = a[1];
							
							
							for (int d=0; d<8; d++) {
								int nx = x + dx[d];
								int ny = y + dy[d];
								
								if (visited[nx][ny])
									continue;
								
								visited[nx][ny] = true;
								
								if (graph[nx][ny] == 1)
									q.offer(new Integer[] {nx, ny});
							}
						}
					}
				}
			}
			
			System.out.println(cnt);
		}
	}

}
