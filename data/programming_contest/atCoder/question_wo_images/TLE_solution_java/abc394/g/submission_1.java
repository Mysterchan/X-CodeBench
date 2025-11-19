import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;
import java.util.Map;
import java.util.HashMap;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {

    static int H, W;
    static int[][] F;

    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    static final long MAX_FLOOR_PLUS_ONE = 1000001L;

    static long encode(int r, int c, int floor) {

        return ((long)r * W + c) * MAX_FLOOR_PLUS_ONE + floor;
    }

    static int solve(int Ar, int Ac, int Y, int Cr, int Cc, int Z) {

        Deque<long[]> deque = new ArrayDeque<>();

        Map<Long, Integer> dist = new HashMap<>();

        long startId = encode(Ar, Ac, Y);
        dist.put(startId, 0);

        deque.addFirst(new long[]{Ar, Ac, Y, 0});

        while (!deque.isEmpty()) {
            long[] state = deque.pollFirst();
            int r = (int)state[0];
            int c = (int)state[1];
            int floor = (int)state[2];
            int cost = (int)state[3];
            long stateId = encode(r, c, floor);

            if (cost > dist.getOrDefault(stateId, Integer.MAX_VALUE)) {
                 continue;
            }

            int floor_up = floor + 1;
            if (floor_up <= F[r][c]) {
                long upId = encode(r, c, floor_up);
                if (dist.getOrDefault(upId, Integer.MAX_VALUE) > cost + 1) {
                    dist.put(upId, cost + 1);
                    deque.addLast(new long[]{r, c, floor_up, cost + 1});
                }
            }

            int floor_down = floor - 1;
            if (floor_down >= 1) {
                long downId = encode(r, c, floor_down);
                if (dist.getOrDefault(downId, Integer.MAX_VALUE) > cost + 1) {
                    dist.put(downId, cost + 1);
                    deque.addLast(new long[]{r, c, floor_down, cost + 1});
                }
            }

            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];

                if (nr >= 0 && nr < H && nc >= 0 && nc < W) {

                    if (F[nr][nc] >= floor) {
                        long nextId = encode(nr, nc, floor);
                        if (dist.getOrDefault(nextId, Integer.MAX_VALUE) > cost) {
                            dist.put(nextId, cost);
                            deque.addFirst(new long[]{nr, nc, floor, cost});
                        }
                    }
                }
            }
        }

        long endId = encode(Cr, Cc, Z);
        return dist.getOrDefault(endId, Integer.MAX_VALUE);
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);
        StringTokenizer st = new StringTokenizer(br.readLine());

        H = Integer.parseInt(st.nextToken());
        W = Integer.parseInt(st.nextToken());

        F = new int[H][W];
        for (int i = 0; i < H; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < W; j++) {
                F[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int Q = Integer.parseInt(br.readLine());
        for (int q = 0; q < Q; q++) {
            st = new StringTokenizer(br.readLine());

            int Ar = Integer.parseInt(st.nextToken()) - 1;
            int Ac = Integer.parseInt(st.nextToken()) - 1;
            int Y = Integer.parseInt(st.nextToken());
            int Cr = Integer.parseInt(st.nextToken()) - 1;
            int Cc = Integer.parseInt(st.nextToken()) - 1;
            int Z = Integer.parseInt(st.nextToken());

            out.println(solve(Ar, Ac, Y, Cr, Cc, Z));
        }

        out.flush();
    }
}