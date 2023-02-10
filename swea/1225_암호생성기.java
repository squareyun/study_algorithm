/**
 * TITLE: 암호생성기
 * LEVEL: D3
 * TAG: queue
 * DATE: 20230210
 */

import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Scanner;

public class SWEA_1225 {

	public static void main(String[] args) throws Exception {
		
		Scanner sc = new Scanner(System.in);
		for (int test=1; test<=10; test++) {
			sc.nextInt();
			
			Queue<Integer> q = new ArrayDeque<Integer>();
			for (int i=0; i<8; i++) {
				q.offer(sc.nextInt());
			}
			
			int[] cnt = {1, 2, 3, 4, 5};
			int index = 0;
			while (q.peek() - cnt[index] > 0) {
				q.offer(q.poll() - cnt[index]);
				index = (index + 1) % 5;
			}
			q.poll();
			q.offer(0);
			
			System.out.printf("#%d ", test);
			while (!q.isEmpty()) {
				System.out.printf("%d ", q.poll());
			}
			System.out.println();
		}
	}
}
