import java.util.Scanner;

public class Main {
    private static final int MOD = 998244353;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        int[] s = new int[m];
        for (int i = 0; i < m; i++) {
            s[i] = scanner.nextInt();
        }
        scanner.close();

        int target = 1 << n;
        long[] dp = new long[target + 1];
        dp[0] = 1;

        for (int x = 0; x < target; x++) {
            if (dp[x] > 0) {
                for (int si : s) {
                    int next_x = (x | si) + 1;
                    if (next_x > target) {
                        break;  // No need to continue if next_x exceeds target
                    }
                    dp[next_x] = (dp[next_x] + dp[x]) % MOD;
                }
            }
        }

        System.out.println(dp[target]);
    }
}