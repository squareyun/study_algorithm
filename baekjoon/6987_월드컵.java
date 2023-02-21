/**
 * TITLE: 월드
 * LEVEL: Gold 5
 * TAG: backtracking
 * DATE: 20230221
 */

import java.util.Scanner;

public class BOJ_6987 {

    static int[][] arr;
    static int[] A = {0,0,0,0,0,1,1,1,1,2,2,2,3,3,4};
    static int[] B = {1,2,3,4,5,2,3,4,5,3,4,5,4,5,5};
    static boolean isPossible;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        arr = new int[6][3];
        for (int tc = 0; tc < 4; tc++) {
            int cnt = 0;
            for (int i = 0; i < 6; i++) {
                for (int j = 0; j < 3; j++) {
                    arr[i][j] = sc.nextInt();
                    cnt += arr[i][j];
                }

            }

            if (cnt != 30) { // 한 팀당 5번 경기 필수
            }
            else {
                isPossible = false;
                dfs(0);
            }

            String ans = (isPossible) ? "1 " : "0 ";
            System.out.print(ans);
        }

    }

    private static void dfs(int game) {
        if (isPossible) {
            return;
        }

        if (game == 15) { // 최대 경기 횟수는 15회이다. 이 경우 가능
            isPossible = true;
            return;
        }

        // 경기 진행할 두 팀
        int a = A[game];
        int b = B[game];

        // a 승리
        if (arr[a][0] > 0 && arr[b][2] > 0) {
            arr[a][0]--; arr[b][2]--;
            dfs(game + 1);
            arr[a][0]++; arr[b][2]++;
        }

        // b 승리
        if (arr[a][2] > 0 && arr[b][0] > 0) {
            arr[a][2]--; arr[b][0]--;
            dfs(game + 1);
            arr[a][2]++; arr[b][0]++;
        }

        // 무승부
        if (arr[a][1] > 0 && arr[b][1] > 0) {
            arr[a][1]--; arr[b][1]--;
            dfs(game + 1);
            arr[a][1]++; arr[b][1]++;
        }
    }

}
