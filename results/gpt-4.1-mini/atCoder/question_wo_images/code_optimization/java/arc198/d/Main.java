import java.io.*;
import java.util.*;

public class Main {

    static int n;
    static List<Integer>[] ed;
    static int LOG;
    static int[][] up;
    static int[] depth;
    static int[] w;
    static DSU dsu;
    static char[][] A;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        ed = new ArrayList[n];
        for (int i = 0; i < n; i++) ed[i] = new ArrayList<>();
        for (int i = 0; i < n - 1; i++) {
            String[] uv = br.readLine().split(" ");
            int u = Integer.parseInt(uv[0]) - 1;
            int v = Integer.parseInt(uv[1]) - 1;
            ed[u].add(v);
            ed[v].add(u);
        }
        A = new char[n][];
        for (int i = 0; i < n; i++) {
            A[i] = br.readLine().toCharArray();
        }

        // Preprocessing for LCA
        LOG = 1;
        while ((1 << LOG) <= n) LOG++;
        up = new int[n][LOG];
        depth = new int[n];
        dfs(0, -1);

        // Build binary lifting table
        for (int j = 1; j < LOG; j++) {
            for (int i = 0; i < n; i++) {
                if (up[i][j - 1] == -1) up[i][j] = -1;
                else up[i][j] = up[up[i][j - 1]][j - 1];
            }
        }

        dsu = new DSU(n);

        // For each pair (i,j) with A[i][j] == '1', union nodes along the path to enforce palindrome constraints
        // Optimization: process only upper triangle (i<j) since A symmetric and A[i][i]=1
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (A[i][j] == '1') {
                    int lca = lca(i, j);
                    // Get path from i to lca
                    List<Integer> path1 = new ArrayList<>();
                    int x = i;
                    while (x != lca) {
                        path1.add(x);
                        x = up[x][0];
                    }
                    path1.add(lca);
                    // Get path from j to lca
                    List<Integer> path2 = new ArrayList<>();
                    x = j;
                    while (x != lca) {
                        path2.add(x);
                        x = up[x][0];
                    }
                    // Combine path: path1 + reversed(path2)
                    int len1 = path1.size();
                    int len2 = path2.size();
                    // Union symmetric nodes on the path
                    int left = 0, right = len1 + len2 - 1;
                    while (left < right) {
                        int uNode, vNode;
                        if (left < len1) uNode = path1.get(left);
                        else uNode = path2.get(len1 + len2 - 1 - left);
                        if (right < len1) vNode = path1.get(right);
                        else vNode = path2.get(len1 + len2 - 1 - right);
                        dsu.union(uNode, vNode);
                        left++;
                        right--;
                    }
                }
            }
        }

        // Assign w[i] = dsu.find(i)
        w = new int[n];
        for (int i = 0; i < n; i++) {
            w[i] = dsu.find(i);
        }

        // Now check if any pair (i,j) with A[i][j] == '1' violates palindrome condition
        // Actually, the union above ensures no violation for these pairs.
        // But we must check pairs with A[i][j] == '1' to confirm no conflict.
        // If conflict found, print 10^100 and return.

        // Since union done, if any pair (i,j) with A[i][j] == '1' has path nodes not symmetric in w, conflict.
        // But union ensures this cannot happen, so no need to check again.

        // Now count the number of palindromic pairs (i,j)
        // (i,i) always palindromic, so start with n
        long ans = n;

        // For pairs (i,j), i<j, check if path is palindrome under w
        // To optimize, we can precompute for all pairs:
        // But O(n^2) is acceptable with efficient path retrieval.

        // We'll implement a function to get path nodes quickly using binary lifting:
        // But path retrieval is O(path length), which can be O(n) worst case.
        // To optimize, we can precompute Euler Tour and RMQ for LCA, but still path retrieval is needed.

        // Instead, we can precompute for each node its parent and depth, and reconstruct path quickly.

        // To speed up, we can cache paths or do a two-pointer approach on the path.

        // Since N=3000, O(N^2) with efficient code is acceptable.

        // We'll implement a function to get path nodes from i to j.

        // To avoid repeated list creation, we can reuse arrays.

        // Implement path retrieval and palindrome check:

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (isPalindromePath(i, j)) {
                    ans += 2; // (i,j) and (j,i)
                }
            }
        }

        System.out.println(ans);
    }

    static boolean isPalindromePath(int u, int v) {
        int lca = lca(u, v);
        // Collect path nodes from u to lca
        int len1 = depth[u] - depth[lca] + 1;
        int len2 = depth[v] - depth[lca];
        int totalLen = len1 + len2;
        // We'll use two pointers from ends to center
        int leftU = u, leftV = v;
        int leftDepth = depth[u];
        int rightDepth = depth[v];
        for (int i = 0; i < totalLen / 2; i++) {
            if (w[leftU] != w[leftV]) return false;
            // Move leftU up one step
            if (leftU != lca) leftU = up[leftU][0];
            // Move leftV up one step
            if (leftV != lca) leftV = up[leftV][0];
        }
        return true;
    }

    static void dfs(int u, int p) {
        up[u][0] = p;
        for (int v : ed[u]) {
            if (v == p) continue;
            depth[v] = depth[u] + 1;
            dfs(v, u);
        }
    }

    static int lca(int u, int v) {
        if (depth[u] < depth[v]) {
            int tmp = u; u = v; v = tmp;
        }
        // Lift u up to depth v
        for (int i = LOG - 1; i >= 0; i--) {
            if (up[u][i] != -1 && depth[up[u][i]] >= depth[v]) {
                u = up[u][i];
            }
        }
        if (u == v) return u;
        for (int i = LOG - 1; i >= 0; i--) {
            if (up[u][i] != -1 && up[u][i] != up[v][i]) {
                u = up[u][i];
                v = up[v][i];
            }
        }
        return up[u][0];
    }

    static class DSU {
        int[] p, sz;

        DSU(int n) {
            p = new int[n];
            sz = new int[n];
            for (int i = 0; i < n; i++) {
                p[i] = i;
                sz[i] = 1;
            }
        }

        int find(int x) {
            while (p[x] != x) {
                p[x] = p[p[x]];
                x = p[x];
            }
            return x;
        }

        void union(int x, int y) {
            x = find(x);
            y = find(y);
            if (x == y) return;
            if (sz[x] < sz[y]) {
                int tmp = x; x = y; y = tmp;
            }
            p[y] = x;
            sz[x] += sz[y];
        }
    }
}