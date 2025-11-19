import java.util.*;

public class Main {
    static int H, W;
    static char[][] grid;
    static final int[] dx = {-1, 1, 0, 0};
    static final int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        H = sc.nextInt();
        W = sc.nextInt();
        grid = new char[H][W];

        for (int i = 0; i < H; i++) {
            String line = sc.next();
            grid[i] = line.toCharArray();
        }

        // Count of black neighbors for each cell
        int[][] blackAdjCount = new int[H][W];

        // Initialize blackAdjCount for white cells
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                if (grid[i][j] == '.') {
                    int count = 0;
                    for (int d = 0; d < 4; d++) {
                        int ni = i + dx[d];
                        int nj = j + dy[d];
                        if (ni >= 0 && ni < H && nj >= 0 && nj < W && grid[ni][nj] == '#') {
                            count++;
                        }
                    }
                    blackAdjCount[i][j] = count;
                }
            }
        }

        // Queue for cells to be turned black
        ArrayDeque<int[]> queue = new ArrayDeque<>();

        // Initially enqueue all white cells with exactly one black neighbor
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                if (grid[i][j] == '.' && blackAdjCount[i][j] == 1) {
                    queue.offer(new int[]{i, j});
                }
            }
        }

        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int i = cell[0], j = cell[1];

            // If already black, skip
            if (grid[i][j] == '#') continue;

            // Paint cell black
            grid[i][j] = '#';

            // Update neighbors' blackAdjCount
            for (int d = 0; d < 4; d++) {
                int ni = i + dx[d];
                int nj = j + dy[d];
                if (ni >= 0 && ni < H && nj >= 0 && nj < W && grid[ni][nj] == '.') {
                    blackAdjCount[ni][nj]++;
                    // If now exactly one black neighbor, enqueue
                    if (blackAdjCount[ni][nj] == 1) {
                        queue.offer(new int[]{ni, nj});
                    }
                }
            }
        }

        // Count black cells
        int blackCount = 0;
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                if (grid[i][j] == '#') blackCount++;
            }
        }

        System.out.println(blackCount);
    }
}