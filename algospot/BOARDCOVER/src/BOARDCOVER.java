import java.util.Scanner;

public class BOARDCOVER {
    static int height, weight, wall;
    static int dir[][][] = { { { 0, 0 }, { 0, 1 }, { 1, 0 } }, { { 0, 0 }, { 0, 1 }, { 1, 1 } },
            { { 0, 0 }, { 1, 0 }, { 1, -1 } }, { { 0, 0 }, { 1, 0 }, { 1, 1 } } };

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int c = sc.nextInt();

        for (int i = 0; i < c; i++) {
            height = sc.nextInt();
            weight = sc.nextInt();
            wall = 0;
            int[][] board = new int[height][weight];

            for (int j = 0; j < height; j++) {
                String input = sc.next();
                for (int k = 0; k < weight; k++) {
                    char temp = input.charAt(k);
                    if (temp == '#') {
                        board[j][k] = 1;
                        wall += 1;
                    }
                }
            }
            // 빈칸의 개수가 3의 배수가 아니면 불가능
            if ((height * weight - wall) % 3 != 0) {
                System.out.println("0");
            } else {
                System.out.println(solve(board));
            }
        }

        sc.close();
    }

    static int solve(int[][] board) {
        int y = -1, x = -1;
        int ret = 0;

        // 비어있는 칸 찾기
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < weight; j++) {
                if (board[i][j] == 0) {
                    y = i;
                    x = j;
                    break;
                }
            }
            // 찾았을 경우 반복문 종료
            if (y != -1)
                break;
        }

        // 모든 칸을 다 채운 경우
        if (y == -1) {
            return 1;
        }

        for (int type = 0; type < 4; type++) {
            if (check(board, y, x, type, 1)) {
                ret += solve(board);
            }
            check(board, y, x, type, -1);
        }

        return ret;
    }

    static boolean check(int[][] board, int y, int x, int type, int delta) {
        boolean flag = true;

        for (int i = 0; i < 3; i++) {
            int ny = y + dir[type][i][0];
            int nx = x + dir[type][i][1];

            if (ny < 0 || ny >= height || nx < 0 || nx >= weight) {
                flag = false;
            } else if ((board[ny][nx] += delta) > 1) {
                flag = false;
            }
        }
        return flag;
    }
}
