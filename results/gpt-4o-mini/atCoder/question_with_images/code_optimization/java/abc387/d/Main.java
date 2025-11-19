import java.util.*;

class Main {

    static Scanner sc = new Scanner(System.in);
    
    static int[] dX = {-1, 1, 0, 0}; // Up, Down
    static int[] dY = {0, 0, -1, 1}; // Left, Right

    public static void main(String[] args) {
        int H = ni();
        int W = ni();
        char[][] grid = new char[H][W];
        int startX = -1, startY = -1;
        
        for (int i = 0; i < H; i++) {
            String row = nn();
            for (int j = 0; j < W; j++) {
                grid[i][j] = row.charAt(j);
                if (grid[i][j] == 'S') {
                    startX = i;
                    startY = j;
                }
            }
        }
        
        int result = bfs(grid, startX, startY, H, W);
        System.out.println(result);
        
        sc.close();
    }

    static int bfs(char[][] grid, int startX, int startY, int H, int W) {
        Queue<int[]> queue = new LinkedList<>();
        boolean[][][] visited = new boolean[H][W][2]; // 2: 0 - vertical last move, 1 - horizontal last move
        queue.offer(new int[]{startX, startY, 0, 0}); // x, y, moves, last move type
        visited[startX][startY][0] = true;
        visited[startX][startY][1] = true;

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int x = current[0], y = current[1], moves = current[2], lastMove = current[3];

            if (grid[x][y] == 'G') {
                return moves;
            }

            if (lastMove == 0) {
                // Last move was vertical, can only move horizontally
                for (int i = 2; i < 4; i++) {
                    int newX = x + dX[i];
                    int newY = y + dY[i];
                    if (isValid(newX, newY, H, W) && !visited[newX][newY][1] && grid[newX][newY] != '#') {
                        visited[newX][newY][1] = true;
                        queue.offer(new int[]{newX, newY, moves + 1, 1});
                    }
                }
            } else {
                // Last move was horizontal, can only move vertically
                for (int i = 0; i < 2; i++) {
                    int newX = x + dX[i];
                    int newY = y + dY[i];
                    if (isValid(newX, newY, H, W) && !visited[newX][newY][0] && grid[newX][newY] != '#') {
                        visited[newX][newY][0] = true;
                        queue.offer(new int[]{newX, newY, moves + 1, 0});
                    }
                }
            }
        }
        
        return -1; // Goal not reachable
    }

    static boolean isValid(int x, int y, int H, int W) {
        return x >= 0 && x < H && y >= 0 && y < W;
    }

    static int ni() {
        return sc.nextInt();
    }

    static String nn() {
        return sc.next();
    }
}