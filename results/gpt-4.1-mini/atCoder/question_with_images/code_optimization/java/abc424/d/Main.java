import java.io.*;
import java.util.*;

public class Main {
    static int T, H, W;
    static int[] grid; // bitmask per row: 1 means black, 0 means white
    static int res;
    static final int INF = 1000000000;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int _ = 0; _ < T; _++) {
            String[] hw = br.readLine().split(" ");
            H = Integer.parseInt(hw[0]);
            W = Integer.parseInt(hw[1]);
            grid = new int[H];
            for (int i = 0; i < H; i++) {
                String s = br.readLine();
                int rowMask = 0;
                for (int j = 0; j < W; j++) {
                    if (s.charAt(j) == '#') {
                        rowMask |= (1 << j);
                    }
                }
                grid[i] = rowMask;
            }
            res = INF;
            dfs(0, 0);
            sb.append(res).append('\n');
        }
        System.out.print(sb);
    }

    // dfs over cells (i,j) with pruning and bitmask operations
    // i: current row, j: current column
    // grid[] is global and modified in place, restored after recursion
    static void dfs(int i, int j) {
        if (res == 0) return; // early stop if already zero

        if (j == W - 1) {
            i++;
            j = 0;
        }
        if (i == H - 1) {
            // Check if grid satisfies condition (no 2x2 black block)
            if (checkGrid()) {
                int painted = countPainted();
                if (painted < res) res = painted;
            }
            return;
        }

        // Check if 2x2 block at (i,j) is all black
        if (isBlackBlock(i, j)) {
            // Try repainting each of the 4 black cells in the block to white
            // For each, repaint, recurse, then restore
            int[] positions = {
                (i << 8) | j,
                (i << 8) | (j + 1),
                ((i + 1) << 8) | j,
                ((i + 1) << 8) | (j + 1)
            };
            for (int pos : positions) {
                int r = pos >> 8;
                int c = pos & 0xFF;
                if ((grid[r] & (1 << c)) != 0) {
                    grid[r] &= ~(1 << c); // repaint black->white
                    dfs(i, j + 1);
                    grid[r] |= (1 << c); // restore
                }
            }
        } else {
            dfs(i, j + 1);
        }
    }

    // Check if 2x2 block at (i,j) is all black
    static boolean isBlackBlock(int i, int j) {
        int mask = (1 << j) | (1 << (j + 1));
        return ((grid[i] & mask) == mask) && ((grid[i + 1] & mask) == mask);
    }

    // Check entire grid for any 2x2 black block
    static boolean checkGrid() {
        int mask2 = 3; // bits for two adjacent columns
        for (int i = 0; i < H - 1; i++) {
            for (int j = 0; j < W - 1; j++) {
                int mask = (1 << j) | (1 << (j + 1));
                if (((grid[i] & mask) == mask) && ((grid[i + 1] & mask) == mask)) {
                    return false;
                }
            }
        }
        return true;
    }

    // Count how many black cells were repainted white
    // Since original grid is lost, we count how many black cells remain
    // and subtract from original black count
    // To avoid storing original black count, we store it once per test case
    // So we store original black count in a global variable before dfs
    static int originalBlackCount;
    static int countPainted() {
        int currentBlack = 0;
        for (int i = 0; i < H; i++) {
            currentBlack += Integer.bitCount(grid[i]);
        }
        return originalBlackCount - currentBlack;
    }

    // We need to set originalBlackCount before dfs
    // So modify main accordingly

    // Modified main to set originalBlackCount before dfs
    // We'll move dfs call into a helper method that sets originalBlackCount

    // So let's refactor main and dfs accordingly

    // Refactored code below:

    // (The above code is the main logic, now the final code below)
}