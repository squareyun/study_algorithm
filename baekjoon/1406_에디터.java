/**
 * TITLE: 에디터
 * LEVEL: Silver 2
 * TAG: stack
 * DATE: 20230211
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        int M = Integer.parseInt(br.readLine());
        Stack<Character> stackL = new Stack<>(); // 커서 왼쪽에 존재하는 글자
        Stack<Character> stackR = new Stack<>(); // 커서 오른쪽에 존재하는 글자

        for (int i = 0; i < str.length(); i++) {
            stackL.add(str.charAt(i)); // 스택 구성
        }

        for (int i = 0; i < M; i++) {
            String[] input = br.readLine().split(" ");
            switch (input[0]) {
                case "L":
                    if (!stackL.isEmpty()) {
                        stackR.add(stackL.pop());
                    }
                    break;
                case "D":
                    if (!stackR.isEmpty()) {
                        stackL.add(stackR.pop());
                    }
                    break;
                case "B":
                    if (!stackL.isEmpty()) {
                        stackL.pop();
                    }
                    break;
                case "P":
                    stackL.add(input[1].charAt(0));
                    break;
            }
        }

        // 출력
        StringBuilder sb = new StringBuilder();
        while (!stackL.isEmpty()) {
            sb.append(stackL.pop());
        }
        sb.reverse();
        while (!stackR.isEmpty()) {
            sb.append(stackR.pop());
        }
        System.out.println(sb.toString());
    }
}