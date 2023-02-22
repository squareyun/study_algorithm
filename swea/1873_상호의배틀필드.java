/**
 * TITLE: 상호의배틀필드
 * LEVEL: D3
 * TAG: simulation
 * DATE: 20230222
 */

import java.util.Scanner;

public class SWEA_1873 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int x = 0;
		int y = 0;
		int[] dx = {-1, 1, 0, 0};
		int[] dy = {0, 0, -1, 1};
		int T = sc.nextInt();
		int d = 0;
		for (int tc = 1; tc <= T; tc++) {
			StringBuilder sb = new StringBuilder();
			int H = sc.nextInt();
			int W = sc.nextInt();
			char[][] map = new char[H + 2][W + 2];
			for (int i=0; i<H+2; i++) {
				for (int j=0; j<W+2; j++) {
					map[i][j] = '0';
				}
			}
			
			for (int i = 1; i <= H; i++) {
				String[] s = sc.next().split("");
				for (int j = 1; j <= W; j++) {
					map[i][j] = s[j-1].charAt(0);
					switch (map[i][j]) {
					case '^':
						d = 0;
						x = i; y = j;
						break;
					case 'v':
						d = 1;
						x = i; y = j;
						break;
					case '<':
						d = 2;
						x = i; y = j;
						break;
					case '>':
						d = 3; 
						x = i; y = j;
						break;
					}
				}
			}
			
			int N = sc.nextInt();
			char[] cmd = new char[N];
			String[] s = sc.next().split("");
			for (int i = 0; i < N; i++)
				cmd[i] = s[i].charAt(0);
			// 입력 끝
			
			int nx = 0;
			int ny = 0;
			for (char c : cmd) {
				switch(c) {
				case 'U':
					d = 0;
					nx = x + dx[d];
					ny = y + dy[d];
					if (map[nx][ny] == '.') {
						map[x][y] = '.';
						map[nx][ny] = '^';
						x = nx;
						y = ny;
					} else {
						map[x][y] = '^';
					}
					break;
				case 'D':
					d = 1;
					nx = x + dx[d];
					ny = y + dy[d];
					if (map[nx][ny] == '.') {
						map[x][y] = '.';
						map[nx][ny] = 'v';
						x = nx;
						y = ny;
					} else {
						map[x][y] = 'v';
					}
					break;
				case 'L':
					d = 2;
					nx = x + dx[d];
					ny = y + dy[d];
					if (map[nx][ny] == '.') {
						map[x][y] = '.';
						map[nx][ny] = '<';
						x = nx;
						y = ny;
					} else {
						map[x][y] = '<';
					}
					break;
				case 'R':
					d = 3;
					nx = x + dx[d];
					ny = y + dy[d];
					if (map[nx][ny] == '.') {
						map[x][y] = '.';
						map[nx][ny] = '>';
						x = nx;
						y = ny;
					} else {
						map[x][y] = '>';
					}
					break;
				case 'S':
					int tx = x;
					int ty = y;
					while (true) {
						nx = tx + dx[d];
						ny = ty + dy[d];
						if (map[nx][ny] == '0' || map[nx][ny] == '#') {
							break;
						}
						
						if (map[nx][ny] == '*') {
							map[nx][ny] = '.';
							break;
						}
						tx = nx; ty = ny;
					}
					break;
				}
			}
			
			sb.append('#').append(tc).append(' ');
			for (int i=1; i<=H; i++) {
				for (int j=1; j<=W; j++) {
					sb.append(map[i][j]);
				}
				if (i!=H) sb.append('\n');
			}
			System.out.println(sb);
		}
	}

}
