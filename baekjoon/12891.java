/**
 * TITLE: DNA 비밀번호
 * LEVEL: Silver 2
 * TAG: string, sliding_window
 * DATE: 20230209
 */

import java.util.Scanner;

public class BOJ_12891 {

	static int s, p;
	static String dna;
	static int[] shouldContain;
	static int[] nowContain;
	static int totalCnt;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		s = sc.nextInt();
		p = sc.nextInt();
		shouldContain = new int[4];
		nowContain = new int[4];
		dna = sc.next();
		
		for (int i=0; i<4; i++) {
			shouldContain[i] = sc.nextInt();
		}
		
		
		String subDna = dna.substring(0, p);
		for (int j=0; j<p; j++) {
			nowContain[dnaIndex(subDna.charAt(j))] += 1;
		}
		checkCnt();
		
		for (int i=1; i<=s-p; i+=1) {
			nowContain[dnaIndex(dna.charAt(i-1))] -= 1;
			nowContain[dnaIndex(dna.charAt(i+p-1))] += 1;
			checkCnt();
		}
		
		System.out.println(totalCnt);
		
	}
	
	private static void checkCnt() {
		boolean flag = true;
		for (int j=0; j<4; j++) {
			if (nowContain[j] < shouldContain[j]) {
				flag = false;
				break;
			}
		}
		if (flag) totalCnt += 1;
	}
	
	private static int dnaIndex(char i) {
		switch(i) {
		case 'A':
			return 0;
		case 'C':
			return 1;
		case 'G':
			return 2;
		case 'T':
			return 3;
		}
		return -1;
	}
}
