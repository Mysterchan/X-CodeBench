import java.io.*;
import java.util.*;

public class Main {
    static final int MOD = 998244353;

    static class Factorial {
        long[] f, g;

        Factorial(int n) {
            f = new long[n + 1];
            g = new long[n + 1];
            f[0] = g[0] = 1;
            for (int i = 1; i <= n; i++) {
                f[i] = f[i - 1] * i % MOD;
            }
            g[n] = pow(f[n], MOD - 2);
            for (int i = n - 1; i >= 1; i--) {
                g[i] = g[i + 1] * (i + 1) % MOD;
            }
        }

        long fac(int n) {
            return f[n];
        }

        long fac_inv(int n) {
            return g[n];
        }

        long comb(int n, int m) {
            if (n < m || m < 0) return 0;
            return f[n] * g[m] % MOD * g[n - m] % MOD;
        }

        long perm(int n, int m) {
            if (n < m || m < 0) return 0;
            return f[n] * g[n - m] % MOD;
        }

        long catalan(int n) {
            return (comb(2 * n, n) - comb(2 * n, n - 1)) % MOD;
        }

        long inv(int n) {
            return f[n - 1] * g[n] % MOD;
        }

        long pow(long a, long n) {
            long res = 1;
            while (n > 0) {
                if ((n & 1) == 1) res = res * a % MOD;
                a = a * a % MOD;
                n >>= 1;
            }
            return res;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int W = Integer.parseInt(st.nextToken());
        int H = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());
        int D = Integer.parseInt(st.nextToken());
        int U = Integer.parseInt(st.nextToken());

        Factorial fact = new Factorial(2000000);
        long ans = 0;

        for (int i = 0; i <= W; i++) {
            for (int j = 0; j <= H; j++) {
                if ((i < L || i > R) && (j < D || j > U)) {
                    int a = Math.max(i, W - i + 1);
                    int b = Math.max(j, H - j + 1);
                    ans = (ans + fact.comb(a + b - 2, a - 1)) % MOD;
                }
            }
        }

        System.out.println(ans);
    }
}