import java.util.*;

public class Main {
    static final int MAXN = 405;
    static long[][] dp = new long[MAXN][MAXN];
    static long[] a = new long[MAXN];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        while (T-- > 0) {
            int n = sc.nextInt();
            Arrays.fill(a, 0);
            for (int i = 1; i <= n; i++) {
                a[i] = sc.nextLong();
            }

            for (long[] row : dp) {
                Arrays.fill(row, 0);
            }

            for (int k = 3; k <= n; k++) {
                for (int l = 1; l <= n; l++) {
                    int r = l + k - 1;
                    if (r > n) break;

                    for (int i = l; i <= r; i++) {
                        dp[l][r] = Math.max(dp[l][i] + dp[i + 1][r], dp[l][r]);
                        if (i != l && i != r) {
                            dp[l][r] = Math.max(dp[l + 1][i - 1] + dp[i + 1][r - 1] + a[i] * a[l] * a[r], dp[l][r]);
                        }
                    }
                }
            }

            System.out.println(dp[1][n]);
        }

        sc.close();
    }
}
