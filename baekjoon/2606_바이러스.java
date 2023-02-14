/**
 * TITLE: 바이러스
 * LEVEL: Silver 3
 * TAG: graph, bfs
 * DATE: 20230214
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_2606 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int M = Integer.parseInt(st.nextToken());

        // 인접 리스트 구성
        ArrayList<ArrayList<Integer>> adjList = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            adjList.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            adjList.get(a).add(b);
            adjList.get(b).add(a);
        }

        Queue<Integer> q = new ArrayDeque<>();
        q.offer(1);
        boolean[] visited = new boolean[N + 1];
        while (!q.isEmpty()) {
            int now = q.poll();

            if (visited[now]) {
                continue;
            }
            visited[now] = true;

            ArrayList<Integer> al = adjList.get(now);
            for (int a : al) { // 인접하는 컴퓨터 큐에 삽입
                if (visited[a]) {
                    continue;
                }
                q.offer(a);
            }
        }

        int cnt = 0;
        for (boolean v : visited) {
            if (v) {
                cnt++;
            }
        }
        System.out.println(cnt - 1);
    }
}
