import java.io.IOException;
import java.io.InputStream;
import java.util.NoSuchElementException;
import java.util.function.IntUnaryOperator;

public class Main {
    public static void main(String[] args) {
        Main o = new Main();
        o.solve();
    }

    static final int MOD = 998244353;

    public void solve() {
        FastScanner sc = new FastScanner(System.in);
        int N = sc.nextInt();
        int L = sc.nextInt();
        int R = sc.nextInt();
        int[] A = sc.nextIntArray(N);
        int[] B = sc.nextIntArray(N);

        int[] cumB = new int[N + 1];
        for (int i = 0; i < N; i++) {
            cumB[i + 1] = cumB[i] + B[i];
        }

        long[][] dp = new long[N + 1][N + 1];
        dp[0][0] = 1; // One way to perform no operations
        
        for (int ai = 0; ai <= N; ai++) {
            for (int bi = 0; bi <= ai; bi++) {
                if (ai > 0) {
                    dp[ai][bi] = (dp[ai][bi] + dp[ai - 1][bi]) % MOD; // Use action 1
                }
                if (bi > 0) {
                    dp[ai][bi] = (dp[ai][bi] + dp[ai][bi - 1]) % MOD; // Use action 2
                }
            }
        }
        
        long totalWays = 0;
        for (int bi = 0; bi <= N; bi++) {
            int finalC = cumB[bi] - (N * 5000 - bi); // The maximum possible C with bi insertions
            if (finalC >= L && finalC <= R) {
                totalWays = (totalWays + dp[N][bi]) % MOD;
            }
        }

        System.out.println(totalWays);
    }

    public static class FastScanner {
        private final InputStream in;
        private final byte[] buf = new byte[1024];
        private int ptr = 0;
        private int buflen = 0;

        FastScanner(InputStream source) {
            this.in = source;
        }

        private boolean hasNextByte() {
            if (ptr < buflen) return true;
            else {
                ptr = 0;
                try {
                    buflen = in.read(buf);
                } catch (IOException e) {
                    e.printStackTrace();
                }
                return buflen > 0;
            }
        }

        private int readByte() {
            if (hasNextByte()) return buf[ptr++];
            else return -1;
        }

        private boolean isPrintableChar(int c) {
            return 33 <= c && c <= 126;
        }

        public boolean hasNext() {
            skipToNextPrintableChar();
            return hasNextByte();
        }

        public String next() {
            if (!hasNext()) throw new NoSuchElementException();
            StringBuilder ret = new StringBuilder();
            int b = readByte();
            while (isPrintableChar(b)) {
                ret.appendCodePoint(b);
                b = readByte();
            }
            return ret.toString();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

        public int[] nextIntArray(int N) {
            return nextIntArray(N, n -> n);
        }

        public int[] nextIntArray(int N, IntUnaryOperator conv) {
            int[] ret = new int[N];
            for (int i = 0; i < N; i++)
                ret[i] = conv.applyAsInt(nextInt());
            return ret;
        }
    }
}