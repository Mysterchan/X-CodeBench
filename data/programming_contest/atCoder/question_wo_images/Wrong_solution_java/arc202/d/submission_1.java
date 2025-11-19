import java.util.*;

public class Main {
    static final int MOD = 998244353;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int H = sc.nextInt();
        int W = sc.nextInt();
        int T = sc.nextInt();
        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();
        int D = sc.nextInt();

        long[] dp = new long[3];
        if (A == C && B == D) dp[0] = 1;
        else if (A == C || B == D) dp[1] = 1;
        else dp[2] = 1;

        for (int t = 0; t < T; t++) {
            long[] ndp = new long[3];

            ndp[1] = (ndp[1] + dp[0]) % MOD;

            ndp[0] = (ndp[0] + dp[1]) % MOD;

            ndp[1] = (ndp[1] + dp[1] * (H + W - 4)) % MOD;

            ndp[2] = (ndp[2] + dp[1] * (long)(H - 1) * (W - 1) % MOD) % MOD;

            ndp[1] = (ndp[1] + dp[2] * (H + W - 2)) % MOD;

            ndp[2] = (ndp[2] + dp[2] * ((long)(H - 2) * (W - 2)) % MOD) % MOD;

            dp = ndp;
        }

        System.out.println(dp[0]);
    }
}