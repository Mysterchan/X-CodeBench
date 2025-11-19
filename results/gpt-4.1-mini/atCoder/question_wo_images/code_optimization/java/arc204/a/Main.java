import java.io.IOException;
import java.io.InputStream;
import java.util.NoSuchElementException;

public class Main {
    static final int MOD = 998244353;

    public static void main(String[] args) {
        new Main().solve();
    }

    public void solve() {
        FastScanner sc = new FastScanner(System.in);
        int N = sc.nextInt();
        int L = sc.nextInt();
        int R = sc.nextInt();
        int[] A = sc.nextIntArray(N);
        int[] B = sc.nextIntArray(N);

        // dp[j]: number of ways with j elements currently in Q
        int[] dp = new int[N + 1];
        dp[0] = 1;

        // We will track the possible C values using offset technique:
        // The value of C after i insertions and j removals is:
        // C = sum(B of removed) - sum(A of inserted)
        // But since C is max(0, C - A[i]) after insertion, we need to track the minimal C=0 cutoff.
        // The original problem is complex, but the given solution uses a DP over counts of inserted and removed,
        // and a binary state to represent whether the final C is in [L,R].
        // We can optimize by using prefix sums and a 2D DP with only two states.

        // Precompute prefix sums of A and B
        int[] cumA = new int[N + 1];
        int[] cumB = new int[N + 1];
        for (int i = 0; i < N; i++) {
            cumA[i + 1] = cumA[i] + A[i];
            cumB[i + 1] = cumB[i] + B[i];
        }

        // The maximum possible sum of B is up to 5000*5000=25,000,000, which is too large for direct DP on C.
        // The original code cleverly uses a DP on counts and a binary state to represent if final C in [L,R].
        // We'll replicate that logic but optimize the DP transitions.

        // dp[ai][bi][state]: number of ways after ai insertions and bi removals,
        // state=0 means final C < L, state=1 means final C in [L,R], else 0 ways.
        // We'll use two 2D arrays and swap them to save memory and improve cache locality.

        int[][] dp0 = new int[N + 1][N + 1];
        int[][] dp1 = new int[N + 1][N + 1];

        // Initialize dp for (0,0)
        int tot = cumB[N] - cumA[N];
        if (R < tot) {
            dp0[0][0] = 0;
            dp1[0][0] = 0;
        } else if (L <= tot) {
            dp0[0][0] = 0;
            dp1[0][0] = 1;
        } else {
            dp0[0][0] = 1;
            dp1[0][0] = 0;
        }

        // We'll fill dp row by row for ai from 0 to N, and bi from 0 to ai
        // Use prefix sums to speed up transitions

        for (int ai = 0; ai <= N; ai++) {
            for (int bi = 0; bi <= ai; bi++) {
                if (ai == 0 && bi == 0) continue;
                int sum = cumB[bi] - cumA[ai];
                int lessThanL = (tot - sum) < L ? 1 : 0;
                int inRange = (L <= tot - sum && tot - sum <= R) ? 1 : 0;
                // dp0 = count of ways with final C < L
                // dp1 = count of ways with final C in [L,R]

                dp0[ai][bi] = 0;
                dp1[ai][bi] = 0;

                if (lessThanL == 1) {
                    // final C < L, all ways go to dp0
                    if (ai > bi) {
                        dp0[ai][bi] = modAdd(dp0[ai][bi], dp0[ai - 1][bi]);
                        dp0[ai][bi] = modAdd(dp0[ai][bi], dp1[ai - 1][bi]);
                    }
                    if (bi > 0) {
                        dp0[ai][bi] = modAdd(dp0[ai][bi], dp0[ai][bi - 1]);
                        dp0[ai][bi] = modAdd(dp0[ai][bi], dp1[ai][bi - 1]);
                    }
                } else if (inRange == 1) {
                    // final C in [L,R], all ways go to dp1
                    if (ai > bi) {
                        dp1[ai][bi] = modAdd(dp1[ai][bi], dp0[ai - 1][bi]);
                        dp1[ai][bi] = modAdd(dp1[ai][bi], dp1[ai - 1][bi]);
                    }
                    if (bi > 0) {
                        dp1[ai][bi] = modAdd(dp1[ai][bi], dp0[ai][bi - 1]);
                        dp1[ai][bi] = modAdd(dp1[ai][bi], dp1[ai][bi - 1]);
                    }
                } else {
                    // final C > R, all ways go to dp0 (invalid)
                    if (ai > bi) {
                        dp0[ai][bi] = modAdd(dp0[ai][bi], dp0[ai - 1][bi]);
                        dp0[ai][bi] = modAdd(dp0[ai][bi], dp1[ai - 1][bi]);
                    }
                    if (bi > 0) {
                        dp0[ai][bi] = modAdd(dp0[ai][bi], dp0[ai][bi - 1]);
                        dp0[ai][bi] = modAdd(dp0[ai][bi], dp1[ai][bi - 1]);
                    }
                }
            }
        }

        System.out.println(dp1[N][N]);
    }

    int modAdd(int a, int b) {
        a += b;
        if (a >= MOD) a -= MOD;
        return a;
    }
}

class FastScanner {
    private final InputStream in;
    private final byte[] buf = new byte[1 << 15];
    private int ptr = 0, buflen = 0;

    FastScanner(InputStream source) {
        this.in = source;
    }

    private boolean hasNextByte() {
        if (ptr < buflen) return true;
        ptr = 0;
        try {
            buflen = in.read(buf);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return buflen > 0;
    }

    private int readByte() {
        return hasNextByte() ? buf[ptr++] : -1;
    }

    private static boolean isPrintableChar(int c) {
        return 33 <= c && c <= 126;
    }

    private void skipUnprintable() {
        while (hasNextByte() && !isPrintableChar(buf[ptr])) ptr++;
    }

    public boolean hasNext() {
        skipUnprintable();
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

    public int nextInt() {
        return (int) nextLong();
    }

    public long nextLong() {
        if (!hasNext()) throw new NoSuchElementException();
        long num = 0;
        boolean minus = false;
        int b = readByte();
        if (b == '-') {
            minus = true;
            b = readByte();
        }
        if (b < '0' || b > '9') throw new NumberFormatException();
        while (true) {
            if ('0' <= b && b <= '9') {
                num = num * 10 + b - '0';
            } else {
                return minus ? -num : num;
            }
            b = readByte();
        }
    }

    public int[] nextIntArray(int n) {
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = nextInt();
        return arr;
    }
}