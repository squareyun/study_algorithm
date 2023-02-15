/**
 * LEVEL: Silver 1
 * TAG: priority_queue
 * DATE: 20230215
 */

import java.util.PriorityQueue;
import java.util.Scanner;

public class BOJ_11286 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		
		PriorityQueue<Data> pq = new PriorityQueue<>((o1, o2) -> (o1.abs == o2.abs)? (o1.x - o2.x) : (o1.abs - o2.abs));
		StringBuilder sb = new StringBuilder();
		for (int i=0; i<N; i++) {
			int op = sc.nextInt();
			if (op == 0) {
				if (pq.isEmpty())
					sb.append("0\n");
				else
					sb.append(pq.poll().x).append("\n");
			} else {
				pq.offer(new Data(Math.abs(op), op));
			}
		}
		System.out.println(sb);
	}

}

class Data {
	int abs;
	int x;
	public Data(int abs, int x) {
		this.abs=abs;
		this.x=x;
	}
}