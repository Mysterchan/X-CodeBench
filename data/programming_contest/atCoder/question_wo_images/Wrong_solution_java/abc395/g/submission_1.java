import java.io.*;
import java.util.*;

public class Main {
    static final int INF = 1000000000;
    static final long INFLL = 1000000000000000000L;

    public static void main(String[] args) throws IOException {
        FastScanner fs = new FastScanner();
        PrintWriter out = new PrintWriter(System.out);

        int n = fs.nextInt();
        int k = fs.nextInt();
        long[][] c = new long[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                c[i][j] = fs.nextLong();
            }
        }

        long[][] dp = new long[n + 1][1 << (k + 1)];
        for (int i = 0; i <= n; i++) {
            Arrays.fill(dp[i], INFLL);
        }
        dp[0][0] = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < (1 << (k + 1)); j++) {
                if (dp[i][j] == INFLL) continue;
                for (int l = 0; l < n; l++) {
                    if (i == l) continue;
                    int nj = j;
                    if (l <= k) nj |= (1 << l);
                    dp[l][nj] = Math.min(dp[l][nj], dp[i][j] + c[i][l]);
                }
            }
        }

        long[] ans = new long[n + 1];
        Arrays.fill(ans, INFLL);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < (1 << (k + 1)); j++) {
                if (dp[i][j] == INFLL) continue;
                if (Integer.bitCount(j) == k + 1) {
                    ans[i] = Math.min(ans[i], dp[i][j]);
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                ans[j] = Math.min(ans[j], ans[i] + c[i][j]);
            }
        }

        int q = fs.nextInt();
        for (int i = 0; i < q; i++) {
            int s = fs.nextInt() - 1;
            int t = fs.nextInt() - 1;
            out.println(ans[s] + ans[t] - c[s][t]);
        }

        out.close();
    }

    static class FastScanner {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer("");

        String next() throws IOException {
            while (!st.hasMoreTokens()) {
                st = new StringTokenizer(br.readLine());
            }
            return st.nextToken();
        }

        int nextInt() throws IOException {
            return Integer.parseInt(next());
        }

        long nextLong() throws IOException {
            return Long.parseLong(next());
        }
    }
}