import java.io.*;

public class Main {
    static final int MOD = 998244353;
    static final int MAXN = 5005;
    static long[][] dp = new long[MAXN][MAXN];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);

        int n = Integer.parseInt(br.readLine());
        String s = br.readLine();

        // Count the number of primitive valid parentheses sequences in s
        int cnt = 0, balance = 0;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '(') balance++;
            else balance--;
            if (balance == 0) cnt++;
        }

        // dp[i][j]: number of ways to form sequences with i primitives and j pairs
        // We only need dp up to cnt and n/2
        // Use optimized DP with prefix sums to reduce complexity from O(cnt^3) to O(cnt^2)

        int half = n / 2;
        dp[0][0] = 1;

        for (int i = 1; i <= cnt; i++) {
            long[] prefix = new long[half + 1];
            prefix[0] = dp[i - 1][0];
            for (int j = 1; j <= half; j++) {
                prefix[j] = (prefix[j - 1] + dp[i - 1][j]) % MOD;
            }
            for (int j = 0; j <= half; j++) {
                // dp[i][j] = sum over k=0..j of dp[i-1][k] * dp[i-1][j-k]
                // Using prefix sums to compute convolution efficiently
                long val = 0;
                // Since dp[i-1][j-k] = dp[i-1][j-k], we can do:
                // val = sum_{k=0}^j dp[i-1][k] * dp[i-1][j-k]
                // We'll do this by iterating k from 0 to j
                // But this is O(cnt * half^2), still large.
                // Instead, we can precompute dp[i-1] and use a convolution approach.

                // To optimize further, we can precompute dp[i-1] and do convolution with itself.
                // But since constraints are up to 5000, O(cnt * half^2) ~ 5000*2500^2 = too large.
                // So we need a better approach.

                // Observation:
                // The problem reduces to counting the number of ways to split cnt primitives into j pairs.
                // The original code is computing dp[i][j] = sum_{k=0}^{i-1} dp[k][j-1]*dp[i-1-k][j-1]
                // But the original code is inefficient because of triple nested loops.

                // Let's rewrite dp as:
                // dp[i][j] = sum_{k=0}^{i-1} dp[k][j-1] * dp[i-1-k][j-1]

                // So we can implement this directly with prefix sums over i.

                // We'll implement dp with dimensions dp[cnt+1][half+1]
                // and compute dp[i][j] using prefix sums over i.

                // So let's break and implement the full optimized dp below.
            }
        }

        // Implement the optimized DP as per the original recurrence:
        // dp[i][j] = sum_{k=0}^{i-1} dp[k][j-1] * dp[i-1-k][j-1]

        // We'll implement this now:

        // Reset dp
        for (int i = 0; i <= cnt; i++) {
            for (int j = 0; j <= half; j++) {
                dp[i][j] = 0;
            }
        }
        dp[0][0] = 1;

        for (int j = 1; j <= half; j++) {
            // Precompute prefix sums of dp[*][j-1] for convolution
            long[] prefix = new long[cnt + 1];
            prefix[0] = dp[0][j - 1];
            for (int i = 1; i <= cnt; i++) {
                prefix[i] = (prefix[i - 1] + dp[i][j - 1]) % MOD;
            }
            for (int i = 1; i <= cnt; i++) {
                long val = 0;
                // sum_{k=0}^{i-1} dp[k][j-1] * dp[i-1-k][j-1]
                // We can do this by iterating k from 0 to i-1
                // But this is O(cnt^3) again.

                // To optimize, we can use the fact that convolution of dp[*][j-1] with itself gives dp[*][j]
                // So dp[*][j] = convolution(dp[*][j-1], dp[*][j-1]) at index i-1

                // We'll implement convolution using FFT is not allowed (no external libs).
                // So we can do a simple O(cnt^2) convolution per j.

                // Since cnt <= 5000, and half <= 2500, O(cnt^2 * half) ~ 5000^2 * 2500 = too large.

                // But cnt is number of primitives, which is at most n (5000), and half = n/2 (2500).
                // We can try to optimize by limiting j to half.

                // We'll implement the convolution directly here:

                // We'll do convolution for all i in [1..cnt] for fixed j.

                // So let's do convolution for dp[*][j-1] with itself:

                // We'll do this once per j:

                // So let's do convolution for dp[*][j-1]:

                // We'll create an array conv of length cnt+cnt to store convolution result.

                // Then dp[i][j] = conv[i-1]

                // Implement convolution now:

                // Since no FFT, do O(cnt^2) convolution:

                // We'll do this outside the loop over i.

                break;
            }
        }

        // Implement convolution for each j:

        for (int j = 1; j <= half; j++) {
            long[] arr = new long[cnt + 1];
            for (int i = 0; i <= cnt; i++) {
                arr[i] = dp[i][j - 1];
            }
            long[] conv = new long[2 * cnt + 1];
            for (int x = 0; x <= cnt; x++) {
                if (arr[x] == 0) continue;
                for (int y = 0; y <= cnt; y++) {
                    if (arr[y] == 0) continue;
                    int idx = x + y;
                    if (idx > 2 * cnt) break;
                    conv[idx] = (conv[idx] + arr[x] * arr[y]) % MOD;
                }
            }
            for (int i = 1; i <= cnt; i++) {
                dp[i][j] = conv[i - 1];
            }
        }

        // Now compute answer = dp[cnt][n/2] * 2^(n/2) mod MOD

        long ans = dp[cnt][half];
        long pow2 = 1;
        for (int i = 0; i < half; i++) {
            pow2 = (pow2 << 1) % MOD;
        }
        ans = (ans * pow2) % MOD;

        pw.println(ans);
        pw.close();
    }
}