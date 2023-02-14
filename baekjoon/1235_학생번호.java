/**
 * TITLE: 학생 번호
 * LEVEL: Silver 4
 * TAG: hash
 * DATE: 20230214
 */

import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class BOJ_1235 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		String[] arr = new String[N];
		for (int i=0; i<N; i++) {
			arr[i] = sc.next();
		}
		
		int len = arr[0].length();
		int ans = 0;
		for (int i=len-1; i>=0; i--) {
			Set<String> set = new HashSet<>();
			for (String a : arr) {
				set.add(a.substring(i, len));
			}
			if (set.size() == N) {
				ans = len-i;
				break;
			}
		}
		
		System.out.println(ans);
		
	}

}
