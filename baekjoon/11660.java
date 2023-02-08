/* TITLE: 구간 합 구하기 5
** LEVEL: Silver 1
** TAG: prefix_sum
** DATE: 20230208
*/

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int[][] arr = new int[N+1][N+1];
		int[][] sumR = new int[N+1][N+1];
		
		for (int i=1; i<=N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j=1; j<=N; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
				sumR[i][j] = sumR[i][j-1] + arr[i][j];
			}
		}
		StringBuilder sb = new StringBuilder();
		for (int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine());
			int x1 = Integer.parseInt(st.nextToken());
			int y1 = Integer.parseInt(st.nextToken());
			int x2 = Integer.parseInt(st.nextToken());
			int y2 = Integer.parseInt(st.nextToken());
			
			int answer = 0;
			for (int j=x1; j<=x2; j++) {
				answer += (sumR[j][y2] - sumR[j][y1-1]);
			}
			sb.append(answer + "\n");
		}
		System.out.println(sb.toString());
	}
}
