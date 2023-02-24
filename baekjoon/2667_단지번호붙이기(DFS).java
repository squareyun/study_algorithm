/**
 * TITLE: 단지번호붙이기
 * LEVEL: Silver 1
 * TAG: dfs, graph
 * DATE: 20230224
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

public class BOJ_2667DFS {

	static int N, cnt;
	static int[][] map;
	static boolean[][] v;
	static int[] dx;
	static int[] dy;

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		map = new int[N][N];
		v = new boolean[N][N];

		for (int i = 0; i < N; i++) {
			String[] s = br.readLine().split("");
			for (int j = 0; j < N; j++) {
				map[i][j] = s[j].charAt(0) - '0';
			}
		}

		dx = new int[] { 0, 1, 0, -1 };
		dy = new int[] { 1, 0, -1, 0 };

		ArrayList<Integer> ans = new ArrayList<>();
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (!v[i][j] && map[i][j] != 0) {
					cnt = 0;
					dfs(i, j);
					ans.add(cnt);
				}
			}
		}
		Collections.sort(ans);
		System.out.println(ans.size());
		for (int a : ans) {
			System.out.println(a);
		}
	}

	private static void dfs(int x, int y) {

		v[x][y] = true;
		cnt += 1;

		int nx, ny;
		for (int d = 0; d < 4; d++) {
			nx = x + dx[d];
			ny = y + dy[d];
			if (nx < 0 || nx >= N || ny < 0 || ny >= N) {
				continue;
			}
			if (v[nx][ny]) {
				continue;
			}
			if (map[nx][ny] == 0) {
				continue;
			}
			dfs(nx, ny);
		}
	}
}
