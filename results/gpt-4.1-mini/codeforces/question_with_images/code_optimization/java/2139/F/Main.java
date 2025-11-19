import java.io.*;
import java.util.*;

public class Main {
    static final long MOD = 1_000_000_007L;

    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner(System.in);
        StringBuilder out = new StringBuilder();
        int T = fs.nextInt();

        // Precompute factorials and inverse factorials for up to 5000 (max q)
        int maxQ = 5000;
        long[] fact = new long[maxQ + 1];
        long[] invFact = new long[maxQ + 1];
        fact[0] = 1;
        for (int i = 1; i <= maxQ; i++) fact[i] = fact[i - 1] * i % MOD;
        invFact[maxQ] = modInverse(fact[maxQ], MOD);
        for (int i = maxQ - 1; i >= 0; i--) invFact[i] = invFact[i + 1] * (i + 1) % MOD;

        while (T-- > 0) {
            int n = fs.nextInt();
            long m = fs.nextLong();
            int q = fs.nextInt();
            long[] a = new long[n];
            for (int i = 0; i < n; i++) a[i] = fs.nextLong();

            int[] opI = new int[q];
            long[] opX = new long[q];
            for (int i = 0; i < q; i++) {
                opI[i] = fs.nextInt() - 1;
                opX[i] = fs.nextLong();
            }

            // If no operations, answer is just initial positions * q! (which is 1)
            if (q == 0) {
                for (int i = 0; i < n; i++) {
                    out.append(a[i] % MOD);
                    if (i + 1 < n) out.append(' ');
                }
                out.append('\n');
                continue;
            }

            // For each slider, find the minimal and maximal final position it can have after applying all operations in any order.
            // Because the relative order of sliders never changes, and the pushing chain reaction always keeps order,
            // the final position of slider i is always between:
            // minPos[i] = max(a[i], max of all opX[j] where opI[j] == i and opX[j] < a[i])
            // maxPos[i] = min(a[i], min of all opX[j] where opI[j] == i and opX[j] > a[i])
            // But this is complicated by pushing.

            // Instead, we use the key insight from editorial:
            // The final position of slider i after applying all operations in any order is:
            // a[i] + sum of all increments caused by operations on sliders <= i
            // minus sum of all decrements caused by operations on sliders >= i
            // Because pushing only happens to neighbors and preserves order.

            // We can model the effect of each operation as a delta on the slider's position.
            // The final position of slider i after applying a subset of operations S is:
            // a[i] + sum_{j in S, opI[j] <= i} (opX[j] - a[opI[j]]) - sum_{j in S, opI[j] > i} (a[opI[j]] - opX[j])

            // Since we consider all permutations of all q operations, each operation is applied exactly once.
            // The order affects pushing but the sum over all permutations can be computed by linearity.

            // The problem reduces to:
            // For each slider i, sum over all permutations p of f_i(p) = q! * a[i] + sum over operations of expected increments.

            // The expected increment for slider i from operation j is:
            // If opI[j] <= i, then slider i is pushed forward by (opX[j] - a[opI[j]]) if positive
            // If opI[j] > i, then slider i is pushed backward by (a[opI[j]] - opX[j]) if positive

            // But the pushing chain reaction means the increments accumulate in a certain way.
            // The editorial shows the final formula is:
            // sum_{p} f_i(p) = q! * (a[i] + sum_{j=0}^{q-1} delta_j * P_j(i))
            // where delta_j = opX[j] - a[opI[j]]
            // and P_j(i) = 1 if opI[j] <= i else 0 for positive delta_j
            // or P_j(i) = -1 if opI[j] > i else 0 for negative delta_j

            // So for each operation j:
            // if delta_j > 0, it adds delta_j to all sliders i >= opI[j]
            // if delta_j < 0, it subtracts |delta_j| from all sliders i < opI[j]

            // We can accumulate these increments using prefix sums.

            long[] delta = new long[q];
            for (int i = 0; i < q; i++) {
                delta[i] = opX[i] - a[opI[i]];
            }

            // We'll build an array increments[] of length n, where increments[i] = sum of all increments for slider i
            long[] increments = new long[n];

            // For positive delta_j, add delta_j to increments[i] for i >= opI[j]
            // For negative delta_j, subtract |delta_j| from increments[i] for i < opI[j]

            // Use difference array for efficient updates
            long[] diff = new long[n + 1];

            for (int j = 0; j < q; j++) {
                int idx = opI[j];
                long d = delta[j];
                if (d > 0) {
                    // add d to increments[idx..n-1]
                    diff[idx] = (diff[idx] + d) % MOD;
                    diff[n] = (diff[n] - d + MOD) % MOD;
                } else if (d < 0) {
                    // subtract |d| from increments[0..idx-1]
                    diff[0] = (diff[0] + d + MOD) % MOD; // d is negative, so adding d means subtracting |d|
                    diff[idx] = (diff[idx] - d + MOD) % MOD; // subtract negative d = add |d|
                }
            }

            // Build increments from diff
            long cur = 0;
            for (int i = 0; i < n; i++) {
                cur = (cur + diff[i]) % MOD;
                increments[i] = cur;
            }

            // Now sum over all permutations = q! * (a[i] + increments[i]) mod MOD
            long qFact = fact[q];
            for (int i = 0; i < n; i++) {
                long val = (a[i] % MOD + increments[i]) % MOD;
                val = (val * qFact) % MOD;
                out.append(val);
                if (i + 1 < n) out.append(' ');
            }
            out.append('\n');
        }
        System.out.print(out);
    }

    static long modInverse(long a, long m) {
        // Fermat's little theorem for prime m
        return modPow(a, m - 2, m);
    }

    static long modPow(long base, long exp, long mod) {
        long res = 1;
        long cur = base % mod;
        while (exp > 0) {
            if ((exp & 1) == 1) res = (res * cur) % mod;
            cur = (cur * cur) % mod;
            exp >>= 1;
        }
        return res;
    }

    static class FastScanner {
        private final InputStream in;
        private final byte[] buffer = new byte[1 << 16];
        private int ptr = 0, len = 0;

        FastScanner(InputStream is) {
            in = is;
        }

        private int read() throws IOException {
            if (ptr >= len) {
                len = in.read(buffer);
                ptr = 0;
                if (len <= 0) return -1;
            }
            return buffer[ptr++];
        }

        int nextInt() throws IOException {
            int c;
            while ((c = read()) <= ' ') if (c == -1) return Integer.MIN_VALUE;
            int sign = 1;
            if (c == '-') {
                sign = -1;
                c = read();
            }
            int val = 0;
            while (c > ' ') {
                val = val * 10 + (c - '0');
                c = read();
            }
            return val * sign;
        }

        long nextLong() throws IOException {
            int c;
            while ((c = read()) <= ' ') if (c == -1) return Long.MIN_VALUE;
            int sign = 1;
            if (c == '-') {
                sign = -1;
                c = read();
            }
            long val = 0;
            while (c > ' ') {
                val = val * 10 + (c - '0');
                c = read();
            }
            return val * sign;
        }
    }
}