/**
 * TITLE: 보급로
 * LEVEL: D4
 * TAG: bfs, dp?
 * DATE: 20230304
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;

public class SWEA_1249 {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            int N = Integer.parseInt(br.readLine());
            int[][] map = new int[N][N];
            int[][] cost = new int[N][N];
            for (int i = 0; i < N; i++) {
                String[] input = br.readLine().split("");
                for (int j = 0; j < N; j++) {
                    map[i][j] = input[j].charAt(0) - '0';
                }
            }

            Queue<Pos> q = new ArrayDeque<>();
            boolean[][] v = new boolean[N][N];
            q.offer(new Pos(0, 0));
            v[0][0] = true;

            int[] dx = {0, 0, 1, -1};
            int[] dy = {1, -1, 0, 0};

            int ans = Integer.MAX_VALUE;
            while (!q.isEmpty()) {
                Pos cur = q.poll();

                if (cur.x == N - 1 && cur.y == N - 1) {
                    ans = Math.min(ans, cost[N-1][N-1]);
                    continue;
                }

                for (int d = 0; d < 4; d++) {
                    int nx = cur.x + dx[d];
                    int ny = cur.y + dy[d];

                    if (nx < 0 || nx >= N || ny < 0 || ny >= N) {
                        continue;
                    }

                    if (!v[nx][ny] || cost[nx][ny] > cost[cur.x][cur.y] + map[nx][ny]) {
                        v[nx][ny] = true;
                        cost[nx][ny] = cost[cur.x][cur.y] + map[nx][ny];
                        q.offer(new Pos(nx, ny));
                    }
                }
            }

            System.out.println("#" + tc + " " + ans);

        }
    }

    static class Pos {

        int x, y;

        public Pos(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
