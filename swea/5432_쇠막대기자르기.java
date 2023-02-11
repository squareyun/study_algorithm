/**
 * TITLE: 쇠막대기 자르기 (https://swexpertacademy.com/main/code/problem/problemSubmitHistory.do?contestProbId=AWVl47b6DGMDFAXm)
 * LEVEL: D4
 * TAG: implementation, string
 * DATE: 20230211
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Solution {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int test_case = 1; test_case <= T; test_case++) {
            int answer = 1;
            String input = br.readLine();
            int stick = 0;
            for (int i = 0; i < input.length() - 1; i++) {
                char c = input.charAt(i);
                char c2 = input.charAt(i+1);
                if (c == '(' && c2 == ')') {
                    answer += stick; // 막대기 자르기
                    i += 1;
                } else if (c == '(') {
                    stick += 1;
                } else if (c == ')') {
                    stick -=1;
                    answer += 1; // 남은 막대기
                }
            }
            System.out.printf("#%d %d\n", test_case, answer);
        }
    }
}
