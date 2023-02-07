/* TITLE: 스위치 켜고 끄기
** LEVEL: Silver 4
** TAG: implementation
** DATE: 20230207
*/

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n + 1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int T = Integer.parseInt(br.readLine());
        for (int test_case = 0; test_case < T; test_case++) {
            st = new StringTokenizer(br.readLine());
            int gender = Integer.parseInt(st.nextToken());
            int number = Integer.parseInt(st.nextToken());

            // 남자일 경우
            if (gender == 1) {
                int i = 1;
                int number2 = number;
                while ((number2 = number * i++) <= n) {
                    arr[number2] = (arr[number2] == 0) ? 1 : 0;
                }
            } else {
                int l = number;
                int r = number;

                while (true) {
                    if (l == 1 || r == n) {
                        break;
                    }
                    l -= 1;
                    r += 1;
                    if (arr[l] != arr[r]) {
                        l += 1;
                        r -= 1;
                        break;
                    } else if (l == 1 || r == n) {
                        break;
                    }
                }

                for (int i = l; i <= r; i++) {
                    arr[i] = (arr[i] == 0) ? 1 : 0;
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= n; i++) {
            sb.append(arr[i] + " ");
            if (i % 20 == 0) {
                sb.append("\n");
            }
        }
        System.out.print(sb);
    }
}