import java.io.*;
import java.util.*;

public class Main {

    static class FastScanner {
        BufferedReader br;
        StringTokenizer st;
        FastScanner(InputStream in) { br = new BufferedReader(new InputStreamReader(in)); }
        String next() {
            while (st == null || !st.hasMoreTokens()) {
                try { st = new StringTokenizer(br.readLine()); }
                catch (IOException e) { throw new RuntimeException(e); }
            }
            return st.nextToken();
        }
        int nextInt() { return Integer.parseInt(next()); }
        long nextLong() { return Long.parseLong(next()); }
        String nextLine() {
            try { return br.readLine(); }
            catch (IOException e) { throw new RuntimeException(e); }
        }
    }

    static void solve(FastScanner sc) {
        int n = sc.nextInt();
        int m = sc.nextInt();
        int k = sc.nextInt();

        String[] grid = new String[n];
        for (int i = 0; i < n; i++) grid[i] = sc.next();

        long[][] prefix = new long[n + 1][m + 1];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                prefix[i + 1][j + 1] = prefix[i + 1][j] + prefix[i][j + 1] - prefix[i][j] + (grid[i].charAt(j) == 'g' ? 1 : 0);
            }
        }

        long totalGold = 0;
        for (String row : grid)
            for (char c : row.toCharArray())
                if (c == 'g') totalGold++;

        long minGoldInside = Long.MAX_VALUE;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i].charAt(j) != '.') continue;

                int x1 = Math.max(0, i - k);
                int y1 = Math.max(0, j - k);
                int x2 = Math.min(n, i + k + 1);
                int y2 = Math.min(m, j + k + 1);

                long goldInside = prefix[x2][y2] - prefix[x2][y1] - prefix[x1][y2] + prefix[x1][y1];
                minGoldInside = Math.min(minGoldInside, goldInside);
            }
        }

        System.out.println(totalGold - minGoldInside);
    }

    public static void main(String[] args) {
        FastScanner sc = new FastScanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) solve(sc);
    }
}
