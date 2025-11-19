import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;
import java.util.LinkedList;

public class Main {

    static int H, W;
    static int[][] F;
    
    static class State {
        int r, c, floor, cost;

        State(int r, int c, int floor, int cost) {
            this.r = r;
            this.c = c;
            this.floor = floor;
            this.cost = cost;
        }
    }
    
    static final int[] dr = {-1, 1, 0, 0};
    static final int[] dc = {0, 0, -1, 1};
    static final int MAX_FLOORS = 1000001;

    static int solve(int Ar, int Ac, int Y, int Cr, int Cc, int Z) {
        LinkedList<State> queue = new LinkedList<>();
        int[][][] dist = new int[H][W][MAX_FLOORS];
        
        for (int[][] d1 : dist) {
            for (int[] d2 : d1) {
                java.util.Arrays.fill(d2, Integer.MAX_VALUE);
            }
        }
        
        queue.add(new State(Ar, Ac, Y, 0));
        dist[Ar][Ac][Y] = 0;

        while (!queue.isEmpty()) {
            State cur = queue.poll();
            int r = cur.r, c = cur.c, floor = cur.floor, cost = cur.cost;

            // Moving up
            if (floor + 1 <= F[r][c]) {
                if (dist[r][c][floor + 1] > cost + 1) {
                    dist[r][c][floor + 1] = cost + 1;
                    queue.add(new State(r, c, floor + 1, cost + 1));
                }
            }

            // Moving down
            if (floor - 1 >= 1) {
                if (dist[r][c][floor - 1] > cost + 1) {
                    dist[r][c][floor - 1] = cost + 1;
                    queue.add(new State(r, c, floor - 1, cost + 1));
                }
            }

            // Moving to adjacent blocks
            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i], nc = c + dc[i];
                if (nr >= 0 && nr < H && nc >= 0 && nc < W && F[nr][nc] >= floor) {
                    if (dist[nr][nc][floor] > cost) {
                        dist[nr][nc][floor] = cost;
                        queue.addFirst(new State(nr, nc, floor, cost));
                    }
                }
            }
        }

        return dist[Cr][Cc][Z] == Integer.MAX_VALUE ? -1 : dist[Cr][Cc][Z];
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