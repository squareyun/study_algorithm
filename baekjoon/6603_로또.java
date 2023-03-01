/**
 * TITLE: 로또
 * LEVEL: Silver 2
 * TAG: combinatorics
 * DATE: 20230301
 */

import java.util.Scanner;

public class BOJ_6603 {

    static int N;
    static int[] arr;
    static int[] brr;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        while ((N = sc.nextInt()) != 0) {
            arr = new int[N];
            brr = new int[6];

            for (int i = 0; i < N; i++) {
                arr[i] = sc.nextInt();
            }

            dfs(0, 0);
            sb.append("\n");
        }
        System.out.println(sb);
    }

    public static void dfs(int cnt, int start) {
        if (cnt == 6) {
            for (int i = 0; i < 6; i++) {
                sb.append(brr[i]).append(' ');
            }
            sb.append("\n");
            return;
        }

        for (int i = start; i < N; i++) {
            brr[cnt] = arr[i];
            dfs(cnt + 1, i + 1);
        }
    }
}
