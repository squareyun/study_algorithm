/**
 * TITLE: 기타콘서트
 * LEVEL: Silver 2
 * TAG: bitmask, combinatorics
 * DATE: 20230209
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

    static int N, M;
    static int answer = Integer.MAX_VALUE;
    static boolean[] isSelected;
    static long[] guitar;
    static long target;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        N = Integer.parseInt(input[0]);
        M = Integer.parseInt(input[1]);
        isSelected = new boolean[N];
        guitar = new long[N];

        for (int i=0; i<N; i++) {
            String temp = br.readLine().split(" ")[1];
            for (int j=0; j<M; j++) {
                if (temp.charAt(j) == 'Y')
                    guitar[i] |= (1L << (M-j-1)); // long type 확인
            }
            target = Math.max(target, guitar[i]);
        }

        dfs(0);
        if (target == 0 || answer == Integer.MAX_VALUE) {
            System.out.println(-1);
        } else {
            System.out.println(answer);
        }
    }

    private static void dfs(int cnt) {
        if (cnt == N) {
            int selectedCnt = 0;
            long selectedGuitar = 0;
            for (int i=0; i<N; i++) {
                if (isSelected[i]) {
                    selectedCnt += 1;
                    selectedGuitar |= guitar[i];
                }
            }
            if (selectedGuitar >= target) {
                answer = Math.min(answer, selectedCnt);
                target = selectedGuitar;
            }
            return;
        }

        // 부분 집합
        isSelected[cnt] = true;
        dfs(cnt + 1);
        isSelected[cnt] = false;
        dfs(cnt + 1);
    }


}