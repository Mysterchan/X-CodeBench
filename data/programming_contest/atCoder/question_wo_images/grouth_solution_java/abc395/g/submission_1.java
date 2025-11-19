import java.io.*;
import java.util.*;

public class Main implements Runnable {
    private static int n, k;
    private static long[][] g;
    private static long[][] dp;

    private static void spfa(int S) {
        Queue<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            if (dp[S][i] != Long.MAX_VALUE) {
                q.add(i);
            }
        }
        while (!q.isEmpty()) {
            int u = q.poll();
            for (int v = 0; v < n; v++) {
                if (u == v) continue;
                long w = g[u][v];
                if (add(dp[S][u],w) < dp[S][v]) {
                    dp[S][v] = dp[S][u] + w;
                    q.add(v);
                }
            }
        }
    }

    static long add(long a, long b) {
        return a == Long.MAX_VALUE || b == Long.MAX_VALUE ? Long.MAX_VALUE : a + b;
    }

    public void solve() {
        n = nextInt();
        k = nextInt();

        long[][] res = new long[n][n];
        g = new long[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                g[i][j]=nextInt();
            }
        }

        for (int t = 0; t < n; t++) {
            dp = new long[1 << (k + 1)][n];
            for (long[] row : dp) {
                Arrays.fill(row, Long.MAX_VALUE);
            }

            for (int i = 0; i < k; i++) {
                dp[1 << i][i] = 0;
            }
            dp[1 << k][t]=0;

            for (int S = 1; S < 1 << (k + 1); S++) {
                for (int T = (S - 1) & S; T > 0; T = (T - 1) & S) {
                    if (T < (S ^ T)) break;
                    for (int i = 0; i < n; i++) {
                        dp[S][i] = Math.min(dp[S][i], add(dp[T][i], dp[S ^ T][i]));
                    }
                }
                spfa(S);
            }

            int S = (1 << (k + 1)) - 1;
            for (int i = 0; i < n; i++) {
                res[i][t] = dp[S][i];
            }
        }

        int q = nextInt();
        for (int qi = 0; qi < q; qi++) {
            int s = nextInt() - 1, t = nextInt() - 1;
            out.println(res[s][t]);
        }
    }

    @Override
    public void run() {
        int t = 1;
        for (int i = 0; i < t; i++) {
            new Main().solve();
        }
        out.flush();
    }

    public static void main(String[] args) throws Exception {
        new Thread(null, new Main(), "CustomThread", 1024 * 1024 * 100).start();
    }

    static PrintWriter out = new PrintWriter(System.out, false);
    static InputReader in = new InputReader(System.in);
    static String next() { return in.next(); }
    static int nextInt() { return Integer.parseInt(in.next()); }
    static long nextLong() { return Long.parseLong(in.next()); }
    static class InputReader {
        public BufferedReader reader;
        public StringTokenizer tokenizer;

        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream), 32768);
            tokenizer = null;
        }

        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }
    }
}