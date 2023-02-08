/* TITLE: N과 M(2)
** LEVEL: Silver 3
** TAG: combination, recursion
** DATE: 20230208
*/

import java.util.Scanner;

public class Main {
	static int N, M;
	static int[] arr;
	static int[] brr;
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		arr = new int[N];
		brr = new int[M];
		for (int i=0; i<N; i++)
			arr[i] = i+1;
		dfs(0, 0);
		System.out.println(sb.toString());
	}

	private static void dfs(int cnt, int start) {
		if (cnt == M) {
			for (int i=0; i<M; i++) {
				sb.append(brr[i] + " ");
			}
			sb.append("\n");
			return;
		}
		
		for (int i=start; i<N; i++) {
			brr[cnt] = arr[i];
			dfs(cnt + 1, i + 1);
		}
		
	}
}
