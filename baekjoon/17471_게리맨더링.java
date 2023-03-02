/**
 * TITLE: 게리맨더링
 * LEVEL: Gold 4
 * TAG: bfs, graph, combinatorics
 * DATE: 20230302
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_17471 {

	static int N;
	static int[] arr;
	static int[] person;
	static boolean[] selected;
	static boolean[] v;
	static ArrayList<Integer>[] list;
	static int answer = Integer.MAX_VALUE;

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		arr = new int[N];
		person = new int[N];
		selected = new boolean[N];
		list = new ArrayList[N + 1];
		for (int i = 0; i < N + 1; i++) {
			list[i] = new ArrayList<>();
		}

		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			person[i] = Integer.parseInt(st.nextToken());
			arr[i] = i + 1;
		}

		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine());
			int M = Integer.parseInt(st.nextToken());

			for (int j = 0; j < M; j++) {
				list[i].add(Integer.parseInt(st.nextToken()));
			}
		}

		dfs(0);
		System.out.println((answer == Integer.MAX_VALUE) ? -1 : answer);
	}

	static void dfs(int cnt) {
		if (cnt == N) {
			ArrayList<Integer> a = new ArrayList<>();
			ArrayList<Integer> b = new ArrayList<>();
			for (int i=1; i<=N; i++) {
				if (selected[i-1]) a.add(i);
				else b.add(i);
			}
			
			if (a.size() == 0 || b.size() == 0)
				return;
			
			if(bfs(a) && bfs(b)) { // 조건 만족
				// 인구수 계산
				int sumA = 0;
				for (int k : a) {
					sumA += person[k-1];
//					System.out.println(k);
				}
//				System.out.println("--");
				int sumB = 0;
				for (int k : b) {
					sumB += person[k-1];
				}
				answer = Math.min(answer, Math.abs(sumA - sumB));
			}
			
			return;
		}
		
		selected[cnt] = true;
		dfs(cnt + 1);
		selected[cnt] = false;
		dfs(cnt + 1);
	}
	
	static boolean bfs(ArrayList<Integer> a) {
		Queue<Integer> q = new ArrayDeque<>();
		v = new boolean[N+1];
		
		q.offer(a.get(0));
		v[a.get(0)] = true;
		
		int cnt = 1;
		while (!q.isEmpty()) {
			int cur = q.poll();
			
			for (Integer k : list[cur]) {
				if (!v[k] && a.contains(k)) {
					cnt++;
					v[k] = true;
					q.offer(k);
				}
			}
		}
		
		return (cnt == a.size()) ? true : false;
	}

}
