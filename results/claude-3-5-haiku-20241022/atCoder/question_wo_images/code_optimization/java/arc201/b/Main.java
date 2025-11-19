import java.io.*;
import java.util.*;

public class Main {

    private static final class State {
        long w;
        long v;
        State(long w, long v) { this.w = w; this.v = v; }
    }

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

    private static ArrayList<State> compress(List<State> src) {
        src.sort(Comparator.comparingLong(s -> s.w));
        ArrayList<State> res = new ArrayList<>();
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
        while (T-- > 0) {
            int N   = fs.nextInt();
            long W  = fs.nextLong();

            ArrayList<Integer>[] bucket = new ArrayList[MAX_X];
            for (int i = 0; i < MAX_X; i++) bucket[i] = new ArrayList<>();

            for (int i = 0; i < N; i++) {
                int x = fs.nextInt();
                int y = fs.nextInt();
                bucket[x].add(y);
            }

            for (ArrayList<Integer> b : bucket) {
                if (!b.isEmpty()) b.sort(Collections.reverseOrder());
            }

            ArrayList<State> dp = new ArrayList<>();
            dp.add(new State(0, 0));

            for (int x = 0; x < MAX_X; x++) {
                if (bucket[x].isEmpty()) continue;

                long wUnit = 1L << x;
                int m      = bucket[x].size();

                long[] pref = new long[m + 1];
                for (int i = 0; i < m; i++) pref[i + 1] = pref[i] + bucket[x].get(i);

                ArrayList<State> next = new ArrayList<>();

                for (State st : dp) {
                    long baseW = st.w, baseV = st.v;
                    long kMax  = Math.min((W - baseW) / wUnit, m);
                    
                    for (int k = 0; k <= kMax; k++) {
                        next.add(new State(baseW + wUnit * k, baseV + pref[k]));
                    }
                }
                dp = compress(next);
            }

            long best = 0;
            for (State st : dp) best = Math.max(best, st.v);

            out.append(best).append('\n');
        }
        System.out.print(out.toString());
    }
}