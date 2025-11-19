import java.util.*;
import java.io.*;

public class Main {
    static final int MOD = 998244353;
    static final int MAXN = 5005;
    static long[][] dp = new long[MAXN][MAXN];
    static long[][] C = new long[MAXN][MAXN];

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

    static long inv(long x) {
        return qpow(x, MOD - 2);
    }

    static void init() {
        for (int i = 0; i < MAXN; i++) {
            C[i][0] = 1;
            for (int j = 1; j <= i; j++) {
                C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
            }
        }
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
        init();
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
        long ans = dp[cnt][n / 2];
        for (int i = 1; i <= n / 2; i++) {
            ans = ans * 2 % MOD;
        }
        pw.println(ans);
        pw.close();
    }
}