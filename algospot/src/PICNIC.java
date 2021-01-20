import java.util.Scanner;

public class PICNIC {
    static int n, m;
    static boolean[][] areFriends;

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        int C = sc.nextInt();
        for (int k = 0; k < C; k++) {
            n = sc.nextInt();
            m = sc.nextInt();
            areFriends = new boolean[n][n];
            boolean[] checked = new boolean[n];

            for (int i = 0; i < m; i++) {
                int a = sc.nextInt();
                int b = sc.nextInt();
                areFriends[a][b] = true;
                areFriends[b][a] = true;
            }
            System.out.println(solution(checked));
        }
        sc.close();
    }

    static int solution(boolean[] checked) {
        int firstFree = -1;
        for (int i = 0; i < n; i++) {
            if (!checked[i]) {
                firstFree = i;
                break;
            }
        }
        if (firstFree == -1) {
            return 1;
        }
        int cnt = 0;
        for (int i = firstFree + 1; i < n; i++) {
            if (!checked[i] && areFriends[firstFree][i]) {
                checked[firstFree] = checked[i] = true;
                cnt += solution(checked);
                checked[firstFree] = checked[i] = false;
            }
        }
        return cnt;
    }
}
