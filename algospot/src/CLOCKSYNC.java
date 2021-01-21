import java.util.Scanner;

public class CLOCKSYNC {
    static final int INF = 9999, SWITCHES = 10, CLOCKS = 16;
    static final String linked[] = { "xxx.............", "...x...x.x.x....", "....x.....x...xx", "x...xxxx........",
            "......xxx.x.x...", "x.x...........xx", "...x..........xx", "....xx.x......xx", ".xxxxx..........",
            "...xxx...x...x.." };
    static int[] clocks = new int[CLOCKS];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int c = sc.nextInt();

        for (int i = 0; i < c; i++) {
            for (int j = 0; j < CLOCKS; j++) {
                clocks[j] = sc.nextInt();
            }
            int answer = solve(clocks, 0);
            System.out.println(answer == INF ? -1 : answer);
        }

        sc.close();
    }

    static int solve(int[] clocks, int number) {
        if (number == SWITCHES) {
            return isAnswer(clocks) ? 0 : INF;
        }

        int ret = INF;
        for (int i = 0; i < 4; i++) {
            ret = Math.min(ret, i + solve(clocks, number + 1));
            pressButton(clocks, number);
        }
        return ret;
    }

    static void pressButton(int[] clocks, int number) {
        for (int i = 0; i < CLOCKS; i++) {
            if (linked[number].charAt(i) == 'x') {
                clocks[i] += 3;
                if (clocks[i] == 15)
                    clocks[i] = 3;
            }
        }
    }

    static boolean isAnswer(int[] clocks) {
        boolean flag = true;
        for (int i = 0; i < CLOCKS; i++) {
            if (clocks[i] != 12) {
                flag = false;
                break;
            }
        }
        return flag;
    }
}