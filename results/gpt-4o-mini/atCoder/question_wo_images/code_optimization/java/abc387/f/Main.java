import java.util.*;

public class Main {
    static final int MOD = 998244353;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] A = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            A[i] = sc.nextInt();
        }

        long[] dp = new long[m + 1];
        Arrays.fill(dp, 1); // Base case: 1 way to choose x_i = 1 for all i

        for (int i = 1; i <= n; i++) {
            long[] newDp = new long[m + 1];
            for (int j = 1; j <= m; j++) {
                newDp[j] = dp[j];
                if (j > 1) {
                    newDp[j] = (newDp[j] + newDp[j - 1]) % MOD; // Cumulative sum
                }
            }
            dp = newDp;

            // Update dp based on the constraints from A
            for (int j = 1; j <= m; j++) {
                if (A[i] <= j) {
                    dp[j] = dp[A[i]];
                } else {
                    dp[j] = 0; // If A[i] > j, no valid x_i can be chosen
                }
            }
        }

        long result = 0;
        for (int j = 1; j <= m; j++) {
            result = (result + dp[j]) % MOD;
        }

        System.out.println(result);
    }
}