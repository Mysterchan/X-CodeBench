import java.util.*;

public class Main {
    static int H, W;
    static char[][] grid;
    static int startX, startY, goalX, goalY;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        H = sc.nextInt();
        W = sc.nextInt();
        grid = new char[H][W];
        for (int i = 0; i < H; i++) {
            String line = sc.next();
            for (int j = 0; j < W; j++) {
                grid[i][j] = line.charAt(j);
                if (grid[i][j] == 'S') {
                    startX = i;
                    startY = j;
                } else if (grid[i][j] == 'G') {
                    goalX = i;
                    goalY = j;
                }
            }
        }
        sc.close();

        // visited[x][y][d]: whether cell (x,y) has been visited with last move direction d
        // d = 0 means last move was vertical, d = 1 means last move was horizontal
        // We start with no last move, so we try both directions from start.
        int[][][] dist = new int[H][W][2];
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                Arrays.fill(dist[i][j], -1);
            }
        }

        Deque<State> queue = new ArrayDeque<>();
        // Enqueue start with last move vertical (0) and horizontal (1) with distance 0
        dist[startX][startY][0] = 0;
        dist[startX][startY][1] = 0;
        queue.add(new State(startX, startY, 0));
        queue.add(new State(startX, startY, 1));

        int ans = -1;
        while (!queue.isEmpty()) {
            State cur = queue.poll();
            int x = cur.x, y = cur.y, lastDir = cur.lastDir;
            int curDist = dist[x][y][lastDir];
            if (x == goalX && y == goalY) {
                ans = curDist;
                break;
            }

            // Next move direction must alternate
            int nextDir = 1 - lastDir;
            if (nextDir == 0) {
                // vertical moves
                if (x > 0 && grid[x - 1][y] != '#' && dist[x - 1][y][nextDir] == -1) {
                    dist[x - 1][y][nextDir] = curDist + 1;
                    queue.add(new State(x - 1, y, nextDir));
                }
                if (x + 1 < H && grid[x + 1][y] != '#' && dist[x + 1][y][nextDir] == -1) {
                    dist[x + 1][y][nextDir] = curDist + 1;
                    queue.add(new State(x + 1, y, nextDir));
                }
            } else {
                // horizontal moves
                if (y > 0 && grid[x][y - 1] != '#' && dist[x][y - 1][nextDir] == -1) {
                    dist[x][y - 1][nextDir] = curDist + 1;
                    queue.add(new State(x, y - 1, nextDir));
                }
                if (y + 1 < W && grid[x][y + 1] != '#' && dist[x][y + 1][nextDir] == -1) {
                    dist[x][y + 1][nextDir] = curDist + 1;
                    queue.add(new State(x, y + 1, nextDir));
                }
            }
        }

        System.out.println(ans);
    }

    static class State {
        int x, y, lastDir;

        State(int x, int y, int lastDir) {
            this.x = x;
            this.y = y;
            this.lastDir = lastDir;
        }
    }
}