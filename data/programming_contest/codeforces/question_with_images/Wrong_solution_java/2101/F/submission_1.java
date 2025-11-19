import java.io.*;
import java.util.*;

public class Main {
    static final int MOD = 998244353;

    static class ModInt {
        long val;
        ModInt(long v) { val = ((v % MOD) + MOD) % MOD; }
        ModInt add(ModInt other) { return new ModInt(val + other.val); }
        ModInt sub(ModInt other) { return new ModInt(val - other.val); }
        ModInt mul(ModInt other) { return new ModInt(val * other.val); }
        ModInt pow(long exp) {
            ModInt res = new ModInt(1);
            ModInt base = new ModInt(val);
            while (exp > 0) {
                if ((exp & 1) != 0) res = res.mul(base);
                base = base.mul(base);
                exp >>= 1;
            }
            return res;
        }
    }

    static class DFSForest {
        int n;
        ArrayList<Integer>[] g;
        int[] parent, root, depth;
        long[] dist;

        DFSForest(int nodes) {
            n = nodes;
            g = new ArrayList[n];
            for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
            parent = new int[n];
            root = new int[n];
            depth = new int[n];
            dist = new long[n];
        }

        void addEdge(int u, int v) {
            g[u].add(v);
            g[v].add(u);
        }

        void dfs(int v, int p, int r, long d) {
            parent[v] = p;
            root[v] = r;
            depth[v] = (p == -1 ? 0 : depth[p] + 1);
            dist[v] = d;
            for (int to : g[v]) {
                if (to != p) dfs(to, v, r, d + 1);
            }
        }

        void dfsAll() {
            for (int i = 0; i < n; i++)
                if (parent[i] == 0 && depth[i] == 0) dfs(i, -1, -1, 0);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);
        int tt = Integer.parseInt(br.readLine());
        while (tt-- > 0) {
            int n = Integer.parseInt(br.readLine());
            DFSForest g = new DFSForest(2 * n - 1);
            for (int i = 0; i < n - 1; i++) {
                String[] parts = br.readLine().split(" ");
                int x = Integer.parseInt(parts[0]) - 1;
                int y = Integer.parseInt(parts[1]) - 1;
                g.addEdge(x, n + i);
                g.addEdge(y, n + i);
            }

            int[] order = new int[n];
            for (int i = 0; i < n; i++) order[i] = i;
            ModInt ans = new ModInt(0);
            out.println(ans.val);
        }
        out.close();
    }
}
