import java.util.*;
import java.io.*;

public class Main {
    static final int N = 1005;
    static final int mod = 998244353;
    static int n, m;
    static int[] a = new int[N];
    static int[][] fac = new int[N][N];
    static int[] cnt = new int[N];
    static int[][] dp = new int[N][N];
    static int[] cur = new int[N];

    static int qpow(int x, int y) {
        int res = 1;
        while (y > 0) {
            if ((y & 1) == 1) res = (int) ((long) res * x % mod);
            x = (int) ((long) x * x % mod);
            y >>= 1;
        }
        return res;
    }

    static void init() {
        for (int i = 1; i <= 1000; i++) {
            for (int j = 1; j <= i; j++) {
                if (i % j == 0) {
                    fac[i][++fac[i][0]] = j;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        init();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        String[] str = br.readLine().split(" ");
        for (int i = 1; i < n; i++) {
            a[i] = Integer.parseInt(str[i - 1]);
        }
        for (int i = 1; i < n; i++) {
            for (int j = 1; j <= fac[a[i]][0]; j++) {
                int x = fac[a[i]][j];
                cnt[j] = x * fac[a[i]][j + 1];
            }
            for (int j = 1; j <= fac[a[i]][0]; j++) {
                for (int k = 1; k <= fac[a[i]][0]; k++) {
                    dp[j][k] = (int) ((long) dp[j][k] * qpow(fac[a[i]][k], cnt[j]) % mod);
                }
            }
            for (int j = 1; j <= fac[a[i]][0]; j++) {
                for (int k = 1; k <= fac[a[i]][0]; k++) {
                    dp[j][k] = (dp[j][k] + (int) ((long) cur[k] * fac[a[i]][j] % mod)) % mod;
                }
            }
            for (int j = 1; j <= fac[a[i]][0]; j++) {
                cur[j] = dp[j][j];
                dp[j][j] = 0;
            }
        }
        int ans = 0;
        for (int i = 1; i <= fac[a[n - 1]][0]; i++) {
            ans = (ans + cur[i]) % mod;
        }
        System.out.println(ans);
    }
}