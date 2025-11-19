import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.NoSuchElementException;

class Main implements Runnable {
    public static void main(String[] args) {
        new Thread(null, new Main(), "", 1024 * 1024 * 1024).start();
    }

    long N;
    int M, A, B;
    long[] L, R;

    public void run() {
        FastScanner sc = FastScanner.getInstance();
        PrintWriter pw = new PrintWriter(System.out);

        N = sc.nextLong();
        M = sc.nextInt();
        A = sc.nextInt();
        B = sc.nextInt();
        L = new long[M];
        R = new long[M];
        for (int i = 0; i < M; i++) {
            L[i] = sc.nextLong();
            R[i] = sc.nextLong();
        }

        // If no bad squares, always possible
        if (M == 0) {
            pw.println("Yes");
            pw.flush();
            return;
        }

        // We will process intervals of good squares between bad intervals
        // plus the start and end segments

        // The maximum jump length is B, minimum is A
        // We can only move forward by steps in [A,B]

        // We'll keep track of reachable positions modulo (B)
        // Because max jump is small, we can use a boolean array of size B to represent reachable remainders
        // We simulate moving through good intervals and skipping bad intervals

        // Initialize reachable states at position 1
        // We represent reachable positions by their offset modulo B
        // At position 1, offset = (1-1) % B = 0 is reachable
        boolean[] reachable = new boolean[B];
        reachable[0] = true;

        long curPos = 1;

        for (int i = 0; i < M; i++) {
            long badL = L[i];
            long badR = R[i];

            // Good interval before this bad interval: [curPos, badL - 1]
            if (curPos <= badL - 1) {
                reachable = advance(reachable, badL - 1 - curPos + 1);
                curPos = badL;
            }

            // Now we are at bad interval [badL, badR], we cannot stand on these squares
            // We must jump over them

            long gap = badR - badL + 1;
            if (gap >= B) {
                // If the bad interval length >= B, no way to jump over it because max jump is B
                // We cannot land on bad squares, so no path
                pw.println("No");
                pw.flush();
                return;
            }

            // Try to jump over the bad interval
            // We need to check if from reachable states we can jump over gap length
            // i.e. from some reachable remainder r, there exists jump length j in [A,B]
            // such that (r + j) % B is reachable after skipping gap squares

            // We simulate the jump over the bad interval by shifting reachable states by jump length - gap
            // Because we cannot land on bad squares, we must jump at least gap+1 squares ahead

            boolean[] newReachable = new boolean[B];
            for (int r = 0; r < B; r++) {
                if (!reachable[r]) continue;
                // From remainder r, try all jumps j in [A,B]
                for (int j = A; j <= B; j++) {
                    // We jump j squares from current position
                    // But we must skip gap squares (bad interval)
                    // So actual jump over bad interval is j - gap
                    int nr = (r + j) % B;
                    // We can only land on good squares, so jump must be > gap
                    if (j > gap) {
                        newReachable[nr] = true;
                    }
                }
            }
            reachable = newReachable;
            curPos = badR + 1;
            if (curPos > N) {
                // We have passed beyond N, check if reachable includes position N
                // Position N offset:
                int offset = (int) ((N - 1) % B);
                pw.println(reachable[offset] ? "Yes" : "No");
                pw.flush();
                return;
            }
        }

        // After last bad interval, move to N if possible
        if (curPos <= N) {
            reachable = advance(reachable, N - curPos + 1);
        }

        int offset = (int) ((N - 1) % B);
        pw.println(reachable[offset] ? "Yes" : "No");
        pw.flush();
    }

    // Advance reachable states by length steps in good squares
    // We simulate steps of length steps, each step can be jump length in [A,B]
    // We use DP with boolean array of size B representing reachable remainders modulo B
    // We use fast exponentiation of the adjacency matrix representing transitions
    boolean[] advance(boolean[] reachable, long length) {
        if (length == 0) return reachable;

        // Build adjacency matrix of size B x B
        // adj[i][j] = true if from remainder i we can jump to remainder j in one step
        boolean[][] adj = new boolean[B][B];
        for (int i = 0; i < B; i++) {
            for (int jump = A; jump <= B; jump++) {
                int j = (i + jump) % B;
                adj[i][j] = true;
            }
        }

        // Use boolean matrix exponentiation to compute adj^length
        boolean[][] mat = matPow(adj, length);

        // Multiply mat by reachable vector
        boolean[] res = new boolean[B];
        for (int i = 0; i < B; i++) {
            if (!reachable[i]) continue;
            for (int j = 0; j < B; j++) {
                if (mat[i][j]) {
                    res[j] = true;
                }
            }
        }
        return res;
    }

    boolean[][] matMul(boolean[][] a, boolean[][] b) {
        int n = a.length;
        boolean[][] c = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            for (int k = 0; k < n; k++) {
                if (!a[i][k]) continue;
                for (int j = 0; j < n; j++) {
                    if (b[k][j]) {
                        c[i][j] = true;
                    }
                }
            }
        }
        return c;
    }

    boolean[][] matPow(boolean[][] a, long n) {
        int size = a.length;
        boolean[][] res = new boolean[size][size];
        for (int i = 0; i < size; i++) res[i][i] = true;
        boolean[][] base = a;
        while (n > 0) {
            if ((n & 1) == 1) {
                res = matMul(res, base);
            }
            base = matMul(base, base);
            n >>= 1;
        }
        return res;
    }
}

class FastScanner {
    private static FastScanner instance = null;

    private final InputStream in = System.in;
    private final byte[] buffer = new byte[1024];
    private int ptr = 0;
    private int buflen = 0;

    private FastScanner() {}

    public static FastScanner getInstance() {
        if (instance == null) {
            instance = new FastScanner();
        }
        return instance;
    }

    private boolean hasNextByte() {
        if (ptr < buflen) return true;
        ptr = 0;
        try {
            buflen = in.read(buffer);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return buflen > 0;
    }

    private int readByte() {
        if (hasNextByte()) return buffer[ptr++];
        else return -1;
    }

    private boolean isPrintableChar(int c) {
        return 33 <= c && c <= 126;
    }

    public boolean hasNext() {
        while (hasNextByte() && !isPrintableChar(buffer[ptr])) ptr++;
        return hasNextByte();
    }

    public String next() {
        if (!hasNext()) throw new NoSuchElementException();
        StringBuilder sb = new StringBuilder();
        int b = readByte();
        while (isPrintableChar(b)) {
            sb.appendCodePoint(b);
            b = readByte();
        }
        return sb.toString();
    }

    public long nextLong() {
        if (!hasNext()) throw new NoSuchElementException();
        long n = 0;
        boolean minus = false;
        int b = readByte();
        if (b == '-') {
            minus = true;
            b = readByte();
        }
        while (b >= '0' && b <= '9') {
            n = n * 10 + (b - '0');
            b = readByte();
        }
        return minus ? -n : n;
    }

    public int nextInt() {
        return (int) nextLong();
    }
}