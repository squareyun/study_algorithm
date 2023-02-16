/**
 * TITLE: 나무 탈출
 * LEVEL: Silver 1
 * TAG: dfs, tree, leaf node depth
 * DATE: 20230216
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class BOJ_15900 {

    static boolean[] visited;
    static ArrayList<ArrayList<Integer>> list;
    static int totalLevel;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        visited = new boolean[N+1];

        list = new ArrayList<>();
        for (int i=0; i<=N; i++) {
            list.add(new ArrayList<>());
        }

        for (int i=0; i<N-1; i++) {
            String[] input = br.readLine().split(" ");
            int a = Integer.parseInt(input[0]);
            int b = Integer.parseInt(input[1]);
            list.get(a).add(b);
            list.get(b).add(a);
        }

        dfs(1, 0);

        if (totalLevel % 2 == 0)
            System.out.println("No");
        else
            System.out.println("Yes");

        br.close();
    }

    static void dfs(int node, int level) {
        visited[node] = true;

        int num = 0;
        for (Integer child : list.get(node)) {
            if (visited[child])
                continue;

            num += 1;
            dfs(child, level + 1);
        }

        if (num == 0) { // 리프노드일 경우
            totalLevel += level;
//          System.out.println(level);
        }
    }
}
