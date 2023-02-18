/**
 * TITLE: 팰린드롬 만들기
 * LEVEL: Silver 3
 * TAG: greedy
 * DATE: 20230218
 */

import java.util.Arrays;
import java.util.Scanner;

public class BOJ_1213 {

    static char[] s;
    static char[] answer;
    static int[] dict;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        s = sc.next().toCharArray();
        answer = Arrays.copyOf(s, s.length);
        Arrays.sort(s);
        dict = new int[27];
        for (char c : s) {
            dict[c - 'A']++;
        }

        solve();
    }

    private static void solve() {
        int idx = 0;
        if (s.length % 2 == 0) {
            for (int i = 0; i < s.length; i++) {
                int a = s[i] - 'A';
                if (dict[a] == 0) {
                    continue;
                }
                while (dict[a]-- > 0) {
                    answer[idx] = s[i];
                    if (dict[a] == 0) {
                        System.out.println("I'm Sorry Hansoo");
                        return;
                    }
                    answer[s.length - idx - 1] = s[i];
                    dict[a]--;
                    idx++; i++;
                }
            }
        } else {
            int oddAlpha = -1;
            for (int i = 0; i < s.length; i++) {
                int a = s[i] - 'A';
                if (dict[a] == 0)
                    continue;
                if (dict[a] % 2 == 1) {
                    if (oddAlpha != -1) { // 홀수인 알파벳이 2개 이상 되는 경우
                        System.out.println("I'm Sorry Hansoo");
                        return;
                    }
                    oddAlpha = s[i];
                    break;
                }
            }

            for (int i = 0; i < s.length; i++) {
                if (s[i] == oddAlpha && dict[s[i]-'A'] == 1) continue;
                int a = s[i] - 'A';
                if (dict[a] == 0) {
                    continue;
                }
                while (dict[a]-- > 0) {
                    answer[idx] = s[i];
                    if (dict[a] == 0) {
                        System.out.println("I'm Sorry Hansoo");
                        return;
                    }
                    answer[s.length - idx - 1] = s[i];
                    dict[a]--;
                    idx++;
                    i++;
                    if (s[i] == oddAlpha && dict[a] == 1) {
                        i++;
                        break;
                    }
                }
            }
            answer[s.length/2] = (char)oddAlpha; // 중간에 넣기
        }
        StringBuilder sb = new StringBuilder();
        for (char c : answer)
            sb.append(c);
        System.out.println(sb);
    }

}
