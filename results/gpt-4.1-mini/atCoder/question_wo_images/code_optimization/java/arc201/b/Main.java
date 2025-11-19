import java.io.*;
import java.util.*;

public class Main {

    private static final int MAX_X = 60;

    private static final class FastScanner {
        private final byte[] buf = new byte[1 << 16];
        private int len = 0, ptr = 0;
        private final InputStream in;
        FastScanner(InputStream in) { this.in = in; }
        private int readByte() throws IOException {
            if (ptr >= len) {
                len = in.read(buf);
                ptr = 0;
                if (len <= 0) return -1;
            }
            return buf[ptr++];
        }
        long nextLong() throws IOException {
            int c;
            do { c = readByte(); } while (c <= 32);
            boolean neg = false;
            if (c == '-') { neg = true; c = readByte(); }
            long val = 0;
            while (c > 32) {
                val = val * 10 + (c - '0');
                c = readByte();
            }
            return neg ? -val : val;
        }
        int nextInt() throws IOException { return (int) nextLong(); }
    }

    // State class to hold weight and value pairs
    private static final class State {
        long w, v;
        State(long w, long v) { this.w = w; this.v = v; }
    }

    // Compress states by sorting by weight and keeping only states with strictly increasing value
    private static ArrayList<State> compress(List<State> src) {
        src.sort(Comparator.comparingLong(s -> s.w));
        ArrayList<State> res = new ArrayList<>(src.size());
        long bestVal = -1;
        for (State st : src) {
            if (st.v > bestVal) {
                res.add(st);
                bestVal = st.v;
            }
        }
        return res;
    }

    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner(System.in);
        StringBuilder out = new StringBuilder();

        int T = fs.nextInt();

        // Since sum of N over all test cases is at most 2*10^5, we can process each test case efficiently.

        while (T-- > 0) {
            int N = fs.nextInt();
            long W = fs.nextLong();

            // Buckets for values by weight exponent
            ArrayList<Integer>[] bucket = new ArrayList[MAX_X];
            for (int i = 0; i < MAX_X; i++) bucket[i] = new ArrayList<>();

            for (int i = 0; i < N; i++) {
                int x = fs.nextInt();
                int y = fs.nextInt();
                bucket[x].add(y);
            }

            // Sort each bucket descending to pick top values first
            for (int i = 0; i < MAX_X; i++) {
                if (!bucket[i].isEmpty()) {
                    bucket[i].sort(Collections.reverseOrder());
                }
            }

            // dp holds states of (weight, value)
            ArrayList<State> dp = new ArrayList<>();
            dp.add(new State(0, 0));

            // For each weight class, we combine dp with possible picks from that class
            for (int x = 0; x < MAX_X; x++) {
                if (bucket[x].isEmpty()) continue;

                long wUnit = 1L << x;
                int m = bucket[x].size();

                // Prefix sums of values for quick sum calculation
                long[] pref = new long[m + 1];
                for (int i = 0; i < m; i++) {
                    pref[i + 1] = pref[i] + bucket[x].get(i);
                }

                // Instead of naive O(dp.size() * m), we optimize by:
                // For each dp state, we can pick 0..k items from current bucket,
                // but picking all k items is equivalent to adding (k * wUnit, pref[k]) to dp state.
                // We will merge all these new states and compress.

                // To avoid large complexity, we use a two-pointer merge approach:
                // We generate all possible new states from current bucket (0..m items),
                // then merge with dp states.

                // Generate all possible increments from current bucket
                ArrayList<State> addStates = new ArrayList<>(m + 1);
                for (int k = 0; k <= m; k++) {
                    addStates.add(new State(wUnit * k, pref[k]));
                }

                // Merge dp and addStates to form new dp
                ArrayList<State> next = new ArrayList<>(dp.size() * addStates.size());

                // We will do a convolution-like merge:
                // For each dp state, combine with each addState
                // But this is O(dp.size() * addStates.size()), which can be large.

                // Optimization:
                // Since dp and addStates are sorted by weight (dp is compressed and sorted, addStates is sorted by weight),
                // we can do a "knapsack-like" merge using a two-pointer approach.

                // However, the problem is that we need all combinations, so two-pointer merge is not straightforward.

                // Instead, we use a meet-in-the-middle approach:
                // We can process addStates in increasing order and for each dp state,
                // we can add the addState weight and value.

                // To optimize, we process dp states in order and for each addState,
                // we add dp.w + addState.w and dp.v + addState.v.

                // Since dp size and addStates size are manageable (dp compressed), this is acceptable.

                // We'll do nested loops but with compressed dp, it should be efficient.

                // To further optimize, we can process addStates in increasing order and for each dp state,
                // we can break early if weight exceeds W.

                // But since W can be large, we just generate all and compress later.

                for (State st : dp) {
                    long baseW = st.w;
                    long baseV = st.v;
                    for (State add : addStates) {
                        long nw = baseW + add.w;
                        if (nw > W) break; // Since addStates sorted by weight, no need to continue
                        long nv = baseV + add.v;
                        next.add(new State(nw, nv));
                    }
                }

                dp = compress(next);
            }

            // Find best value with weight <= W
            long best = 0;
            for (State st : dp) {
                if (st.w <= W && st.v > best) best = st.v;
            }

            out.append(best).append('\n');
        }

        System.out.print(out);
    }
}