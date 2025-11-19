import java.util.*;
import java.io.*;

public class Main {
    static int H, W, N;
    static long[][] grid;
    static long maxScore = 0;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] hw = br.readLine().split(" ");
        H = Integer.parseInt(hw[0]);
        W = Integer.parseInt(hw[1]);
        N = H * W;
        grid = new long[H][W];
        for (int i = 0; i < H; i++) {
            String[] line = br.readLine().split(" ");
            for (int j = 0; j < W; j++) {
                grid[i][j] = Long.parseLong(line[j]);
            }
        }

        // We'll use bitmask DP with memoization to try all placements of dominoes.
        // State: bitmask of used cells (N bits)
        // We try to place dominoes on adjacent free cells or skip cells.
        // Since N <= 20, 2^N = 1,048,576 states, feasible with pruning and memo.

        // Memoization map: from used mask to max score achievable
        // We'll store max score for each used mask.
        // To avoid recomputation, use a HashMap or array.

        // But 2^20 is 1 million, so we can use an array.

        // We'll do DFS with memoization.

        int fullMask = (1 << N) - 1;
        long[] memo = new long[1 << N];
        Arrays.fill(memo, -1L);

        maxScore = dfs(0, memo);

        System.out.println(maxScore);
    }

    // dfs returns max score achievable from current used mask
    static long dfs(int used, long[] memo) {
        if (memo[used] != -1) return memo[used];

        // Find first free cell
        int pos = -1;
        for (int i = 0; i < N; i++) {
            if ((used & (1 << i)) == 0) {
                pos = i;
                break;
            }
        }
        if (pos == -1) {
            // All cells used or skipped, compute XOR of uncovered cells
            // uncovered cells = cells not covered by dominoes
            // Here, "used" means cells covered by dominoes
            // So uncovered cells are those not in used
            long xorVal = 0;
            for (int i = 0; i < N; i++) {
                if ((used & (1 << i)) == 0) {
                    int r = i / W;
                    int c = i % W;
                    xorVal ^= grid[r][c];
                }
            }
            memo[used] = xorVal;
            return xorVal;
        }

        long res = 0;

        // Option 1: skip this cell (do not cover it with domino)
        // So leave it uncovered, move on
        res = Math.max(res, dfs(used | 0, memo)); // same as dfs(used, memo), but we must avoid infinite loop
        // But if we do not mark this cell as used, we will loop infinitely.
        // So we must mark it as "used" to avoid revisiting.
        // But skipping means leaving uncovered, so we do NOT mark it as used.
        // So we must move to next cell without marking this cell as used.
        // But this causes infinite loop because pos will be same next time.
        // So we must mark it as "visited" in some way.

        // To fix this, we can think differently:
        // We must either cover this cell with a domino (covering two cells),
        // or leave it uncovered and mark it as "used" to avoid revisiting.

        // So let's define "used" as cells that are either covered by domino or skipped (uncovered but processed).
        // Then uncovered cells are those skipped cells.

        // So we must mark skipped cells as used to avoid infinite loop.

        // So option 1: skip this cell (leave uncovered), mark it as used
        res = Math.max(res, dfs(used | (1 << pos), memo));

        // Option 2: try to place domino horizontally (pos and pos+1 if in same row and free)
        int r = pos / W;
        int c = pos % W;
        if (c + 1 < W) {
            int right = pos + 1;
            if ((used & (1 << right)) == 0) {
                // place domino covering pos and right
                res = Math.max(res, dfs(used | (1 << pos) | (1 << right), memo));
            }
        }

        // Option 3: try to place domino vertically (pos and pos+W if in range and free)
        if (r + 1 < H) {
            int down = pos + W;
            if ((used & (1 << down)) == 0) {
                // place domino covering pos and down
                res = Math.max(res, dfs(used | (1 << pos) | (1 << down), memo));
            }
        }

        memo[used] = res;
        return res;
    }
}