/* TITLE: 하노이 탑
** LEVEL: Silver 1
** TAG: recursion
** DATE: 20230207
*/

import java.math.BigInteger;
import java.util.Scanner;

class Main {

    static int N = 1;
    static BigInteger cnt = new BigInteger("2");
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        System.out.println(cnt.pow(N).subtract(new BigInteger("1")));
        if (N <= 20) {
            dfs(N, 1, 2, 3);
            System.out.println(sb.toString());
        }
    }

    private static void dfs(int n, int from, int temp, int to) {
        if (n == 0) {
            return;
        }

        dfs(n - 1, from, to, temp);
        if (N <= 20)
            sb.append(from + " " + to + "\n");
        dfs(n - 1, temp, from, to);
    }
}