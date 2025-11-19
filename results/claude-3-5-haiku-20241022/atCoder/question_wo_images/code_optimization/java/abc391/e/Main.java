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
    }
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static MyScanner sc = new MyScanner();
    static final int MAXN = 1600000;
    static int N;
    static int[] a = new int[MAXN], p = new int[15];
    static int[][][] dp = new int[MAXN][15][2];
    static Map<Long, Integer> memo = new HashMap<>();
    
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
        
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= p[N]; j += p[i]) {
                int min1_zero = Integer.MAX_VALUE, min2_zero = Integer.MAX_VALUE;
                int min1_one = Integer.MAX_VALUE, min2_one = Integer.MAX_VALUE;
                
                for (int k = j; k < j + p[i]; k += p[i - 1]) {
                    int val0 = dp[k][i - 1][0];
                    int val1 = dp[k][i - 1][1];
                    
                    if (val0 < min1_zero) {
                        min2_zero = min1_zero;
                        min1_zero = val0;
                    } else if (val0 < min2_zero) {
                        min2_zero = val0;
                    }
                    
                    if (val1 < min1_one) {
                        min2_one = min1_one;
                        min1_one = val1;
                    } else if (val1 < min2_one) {
                        min2_one = val1;
                    }
                }
                
                dp[j][i][0] = min1_zero + min2_zero;
                dp[j][i][1] = min1_one + min2_one;
            }
        }
        int d = dfs(1, p[N], N);
        bw.write(dp[1][N][d ^ 1] + "");
        bw.flush();
    }

    private static int dfs(int l, int r, int n) {
        if (l == r) return a[l];
        
        long key = ((long)l << 32) | ((long)r << 16) | n;
        if (memo.containsKey(key)) {
            return memo.get(key);
        }
        
        int one = 0;
        for (int i = l; i <= r; i += p[n - 1]) {
            if (dfs(i, i + p[n - 1] - 1, n - 1) == 1) one++;
        }
        
        int result = (one >= 2 ? 1 : 0);
        memo.put(key, result);
        return result;
    }
}