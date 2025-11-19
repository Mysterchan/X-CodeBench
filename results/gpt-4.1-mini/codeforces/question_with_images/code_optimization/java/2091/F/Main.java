import java.io.*;
import java.util.*;

public class Main {
    static final int MOD = 998244353;

    public static void main(String[] args) throws IOException {
        // Use BufferedReader and BufferedWriter for faster IO
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int t = Integer.parseInt(br.readLine());

        // We'll process each test case
        while (t-- > 0) {
            String[] parts = br.readLine().split(" ");
            int n = Integer.parseInt(parts[0]);
            int m = Integer.parseInt(parts[1]);
            int d = Integer.parseInt(parts[2]);

            char[][] grid = new char[n][];
            for (int i = 0; i < n; i++) {
                grid[i] = br.readLine().toCharArray();
            }

            // dp[row][col][0 or 1]: number of ways to reach hold at (row,col)
            // with 1 hold used on this level (1) or 2 holds used (0)
            // We'll keep only two rows to save memory and improve cache locality
            int[][][] dp = new int[2][m][2];

            // Initialize dp for top row (row 0)
            // According to problem, first hold is on bottom level (row n-1),
            // but input rows are from top to bottom, so bottom level is row n-1.
            // So we must start from bottom row (n-1) and go upwards to row 0.
            // We'll process from bottom to top.

            // So we reverse the rows for processing: bottom row is row 0 in dp logic
            // We'll process rows from bottom (n-1) to top (0)
            // So we remap rows: dpRow = n-1 - actualRow

            // To avoid confusion, let's create a mapping function:
            // dpRow = n-1 - actualRow

            // We'll process rows in increasing dpRow order: 0 to n-1
            // dpRow 0 corresponds to actual row n-1 (bottom)
            // dpRow n-1 corresponds to actual row 0 (top)

            // Initialize dp for bottom row (dpRow=0, actualRow=n-1)
            int dpRow = 0;
            int actualRow = n - 1;
            for (int col = 0; col < m; col++) {
                if (grid[actualRow][col] == 'X') {
                    dp[dpRow][col][1] = 1; // one hold used on this level
                    dp[dpRow][col][0] = 1; // two holds used count starts same as one hold
                }
            }

            // For dpRow=0, update dp[0][col][0] by adding dp[0][j][1] for j in [col-d, col+d], j != col
            // This is to count routes with two holds on the same level
            // We'll do this efficiently using prefix sums

            // Build prefix sums of dp[0][*][1]
            int[] prefix1 = new int[m + 1];
            for (int i = 0; i < m; i++) {
                prefix1[i + 1] = (prefix1[i] + dp[dpRow][i][1]) % MOD;
            }

            for (int col = 0; col < m; col++) {
                if (grid[actualRow][col] == 'X') {
                    int left = Math.max(0, col - d);
                    int right = Math.min(m - 1, col + d);
                    int sum = prefix1[right + 1] - prefix1[left];
                    if (sum < 0) sum += MOD;
                    sum -= dp[dpRow][col][1]; // exclude self
                    if (sum < 0) sum += MOD;
                    dp[dpRow][col][0] = (dp[dpRow][col][0] + sum) % MOD;
                }
            }

            // Now process rows from dpRow=1 to dpRow=n-1 (actualRow from n-2 down to 0)
            for (dpRow = 1; dpRow < n; dpRow++) {
                actualRow = n - 1 - dpRow;

                // Clear current dp row
                for (int i = 0; i < m; i++) {
                    dp[dpRow & 1][i][0] = 0;
                    dp[dpRow & 1][i][1] = 0;
                }

                // prefix sums of previous dp row dp[prev][col][0]
                int[] prefix0 = new int[m + 1];
                for (int i = 0; i < m; i++) {
                    prefix0[i + 1] = (prefix0[i] + dp[(dpRow - 1) & 1][i][0]) % MOD;
                }

                // For each hold in current row, calculate dp[row][col][0] and dp[row][col][1]
                // dp[row][col][f] = sum of dp[row-1][j][0] for j in [col - d + 1, col + d - 1]
                // f in {0,1} same value

                for (int col = 0; col < m; col++) {
                    if (grid[actualRow][col] == 'X') {
                        int left = Math.max(0, col - d + 1);
                        int right = Math.min(m - 1, col + d - 1);
                        int val = prefix0[right + 1] - prefix0[left];
                        if (val < 0) val += MOD;
                        dp[dpRow & 1][col][0] = val;
                        dp[dpRow & 1][col][1] = val;
                    }
                }

                // Now update dp[row][col][0] by adding dp[row][j][1] for j in [col - d, col + d]
                // and subtract dp[row][col][1] to avoid counting same hold twice

                // prefix sums of dp[row][*][1]
                int[] prefix1_curr = new int[m + 1];
                for (int i = 0; i < m; i++) {
                    prefix1_curr[i + 1] = (prefix1_curr[i] + dp[dpRow & 1][i][1]) % MOD;
                }

                for (int col = 0; col < m; col++) {
                    if (grid[actualRow][col] == 'X') {
                        int left = Math.max(0, col - d);
                        int right = Math.min(m - 1, col + d);
                        int val = prefix1_curr[right + 1] - prefix1_curr[left];
                        if (val < 0) val += MOD;
                        val -= dp[dpRow & 1][col][1];
                        if (val < 0) val += MOD;
                        dp[dpRow & 1][col][0] = (dp[dpRow & 1][col][0] + val) % MOD;
                    }
                }
            }

            // The answer is sum of dp[n-1][col][0] for all holds in top row (actualRow=0)
            int ans = 0;
            dpRow = n - 1;
            actualRow = 0;
            for (int col = 0; col < m; col++) {
                if (grid[actualRow][col] == 'X') {
                    ans += dp[dpRow & 1][col][0];
                }
            }
            ans %= MOD;

            bw.write(ans + "\n");
        }
        bw.flush();
    }
}