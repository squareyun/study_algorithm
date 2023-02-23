/**
 * TITLE: 촌수계산
 * LEVEL: Silver 2
 * TAG: bfs, graph
 * DATE: 20230223
 */

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.Scanner;

public class BOJ_2644 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int x = sc.nextInt();
		int y = sc.nextInt();
		int m = sc.nextInt();
		ArrayList<Integer>[] list = new ArrayList[n+1];
		boolean[] v = new boolean[n+1];
		for (int i=0; i<=n; i++) {
			list[i] = new ArrayList<>();
		}
		
		for (int i=0; i<m; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			list[a].add(b);
			list[b].add(a);
		}
		
		Queue<Data> q = new ArrayDeque<>();
		boolean flag = false;
		q.offer(new Data(x, 0));
		while (!q.isEmpty()) {
			Data cur = q.poll();
			if (cur.x == y) {
				System.out.println(cur.cnt);
				flag = true;
				break;
			}
			
			for (Integer a : list[cur.x]) {
				if (v[a]) continue;
				q.offer(new Data(a, cur.cnt+1));
				v[a] = true;
			}
		}
		if (!flag) {
			System.out.println("-1");
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
