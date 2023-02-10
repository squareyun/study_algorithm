/**
 * TITLE: 괄호 짝짓기
 * LEVEL: D4
 * TAG: stack
 * DATE: 20230210
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class SWEA_1218 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		for (int test=1; test<=10; test++) {
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			
			st = new StringTokenizer(br.readLine());
			String input = st.nextToken();
			
			Stack<Character> s1 = new Stack<>();
			Stack<Character> s2 = new Stack<>();
			Stack<Character> s3 = new Stack<>();
			Stack<Character> s4 = new Stack<>();

			
			int answer = 1;
			
			try {
				for (int i=0; i<N; i++) {
					char token = input.charAt(i);
					switch (token) {
					case '(':
						s1.add(token);
						break;
					case '[':
						s2.add(token);
						break;
					case '{':
						s3.add(token);
						break;
					case '<':
						s4.add(token);
						break;
					case ')':
						if (s1.pop() == ')')
							throw new Exception();
						break;
					case ']':
						if (s2.pop() == ']')
							throw new Exception();
						break;
					case '}':
						if (s3.pop() == '}')
							throw new Exception();
						break;
					case '>':
						if (s4.pop() == '>')
							throw new Exception();
						break;
					}
				}
			} catch (Exception e) {
				answer = 0;
			}
			System.out.printf("#%d %d\n", test, answer);
		}
	}

}
