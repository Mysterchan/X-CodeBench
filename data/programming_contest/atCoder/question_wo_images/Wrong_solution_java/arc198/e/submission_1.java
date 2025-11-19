import java.util.*;

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
        Queue<Integer> q = new LinkedList<>();
        q.offer(0);
        boolean[] enqueued = new boolean[target + 1];
        enqueued[0] = true;

        while (!q.isEmpty()) {
            int current_x = q.poll();
            for (int si : s) {
                int next_x = (current_x | si) + 1;
                if (next_x <= target) {
                    dp[next_x] = (dp[next_x] + dp[current_x]) % MOD;
                    if (!enqueued[next_x]) {
                        enqueued[next_x] = true;
                        q.offer(next_x);
                    }
                }
            }
        }

        System.out.println(dp[target]);
    }
}