/**
 * TITLE: 알파벳
 * LEVEL: Gold 4
 * TAG: dfs, graph
 * DATE: 20230224
 */

import java.util.Scanner;

public class BOJ_1987 {

	static int R, C;
	static int[] dx = {0, 1, 0, -1};
	static int[] dy = {1, 0, -1, 0};
	static int[][] map;
	static boolean[][] v;
	static int[] alpha;
	static int answer = -1;
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		R = sc.nextInt();
		C = sc.nextInt();
		map = new int[R][C];
		v = new boolean[R][C];
		alpha = new int[28];
		for (int i=0; i<R; i++) {
			String[] input = sc.next().split("");
			for (int j=0; j<C; j++) {
				map[i][j] = input[j].charAt(0) - 'A';
			}
		}
		
		dfs(0, 0, 1);
		System.out.println(answer);
	}

	private static void dfs(int x, int y, int cnt) {
		alpha[map[x][y]]++;
		answer = Math.max(answer, cnt);
		
		int nx, ny;
		for (int d=0; d<4; d++) {
			nx = x + dx[d];
			ny = y + dy[d];
			
			if (nx < 0 || nx >= R || ny < 0 || ny >= C) {
				continue;
			}
			if (alpha[map[nx][ny]] != 0) {
				continue;
			}
			dfs(nx, ny, cnt + 1);
			alpha[map[nx][ny]]--;
		}
	}
}
