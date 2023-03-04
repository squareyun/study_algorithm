/**
 * TITLE: 미세먼지 안녕!
 * LEVEL: Gold 4
 * TAG: simulation
 * DATE: 20230304
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_17144 {

    static int R, C, T, ax;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        T = Integer.parseInt(st.nextToken());
        int[][] map = new int[R][C];
        ax = -1; // 공기청정기 윗 부분의 x좌표

        for (int i = 0; i < R; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < C; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if (map[i][j] == -1 && ax == -1) {
                    ax = i;
                }
            }
        }

        while (T-- > 0) {
            // 미세먼지 확산
            map = spread(map);
//            print(map);

            // 공기청정기 작동
            map = air(map);
//            print(map);
        }

        int ans = 0;
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                ans += map[i][j];
            }
        }
        ans += 2; // 공기 청정기
        System.out.println(ans);
    }

    private static int[][] air(int[][] map) {

        // 윗부분 돌리기 방향 순서
        int[] dx = {0, -1, 0, 1};
        int[] dy = {1, 0, -1, 0};
        int d = 0;
        int x = ax, y = 1;
        int prev = map[ax][1];
        map[ax][1] = 0;
        while (true) {
            int nx = x + dx[d];
            int ny = y + dy[d];

            if (nx == ax && ny == 0) {
                break;
            }

            if (nx < 0 || nx >= R || ny < 0 || ny >= C) {
                d = (d + 1) % 4;
                continue;
            }

            int temp = map[nx][ny];
            map[nx][ny] = prev;
            prev = temp;
            x = nx;
            y = ny;
        }

        // 아래부분 돌리기
        dx = new int[]{0, 1, 0, -1};
        dy = new int[]{1, 0, -1, 0};
        d = 0;
        x = ax + 1;
        y = 1;
        prev = map[ax + 1][1];
        map[ax + 1][1] = 0;
        while (true) {
            int nx = x + dx[d];
            int ny = y + dy[d];

            if (nx == ax + 1 && ny == 0) {
                break;
            }

            if (nx < 0 || nx >= R || ny < 0 || ny >= C) {
                d = (d + 1) % 4;
                continue;
            }

            int temp = map[nx][ny];
            map[nx][ny] = prev;
            prev = temp;
            x = nx;
            y = ny;
        }

        return map;
    }

    private static void print(int[][] map) {
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                System.out.print(map[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println("---");
    }

    private static int[][] spread(int[][] map) {
        int[][] newMap = new int[R][C];
        int[] dx = {-1, 0, 1, 0};
        int[] dy = {0, 1, 0, -1};

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (map[i][j] <= 0) {
                    continue;
                }

                int cnt = 0; // 확산된 방향의 개수
                for (int d = 0; d < 4; d++) {
                    int nx = i + dx[d];
                    int ny = j + dy[d];

                    if (nx < 0 || nx >= R || ny < 0 || ny >= C) {
                        continue;
                    }

                    if (map[nx][ny] == -1) {
                        continue;
                    }

                    newMap[nx][ny] += map[i][j] / 5;
                    cnt++;
                }
                newMap[i][j] += map[i][j] - (map[i][j] / 5) * cnt;
            }
        }
        newMap[ax][0] = -1;
        newMap[ax + 1][0] = -1;
        return newMap;
    }
}
