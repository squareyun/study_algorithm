import java.util.Scanner;

public class QUADTREE {
    static String quadtree;
    static int it;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int c = sc.nextInt();
        sc.nextLine(); // 개행문자

        for (int i = 0; i < c; i++) {
            quadtree = sc.nextLine();
            it = 0;
            System.out.println(reverse());
        }

        sc.close();
    }

    static String reverse() {
        char head = quadtree.charAt(it);
        if (head == 'w' || head == 'b') {
            return head + "";
        }
        it++;
        String first = reverse();
        it++;
        String second = reverse();
        it++;
        String third = reverse();
        it++;
        String fourth = reverse();
        return "x" + third + fourth + first + second;
    }

    // 주어진 문자열을 가지고 그림을 그려보는 함수
    // 그러나, N이 엄청 클 때 점 하나만 다른 색이라면 매우 비효율적이다.

    // static int decompress(String quadtree, int it, int y, int x, int size) {
    // char head = quadtree.charAt(it);
    // it += 1; // 교재에서는 iterator을 사용했으나 여기서는 it을 통해 참조할 위치를 정하기
    // if (head == 'w' || head == 'b') {
    // for (int dy = 0; dy < size; dy++) {
    // for (int dx = 0; dx < size; dx++) {
    // decompressed[y + dy][x + dx] = head;
    // }
    // }
    // } else {
    // int half = size / 2;
    // it = decompress(quadtree, it, y, x, half); // 1사분면
    // it = decompress(quadtree, it, y, x + half, half); // 2사분면
    // it = decompress(quadtree, it, y + half, x, half); // 3사분면
    // it = decompress(quadtree, it, y + half, x + half, half); // 4사분면
    // }

    // return it;
    // }

}
