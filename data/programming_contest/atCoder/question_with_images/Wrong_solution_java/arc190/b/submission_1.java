import java.util.*;
import java.io.*;

public class Main {
    static final long MOD = 998244353;
    static final int MAXN = (int) 1e7 + 10;
    static long[] fact = new long[MAXN];
    static long[] invfact = new long[MAXN];
    static long[] pow2 = new long[MAXN];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        fact[0] = 1;
        invfact[0] = 1;
        pow2[0] = 1;
        for (int i = 1; i <= n; i++) {
            fact[i] = fact[i - 1] * i % MOD;
            invfact[i] = invfact[i - 1] * modInverse(i, MOD) % MOD;
            pow2[i] = pow2[i - 1] * 2 % MOD;
        }

        int q = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        int[] k = new int[q];
        for (int i = 0; i < q; i++) {
            k[i] = Integer.parseInt(st.nextToken());
        }

        long[] res = new long[q];
        long[] f = new long[n + 1];
        long[] g = new long[n + 1];
        f[0] = 1;
        g[0] = 1;
        for (int i = 1; i <= n; i++) {
            f[i] = (f[i - 1] * (n - i + 1) % MOD * 2 % MOD + (i > 1 ? g[i - 2] : 0)) % MOD;
            g[i] = (g[i - 1] * (n - i + 1) % MOD * 2 % MOD + (i > 1 ? f[i - 2] : 0)) % MOD;
        }

        long[] h = new long[n + 1];
        h[n] = 1;
        for (int i = n - 1; i >= 0; i--) {
            h[i] = (h[i + 1] * (n - i) % MOD * 2 % MOD + (i < n - 1 ? f[i + 2] : 0)) % MOD;
        }

        for (int i = 0; i < q; i++) {
            int x = k[i];
            long ans = 0;
            if (a <= x && b <= x) {
                ans = (ans + C(x - 1, a - 1) * C(x - 1, b - 1) % MOD * f[n - x]) % MOD;
                ans = (ans + C(x - 1, a - 1) * C(x - 1, b - 1) % MOD * g[n - x]) % MOD;
            }
            if (a <= x && b > x) {
                ans = (ans + C(x - 1, a - 1) * C(n - x, b - x) % MOD * h[x]) % MOD;
                ans = (ans + C(x - 1, a - 1) * C(n - x, b - x) % MOD * f[n - x]) % MOD;
            }
            if (a > x && b <= x) {
                ans = (ans + C(n - x, a - x) * C(x - 1, b - 1) % MOD * h[x]) % MOD;
                ans = (ans + C(n - x, a - x) * C(x - 1, b - 1) % MOD * g[n - x]) % MOD;
            }
            if (a > x && b > x) {
                ans = (ans + C(n - x, a - x) * C(n - x, b - x) % MOD * f[n - x]) % MOD;
                ans = (ans + C(n - x, a - x) * C(n - x, b - x) % MOD * g[n - x]) % MOD;
            }
            res[i] = ans;
        }

        for (int i = 1; i < q; i++) {
            res[i] = (res[i] - res[i - 1] + MOD) % MOD;
        }

        for (int i = 0; i < q; i++) {
            pw.println(res[i]);
        }

        pw.close();
    }

    static long C(int n, int k) {
        if (k < 0 || k > n) return 0;
        return fact[n] * invfact[k] % MOD * invfact[n - k] % MOD;
    }

    static long modInverse(long a, long m) {
        long m0 = m;
        long y = 0, x = 1;
        if (m == 1) return 0;
        while (a > 1) {
            long q = a / m;
            long t = m;
            m = a % m;
            a = t;
            t = y;
            y = x - q * y;
            x = t;
        }
        if (x < 0) x += m0;
        return x;
    }
}