/**
 * TITLE: 달팽이2
 * LEVEL: Bronze 1
 * TAG: simulation
 * DATE: 20230214
 */

import java.util.Scanner;

public class BOJ_1952 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int M = sc.nextInt();
		int N = sc.nextInt();
		
		int[][] graph = new int [M][N];
		int[] dx = {0, 1, 0, -1};
		int[] dy = {1, 0, -1, 0};
		
		int dir = 0;
		int cnt = 1;
		int exitCnt = M * N;
		int ans = 0;
		int x = 0, y = -1;
		while (cnt <= exitCnt) {
			int nx = x + dx[dir];
			int ny = y + dy[dir];
			
			if (nx < 0 || nx >= M || ny < 0 || ny >= N || graph[nx][ny] > 0) {
				dir = (dir + 1) % 4;
				ans += 1;
				continue;
			}
			
			graph[nx][ny] = cnt++;
			x = nx;
			y = ny;
		}
		
		System.out.println(ans);
	}

}
