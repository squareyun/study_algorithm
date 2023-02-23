/**
 * TITLE: 트리의 부모 찾기
 * LEVEL: Silver 2
 * TAG: bfs, graph
 * DATE: 20230223
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;

public class BOJ_11725 {

    static int N;
    static ArrayList<Integer>[] list;
    static boolean[] v;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        list = new ArrayList[N + 1];
        v = new boolean[N + 1];
        int[] ans = new int[N + 1];

        for (int i = 0; i <= N; i++) {
            list[i] = new ArrayList<>();
        }

        for (int i = 0; i < N - 1; i++) {
            String[] input = br.readLine().split(" ");
            int a = Integer.parseInt(input[0]);
            int b = Integer.parseInt(input[1]);
            list[a].add(b);
            list[b].add(a);
        }

        Queue<Integer> q = new ArrayDeque<>();
        q.offer(1);
        v[1] = true;
        while (!q.isEmpty()) {
            int cur = q.poll();
            for (Integer a : list[cur]) {
                if (v[a]) {
                    continue;
                }

                v[a] = true;
                q.offer(a);
                ans[a] = cur;
            }
        }

        for (int i = 2; i <= N; i++) {
            System.out.println(ans[i]);
        }
    }
}
