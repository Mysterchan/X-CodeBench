import java.util.*;

public class Main {
    final static int M = 998244353;
    static long[][] dp;

    public static long func(int n, int m, String[] str, int d) {
        dp = new long[n][m];

        for (int i = 0; i < m; i++) {
            if (str[0].charAt(i) == 'X') {
                dp[0][i] = 1;
            }
        }

        for (int row = 1; row < n; row++) {
            long[] prefix = new long[m + 1];

            for (int col = 0; col < m; col++) {
                prefix[col + 1] = (prefix[col] + dp[row - 1][col]) % M;
            }

            for (int col = 0; col < m; col++) {
                if (str[row].charAt(col) == 'X') {
                    int left = Math.max(col - d, 0);
                    int right = Math.min(col + d, m - 1);

                    dp[row][col] = (prefix[right + 1] - prefix[left] + M) % M;
                }
            }
        }

        long ans = 0;
        for (int col = 0; col < m; col++) {
            ans = (ans + dp[n - 1][col]) % M;
        }

        return ans;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        while (t-- > 0) {
            int n = sc.nextInt(), m = sc.nextInt(), d = sc.nextInt();
            String[] str = new String[n];

            for (int i = 0; i < n; i++) str[i] = sc.next();

            System.out.println(func(n, m, str, d));
        }
    }
}