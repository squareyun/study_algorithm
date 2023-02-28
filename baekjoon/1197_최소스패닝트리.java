/**
 * TITLE: 최소 스패닝 트리
 * LEVEL: Gold 4
 * TAG: prim
 * DATE: 20230228
 */


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class BOJ_1197 {

    static int V, E;
    static ArrayList<Edge>[] list;
    static boolean[] v;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        st = new StringTokenizer(br.readLine());
        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());

        list = new ArrayList[V + 1];
        for (int i = 0; i < V + 1; i++) {
            list[i] = new ArrayList<>();
        }

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            list[a].add(new Edge(b, w));
            list[b].add(new Edge(a, w));

        }

        v = new boolean[V + 1];
        PriorityQueue<Edge> pq = new PriorityQueue<>();
        pq.offer(new Edge(1, 0));

        long ans = 0;
        int cnt = 0;
        while (!pq.isEmpty()) {
            Edge cur = pq.poll();

            if (v[cur.a]) {
                continue;
            }

            v[cur.a] = true;
            ans += cur.w;
            cnt += 1;

            if (cnt == V) {
                break;
            }

            for (Edge e : list[cur.a]) {
                if (v[e.a]) {
                    continue;
                }

                pq.offer(e);
            }
        }

        System.out.println(ans);

    }

    static class Edge implements Comparable<Edge> {

        int a, w;

        public Edge(int a, int w) {
            this.a = a;
            this.w = w;
        }

        @Override
        public int compareTo(Edge o) {
            return Integer.compare(this.w, o.w);
        }
    }
}
