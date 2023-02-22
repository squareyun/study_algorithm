/**
 * TITLE: 최적 경로
 * LEVEL: D5
 * TAG: combinatorics
 * DATE: 20230222
 */

import java.util.Scanner;

public class SWEA_1247 {

    static int N, sx, sy, tx, ty, answer;
    static int[][] arr;
    static int[][] brr;
    static boolean[] v;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int tc = 1; tc <= T; tc++) {
            answer = Integer.MAX_VALUE;

            N = sc.nextInt();
            sx = sc.nextInt();
            sy = sc.nextInt();
            tx = sc.nextInt();
            ty = sc.nextInt();
            arr = new int[N][2];
            brr = new int[N][2];
            v = new boolean[N];
            for (int i = 0; i < N; i++) {
                arr[i][0] = sc.nextInt();
                arr[i][1] = sc.nextInt();
            }
            dfs(0);
            System.out.printf("#%d %d\n", tc, answer);
        }
    }

    private static void dfs(int cnt) {
        if (cnt == N) {
            int dist = 0;
            dist += Math.abs(sx - brr[0][0]) + Math.abs(sy - brr[0][1]);
            for (int i = 0; i < N - 1; i++) {
                dist += Math.abs(brr[i][0] - brr[i + 1][0]) + Math.abs(brr[i][1] - brr[i + 1][1]);
            }
            dist += Math.abs(tx - brr[N - 1][0]) + Math.abs(ty - brr[N - 1][1]);
            answer = Math.min(answer, dist);
            return;
        }

        for (int i = 0; i < N; i++) {
            if (v[i]) {
                continue;
            }
            v[i] = true;
            brr[cnt][0] = arr[i][0];
            brr[cnt][1] = arr[i][1];
            dfs(cnt + 1);
            v[i] = false;
        }

    }
}