import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    static class DSU {
        DSU(int n) {
            init(n);
        }

        private int[] p, sz;

        void init(int n) {
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
            sz[x] += sz[y];
            p[y] = x;
        }

        int find(int x) {
            while (p[x] != x) {
                p[x] = p[p[x]];
                x = p[x];
            }
            return x;
        }

        boolean same(int x, int y) {
            return find(x) == find(y);
        }

        int size(int x) {
            return sz[find(x)];
        }
    }

    public static void main(String[] args) {
        buildTree();
        char[][] s = new char[n][n];
        for (int i = 0; i < n; i++) {
            s[i] = sc.next().toCharArray();
        }
        dep = new int[n];
        fa = new int[n];
        fa[0] = -1;
        dfs(0,-1);
        DSU dsu = new DSU(n);
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (s[i][j] == '1') {
                    dsu.union(i, j);
                    int lca = lca(i, j);
                    List<Integer> l = new ArrayList<>();
                    int x = i;
                    while (x != lca) {
                        l.add(x);
                        x = fa[x];
                    }
                    l.add(lca);
                    List<Integer> l2 = new ArrayList<>();
                    x = j;
                    while (x != lca) {
                        l2.add(x);
                        x = fa[x];
                    }
                    int sz = l2.size();
                    for (int k = sz - 1; k >= 0; k--) {
                        l.add(l2.get(k));
                    }
                    int ll = 0, rr = l.size() - 1;
                    while (ll < rr) {
                        dsu.union(l.get(ll), l.get(rr));
                        ll++;
                        rr--;
                    }
                }
            }
        }
        w = new int[n];
        for (int i = 0; i < n; i++) {
            w[i] = dsu.find(i);
        }
        int ans = n;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int lca = lca(i, j);
                List<Integer> l = new ArrayList<>();
                int x = i;
                while (x != lca) {
                    l.add(x);
                    x = fa[x];
                }
                l.add(lca);
                List<Integer> l2 = new ArrayList<>();
                x = j;
                while (x != lca) {
                    l2.add(x);
                    x = fa[x];
                }
                int sz = l2.size();
                for (int k = sz - 1; k >= 0; k--) {
                    l.add(l2.get(k));
                }
                int ll = 0, rr = l.size() - 1;
                boolean ok = true;
                while (ll < rr) {
                    if (w[l.get(ll)] != w[l.get(rr)]) {
                        ok = false;
                        break;
                    }
                    ll++;
                    rr--;
                }
                if (ok) {
                    ans += 2;
                }

            }

        }

        out.println(ans);
        out.close();
    }

    static int[] w;

    static int[] fa, dep;

    static int lca(int u, int v) {
        while (u != v) {
            if (dep[u] > dep[v]) u = fa[u];
            else if (dep[u] < dep[v]) v = fa[v];
            else {
                u = fa[u];
                v = fa[v];
            }
        }
        return u;

    }

    static void dfs(int u, int p) {
        for (int v : ed[u]) {
            if (v == p) continue;
            fa[v] = u;
            dep[v] = dep[u] + 1;
            dfs(v, u);

        }

    }

    static void buildTree() {
        n = sc.nextInt();
        ed = new List[n + 1];
        for (int i = 0; i <= n; i++) {
            ed[i] = new ArrayList<>();
        }
        for (int i = 1; i < n; i++) {
            int u = sc.nextInt() - 1, v = sc.nextInt() - 1;
            ed[u].add(v);
            ed[v].add(u);
        }
    }

    static int[] a;
    static List<Integer>[] ed;
    static int n;

    static Kattio sc = new Kattio();
    static PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

    static class Kattio {
        static BufferedReader r;
        static StringTokenizer st;

        public Kattio() {
            r = new BufferedReader(new InputStreamReader(System.in));
        }

        public String next() {
            try {
                while (st == null || !st.hasMoreTokens()) {
                    st = new StringTokenizer(r.readLine());
                }
                return st.nextToken();
            } catch (Exception e) {
                return null;
            }
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

        public long nextLong() {
            return Long.parseLong(next());
        }

        public double nextDouble() {
            return Double.parseDouble(next());
        }
    }
}