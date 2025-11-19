import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int H = scan.nextInt();
        int W = scan.nextInt();
        int K = scan.nextInt();

        boolean[][] grid = new boolean[H][W];
        for (int i = 0; i < K; i++) {
            int r = scan.nextInt() - 1;
            int c = scan.nextInt() - 1;
            grid[r][c] = true; // true indicates an obstacle
        }
        scan.close();

        if (canReachEnd(grid, H, W)) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }

    private static boolean canReachEnd(boolean[][] grid, int H, int W) {
        if (grid[0][0] || grid[H-1][W-1]) return false; // Start or end is blocked

        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{0, 0});
        grid[0][0] = true; // mark as visited

        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int x = curr[0];
            int y = curr[1];

            if (x == H - 1 && y == W - 1) return true; // Reached the end

            for (int[] dir : directions) {
                int newX = x + dir[0];
                int newY = y + dir[1];

                if (newX >= 0 && newX < H && newY >= 0 && newY < W && !grid[newX][newY]) {
                    queue.add(new int[]{newX, newY});
                    grid[newX][newY] = true; // mark as visited
                }
            }
        }
        return false; // No path found
    }
}