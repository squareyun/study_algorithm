/**
 * TITLE: 집합
 * LEVEL: Silver 5
 * TAG: bitmask
 * DATE: 20230209
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_11723 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int M = Integer.parseInt(br.readLine());
		
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		int S = 0; // using bit-masking
		for(int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine());
			String mode = st.nextToken();
			int x = 0;
			if (!mode.equals("all") && !mode.equals("empty")) {
				x = Integer.parseInt(st.nextToken());
			}
			
			switch (mode) {
			case "add":
				S |= (1 << x);					
				break;
			case "remove":
				if ((S & 1 << x) > 0)
					S &= ~(1 << x);
				break;
			case "check":
				int check = S & (1 << x);
				sb.append((check > 0) ? "1" : "0").append("\n");
				break;
			case "toggle":
				S ^= (1 << x);
				break;
			case "all":
				S = (int)Math.pow(2, 21) - 1;
				break;
			case "empty":
				S = 0;
				break;
			}
		}
		System.out.println(sb.toString());
	}

}
