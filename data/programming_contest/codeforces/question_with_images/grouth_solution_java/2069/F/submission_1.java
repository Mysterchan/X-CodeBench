import java.io.*;
import java.util.*;

public class Main {
    static int n, t, tot;
    static int[] fa, sz;
    static int[][] f;
    static SB sb;

    static int find(int x) {
        while (x != fa[x]) x = fa[x];
        return x;
    }

    static class Op {
        int t, x, y;
        Op(int t, int x, int y) {
            this.t = t; this.x = x; this.y = y;
        }
    }

    static class P {
        int x, y;
        P(int x, int y) { this.x = x; this.y = y; }
        public boolean equals(Object o) {
            if (this == o) return true;
            if (!(o instanceof P)) return false;
            P p = (P) o;
            return x == p.x && y == p.y;
        }
        public int hashCode() { return Objects.hash(x, y); }
    }

    static class T {
        int i, p, s;
        T(int i, int p, int s) { this.i = i; this.p = p; this.s = s; }
    }

    static class SB {
        ArrayList<P>[] v;
        @SuppressWarnings("unchecked")
        SB(int ts) {
            v = new ArrayList[ts];
            for (int i = 0; i < ts; i++) v[i] = new ArrayList<>();
        }
        void add(int id, int l, int r, int x, int y, P p) {
            if (x <= l && r <= y) { v[id].add(p); return; }
            int m = (l + r) / 2;
            if (x <= m) add(id * 2, l, m, x, y, p);
            if (y > m) add(id * 2 + 1, m + 1, r, x, y, p);
        }
        void dfs(int id, int l, int r, int ti) {
            ArrayList<T> st = new ArrayList<>();
            for (P p : v[id]) {
                int x = find(p.x), y = find(p.y);
                if (x == y) continue;
                if (sz[x] < sz[y]) { int tmp = x; x = y; y = tmp; }
                st.add(new T(y, fa[y], sz[y]));
                fa[y] = x; sz[x] += sz[y]; tot--;
            }
            if (l == r) f[l][ti] = tot;
            else {
                int m = (l + r) / 2;
                dfs(id * 2, l, m, ti);
                dfs(id * 2 + 1, m + 1, r, ti);
            }
            Collections.reverse(st);
            for (T t : st) {
                sz[fa[t.i]] -= t.s;
                fa[t.i] = t.p; sz[t.i] = t.s; tot++;
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);
        String[] p = br.readLine().trim().split(" ");
        n = Integer.parseInt(p[0]); t = Integer.parseInt(p[1]);
        fa = new int[n + 1]; sz = new int[n + 1]; f = new int[t + 1][2]; tot = n;
        for (int i = 1; i <= n; i++) { fa[i] = i; sz[i] = 1; }
        @SuppressWarnings("unchecked") ArrayList<Op>[] op = new ArrayList[2];
        op[0] = new ArrayList<>(); op[1] = new ArrayList<>();
        for (int i = 1; i <= t; i++) {
            String[] s = br.readLine().trim().split(" ");
            int x = Integer.parseInt(s[1]), y = Integer.parseInt(s[2]);
            if (x > y) { int tmp = x; x = y; y = tmp; }
            op[s[0].equals("B") ? 1 : 0].add(new Op(i, x, y));
        }
        int ts = 4 * t + 5; sb = new SB(ts);
        for (int T = 0; T < 2; T++) {
            HashMap<P, Integer> mp = new HashMap<>();
            for (Op o : op[T]) {
                P p1 = new P(o.x, o.y);
                if (mp.containsKey(p1)) {
                    sb.add(1, 1, t, mp.get(p1), o.t - 1, p1);
                    mp.remove(p1);
                } else mp.put(p1, o.t);
            }
            for (Map.Entry<P, Integer> e : mp.entrySet()) sb.add(1, 1, t, e.getValue(), t, e.getKey());
            sb.dfs(1, 1, t, T);
        }
        for (int i = 1; i <= t; i++) out.println(f[i][0] - f[i][1]);
        out.flush(); out.close();
    }
}
