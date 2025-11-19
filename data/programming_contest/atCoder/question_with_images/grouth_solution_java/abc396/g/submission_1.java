import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), m = sc.nextInt();
        int[][] dp = new int[m + 1][1 << m];
        for (int i = 0; i < n; i++) {
            String s = sc.next();
            int x = 0;
            for (int j = 0; j < m; j++) {
                x = x << 1 | s.charAt(j) - '0';
            }
            dp[0][x]++;
        }
        for (int i = 0; i < m; i++) {
            for (int j = m; j >= 1; j--) {
                for (int s = 0; s < (1 << m); s++) {
                    dp[j][s] += dp[j - 1][s ^ (1 << i)];
                }
            }
        }
        int ans = Integer.MAX_VALUE;
        for (int s = 0; s < (1 << m); s++) {
            int cur = 0;
            for (int j = 0; j <= m; j++) {
                cur += dp[j][s] * Integer.min(j, m - j);
            }
            ans = Integer.min(ans, cur);
        }
        System.out.println(ans);
    }
}