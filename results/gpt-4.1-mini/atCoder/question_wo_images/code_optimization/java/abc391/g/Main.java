import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;

public class Main {
    static final int MOD = 998244353;

    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        FastScanner in = new FastScanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        solve(in, out);
        out.close();
    }

    static void solve(FastScanner in, PrintWriter out) {
        int n = in.nextInt();
        int m = in.nextInt();
        char[] s = in.next().toCharArray();

        // Precompute factorials and inverse factorials for combinations
        // max length is up to m+n, but we only need up to m+n for combinations
        int max = m + n + 10;
        long[] fact = new long[max];
        long[] invFact = new long[max];
        fact[0] = 1;
        for (int i = 1; i < max; i++) fact[i] = fact[i - 1] * i % MOD;
        invFact[max - 1] = modInv(fact[max - 1], MOD);
        for (int i = max - 2; i >= 0; i--) invFact[i] = invFact[i + 1] * (i + 1) % MOD;

        // Combination function
        // C(n,k) = fact[n] * invFact[k] * invFact[n-k] mod MOD
        // n,k <= max

        // dpLCS[i][j]: length of LCS of s[0..i-1] and t[0..j-1]
        // But we don't have t, we want to count number of strings t of length m
        // whose LCS with s is exactly k.

        // Approach:
        // Use DP over length of s and length of t to count number of strings t
        // with LCS length exactly k.

        // Let dp[i][j][k] = number of strings t of length j such that LCS(s[0..i-1], t) = k
        // But this is too large: n=10, m=100, k up to 10 => 10*100*11=11000 states, but
        // transitions are expensive.

        // Instead, use a standard DP for counting number of strings with LCS length >= k,
        // then use inclusion-exclusion to get exact k.

        // We use a DP similar to the classic LCS counting problem but counting number of strings t.

        // Define dp[i][k]: number of strings t of length i whose LCS with s is at least k.

        // We can compute dp[i][k] for k=0..n, i=0..m.

        // Base case:
        // dp[0][0] = 1 (empty string t, LCS length 0)
        // dp[0][k>0] = 0

        // Transition:
        // For each position in t (length i), we add one character c in 'a'..'z'.
        // For each k, dp[i][k] = sum over previous dp[i-1][k'] * ways to increase LCS from k' to k by adding c.

        // But this is complicated.

        // Alternative approach:
        // Use a DP over states representing the length of LCS so far.

        // Let's define dp[i][l]: number of strings t of length i whose LCS with s is exactly l.

        // We can compute dp[i][l] from dp[i-1][*].

        // For each dp[i-1][l'], when we add a character c, the LCS length can increase by 0 or 1.

        // To know if LCS length increases by 1, the character c must match some character in s that can extend the LCS.

        // Since s is fixed and small (n <= 10), we can precompute for each LCS length l, which characters can increase LCS length.

        // But this is complicated.

        // Instead, use a classic DP for counting number of strings with LCS length exactly k:
        // Use a DP over states representing the length of the longest prefix of s matched so far.

        // Let's define dp[i][j]: number of strings t of length i whose LCS with s is j.

        // We can compute dp[i][j] using the following:

        // For i=0: dp[0][0] = 1, dp[0][j>0] = 0

        // For each position i in t (1 to m):
        // For each LCS length j (0 to n):
        // dp[i][j] = dp[i-1][j] * (26 - count of characters that can increase LCS from j)
        //           + dp[i-1][j-1] * (count of characters that can increase LCS from j-1 to j)

        // So we need to know for each LCS length j, how many characters can increase LCS from j to j+1.

        // To do this, we precompute the set of characters that can increase LCS from length j.

        // For s, we can precompute next occurrence arrays.

        // Let's implement next arrays:

        int[][] next = new int[n + 1][26];
        for (int c = 0; c < 26; c++) next[n][c] = n;
        for (int i = n - 1; i >= 0; i--) {
            for (int c = 0; c < 26; c++) next[i][c] = next[i + 1][c];
            next[i][s[i] - 'a'] = i;
        }

        // For each LCS length j (0..n), we consider the position in s where the LCS of length j ends.
        // Actually, we track the minimal position in s where LCS length j can be achieved.

        // We'll keep an array minPos[j] = minimal position in s where LCS length j ends.
        // Initially, minPos[0] = -1 (empty subsequence), others = n (impossible)
        int[] minPos = new int[n + 1];
        Arrays.fill(minPos, n);
        minPos[0] = -1;

        // For each LCS length j, we find the set of characters c that can increase LCS from j to j+1:
        // That is, characters c where next[minPos[j] + 1][c] < n

        // We'll precompute for each j the count of such characters.

        int[] canIncreaseCount = new int[n + 1];
        for (int j = 0; j <= n; j++) {
            if (minPos[j] == n) {
                canIncreaseCount[j] = 0;
                continue;
            }
            int pos = minPos[j];
            int count = 0;
            for (int c = 0; c < 26; c++) {
                if (pos + 1 <= n && next[pos + 1][c] < n) {
                    count++;
                }
            }
            canIncreaseCount[j] = count;
        }

        // Now we do DP over length i=0..m and LCS length j=0..n
        // dp[i][j] = number of strings t of length i with LCS length exactly j

        long[][] dp = new long[m + 1][n + 1];
        dp[0][0] = 1;

        for (int i = 1; i <= m; i++) {
            // We need to update minPos for each j to get canIncreaseCount for next iteration
            // But minPos depends on the LCS length j and the minimal position in s where LCS length j ends.
            // We can update minPos for next iteration as follows:

            // For each j, minPos[j] is minimal position in s where LCS length j ends.
            // When we add a character c that can increase LCS from j-1 to j,
            // minPos[j] = min(minPos[j], next[minPos[j-1] + 1][c])

            // But since we only need canIncreaseCount, and minPos is only used to compute canIncreaseCount,
            // we can update minPos after each iteration.

            // To avoid complexity, we can simulate minPos update after each iteration:

            // For dp[i][j]:
            // dp[i][j] = dp[i-1][j] * (26 - canIncreaseCount[j]) + dp[i-1][j-1] * canIncreaseCount[j-1]

            // For j=0:
            // dp[i][0] = dp[i-1][0] * (26 - canIncreaseCount[0]) + 0 (since j-1 < 0)

            long[] ndp = new long[n + 1];
            for (int j = 0; j <= n; j++) {
                long stay = dp[i - 1][j] * (26 - canIncreaseCount[j]) % MOD;
                long inc = 0;
                if (j > 0) inc = dp[i - 1][j - 1] * canIncreaseCount[j - 1] % MOD;
                ndp[j] = (stay + inc) % MOD;
            }
            dp[i] = ndp;

            // Update minPos for next iteration
            int[] newMinPos = new int[n + 1];
            Arrays.fill(newMinPos, n);
            newMinPos[0] = -1;
            for (int j = 1; j <= n; j++) {
                int best = n;
                int prevPos = minPos[j];
                // For each character c that can increase LCS from j-1 to j,
                // minPos[j] = min over c of next[minPos[j-1]+1][c]
                int basePos = minPos[j - 1];
                for (int c = 0; c < 26; c++) {
                    if (basePos + 1 <= n && next[basePos + 1][c] < n) {
                        int candidate = next[basePos + 1][c];
                        if (candidate < best) best = candidate;
                    }
                }
                // Also consider previous minPos[j] (if no increase)
                if (minPos[j] < best) best = minPos[j];
                newMinPos[j] = best;
            }
            minPos = newMinPos;

            // Recompute canIncreaseCount for next iteration
            for (int j = 0; j <= n; j++) {
                if (minPos[j] == n) {
                    canIncreaseCount[j] = 0;
                    continue;
                }
                int pos = minPos[j];
                int count = 0;
                for (int c = 0; c < 26; c++) {
                    if (pos + 1 <= n && next[pos + 1][c] < n) {
                        count++;
                    }
                }
                canIncreaseCount[j] = count;
            }
        }

        // dp[m][k] = number of strings t of length m with LCS length exactly k
        // Output dp[m][0..n]

        for (int k = 0; k <= n; k++) {
            if (k > 0) out.print(" ");
            out.print(dp[m][k]);
        }
        out.println();
    }

    static long modInv(long a, int mod) {
        return modPow(a, mod - 2, mod);
    }

    static long modPow(long base, long exp, int mod) {
        long result = 1;
        long cur = base % mod;
        while (exp > 0) {
            if ((exp & 1) == 1) result = (result * cur) % mod;
            cur = (cur * cur) % mod;
            exp >>= 1;
        }
        return result;
    }

    static class FastScanner {
        private BufferedReader in;
        private StringTokenizer st;

        public FastScanner(InputStream stream) {
            in = new BufferedReader(new InputStreamReader(stream));
        }

        public String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    String line = in.readLine();
                    if (line == null) return null;
                    st = new StringTokenizer(line);
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return st.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }
    }
}