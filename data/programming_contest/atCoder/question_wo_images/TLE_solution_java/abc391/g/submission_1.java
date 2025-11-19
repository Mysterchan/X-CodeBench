import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Set;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.TreeSet;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.InputStream;

public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        FastScanner in = new FastScanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        G_ManyLCS solver = new G_ManyLCS();
        solver.solve(1, in, out);
        out.close();
    }

    static class G_ManyLCS {
        public void solve(int testNumber, FastScanner in, PrintWriter out) {
            final int MOD = 998244353;
            int n = in.nextInt();
            int m = in.nextInt();
            char[] s = in.next().toCharArray();

            int[] maxState = new int[n];
            for (int i = 0; i < n; i++) {
                maxState[i] = i + 1;
            }
            int numStates = encode(maxState) + 1;

            int[] d = new int[numStates];
            int[] nd = new int[numStates];
            int[] state = new int[n];
            int[] nstate = new int[n];
            Set<Integer> nz = new TreeSet<>();
            d[0] = 1;
            nz.add(0);
            for (int len = 1; len <= m; len++) {
                Arrays.fill(nd, 0);
                Set<Integer> nnz = new TreeSet<>();
                for (int code : nz) {
                    decode(code, state);
                    for (int c = 0; c < 26; c++) {
                        int ncode = -1;
                        int max = 0;
                        for (int i = 0; i < n; i++) {
                            if (s[i] == (char) (c + 'a')) {
                                nstate[i] = Math.max(state[i], max + 1);
                            } else {
                                nstate[i] = Math.max(state[i], max + 0);
                            }
                            if (i > 0) {
                                nstate[i] = Math.max(nstate[i], nstate[i - 1]);
                            }
                            max = Math.max(max, state[i]);
                        }
                        ncode = encode(nstate);
                        nd[ncode] += d[code];
                        nnz.add(ncode);
                        if (nd[ncode] >= MOD) {
                            nd[ncode] -= MOD;
                        }
                    }
                }
                int[] t = d;
                d = nd;
                nd = t;
                nz = nnz;
            }

            int[] ans = new int[n + 1];
            for (int code = 0; code < d.length; code++) {
                if (d[code] == 0) {
                    continue;
                }
                decode(code, state);
                int max = 0;
                for (int i = 0; i < n; i++) {
                    max = Math.max(max, state[i]);
                }
                ans[max] += d[code];
                if (ans[max] >= MOD) {
                    ans[max] -= MOD;
                }
            }

            for (int i = 0; i < ans.length; i++) {
                if (i > 0) {
                    out.print(" ");
                }
                out.print(ans[i]);
            }
            out.println();
        }

        int encode(int[] state) {
            int code = 0;
            for (int i = 0; i < state.length; i++) {
                code = (i + 2) * code + state[i];
            }
            return code;
        }

        void decode(int code, int[] state) {
            for (int i = state.length - 1; i >= 0; i--) {
                state[i] = code % (i + 2);
                code /= i + 2;
            }
        }

    }

    static class FastScanner {
        private BufferedReader in;
        private StringTokenizer st;

        public FastScanner(InputStream stream) {
            in = new BufferedReader(new InputStreamReader(stream));
        }

        public String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(in.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return st.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

    }
}