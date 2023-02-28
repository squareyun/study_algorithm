/**
 * TITLE: 최소 스패닝 트리
 * LEVEL: D4
 * TAG: kruskal, union-find
 * DATE: 20230228
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class SWEA_3124 {

    static int V, E;
    static Edge[] edgeList;
    static int[] parents;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());
        for (int tc = 1; tc <= T; tc++) {
            st = new StringTokenizer(br.readLine());
            V = Integer.parseInt(st.nextToken());
            E = Integer.parseInt(st.nextToken());
            edgeList = new Edge[E];

            for (int i = 0; i < E; i++) {
                st = new StringTokenizer(br.readLine());
                edgeList[i] = new Edge(Integer.parseInt(st.nextToken()),
                        Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            }
            Arrays.sort(edgeList);

            makeSet();
            long ans = 0;
            int cnt = 0;
            for (Edge e : edgeList) {
                if (union(e.a, e.b)) {
                    ans = (long) (ans + e.w);
                    if (++cnt == V - 1) {
                        break;
                    }
                }
            }
            System.out.printf("#%d %d\n", tc, ans);
        }
    }

    static void makeSet() {
        parents = new int[V + 1];
        for (int i = 0; i < V + 1; i++) {
            parents[i] = i;
        }
    }

    static boolean union(int a, int b) {
        a = find(a);
        b = find(b);

        if (a == b) {
            return false;
        }

        parents[b] = a;
        return true;
    }

    static int find(int a) {
        if (parents[a] == a) {
            return a;
        }
        return parents[a] = find(parents[a]);
    }

    static class Edge implements Comparable<Edge> {

        int a, b, w;

        public Edge(int a, int b, int w) {
            this.a = a;
            this.b = b;
            this.w = w;
        }

        @Override
        public int compareTo(Edge o) {
            return Integer.compare(this.w, o.w);
        }
    }
}
