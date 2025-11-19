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

        // To track cells to be colored black in the next iteration
        boolean[][] toColorBlack = new boolean[H][W];
        boolean changed;

        do {
            changed = false;

            for (int i = 0; i < H; i++) {
                for (int j = 0; j < W; j++) {
                    if (grid[i][j] == '.') {
                        int blackAdj = 0;

                        for (int d = 0; d < 4; d++) {
                            int ni = i + dx[d];
                            int nj = j + dy[d];
                            if (ni >= 0 && ni < H && nj >= 0 && nj < W && grid[ni][nj] == '#') {
                                blackAdj++;
                            }
                        }

                        if (blackAdj == 1) {
                            toColorBlack[i][j] = true; // Mark for coloring
                            changed = true;
                        }
                    }
                }
            }

            // Apply the changes
            for (int i = 0; i < H; i++) {
                for (int j = 0; j < W; j++) {
                    if (toColorBlack[i][j]) {
                        grid[i][j] = '#';
                        toColorBlack[i][j] = false; // Reset the mark
                    }
                }
            }

        } while (changed);

        // Count the black cells
        int blackCount = 0;
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                if (grid[i][j] == '#') blackCount++;
            }
        }

        System.out.println(blackCount);
    }
}