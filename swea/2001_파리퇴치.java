/**
 * TITLE: 파리 퇴치
 * LEVEL: D2
 * TAG: implementation
 * DATE: 20230209
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());
        for (int test_case = 1; test_case <= T; test_case++) {
            int answer = -1;

            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            int[][] arr = new int[N][N];

            for (int i=0; i<N; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j=0; j<N; j++) {
                    arr[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            // 입력 끝

            for (int i=0; i<=N-M; i++) {
                for (int j=0; j<=N-M; j++) {
                    int temp_sum = 0;
                    for (int k=i; k<i+M; k++) {
                        for (int m=j; m<j+M; m++) {
                            temp_sum += arr[k][m];
                        }
                    }
                    answer = Math.max(answer, temp_sum);
                }
            }

            System.out.printf("#%d %d\n", test_case, answer);
        }
    }
}
