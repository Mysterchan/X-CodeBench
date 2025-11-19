import java.io.*;
import java.util.*;

public class Main {
    static final long MOD = 1_000_000_007L;
    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner(System.in);
        StringBuilder out = new StringBuilder();
        int T = fs.nextInt();
        while (T-- > 0) {
            int n = fs.nextInt();
            long m = fs.nextLong();
            int q = fs.nextInt();
            long[] initPos = new long[n];
            for (int i = 0; i < n; ++i) initPos[i] = fs.nextLong();
            int[] opI = new int[q];
            long[] opX = new long[q];
            for (int i = 0; i < q; ++i) {
                opI[i] = fs.nextInt();
                opX[i] = fs.nextLong();
            }
            long[] sums = new long[n];
            if (q == 0) {
                for (int i = 0; i < n; ++i) sums[i] = initPos[i] % MOD;
            } else {
                int[] perm = new int[q];
                for (int i = 0; i < q; ++i) perm[i] = i;
                long[] pos = new long[n];
                boolean first = true;
                while (first || nextPerm(perm)) {
                    first = false;
                    System.arraycopy(initPos, 0, pos, 0, n);
                    for (int step = 0; step < q; ++step) {
                        int o = perm[step];
                        int idx = opI[o] - 1;
                        long dest = opX[o];
                        pos[idx] = dest;
                        for (int j = idx + 1; j < n; ++j) {
                            if (pos[j] <= pos[j - 1]) pos[j] = pos[j - 1] + 1;
                            else break;
                        }
                        for (int j = idx - 1; j >= 0; --j) {
                            if (pos[j] >= pos[j + 1]) pos[j] = pos[j + 1] - 1;
                            else break;
                        }
                    }
                    for (int i = 0; i < n; ++i) sums[i] += pos[i];
                }
                for (int i = 0; i < n; ++i) sums[i] %= MOD;
            }
            for (int i = 0; i < n; ++i) {
                out.append((sums[i] % MOD + MOD) % MOD);
                if (i + 1 < n) out.append(' ');
            }
            out.append('\n');
        }
        System.out.print(out.toString());
    }

    static boolean nextPerm(int[] a) {
        int n = a.length;
        int i = n - 2;
        while (i >= 0 && a[i] >= a[i + 1]) i--;
        if (i < 0) return false;
        int j = n - 1;
        while (a[j] <= a[i]) j--;
        int t = a[i]; a[i] = a[j]; a[j] = t;
        int l = i + 1, r = n - 1;
        while (l < r) {
            t = a[l]; a[l] = a[r]; a[r] = t;
            l++; r--;
        }
        return true;
    }

    static class FastScanner {
        private final InputStream in;
        private final byte[] buffer = new byte[1 << 16];
        private int ptr = 0, len = 0;
        FastScanner(InputStream is) { in = is; }
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
            if (c == '-') { sign = -1; c = read(); }
            int val = 0;
            while (c > ' ') { val = val * 10 + (c - '0'); c = read(); }
            return val * sign;
        }
        long nextLong() throws IOException {
            int c;
            while ((c = read()) <= ' ') if (c == -1) return Long.MIN_VALUE;
            int sign = 1;
            if (c == '-') { sign = -1; c = read(); }
            long val = 0;
            while (c > ' ') { val = val * 10 + (c - '0'); c = read(); }
            return val * sign;
        }
    }
}
