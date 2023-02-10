/**
 * TITLE: 햄버거 다이어트
 * LEVEL: D3
 * TAG: DP 인데 부분 집합으로 풀었음
 * DATE: 20230210
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class SWEA_5215 {

	static int N, L, answer;
	static int[] T, K;
	static boolean[] v;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int test_case = Integer.parseInt(st.nextToken());
		for (int t=1; t<=test_case; t++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			L = Integer.parseInt(st.nextToken());
			T = new int[N];
			K = new int[N];
			v = new boolean[N];
			for (int i=0; i<N; i++) {
				st = new StringTokenizer(br.readLine());
				T[i] = Integer.parseInt(st.nextToken());
				K[i] = Integer.parseInt(st.nextToken());
			}
			// 입력 끝
			
			answer = -1;
			dfs(0, 0, 0);
			System.out.printf("#%d %d\n", t, answer);
		}
	}

	private static void dfs(int cnt, int score, int cal) {
		if (cnt == N) {
			if (cal > L) {
				return;
			}
			answer = Math.max(answer, score);
			return;
		}
		
		v[cnt] = true;
		dfs(cnt + 1, score + T[cnt], cal + K[cnt]);
		v[cnt] = false;
		dfs(cnt + 1, score, cal);
	}
}
