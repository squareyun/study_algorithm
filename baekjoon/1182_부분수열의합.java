/**
 * TITLE: 부분수열의 합
 * LEVEL: Silver 2
 * TAG: 부분집합
 * DATE: 20230218
 */

import java.util.Scanner;

public class BOJ_1182 {

    static int N, S, answer;
    static int[] arr;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        S = sc.nextInt();
        answer = 0;
        arr = new int[N];
        for (int i=0; i<N; i++)
            arr[i] = sc.nextInt();
        dfs(0, 0);
        if (S == 0) answer--; // 공집합 고려
        System.out.println(answer);

    }

    private static void dfs(int cnt, int sum) {
        if (cnt == N) {
            if (sum == S)
                answer++;
            return;
        }

        dfs(cnt + 1, sum + arr[cnt]);
        dfs(cnt + 1, sum);
    }
}
