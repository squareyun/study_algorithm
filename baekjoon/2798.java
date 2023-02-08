/* TITLE: 블랙잭
** LEVEL: Bronze 2
** TAG: combination, recursion
** DATE: 20230208
*/

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int M;
	static int[] arr;
	static int[] brr;
	static int max = -1;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		arr = new int[N];
		brr = new int[3];
		
		st = new StringTokenizer(br.readLine());
		for (int i=0; i<N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		dfs(0, 0);
		System.out.println(max);
	}

	private static void dfs(int cnt, int start) {
		if (cnt == 3) {
			int t = 0;
			for (int i=0; i<3; i++) {
				t += brr[i];
			}
			if (t <= M)
				max = Math.max(max, t);
			return;
		}
		
		for (int i=start; i<N; i++) {
			brr[cnt] = arr[i];
			dfs(cnt + 1, i + 1);
		}
	}
	
}
