/**
 * TITLE: 빵집
 * LEVEL: Gold 2
 * TAG: dfs, recursion
 * DATE: 20230222
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_3109 {

	static int R, C;
	static int[][] map;
	static int[] dx = {-1, 0, 1};
	static int[] dy = {1, 1, 1};
	static int cnt = 0;
	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		map = new int[R+2][C+2];
		for (int i=1; i<=R; i++) {
			String[] s = br.readLine().split("");
			for (int j=1; j<=C; j++) {
				map[i][j] = (s[j-1].charAt(0) == '.') ? 1 : 0;
			}
		}
		
		for (int r=1; r<=R; r++) {
			if (dfs(r, 1))
				cnt++;
		}
		
		System.out.println(cnt);
	}
	

	// 0: 벽, 1: 이동가능, 2: 이미 방문
	public static boolean dfs(int x, int y) {		
		map[x][y] = 2;
		
		if (y == C) {
			return true;
		}
		
		for (int d=0; d<3; d++) {
			int nx = x + dx[d];
			int ny = y + dy[d];
			if (map[nx][ny] == 1) {
				if (dfs(nx, ny)) {
					return true;
				}
			}
		}
		return false;
	}

//	private static void printmap(int r) {
//		System.out.println("===="+r+"====");
//		for (int i=1; i<=R; i++) {
//			for (int j=1; j<=C; j++) {
//				System.out.print(map[i][j]);
//			}
//			System.out.println();
//		}
//		System.out.println();
//	}
}
