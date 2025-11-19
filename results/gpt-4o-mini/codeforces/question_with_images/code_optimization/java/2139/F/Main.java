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
            for (int i = 0; i < n; i++) initPos[i] = fs.nextLong();

            int[] opI = new int[q];
            long[] opX = new long[q];
            for (int i = 0; i < q; i++) {
                opI[i] = fs.nextInt() - 1; // Store 0-based index
                opX[i] = fs.nextLong();
            }

            long[] finalSum = new long[n];
            long[] count = new long[n];
            long[] delta = new long[n];

            // Process each operation
            for (int step = 0; step < q; step++) {
                int idx = opI[step];
                long newPos = opX[step];

                // Create a temporary array to track positions after the current operation
                long[] tempPos = Arrays.copyOf(initPos, n);
                tempPos[idx] = newPos;

                // Resolve collisions to the right
                for (int j = idx + 1; j < n; j++) {
                    if (tempPos[j] <= tempPos[j - 1]) {
                        tempPos[j] = tempPos[j - 1] + 1;
                    }
                }

                // Resolve collisions to the left
                for (int j = idx - 1; j >= 0; j--) {
                    if (tempPos[j] >= tempPos[j + 1]) {
                        tempPos[j] = tempPos[j + 1] - 1;
                    }
                }

                // Update sums and counts
                for (int i = 0; i < n; i++) {
                    finalSum[i] = (finalSum[i] + tempPos[i]) % MOD;
                }

                // Count how many times this operation affects each slider
                for (int i = 0; i < n; i++) {
                    if (tempPos[i] != initPos[i]) {
                        count[i]++;
                    }
                }
                
                // Adjust initial positions for the next iteration
                System.arraycopy(tempPos, 0, initPos, 0, n);
            }

            // Since each operation's result contributes to all permutations,
            // We multiply each resulting position sum by the number of permutations (q!)
            long factorial = 1;
            for (int i = 2; i <= q; i++) {
                factorial = (factorial * i) % MOD;
            }
            for (int i = 0; i < n; i++) {
                finalSum[i] = (finalSum[i] * factorial) % MOD;
                out.append(finalSum[i]).append(" ");
            }
            out.append("\n");
        }
        System.out.print(out.toString());
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