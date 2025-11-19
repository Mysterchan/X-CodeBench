import java.util.*;
import java.io.*;

public class Main {
    static int[] fa, d1, d2;
    static List<List<Integer>> e;
    static int n, m, s, t;

    static int find(int x) {
        if (fa[x] != x) fa[x] = find(fa[x]);
        return fa[x];
    }

    static void dfs1(int u, int fa) {
        d1[u] = d1[fa] + 1;
        for (int v : e.get(u)) {
            if (v != fa) dfs1(v, u);
        }
    }

    static void dfs2(int u, int fa) {
        d2[u] = d2[fa] + 1;
        for (int v : e.get(u)) {
            if (v != fa) dfs2(v, u);
        }
    }

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        s = sc.nextInt();
        t = sc.nextInt();
        fa = new int[n + 1];
        d1 = new int[n + 1];
        d2 = new int[n + 1];
        e = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            e.add(new ArrayList<>());
            fa[i] = i;
        }
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            e.get(u).add(v);
            e.get(v).add(u);
            fa[find(u)] = find(v);
        }
        if (find(s) != find(t)) {
            System.out.println(-1);
            return;
        }
        dfs1(s, 0);
        dfs2(t, 0);
        int ans = Integer.MAX_VALUE;
        for (int i = 1; i <= n; i++) {
            if (i != s && i != t) ans = Math.min(ans, d1[i] + d2[i]);
        }
        System.out.println(ans);
    }
}