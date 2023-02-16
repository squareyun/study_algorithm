/**
 * TITLE: 요리사
 * TAG: combination, dfs
 * DATE: 20230216
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class SWEA_4012 {

	static int N, answer;
	static int[][] S;
	static int[] arr;
	static int[] brr;
	static int[] brr2;
	static int[] crr;
	static int sumA, sumB;
	
	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int T = Integer.parseInt(st.nextToken());
		for (int tc=1; tc<=T; tc++) {
			answer = Integer.MAX_VALUE;
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			S = new int[N][N];
			arr = new int[N];
			for (int i=0; i<N; i++)
				arr[i] = i;
			for (int i=0; i<N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j=0; j<N; j++)
					S[i][j] = Integer.parseInt(st.nextToken());
			}
			brr = new int[N/2];
			brr2 = new int[N/2];
			crr = new int[2];
			dfs(0, 0);
			System.out.printf("#%d %d\n", tc, answer);
		}
	}

	private static void dfs(int cnt, int start) {
		if (cnt == N/2) {
			boolean[] brrBool = new boolean[N];
			for (int b : brr)
				brrBool[b] = true;
			int k=0;
			for (int i=0; i<N; i++)
				if (!brrBool[i])
					brr2[k++]=i;
			sumA=0; sumB=0;
			for (int i=0; i<N/2; i++) {
				for (int j=i+1; j<N/2; j++) {
					sumA += S[brr[i]][brr[j]] + S[brr[j]][brr[i]];
					sumB += S[brr2[i]][brr2[j]] + S[brr2[j]][brr2[i]];
				}
			}
			answer = Math.min(answer, Math.abs(sumA-sumB));
			return;
		}
		
		for (int i=start; i<N; i++) {
			brr[cnt] = arr[i];
			dfs(cnt + 1, i + 1);
		}
	}
	
	private static void dfs2(int cnt, int start) {
		if (cnt == 2) {
			sumA += S[brr[crr[0]]][brr[crr[1]]];
			sumB += S[brr2[crr[0]]][brr2[crr[1]]];
			
			answer = Math.min(answer, Math.abs(sumA-sumB));
			return;
		}
		
		for (int i=start; i<N; i++) {
			crr[cnt] = brr[i];
			dfs2(cnt + 1, i + 1);
		}
	}
}
