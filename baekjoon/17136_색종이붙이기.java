/**
 * TITLE: 색종이 붙이기
 * LEVEL: Gold 2
 * TAG: bruteforce, backtracking
 * DATE: 20230305
 * REFERENCE: https://steady-coding.tistory.com/43
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_17136 {

    static int[][] map = new int[10][10];
    static int[] paper = {0, 5, 5, 5, 5, 5};
    static int ans = Integer.MAX_VALUE;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        for (int i = 0; i < 10; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 10; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        DFS(0, 0, 0);

        if (ans == Integer.MAX_VALUE) {
            ans = -1;
        }
        System.out.println(ans);
    }

    private static void DFS(int x, int y, int cnt) {
        if (x >= 9 && y > 9) { // 다 순회하였을 때
            ans = Math.min(ans, cnt);
            return;
        }

        if (ans <= cnt) { // 백트래킹. 더 볼 필요가 없음
            return;
        }

        if (y > 9) { // 행 바꾸기
            DFS(x + 1, 0, cnt);
            return;
        }

        if (map[x][y] == 1) {
            // 그리디한 방법으로 큰 숫자부터 붙여보기
            for (int i = 5; i >= 1; i--) {
                if (paper[i] > 0 && isAttach(x, y, i)) {
                    attach(x, y, i, 0); // 색종이 붙이기
                    paper[i]--;
                    DFS(x, y + 1, cnt + 1); // 그리디 하긴 하지만 DFS로 한번더 확인
                    paper[i]++;
                    attach(x, y, i, 1); // 색종이 떼기
                }
            }
        } else {
            DFS(x, y + 1, cnt); // 열 바꾸기
        }
    }

    private static void attach(int x, int y, int size, int flag) {
        for (int i = x; i < x + size; i++) {
            for (int j = y; j < y + size; j++) {
                map[i][j] = flag;
            }
        }
    }

    private static boolean isAttach(int x, int y, int size) {
        for (int i = x; i < x + size; i++) {
            for (int j = y; j < y + size; j++) {
                if (i < 0 || i >= 10 || j < 0 || j >= 10) {
                    return false;
                }

                if (map[i][j] != 1) {
                    return false;
                }
            }
        }
        return true;
    }
}
