import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        FastScanner in = new FastScanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        G_ManyLCS solver = new G_ManyLCS();
        solver.solve(in, out);
        out.close();
    }

    static class G_ManyLCS {
        public void solve(FastScanner in, PrintWriter out) {
            final int MOD = 998244353;
            int n = in.nextInt();
            int m = in.nextInt();
            char[] s = in.next().toCharArray();

            long[] dp = new long[n + 1];
            long[] next = new long[n + 1];
            dp[0] = 1; // There's one way to have an LCS of length 0: the empty string.

            for (int len = 0; len < m; len++) {
                Arrays.fill(next, 0);
                for (int c = 0; c < 26; c++) {
                    char currentChar = (char) (c + 'a');
                    // Use a temporary array to store the frequency updates for this character
                    long[] temp = new long[n + 1];

                    for (int j = 0; j <= n; j++) {
                        // Always propagate previous counts
                        temp[j] = dp[j];

                        if (j > 0 && s[j - 1] == currentChar) {
                            // If we have a match, we can increase the LCS length
                            temp[j] = (temp[j] + dp[j - 1]) % MOD;
                        }
                    }
                    // Add to next counts based on temp array
                    for (int j = 0; j <= n; j++) {
                        next[j] = (next[j] + temp[j]) % MOD;
                    }
                }
                // Move to the next length
                long[] swap = dp;
                dp = next;
                next = swap;
            }

            // Count the results
            long[] ans = new long[n + 1];
            for (int j = 0; j <= n; j++) {
                ans[j] = dp[j];
            }

            for (int i = 0; i < ans.length; i++) {
                if (i > 0) {
                    out.print(" ");
                }
                out.print(ans[i]);
            }
            out.println();
        }
    }

    static class FastScanner {
        private java.io.BufferedReader in;
        private java.util.StringTokenizer st;

        public FastScanner(InputStream stream) {
            in = new java.io.BufferedReader(new java.io.InputStreamReader(stream));
        }

        public String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new java.util.StringTokenizer(in.readLine());
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