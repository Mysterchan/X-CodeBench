import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.TreeSet;

public class Main {

    static int H, W;
    static int[][] F;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    static class State {
        int r, c, floor, cost;
        State(int r, int c, int floor, int cost) {
            this.r = r;
            this.c = c;
            this.floor = floor;
            this.cost = cost;
        }
    }

    static int solve(int Ar, int Ac, int Y, int Cr, int Cc, int Z) {
        TreeSet<Integer> floors = new TreeSet<>();
        floors.add(Y);
        floors.add(Z);
        
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                floors.add(F[i][j]);
            }
        }
        
        int[] floorList = new int[floors.size()];
        int idx = 0;
        for (int f : floors) {
            floorList[idx++] = f;
        }
        
        int[][][] dist = new int[H][W][floorList.length];
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                for (int k = 0; k < floorList.length; k++) {
                    dist[i][j][k] = Integer.MAX_VALUE;
                }
            }
        }
        
        Deque<State> deque = new ArrayDeque<>();
        int startIdx = java.util.Arrays.binarySearch(floorList, Y);
        dist[Ar][Ac][startIdx] = 0;
        deque.addFirst(new State(Ar, Ac, startIdx, 0));
        
        while (!deque.isEmpty()) {
            State state = deque.pollFirst();
            
            if (state.cost > dist[state.r][state.c][state.floor]) {
                continue;
            }
            
            int actualFloor = floorList[state.floor];
            
            if (state.floor + 1 < floorList.length && floorList[state.floor + 1] <= F[state.r][state.c]) {
                int newCost = state.cost + (floorList[state.floor + 1] - actualFloor);
                if (newCost < dist[state.r][state.c][state.floor + 1]) {
                    dist[state.r][state.c][state.floor + 1] = newCost;
                    deque.addLast(new State(state.r, state.c, state.floor + 1, newCost));
                }
            }
            
            if (state.floor > 0) {
                int newCost = state.cost + (actualFloor - floorList[state.floor - 1]);
                if (newCost < dist[state.r][state.c][state.floor - 1]) {
                    dist[state.r][state.c][state.floor - 1] = newCost;
                    deque.addLast(new State(state.r, state.c, state.floor - 1, newCost));
                }
            }
            
            for (int i = 0; i < 4; i++) {
                int nr = state.r + dr[i];
                int nc = state.c + dc[i];
                
                if (nr >= 0 && nr < H && nc >= 0 && nc < W && F[nr][nc] >= actualFloor) {
                    if (state.cost < dist[nr][nc][state.floor]) {
                        dist[nr][nc][state.floor] = state.cost;
                        deque.addFirst(new State(nr, nc, state.floor, state.cost));
                    }
                }
            }
        }
        
        int endIdx = java.util.Arrays.binarySearch(floorList, Z);
        return dist[Cr][Cc][endIdx];
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