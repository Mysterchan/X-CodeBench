import java.util.Scanner;

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

    static long[] polyMul(long[] a, long[] b, int maxVal) {
        int n = 1;
        int minSize = 2 * maxVal + 1;
        while (n < minSize) n <<= 1;

        long[] fa = new long[n];
        long[] fb = new long[n];
        System.arraycopy(a, 0, fa, 0, a.length);
        System.arraycopy(b, 0, fb, 0, b.length);

        ntt(fa, false);
        ntt(fb, false);

        for (int i = 0; i < n; i++) fa[i] = (fa[i] * fb[i]) % MOD;

        ntt(fa, true);

        long[] res = new long[minSize];
        System.arraycopy(fa, 0, res, 0, minSize);
        return res;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int maxVal = 0;
        boolean[] exists = new boolean[1000001];
        long[] P = new long[1000001];

        for (int i = 0; i < N; i++) {
            int s = sc.nextInt();
            exists[s] = true;
            P[s] = 1;
            maxVal = Math.max(maxVal, s);
        }
        sc.close();

        long[] P_resized = new long[maxVal + 1];
        System.arraycopy(P, 0, P_resized, 0, maxVal + 1);

        long[] C = polyMul(P_resized, P_resized, maxVal);

        long count = 0;

        for (int B = 1; B <= maxVal; B++) {

            if (exists[B]) {

                int k = 2 * B;

                count += (C[k] - 1) / 2;
            }
        }

        System.out.println(count);
    }
}