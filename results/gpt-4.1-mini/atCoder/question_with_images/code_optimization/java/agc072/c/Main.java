import java.util.*;
import java.io.*;

public class Main {
    static FastReader sc;
    static PrintWriter out;

    public static void main(String[] args) throws IOException {
        sc = new FastReader();
        out = new PrintWriter(System.out);

        solve();
        out.flush();
    }

    static void solve() {
        int n = sc.nextInt();
        long k = sc.nextLong();

        // The path length is 2N-2 moves: N-1 downs and N-1 rights.
        // The problem reduces to finding the K-th path in the order defined by the problem.
        // The order is lex order with 'D' preferred when counts are equal.
        // This is equivalent to enumerating all paths from (1,1) to (N,N) with moves D and R,
        // where at each step, if counts are equal, choose D first.
        // So the K-th path is the K-th lex path with 'D' < 'R'.

        // We can use combinatorics to find the K-th path:
        // At each step, if we have d downs and r rights left,
        // number of paths starting with D is C(d+r-1, d-1)
        // If K <= that number, choose D, else choose R and subtract that number from K.

        int down = n - 1;
        int right = n - 1;

        // Precompute combinations using Pascal's triangle or DP
        // Since n <= 100, we can store all combinations in long[][] comb
        long[][] comb = new long[2 * n][2 * n];
        for (int i = 0; i < 2 * n; i++) {
            comb[i][0] = 1;
            for (int j = 1; j <= i; j++) {
                comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j];
                if (comb[i][j] > 1_000_000_000_000_000_000L) // cap to avoid overflow
                    comb[i][j] = 1_000_000_000_000_000_000L;
            }
        }

        StringBuilder sb = new StringBuilder();

        while (down > 0 && right > 0) {
            // Number of paths if we choose D first:
            // We have down-1 downs left and right rights left
            long count = comb[down + right - 1][down - 1];
            if (k <= count) {
                sb.append('D');
                down--;
            } else {
                sb.append('R');
                k -= count;
                right--;
            }
        }

        // Append remaining moves
        while (down-- > 0) sb.append('D');
        while (right-- > 0) sb.append('R');

        out.println(sb.toString());
    }

    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    String line = br.readLine();
                    if (line == null) return null;
                    st = new StringTokenizer(line);
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }
    }
}