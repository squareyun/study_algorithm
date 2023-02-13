/**
 * TITLE: 탑
 * LEVEL: Gold 5
 * TAG: stack
 * DATE: 20230213
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class BOJ_2493 {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		Stack<Integer[]> stack1 = new Stack<>();
		Stack<Integer[]> stack2 = new Stack<>();
		int[] res = new int[N+1];
		
		for (int i=1; i<=N; i++) {
			Integer[] input = new Integer[2];
			input[0] = Integer.parseInt(st.nextToken());
			input[1] = i;
			stack1.add(input);
		}
		
		while (!stack1.isEmpty()) {
			stack2.add(stack1.pop());
			
			if (stack1.isEmpty() || stack2.isEmpty()) {
				break;
			}
			while (stack1.peek()[0] > stack2.peek()[0]) {
				res[stack2.pop()[1]] = stack1.peek()[1];
				if (stack2.isEmpty()) break;
			}
		}
		
		StringBuilder sb = new StringBuilder();
		for (int i=1; i<=N; i++) {
			sb.append(res[i]).append(" ");
		}
		System.out.println(sb);
	}

}
