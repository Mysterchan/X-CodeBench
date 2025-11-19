import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
    static final long MOD = 998244353;
    static final long ROOT = 3;

    static long pow(long base, long exp) {
        long res = 1;
        base %= MOD;
        while (exp > 0) {
            if (exp % 2 == 1) res = (res * base) % MOD;
            base = (base * base) % MOD;
            exp /= 2;
        }
        return res;
    }

    static long modInverse(long n) {
        return pow(n, MOD - 2);
    }

    static void ntt(long[] a, boolean invert) {
        int n = a.length;
        for (int i = 1, j = 0; i < n; i++) {
            int bit = n >> 1;
            for (; (j & bit) != 0; bit >>= 1) j ^= bit;
            j ^= bit;
            if (i < j) {
                long temp = a[i]; a[i] = a[j]; a[j] = temp;
            }
        }

        for (int len = 2; len <= n; len <<= 1) {
            long wlen = pow(ROOT, (MOD - 1) / len);
            if (invert) wlen = modInverse(wlen);
            for (int i = 0; i < n; i += len) {
                long w = 1;
                for (int j = 0; j < len / 2; j++) {
                    long u = a[i + j];
                    long v = (a[i + j + len / 2] * w) % MOD;
                    a[i + j] = (u + v) % MOD;
                    a[i + j + len / 2] = (u - v + MOD) % MOD;
                    w = (w * wlen) % MOD;
                }
            }
        }
        if (invert) {
            long nInv = modInverse(n);
            for (int i = 0; i < n; i++) a[i] = (a[i] * nInv) % MOD;
        }
    }

    static long[] polyMul(long[] a, long[] b) {
        int n = 1;
        while (n < a.length + b.length) n <<= 1;
        long[] fa = new long[n];
        long[] fb = new long[n];
        System.arraycopy(a, 0, fa, 0, a.length);
        System.arraycopy(b, 0, fb, 0, b.length);

        ntt(fa, false);
        ntt(fb, false);
        for (int i = 0; i < n; i++) fa[i] = (fa[i] * fb[i]) % MOD;
        ntt(fa, true);

        int resSize = a.length + b.length - 1;
        long[] res = new long[resSize];
        System.arraycopy(fa, 0, res, 0, resSize);
        return res;
    }

    static long[] polyPow(long[] base, long exp) {
        long[] res = new long[]{1};
        while (exp > 0) {
            if (exp % 2 == 1) res = polyMul(res, base);
            base = polyMul(base, base);
            exp /= 2;
        }
        return res;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.close();

        long[] fact = new long[N + 1];
        fact[0] = 1;
        for (int i = 1; i <= N; i++) {
            fact[i] = (fact[i - 1] * i) % MOD;
        }

        long[] n_l = new long[7];
        long[] Sum_l = new long[7];
        long[] W_l = new long[7];
        long[] invW_l = new long[7];

        long start = 1;
        for (int l = 1; l <= 6; l++) {
            long end = Math.min(N, start * 10 - 1);
            if (start > N) break;

            n_l[l] = end - start + 1;

            Sum_l[l] = (n_l[l] % MOD * ((start + end) % MOD)) % MOD;
            Sum_l[l] = (Sum_l[l] * modInverse(2)) % MOD;

            W_l[l] = pow(10, l);
            invW_l[l] = modInverse(W_l[l]);

            start *= 10;
        }

        long[] c = new long[]{1};
        for (int l = 1; l <= 6; l++) {
            if (n_l[l] > 0) {
                long[] P_l = new long[]{W_l[l], 1};
                long[] P_l_pow = polyPow(P_l, n_l[l]);
                c = polyMul(c, P_l_pow);
            }
        }

        long[] c_final = new long[N + 1];
        System.arraycopy(c, 0, c_final, 0, Math.min(c.length, N + 1));

        long[][] d = new long[7][N];
        for (int l = 1; l <= 6; l++) {
            if (n_l[l] == 0) continue;

            long d_prev = 0;
            long invW = invW_l[l];
            for (int i = 0; i < N; i++) {
                d[l][i] = (c_final[i] - d_prev + MOD) % MOD;
                d[l][i] = (d[l][i] * invW) % MOD;
                d_prev = d[l][i];
            }
        }

        long totalSum = 0;
        for (int j = 1; j <= N; j++) {
            long inner_sum = 0;
            for (int l = 1; l <= 6; l++) {
                if (n_l[l] == 0) continue;
                inner_sum = (inner_sum + d[l][j - 1] * Sum_l[l]) % MOD;
            }
            long term = (fact[j - 1] * fact[N - j]) % MOD;
            term = (term * inner_sum) % MOD;
            totalSum = (totalSum + term) % MOD;
        }

        System.out.println(totalSum);
    }
}