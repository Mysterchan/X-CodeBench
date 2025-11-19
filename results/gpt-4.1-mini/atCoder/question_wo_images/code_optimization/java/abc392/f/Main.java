import java.io.*;
import java.util.*;

public class Main {
    static class BIT {
        int n;
        int[] bit;

        BIT(int n) {
            this.n = n;
            bit = new int[n + 2];
        }

        void add(int i, int v) {
            while (i <= n) {
                bit[i] += v;
                i += i & (-i);
            }
        }

        int sum(int i) {
            int s = 0;
            while (i > 0) {
                s += bit[i];
                i -= i & (-i);
            }
            return s;
        }

        // Find the smallest index with prefix sum >= x
        int lowerBound(int x) {
            int pos = 0;
            int bitMask = Integer.highestOneBit(n);
            while (bitMask != 0) {
                int nextPos = pos + bitMask;
                if (nextPos <= n && bit[nextPos] < x) {
                    x -= bit[nextPos];
                    pos = nextPos;
                }
                bitMask >>= 1;
            }
            return pos + 1;
        }
    }

    public static void main(String[] args) throws IOException {
        FastScanner sc = new FastScanner();
        int N = sc.nextInt();
        int[] P = new int[N];
        for (int i = 0; i < N; i++) {
            P[i] = sc.nextInt();
        }

        BIT bit = new BIT(N);
        for (int i = 1; i <= N; i++) {
            bit.add(i, 1);
        }

        int[] ans = new int[N];
        // Process from last to first
        for (int i = N - 1; i >= 0; i--) {
            int pos = bit.lowerBound(P[i]);
            ans[pos - 1] = i + 1;
            bit.add(pos, -1);
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            sb.append(ans[i]).append(' ');
        }
        System.out.println(sb);
    }

    static class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        FastScanner() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    String line = br.readLine();
                    if (line == null) return null;
                    st = new StringTokenizer(line);
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }
    }
}