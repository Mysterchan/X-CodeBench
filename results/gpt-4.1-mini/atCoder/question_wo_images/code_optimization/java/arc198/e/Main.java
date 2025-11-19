import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    private static final int MOD = 998244353;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[] s = new int[m];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            s[i] = Integer.parseInt(st.nextToken());
        }

        int target = 1 << n;
        long[] dp = new long[target + 1];
        dp[0] = 1;

        // Optimization: 
        // Instead of iterating over all x from 0 to target,
        // we iterate over dp states in order of increasing x,
        // but only process states with dp[x] > 0.
        // To avoid scanning all dp array each time, we keep track of active states.

        // Use a queue to process only reachable states
        int[] queue = new int[target + 1];
        int head = 0, tail = 0;
        queue[tail++] = 0;

        boolean[] visited = new boolean[target + 1];
        visited[0] = true;

        while (head < tail) {
            int x = queue[head++];
            long ways = dp[x];
            for (int si : s) {
                int next = (x | si) + 1;
                if (next <= target) {
                    long prev = dp[next];
                    dp[next] = (prev + ways) % MOD;
                    if (!visited[next]) {
                        visited[next] = true;
                        queue[tail++] = next;
                    }
                }
            }
        }

        System.out.println(dp[target]);
    }
}