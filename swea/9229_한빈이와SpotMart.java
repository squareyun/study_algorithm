/**
 * TITLE: 한빈이와 Spot Mart
 * LEVEL: D3
 * TAG: 조합
 * DATE: 20230214
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class SWEA_9229 {
	
	static int N;
	static int M;
	static int[] arr;
	static int[] brr;
	static int answer;

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int T = Integer.parseInt(st.nextToken());
		for (int tc=1; tc<=T; tc++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			arr = new int[N];
			brr = new int[2];
			st = new StringTokenizer(br.readLine());
			for (int i=0; i<N; i++) {
				arr[i] = Integer.parseInt(st.nextToken());
			}
			answer = -1;
			dfs(0, 0);
			System.out.printf("#%d %d\n", tc, answer);
		}
		
	}

	private static void dfs(int cnt, int start) {
		if (cnt == 2) {
			int sum = brr[0] + brr[1];
			if (sum <= M) {
				answer = Math.max(answer, sum);
			}
			return;
		}
		
		for (int i=start; i<N; i++) {
			brr[cnt] = arr[i];
			dfs(cnt + 1, i + 1);
		}
	}

}
