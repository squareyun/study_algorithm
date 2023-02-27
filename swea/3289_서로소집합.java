/**
 * TITLE: 서로소 집합
 * LEVEL: D4
 * TAG: union_find
 * DATE: 20230227
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class SWEA_3289 {

	static int[] p;
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = stoi(br.readLine());
		
		StringTokenizer st = null;
		for (int tc=1; tc<=T; tc++) {
			st = new StringTokenizer(br.readLine());
			int n = stoi(st.nextToken());
			int m = stoi(st.nextToken());
			makeSet(n);
			StringBuilder sb = new StringBuilder();
			sb.append("#").append(tc).append(" ");
			for (int i=0; i<m; i++) {
				st = new StringTokenizer(br.readLine());
				int op = stoi(st.nextToken());
				int a = stoi(st.nextToken());
				int b = stoi(st.nextToken());
				if (op == 0) {
					unionSet(a, b);
				} else if (op == 1) {
					sb.append(connected(a, b) ? 1 : 0);
				}
			}
			System.out.println(sb);
		}
	}
	
	private static void unionSet(int a, int b) {
		int aRoot = findSet(a);
		int bRoot = findSet(b);
		p[bRoot] = aRoot;
	}
	
	private static boolean connected(int a, int b) {
		return (findSet(a) == findSet(b)) ? true : false;
	}
	
	private static int findSet(int x) {
		if (p[x] == x) {
			return x;
		}
		return p[x] = findSet(p[x]);
	}
	
	private static void makeSet(int n) {
		p = new int[n+1];
		for (int i=0; i<n; i++) {
			p[i] = i;
		}
	}

	private static int stoi(String s) {
		return Integer.parseInt(s);
	}
}
