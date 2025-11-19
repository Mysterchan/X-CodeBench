import java.util.*;
import java.io.*;

public class Main {
    static final int MOD = 998244353;
    static final int MAXN = 2505;
    static long[][] dp = new long[MAXN][MAXN];

    static long qpow(long x, long y) {
        long res = 1;
        while (y > 0) {
            if ((y & 1) == 1) {
                res = res * x % MOD;
            }
            x = x * x % MOD;
            y >>= 1;
        }
        return res;
    }

    static void init() {
        dp[0][0] = 1;
        for (int i = 1; i < MAXN; i++) {
            dp[i][0] = 1;
            for (int j = 1; j <= i; j++) {
                for (int k = 0; k < i; k++) {
                    dp[i][j] = (dp[i][j] + dp[k][j - 1] * dp[i - 1 - k][j - 1]) % MOD;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);
        
        int n = Integer.parseInt(br.readLine());
        String s = br.readLine();
        
        int cnt = 0;
        int now = 0;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '(') {
                now++;
            } else {
                now--;
            }
            if (now == 0) {
                cnt++;
            }
        }
        
        // Only initialize what we need
        int maxNeeded = Math.max(cnt, n / 2) + 1;
        dp[0][0] = 1;
        for (int i = 1; i <= maxNeeded; i++) {
            dp[i][0] = 1;
            for (int j = 1; j <= Math.min(i, n / 2); j++) {
                for (int k = 0; k < i; k++) {
                    dp[i][j] = (dp[i][j] + dp[k][j - 1] * dp[i - 1 - k][j - 1]) % MOD;
                }
            }
        }
        
        long ans = dp[cnt][n / 2];
        ans = ans * qpow(2, n / 2) % MOD;
        
        pw.println(ans);
        pw.close();
    }
}