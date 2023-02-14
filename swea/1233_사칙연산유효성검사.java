/**
 * TITLE: 사칙연산 유효성 검사
 * LEVEL: D4
 * TAG: binary_tree
 * DATE: 20230214
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class SWEA_1233 {

	static int N;
	static String[] arr;
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		for (int test_case=1; test_case<=10; test_case++) {			
			N = Integer.parseInt(br.readLine());
			arr = new String[N+1];
			
			for (int i=1; i<=N; i++) {
				String[] input = br.readLine().split(" ");
				arr[i] = input[1];
			}
			
			int answer = solve();
			System.out.printf("#%d %d\n", test_case, answer);
		}
	}
	
	private static int solve() {
		int a = 1;
		for (int i=8; i>=1; i--) {
			if ((int) Math.pow(2, i) <= N) {
				a = i;
				break;
			}
		}
		int aa = (int) Math.pow(2, a-1) - 1;
		for (int i=1; i<=aa; i++) {
			if (isOperator(arr[i])) {
				continue;
			} else {
				return 0;
			}
		}	
		
		for (int i=aa+1; i<=N; i++) {
			// 왼쪽 자식, 오른쪽 자식 있을 때
			if (i*2 <= N && i*2+1 <= N) {
				if (isOperator(arr[i]) && !isOperator(arr[i*2]) && !isOperator(arr[i*2+1]))
					continue;
				else
					return 0;
			}
			// 왼쪽 자식만 있을 때
			else if (i*2 <= N) {
				if (isOperator(arr[i]) && !isOperator(arr[i*2]))
					continue;
				else
					return 0;
			}
			// 리프 노드일 때
			else {
				if (!isOperator(arr[i]))
					continue;
				else
					return 0;
			}
		}
		
		return 1;
	}
	
	private static boolean isOperator(String s) {
		if (s.equals("+") || s.equals("-") || s.equals("*") || s.equals("/"))
			return true;
		return false;
	}

}
