import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        long[] A = new long[N];
        for (int i = 0; i < N; i++) {
            A[i] = scanner.nextLong();
        }

        long ans = Long.MIN_VALUE;
        long sum = 0;
        long[] stack = new long[N];
        int p = 0;
        for (int i = 0; i < N; i++) {
            sum += A[i];
            stack[p++] = sum;
            ans = Math.max(ans, sum);
            if (sum < 0) {
                sum = 0;
                p = 0;
            }
        }

        long[] dp = new long[N];
        for (int i = N - 1; i >= 0; i--) {
            if (i == N - 1) {
                dp[i] = Math.max(0, A[i]);
            } else {
                dp[i] = Math.max(dp[i + 1], Math.max(0, dp[i + 1] + A[i]));
                for (int j = 0; j < p; j++) {
                    if (stack[j] > dp[i + 1] + A[i]) {
                        dp[i] = Math.max(dp[i], stack[j]);
                    }
                }
            }
        }

        System.out.println(dp[0]);
    }
}