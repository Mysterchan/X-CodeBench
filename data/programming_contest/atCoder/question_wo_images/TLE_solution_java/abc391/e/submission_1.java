import java.io.*;
import java.util.*;

public class Main {
    static class MyScanner {
        static BufferedReader r;
        static StringTokenizer st;
        public MyScanner() {
            r = new BufferedReader(new InputStreamReader(System.in));
        }
        public String next() {
            try {
                while (st == null || !st.hasMoreTokens()) {
                    st = new StringTokenizer(r.readLine());
                }
                return st.nextToken();
            } catch (Exception e) {
                return null;
            }
        }
        public int nextInt() {
            return Integer.parseInt(next());
        }
        public long nextLong() {
            return Long.parseLong(next());
        }
        public double nextDouble() {
            return Double.parseDouble(next());
        }
    }
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static MyScanner sc = new MyScanner();
    static final int MAXN = 1600000;
    static int N;
    static int[] a = new int[MAXN], p = new int[15];
    static int[][][] dp = new int[MAXN][15][2];
    public static void main(String[] args) throws IOException {
        N = sc.nextInt();
        p[0] = 1;
        for (int i = 1; i <= 14; i++) {
            p[i] = p[i - 1] * 3;
        }
        char[] t = sc.next().toCharArray();
        for (int i = 1; i <= p[N]; i++) {
            a[i] = t[i - 1] == '1' ? 1 : 0;
        }
        for (int i = 1; i <= p[N]; i++) {
            dp[i][0][a[i]] = 0;
            dp[i][0][a[i] ^ 1] = 1;
        }
        int cnt = 0;
        ArrayList<Integer> one = new ArrayList<>(), zero = new ArrayList<>();
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= p[N]; j += p[i]) {
                one.clear();
                zero.clear();
                for (int k = j; k < j + p[i]; k += p[i - 1]) {
                    one.add(dp[k][i - 1][1]);
                    zero.add(dp[k][i - 1][0]);
                    cnt++;
                }
                one.sort((o1, o2) -> o1 - o2);
                zero.sort((o1, o2) -> o1 - o2);
                for (int k = 0; k < Math.min(2, one.size()); k++) {
                    dp[j][i][0] += zero.get(k);
                    dp[j][i][1] += one.get(k);
                }
            }
        }
        int d = dfs(1, p[N], N);
        bw.write(dp[1][N][d ^ 1] + "");
        bw.flush();
    }

    private static int dfs(int l, int r, int n) {

        if (l == r) return a[l];
        int one = 0, zer = 0;
        for (int i = l; i <= r; i += p[n - 1]) {
            if (dfs(i, i + p[n - 1] - 1, n - 1) == 1) one++;
            else zer++;
        }

        return (one >= zer ? 1 : 0);
    }
}