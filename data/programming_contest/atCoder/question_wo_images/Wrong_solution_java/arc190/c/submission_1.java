import java.util.*;
import java.io.*;

public class Main {

    static final long MOD = 998244353;
    static final int MAXN = 200005;
    static long[][] fact = new long[MAXN][2];
    static long[][] invFact = new long[MAXN][2];

    static long qpow(long a, long b) {
        long ans = 1;
        while (b > 0) {
            if ((b & 1) == 1) {
                ans = ans * a % MOD;
            }
            a = a * a % MOD;
            b >>= 1;
        }
        return ans;
    }

    static void init() {
        fact[0][0] = fact[0][1] = 1;
        invFact[0][0] = invFact[0][1] = 1;
        for (int i = 1; i < MAXN; i++) {
            fact[i][0] = fact[i - 1][0] * i % MOD;
            invFact[i][0] = qpow(fact[i][0], MOD - 2);
        }
        for (int i = 1; i < MAXN; i++) {
            fact[i][1] = fact[i - 1][1] * (MOD + 1 - i) % MOD;
            invFact[i][1] = qpow(fact[i][1], MOD - 2);
        }
    }

    static long C(long n, long m) {
        if (m > n) {
            return 0;
        }
        return fact[(int) n][0] * invFact[(int) m][0] % MOD * invFact[(int) (n - m)][0] % MOD;
    }

    static long C2(long n, long m) {
        if (m > n) {
            return 0;
        }
        return fact[(int) n][1] * invFact[(int) m][1] % MOD * invFact[(int) (n - m)][1] % MOD;
    }

    static class Node {
        long x, y, val;

        public Node(long x, long y, long val) {
            this.x = x;
            this.y = y;
            this.val = val;
        }
    }

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        PrintWriter pw = new PrintWriter(System.out);
        init();
        int n = sc.nextInt();
        int m = sc.nextInt();
        long[][] a = new long[n + 1][m + 1];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                a[i][j] = sc.nextLong();
            }
        }
        int q = sc.nextInt();
        int sx = sc.nextInt();
        int sy = sc.nextInt();
        Node[] p = new Node[q + 1];
        for (int i = 1; i <= q; i++) {
            char op = sc.next().charAt(0);
            long val = sc.nextLong();
            if (op == 'U') {
                p[i] = new Node(sx - 1, sy, val);
                sx--;
            } else if (op == 'D') {
                p[i] = new Node(sx + 1, sy, val);
                sx++;
            } else if (op == 'L') {
                p[i] = new Node(sx, sy - 1, val);
                sy--;
            } else {
                p[i] = new Node(sx, sy + 1, val);
                sy++;
            }
        }
        long[][] sum = new long[n + 1][m + 1];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                sum[i][j] = (sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1] + a[i][j]) % MOD;
            }
        }
        long[][] g = new long[n + 1][m + 1];
        long[][] h = new long[n + 1][m + 1];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                g[i][j] = (C(n + m - 2, i - 1) - C2(n + m - 2, i - 1)) % MOD;
                h[i][j] = (C(n + m - 2, j - 1) - C2(n + m - 2, j - 1)) % MOD;
            }
        }
        long[][] f = new long[n + 1][m + 1];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                f[i][j] = (g[i][j] * sum[i][j] % MOD + h[i][j] * sum[i][j] % MOD) % MOD;
            }
        }
        long ans = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                ans = (ans + f[i][j] * a[i][j] % MOD) % MOD;
            }
        }
        for (int i = 1; i <= q; i++) {
            ans = (ans - f[(int) p[i].x][(int) p[i].y] * a[(int) p[i].x][(int) p[i].y] % MOD + MOD) % MOD;
            a[(int) p[i].x][(int) p[i].y] = p[i].val;
            ans = (ans + f[(int) p[i].x][(int) p[i].y] * a[(int) p[i].x][(int) p[i].y] % MOD) % MOD;
            pw.println(ans);
        }
        pw.close();
    }

    static class Scanner {
        BufferedReader br;
        StringTokenizer st;

        public Scanner(InputStream s) {
            br = new BufferedReader(new InputStreamReader(s));
        }

        public Scanner(FileReader f) {
            br = new BufferedReader(f);
        }

        public String next() throws IOException {
            while (st == null || !st.hasMoreTokens())
                st = new StringTokenizer(br.readLine());
            return st.nextToken();
        }

        public int nextInt() throws IOException {
            return Integer.parseInt(next());
        }

        public long nextLong() throws IOException {
            return Long.parseLong(next());
        }

        public double nextDouble() throws IOException {
            return Double.parseDouble(next());
        }

        public int[] nextIntArr(int n) throws IOException {
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(next());
            }
            return arr;
        }

    }
}