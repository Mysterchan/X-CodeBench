import java.util.*;

public class Main {
    static final int MOD = 998244353;
    static int[] depth, parent;
    static ArrayList<Integer>[] adj, levelNodes;
    static long[] dp;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        // Since sum of n over all test cases <= 3*10^5, we can reuse arrays with max size
        // But here we allocate per test case for clarity and memory efficiency.

        while (t-- > 0) {
            int n = sc.nextInt();
            parent = new int[n + 1];
            depth = new int[n + 1];
            adj = new ArrayList[n + 1];
            for (int i = 1; i <= n; i++) adj[i] = new ArrayList<>();

            for (int i = 2; i <= n; i++) {
                int p = sc.nextInt();
                parent[i] = p;
                adj[p].add(i);
            }

            // BFS to compute depths
            depth[1] = 0;
            Queue<Integer> q = new ArrayDeque<>();
            q.add(1);
            int maxDepth = 0;
            while (!q.isEmpty()) {
                int u = q.poll();
                for (int w : adj[u]) {
                    depth[w] = depth[u] + 1;
                    maxDepth = Math.max(maxDepth, depth[w]);
                    q.add(w);
                }
            }

            // Group nodes by depth
            levelNodes = new ArrayList[maxDepth + 2];
            for (int i = 0; i <= maxDepth + 1; i++) levelNodes[i] = new ArrayList<>();
            for (int i = 1; i <= n; i++) {
                levelNodes[depth[i]].add(i);
            }

            dp = new long[n + 1];

            // Process from bottom to top
            // For leaves (max depth), dp[v] = 1
            for (int d = maxDepth; d >= 0; d--) {
                // Precompute sum of dp for next level
                long sumNextLevel = 0;
                for (int v : levelNodes[d + 1]) {
                    sumNextLevel = (sumNextLevel + dp[v]) % MOD;
                }

                // For each node at depth d
                for (int v : levelNodes[d]) {
                    if (d == maxDepth) {
                        // leaf node
                        dp[v] = 1;
                    } else {
                        if (v == 1) {
                            // root: can move to any node at next level
                            dp[v] = (1 + sumNextLevel) % MOD;
                        } else {
                            // non-root: must exclude children from next level sum
                            long sumChildren = 0;
                            for (int c : adj[v]) {
                                sumChildren = (sumChildren + dp[c]) % MOD;
                            }
                            dp[v] = (1 + (sumNextLevel - sumChildren + MOD) % MOD) % MOD;
                        }
                    }
                }
            }

            System.out.println(dp[1] % MOD);
        }
        sc.close();
    }
}