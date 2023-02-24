import java.util.*;

class Solution {
    
    static ArrayList<Integer>[] list;
    static boolean[] v;
    static int[] arr;

    public int solution(int n, int[][] edge) {
        int answer = 0;
        list = new ArrayList[n+1];
        for (int i=0; i<n+1; i++) {
            list[i] = new ArrayList<>();
        }
        
        for (int i=0; i<edge.length; i++) {
            list[edge[i][0]].add(edge[i][1]);
            list[edge[i][1]].add(edge[i][0]);
        }
        
        v = new boolean[n+1];
        arr = new int[n];
        Queue<Data> q = new ArrayDeque<>();
        q.offer(new Data(1, 0));
        v[1] = true;
        
        while (!q.isEmpty()) {
            Data cur = q.poll();
            
            boolean leaf = true;
            for (int a : list[cur.x]) {
                if (v[a]) continue;
                leaf = false;
                v[a] = true;
                q.offer(new Data(a, cur.cnt + 1));
            }
            
            if (leaf) {
                arr[cur.cnt]++;
            }
        }
        
        for (int i=arr.length-1; i >= 0; i--) {
            if (arr[i] > 0) {
                answer = arr[i];
                break;
            }
        }
        
        return answer;
    }
    
    static class Data {
        int x, cnt;
        public Data(int x, int cnt) {
            this.x=x;
            this.cnt=cnt;
        }
    }
}