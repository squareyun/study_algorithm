/* TITLE: Flatten
** LEVEL: D3
** TAG: implementation, sort
** DATE: 20230207
*/

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {

    public static void main(String[] args) throws Exception {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = 10;
        for(int test_case = 1; test_case <= T; test_case++)
        {
            int dump = Integer.parseInt(br.readLsine());
            int[] arr = new int[100];
            
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i=0; i<100; i++) {
                arr[i] = Integer.parseInt(st.nextToken());
            }
            
            while (dump > 0) {
                Arrays.sort(arr);
                arr[99] -= 1;
                arr[0] += 1;
                dump -= 1;
                if (arr[99] - arr[0] == 0 || arr[99] - arr[0] == 1) {
                    break;
                }
            }
            Arrays.sort(arr);
            System.out.printf("#%d %d\n", test_case, arr[99] - arr[0]);
        }
    }

}