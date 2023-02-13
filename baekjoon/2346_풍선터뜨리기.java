/**
 * TITLE: 풍선 터뜨리기
 * LEVEL: Silver 3
 * TAG: deque
 * DATE: 20230213
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());

        Deque<int[]> queue = new ArrayDeque<>();

        st = new StringTokenizer(br.readLine());
        int next = Integer.parseInt(st.nextToken()); // 첫번째 원소
        for (int i = 2; i <= N; i++) {
            queue.offer(new int[]{Integer.parseInt(st.nextToken()), i});
        }

        StringBuilder sb = new StringBuilder();
        sb.append("1").append(" ");
        while (!queue.isEmpty()) {
            if (next > 0) {
                for (int i = 0; i < next; i++) {
                    queue.offer(queue.pollFirst());
                }
                int[] a = queue.pollLast();
                next = a[0];
                sb.append(a[1]).append(" ");
            } else {
                for (int i = 0; i < -next; i++) {
                    queue.offerFirst(queue.pollLast());
                }
                int[] a = queue.poll();
                next = a[0];
                sb.append(a[1]).append(" ");
            }
        }
        System.out.println(sb);
    }
}