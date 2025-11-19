import java.util.*;
import java.io.*;

public class Main {
    static int n, q;
    static int[] sz, ds, fa;
    static long[] fenw;
    static ArrayList<Integer>[] adj;
    static Pair[] edges;
    static int idx;

    static class Pair {
        int u, v;
        Pair(int u, int v) {
            this.u = u;
            this.v = v;
        }
    }

    static void dfs(int p, int u) {
        ds[u] = ++idx;
        sz[u] = 1;
        for (int w : adj[u]) {
            if (w == p) continue;
            fa[w] = u;
            dfs(u, w);
            sz[u] += sz[w];
        }
    }

    static int lowbit(int x) {
        return x & (-x);
    }

    static void fenwAdd(int i, int v) {
        while (i <= n) {
            fenw[i] += v;
            i += lowbit(i);
        }
    }

    static long fenwSum(int i) {
        long res = 0;
        while (i > 0) {
            res += fenw[i];
            i -= lowbit(i);
        }
        return res;
    }

    public static void main(String[] args) throws IOException {
        // Use BufferedReader and BufferedWriter for faster IO
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        n = Integer.parseInt(br.readLine());
        adj = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) adj[i] = new ArrayList<>();
        edges = new Pair[n];
        sz = new int[n + 1];
        ds = new int[n + 1];
        fa = new int[n + 1];
        fenw = new long[n + 1];

        // Read edges
        for (int i = 1; i < n; i++) {
            String[] parts = br.readLine().split(" ");
            int u = Integer.parseInt(parts[0]);
            int v = Integer.parseInt(parts[1]);
            edges[i] = new Pair(u, v);
            adj[u].add(v);
            adj[v].add(u);
        }

        // DFS to get subtree sizes and dfs order
        idx = 0;
        fa[1] = 0;
        dfs(0, 1);

        // Initialize Fenwick tree with all weights = 1
        for (int i = 1; i <= n; i++) {
            fenwAdd(i, 1);
        }

        q = Integer.parseInt(br.readLine());
        long totalWeight = n;

        for (int _ = 0; _ < q; _++) {
            String line = br.readLine();
            String[] parts = line.split(" ");
            int type = Integer.parseInt(parts[0]);
            if (type == 1) {
                int x = Integer.parseInt(parts[1]);
                int w = Integer.parseInt(parts[2]);
                fenwAdd(ds[x], w);
                totalWeight += w;
            } else {
                int y = Integer.parseInt(parts[1]);
                int u = edges[y].u, v = edges[y].v;
                long subtreeSum;
                if (fa[v] == u) {
                    // v is child of u
                    subtreeSum = fenwSum(ds[v] + sz[v] - 1) - fenwSum(ds[v] - 1);
                } else {
                    // u is child of v
                    subtreeSum = fenwSum(ds[u] + sz[u] - 1) - fenwSum(ds[u] - 1);
                }
                long diff = Math.abs(totalWeight - 2 * subtreeSum);
                bw.write(Long.toString(diff));
                bw.newLine();
            }
        }
        bw.flush();
    }
}