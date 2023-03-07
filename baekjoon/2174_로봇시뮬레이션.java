/**
 * TITLE: 로봇 시뮬레이션
 * LEVEL: Gold 5
 * TAG: simulation, implementation
 * DATE: 20230307
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_2174 {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        // 동남서북 (dir: 0, 1, 2, 3)
        int[] dx = {0, 1, 0, -1};
        int[] dy = {1, 0, -1, 0};
        int[][] map = new int[B][A];

        Robot[] robots = new Robot[N + 1];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int y = Integer.parseInt(st.nextToken()) - 1; // 좌표 주의
            int x = B - Integer.parseInt(st.nextToken()); // 좌표 주의
            String d = st.nextToken();
            int dir = 0;
            if (d.equals("S")) dir = 1;
            else if (d.equals("W")) dir = 2;
            else if (d.equals("N")) dir = 3;
            robots[i+1] = new Robot(x, y, dir);
            map[x][y] = i + 1; // 로봇 번호
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int cmdRobot = Integer.parseInt(st.nextToken());
            String cmd = st.nextToken();
            int cmdCnt = Integer.parseInt(st.nextToken());

            if (cmd.equals("L")) {
                turn(robots[cmdRobot], -1, cmdCnt);
            } else if (cmd.equals("R")) {
                turn(robots[cmdRobot], 1, cmdCnt); // 반대로 돌리기
            } else if (cmd.equals("F")) {
                int x = robots[cmdRobot].x;
                int y = robots[cmdRobot].y;
                int d = robots[cmdRobot].dir;
                for (int j = 0; j < cmdCnt; j++) {
                    int nx = x + dx[d];
                    int ny = y + dy[d];

                    if (nx < 0 || nx >= B || ny < 0 || ny >= A) {
                        System.out.printf("Robot %d crashes into the wall", cmdRobot);
                        System.exit(0);
                    }

                    if (map[nx][ny] != 0) {
                        System.out.printf("Robot %d crashes into robot %d", cmdRobot, map[nx][ny]);
                        System.exit(0);
                    }

                    x = nx;
                    y = ny;
                    
                    if (j == cmdCnt - 1) {
                        map[robots[cmdRobot].x][robots[cmdRobot].y] = 0;
                        robots[cmdRobot].x = nx;
                        robots[cmdRobot].y = ny;
                        map[robots[cmdRobot].x][robots[cmdRobot].y] = cmdRobot;
                    }
                }
            }
        }
        System.out.println("OK");
    }

    static void turn(Robot robot, int flag, int cnt) {
        for (int i = 0; i < cnt; i++) {
            robot.dir = (robot.dir + flag) % 4;
            if (robot.dir < 0) robot.dir = 3;
        }
    }

    static class Robot {
        int x, y, dir;

        public Robot(int x, int y, int dir) {
            this.x = x;
            this.y = y;
            this.dir = dir;
        }
    }

}