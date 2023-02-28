/**
 * TITLE: Contact
 * LEVEL: D4
 * TAG: graph, bfs
 * DATE: 20230228
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

public class SWEA_1238 {

    static ArrayList<Integer>[] list;
    static boolean[] v;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = null;
        for (int tc = 1; tc <= 10; tc++) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int src = Integer.parseInt(st.nextToken());
            list = new ArrayList[101];
            v = new boolean[101];
            for (int i = 0; i < 101; i++) {
                list[i] = new ArrayList<>();
            }
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N / 2; i++) {
                int from = Integer.parseInt(st.nextToken());
                int to = Integer.parseInt(st.nextToken());
                list[from].add(to);
            }
            // 입력끝

            Queue<Data> q = new ArrayDeque<>();
            for (Integer a : list[src]) {
                q.offer(new Data(a, 1));
            }
            v[src] = true;

            int maxCnt = -1;
            int maxNode = -1;
            while (!q.isEmpty()) {
                Data cur = q.poll();

                if (maxCnt < cur.cnt) {
                    maxCnt = cur.cnt;
                    maxNode = cur.x;
                } else if (maxCnt == cur.cnt) {
                    maxNode = Math.max(maxNode, cur.x);
                }

                for (Integer a : list[cur.x]) {
                    if (v[a]) {
                        continue;
                    }
                    q.offer(new Data(a, cur.cnt + 1));
                    v[a] = true;
                }
            }

            System.out.printf("#%d %d\n", tc, maxNode);
        }

    }

    static class Data {

        int x, cnt;

        public Data(int x, int cnt) {
            super();
            this.x = x;
            this.cnt = cnt;
        }

    }

}