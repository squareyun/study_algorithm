/**
 * TITLE: 암호 만들기
 * LEVEL: Gold 5
 * TAG: backtracking
 * DATE: 20230221
 */

import java.util.Arrays;
import java.util.Scanner;

public class BOJ_1759 {

    static int L, C;
    static char[] arr;
    static char[] brr;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        L = sc.nextInt();
        C = sc.nextInt();
        arr = new char[C];
        brr = new char[L];
        for (int i = 0; i < C; i++) {
            arr[i] = sc.next().charAt(0);
        }
        Arrays.sort(arr);

        dfs(0, 0);
        System.out.println(sb);
    }

    private static void dfs(int cnt, int start) {
        if (cnt == L) {
            int aeiou = 0;
            StringBuilder sb2 = new StringBuilder();
            for (char b : brr) {
                switch (b) {
                    case 'a':
                    case 'e':
                    case 'i':
                    case 'o':
                    case 'u':
                        aeiou++;
                        break;
                }
                sb2.append(b);
            }
            // 모음 하나 이상, 자음 두 개 이상
            if (aeiou >= 1 && (L - aeiou) >= 2) {
                sb.append(sb2).append('\n');
            }
            return;
        }

        for (int i = start; i < C; i++) {
            brr[cnt] = arr[i];
            dfs(cnt + 1, i + 1);
        }
    }
}
