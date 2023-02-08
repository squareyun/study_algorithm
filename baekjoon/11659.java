/* TITLE: 구간 합 구하기 4
** LEVEL: Silver 3
** TAG: prefix_sum
** DATE: 20230208
*/

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N, M;
	static int[] sum;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		sum = new int[N+1];
		
		st = new StringTokenizer(br.readLine());
		for (int i=1; i<=N; i++) {
			sum[i] = sum[i-1] + Integer.parseInt(st.nextToken());
		}
		
		StringBuilder sb = new StringBuilder();
		
		for (int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine());
			int p = Integer.parseInt(st.nextToken());
			int q = Integer.parseInt(st.nextToken());
			
			sb.append((sum[q]-sum[p-1]) + "\n");
		}
		System.out.println(sb);
	}
}
