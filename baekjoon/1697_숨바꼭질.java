/**
 * TITLE: 숨바꼭질
 * LEVEL: Silver 1
 * TAG: bfs, graph
 * DATE: 20230223
 */

import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Scanner;

public class BOJ_1697 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int K = sc.nextInt();		
		int[] arr = new int[100001];
		Queue<Integer> q = new ArrayDeque<>();
		q.offer(N);
		
		int[] dx = {1, -1, 2};
		while (!q.isEmpty()) {
			int cur = q.poll();
			if (cur == K) {
				System.out.println(arr[cur]);
				break;
			}
			
			for (int i=0; i<3; i++) {
				int nx = (i!=2) ? cur + dx[i] : cur * dx[i];
				if (nx < 0 || nx > 100000)
					continue;
				if (arr[nx] != 0)
					continue;
				arr[nx] = arr[cur] + 1;
				q.offer(nx);
			}
		}
		
	}
}
