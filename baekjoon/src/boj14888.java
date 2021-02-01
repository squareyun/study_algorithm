import java.util.Scanner;

public class boj14888 {
    static int[] input;
    static int ansMin = Integer.MAX_VALUE;
    static int ansMax = Integer.MIN_VALUE;

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        input = new int[n];

        for (int i = 0; i < n; i++) {
            input[i] = sc.nextInt();
        }

        // 0:plus, 1:minus, 2:mul, 3:div
        int op_num[] = new int[4];
        for (int i = 0; i < 4; i++) {
            op_num[i] = sc.nextInt();
        }

        int opArr[] = new int[n - 1];
        int index = 0;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < op_num[i]; j++) {
                opArr[index++] = i;
            }
        }

        int output[] = new int[n - 1];
        boolean[] visited = new boolean[n - 1];
        permutation(opArr, output, visited, 0, n - 1, n - 1);

        System.out.println(ansMax);
        System.out.println(ansMin);

        sc.close();
    }

    static void permutation(int[] opArr, int[] output, boolean[] visited, int depth, int n, int r) {
        if (depth == r) {
            calculate(output, r);
            return;
        }

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                visited[i] = true;
                output[depth] = opArr[i];
                permutation(opArr, output, visited, depth + 1, n, r);
                visited[i] = false;
            }
        }
    }

    static void calculate(int[] output, int r) {
        int temp = input[0];

        for (int i = 1; i < input.length; i++) {
            switch (output[i - 1]) {
                case 0:
                    temp += input[i];
                    break;
                case 1:
                    temp -= input[i];
                    break;
                case 2:
                    temp *= input[i];
                    break;
                case 3:
                    temp /= input[i];
            }
        }
        ansMin = Math.min(ansMin, temp);
        ansMax = Math.max(ansMax, temp);
    }
}
