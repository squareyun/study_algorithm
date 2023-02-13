/**
 * TITLE: 암호문 1
 * LEVEL: D3
 * TAG: linkedlist
 * DATE: 20230213
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class SWEA_1228 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		for (int test_case=1; test_case<=10; test_case++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			LinkedList<String> linkedList = new LinkedList<String>();
			st = new StringTokenizer(br.readLine());
			for (int i=0; i<N; i++) {
				linkedList.add(st.nextToken());
			}
			st = new StringTokenizer(br.readLine());
			int M = Integer.parseInt(st.nextToken());
			st = new StringTokenizer(br.readLine());
			for (int i=0; i<M; i++) {
				st.nextToken(); // l
				int idx = Integer.parseInt(st.nextToken());
				int num = Integer.parseInt(st.nextToken());
				for (int j=0; j<num; j++) {
					linkedList.add(idx++, st.nextToken());
				}
			}
			
			StringBuilder sb = new StringBuilder();
			sb.append("#").append(test_case).append(" ");
			for (int i=0; i<10; i++) {
				sb.append(linkedList.get(i)).append(" ");
			}
			System.out.println(sb);
		}
	}

}
