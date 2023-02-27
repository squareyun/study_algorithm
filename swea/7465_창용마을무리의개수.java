/**
 * TITLE: 창용 마을 무리의 개수
 * LEVEL: D4
 * TAG: union_find
 * DATE: 20230227
 */

import java.util.Scanner;

public class SWEA_7465 {

	static int[] p;
	
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int tc=1; tc<=T; tc++) {
			int n = sc.nextInt();
			int m = sc.nextInt();
			
			p = new int[n+1];
			for (int i=1; i<=n; i++) {
				p[i] = i;
			}
			
			for (int i=0; i<m; i++) {
				int a = sc.nextInt();
				int b = sc.nextInt();
				
				union(a, b);
			}
			
			
			int cnt = 0;
			for (int i=1; i<=n; i++) {
				if (p[i] == i) {
					cnt++;
				}
			}
			System.out.printf("#%d %d\n", tc, cnt);
		}
	}
	 
	
	private static void union(int a, int b) {
		a = find(a);
		b = find(b);
		p[b] = a;
	}
	
	private static int find(int x) {
		if (p[x] == x) {
			return x;
		}
		return p[x] = find(p[x]);
	}

}
