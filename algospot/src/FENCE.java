import java.util.Scanner;

public class FENCE {
    static int[] h;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int c = sc.nextInt();

        for (int i = 0; i < c; i++) {
            int n = sc.nextInt();
            h = new int[n];
            for (int j = 0; j < n; j++) {
                h[j] = sc.nextInt();
            }
            System.out.println(solve(0, n - 1));
        }

        sc.close();
    }

    static int solve(int left, int right) {
        // 기저 사례
        if (left == right) {
            return h[left];
        }

        // 분할 정복
        int mid = (left + right) / 2;
        int ret = Math.max(solve(left, mid), solve(mid + 1, right));

        // 양쪽 부분 문제에 걸친 경우의 답
        int lo = mid, hi = mid + 1;
        int height = Math.min(h[lo], h[hi]);
        ret = Math.max(ret, height * 2); // mid, mid + 1을 포함하는 너비 2인 사각형

        // 사각형이 입력 전체를 덮을 때 까지 확장
        while (left < lo || hi < right) {
            // 높이가 높은 쪽으로 확장
            if (hi < right && (lo == left || h[lo - 1] < h[hi + 1])) {
                hi++;
                height = Math.min(height, h[hi]);
            } else {
                lo--;
                height = Math.min(height, h[lo]);
            }

            ret = Math.max(ret, height * (hi - lo + 1));
        }
        return ret;
    }
}
