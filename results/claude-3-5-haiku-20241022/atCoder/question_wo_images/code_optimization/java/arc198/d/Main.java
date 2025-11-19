import java.io.*;
import java.util.*;

public class Main {

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

        void union(int x, int y) {
            x = find(x);
            y = find(y);
            if (x == y) return;
            if (sz[x] < sz[y]) {
                int t = x; x = y; y = t;
            }
            sz[x] += sz[y];
            p[y] = x;
        }

        int find(int x) {
            if (p[x] != x) p[x] = find(p[x]);
            return p[x];
        }
    }

    static int n;
    static List<Integer>[] ed;
    static int[] fa, dep;
    static int[][] parent;
    static int maxLog;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        ed = new List[n];
        for (int i = 0; i < n; i++) ed[i] = new ArrayList<>();
        
        for (int i = 1; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken()) - 1;
            int v = Integer.parseInt(st.nextToken()) - 1;
            ed[u].add(v);
            ed[v].add(u);
        }
        
        char[][] s = new char[n][];
        for (int i = 0; i < n; i++) {
            s[i] = br.readLine().toCharArray();
        }
        
        fa = new int[n];
        dep = new int[n];
        fa[0] = -1;
        dfs(0, -1);
        
        maxLog = Integer.numberOfTrailingZeros(Integer.highestOneBit(n)) + 1;
        parent = new int[n][maxLog];
        for (int i = 0; i < n; i++) {
            parent[i][0] = fa[i] == -1 ? i : fa[i];
        }
        for (int j = 1; j < maxLog; j++) {
            for (int i = 0; i < n; i++) {
                parent[i][j] = parent[parent[i][j-1]][j-1];
            }
        }
        
        DSU dsu = new DSU(n);
        int[] path = new int[n];
        
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (s[i][j] == '1') {
                    int len = getPath(i, j, path);
                    for (int k = 0; k < len / 2; k++) {
                        dsu.union(path[k], path[len - 1 - k]);
                    }
                }
            }
        }
        
        int[] w = new int[n];
        for (int i = 0; i < n; i++) {
            w[i] = dsu.find(i);
        }
        
        int ans = n;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int len = getPath(i, j, path);
                boolean ok = true;
                for (int k = 0; k < len / 2; k++) {
                    if (w[path[k]] != w[path[len - 1 - k]]) {
                        ok = false;
                        break;
                    }
                }
                if (ok) ans += 2;
            }
        }
        
        System.out.println(ans);
    }
    
    static int lca(int u, int v) {
        if (dep[u] < dep[v]) {
            int t = u; u = v; v = t;
        }
        int diff = dep[u] - dep[v];
        for (int i = 0; i < maxLog; i++) {
            if (((diff >> i) & 1) == 1) {
                u = parent[u][i];
            }
        }
        if (u == v) return u;
        for (int i = maxLog - 1; i >= 0; i--) {
            if (parent[u][i] != parent[v][i]) {
                u = parent[u][i];
                v = parent[v][i];
            }
        }
        return parent[u][0];
    }
    
    static int getPath(int u, int v, int[] path) {
        int lca = lca(u, v);
        int len = 0;
        int x = u;
        while (x != lca) {
            path[len++] = x;
            x = fa[x];
        }
        path[len++] = lca;
        int start = len;
        x = v;
        while (x != lca) {
            path[len++] = x;
            x = fa[x];
        }
        for (int i = 0; i < (len - start) / 2; i++) {
            int t = path[start + i];
            path[start + i] = path[len - 1 - i];
            path[len - 1 - i] = t;
        }
        return len;
    }
    
    static void dfs(int u, int p) {
        for (int v : ed[u]) {
            if (v == p) continue;
            fa[v] = u;
            dep[v] = dep[u] + 1;
            dfs(v, u);
        }
    }
}