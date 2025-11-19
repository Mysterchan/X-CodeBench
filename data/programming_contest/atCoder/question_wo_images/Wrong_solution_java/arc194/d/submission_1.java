import java.io.*;
import java.util.*;

public class Main {
    static final int MOD = 998244353;
    static final int MAX_N = 5005;

    static long[][] dp = new long[MAX_N][MAX_N];
    static long[][] C = new long[MAX_N][MAX_N];
    static long[] inv = new long[MAX_N];
    static long[] fac = new long[MAX_N];

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        PrintWriter out = new PrintWriter(System.out);

        int n = scanner.nextInt();
        String s = scanner.next();

        init();

        dp[0][0] = 1;

        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '(') {
                cnt++;
            } else {
                cnt--;
            }

            for (int j = i; j >= 0; j--) {
                if (cnt + j <= i) {
                    dp[i + 1][cnt + j] += dp[j][cnt];
                    dp[i + 1][cnt + j] %= MOD;
                }
            }
        }

        long ans = 0;
        for (int i = 0; i <= n / 2; i++) {
            ans += dp[n][i] * C[n / 2][i] % MOD * fac[i] % MOD;
            ans %= MOD;
        }

        out.println(ans);

        out.close();
    }

    static void init() {
        fac[0] = 1;
        for (int i = 1; i < MAX_N; i++) {
            fac[i] = fac[i - 1] * i % MOD;
        }

        inv[0] = 1;
        for (int i = 1; i < MAX_N; i++) {
            inv[i] = qpow(i, MOD - 2);
        }

        for (int i = 0; i < MAX_N; i++) {
            C[i][0] = 1;
            for (int j = 1; j <= i; j++) {
                C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
            }
        }
    }

    static long qpow(long a, long b) {
        long res = 1;
        while (b > 0) {
            if ((b & 1) > 0) {
                res = res * a % MOD;
            }
            a = a * a % MOD;
            b >>= 1;
        }
        return res;
    }
}