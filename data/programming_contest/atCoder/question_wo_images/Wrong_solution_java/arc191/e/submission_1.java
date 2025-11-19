import java.util.*;
import java.io.*;

public class Main {
    static final long MOD = 998244353;
    static final long INF = (long) 1e18;
    static final int N = (int) 2e5 + 5;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        long x = Long.parseLong(st.nextToken());
        long y = Long.parseLong(st.nextToken());

        long[][] a = new long[n][2];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            a[i][0] = Long.parseLong(st.nextToken());
            a[i][1] = Long.parseLong(st.nextToken());
        }

        long[] dp = new long[n + 1];
        dp[0] = 1;
        for (int i = 1; i <= n; i++) {
            dp[i] = (dp[i - 1] * 2) % MOD;
        }

        long[] sg = new long[n];
        for (int i = 0; i < n; i++) {
            long g = 0;
            long r = a[i][1];
            long k = a[i][0];
            while (k-- > 0) {
                g ^= mex(r);
                r += x;
            }
            sg[i] = g;
        }

        Arrays.sort(sg);
        long ans = 0;
        for (int i = 0; i < n; i++) {
            if (sg[i] != 0) {
                ans = (ans + dp[n - i - 1]) % MOD;
            }
        }

        pw.println(ans);
        pw.close();
    }

    static long mex(long x) {
        if (x == 0) return 0;
        if (x % 2 == 1) return 0;
        long y = x / 2;
        if (y % 2 == 0) return 1;
        return 2 * mex(y) + 1;
    }
}