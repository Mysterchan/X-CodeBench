import java.io.*;
import java.util.*;

public class Main {
    static List<Integer>[] adj;
    static int[] degree;
    static int n;

    // dp[node][0]: max size if node is leaf (degree 1)
    // dp[node][1]: max size if node is internal (degree 4)
    // -1 means invalid
    static int[][] dp;

    static void dfs(int u, int p) {
        List<Integer> children = new ArrayList<>();
        for (int v : adj[u]) {
            if (v == p) continue;
            dfs(v, u);
            children.add(v);
        }

        // If leaf: degree must be 1
        // If internal: degree must be 4 (i.e. 4 children)
        // We try both possibilities if possible

        // dp[u][0]: node is leaf (degree 1)
        // For leaf, no children allowed (degree 1 means only one edge, which is to parent)
        // So children must be zero
        if (children.size() == 0) {
            dp[u][0] = 1; // leaf node itself
        } else {
            dp[u][0] = -1; // can't be leaf if has children
        }

        // dp[u][1]: node is internal (degree 4)
        // Must have exactly 4 children
        if (children.size() == 4) {
            // For internal node, all children must be leaves (degree 1)
            // So dp[child][0] must be valid
            int sum = 1; // count self
            for (int c : children) {
                if (dp[c][0] == -1) {
                    dp[u][1] = -1;
                    return;
                }
                sum += dp[c][0];
            }
            dp[u][1] = sum;
        } else {
            dp[u][1] = -1;
        }
    }

    static int best = -1;

    static void dfs2(int u, int p) {
        // We want to find the largest alkane subtree rooted at u
        // We consider dp[u][1] only (internal node with degree 4)
        // Because alkane must have at least one internal node

        if (dp[u][1] != -1) {
            best = Math.max(best, dp[u][1]);
        }

        for (int v : adj[u]) {
            if (v == p) continue;
            dfs2(v, u);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        adj = new ArrayList[n + 1];
        degree = new int[n + 1];
        for (int i = 1; i <= n; i++) adj[i] = new ArrayList<>();

        for (int i = 0; i < n - 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            adj[u].add(v);
            adj[v].add(u);
            degree[u]++;
            degree[v]++;
        }

        dp = new int[n + 1][2];
        for (int i = 1; i <= n; i++) {
            dp[i][0] = dp[i][1] = -1;
        }

        // Run dfs from any node (1)
        dfs(1, -1);

        // Find best alkane subtree
        dfs2(1, -1);

        if (best == -1) {
            System.out.println(-1);
        } else {
            // The problem's sample output shows output = number of vertices in subgraph
            // Our dp counts vertices directly, so print best
            System.out.println(best);
        }
    }
}