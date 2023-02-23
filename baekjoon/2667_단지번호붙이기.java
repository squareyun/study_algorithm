/**
 * TITLE: 단지번호붙이기
 * LEVEL: Silver 1
 * TAG: bfs, graph
 * DATE: 20230223
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Queue;

public class BOJ_2667 {

	static int N;
	static int[][] map;

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		map = new int[N][N];

		for (int i = 0; i < N; i++) {
			String[] s = br.readLine().split("");
			for (int j = 0; j < N; j++) {
				map[i][j] = s[j].charAt(0) - '0';
			}
		}

		int[] dx = { 0, 0, -1, 1 };
		int[] dy = { 1, -1, 0, 0 };
		ArrayList<Integer> ans = new ArrayList<>();
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (map[i][j] != 1)
					continue;

				Queue<Pos> q = new ArrayDeque<>();
				q.offer(new Pos(i, j));
				map[i][j] = 0;

				int cnt = 0;
				while (!q.isEmpty()) {
					Pos cur = q.poll();
					cnt++;
					for (int d = 0; d < 4; d++) {
						int nx = cur.x + dx[d];
						int ny = cur.y + dy[d];
						if (nx < 0 || nx >= N || ny < 0 || ny >= N)
							continue;
						if (map[nx][ny] != 1)
							continue;
						q.offer(new Pos(nx, ny));
						map[nx][ny] = 0;
					}
				}
				ans.add(cnt);
			}
		}
		Collections.sort(ans);
		System.out.println(ans.size());
		for (int a : ans) {
			System.out.println(a);
		}
	}

	static class Pos {
		int x, y;

		public Pos(int x, int y) {
			super();
			this.x = x;
			this.y = y;
		}

	}
}
