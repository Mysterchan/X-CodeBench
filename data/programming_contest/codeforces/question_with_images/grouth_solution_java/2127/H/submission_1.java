import java.io.*;
import java.util.*;

public class Main {
    static final int N = 35;
    static final int M = 90;

    static int n, m;
    static int[] U = new int[M];
    static int[] V = new int[M];
    static int[] du = new int[N];
    static int ans;
    static int[][] h = new int[M + 1][M];

    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner(System.in);
        StringBuilder out = new StringBuilder();

        int T = fs.nextInt();
        while (T-- > 0) {
            n = fs.nextInt();
            m = fs.nextInt();
            for (int i = 0; i < m; i++) {
                U[i] = fs.nextInt();
                V[i] = fs.nextInt();
            }

            int[] lst = h[0];
            for (int i = 0; i < m; i++) lst[i] = i;
            Arrays.fill(du, 0);
            ans = 0;
            dfs(0, m, 0, lst);
            out.append(ans).append('\n');
        }

        System.out.print(out.toString());
    }

    static void dfs(int dep, int len, int cnt, int[] lst) {
        if (len == 0) {
            if (cnt > ans) ans = cnt;
            return;
        }

        int[] inc = new int[N];
        for (int i = 0; i < len; i++) {
            int e = lst[i];
            inc[U[e]]++;
            inc[V[e]]++;
        }

        int X = 0, Y = 0;
        for (int v = 1; v <= n; v++) {
            int t = 2 - du[v];
            if (t < 0) t = 0;
            X += t;
            if (t > 0) {
                Y += Math.min(inc[v], t);
            }
        }

        int ub = cnt + (Y >> 1);
        ub = Math.min(ub, cnt + len);
        ub = Math.min(ub, cnt + (X >> 1));
        if (ub <= ans) return;
        for (int v = 1; v <= n; v++) {
            if (du[v] < 2 && inc[v] == 1) {
                int id = -1;
                for (int i = 0; i < len; i++) {
                    int e = lst[i];
                    if (U[e] == v || V[e] == v) { id = e; break; }
                }
                if (id == -1) continue;
                int a = U[id], b = V[id];
                du[a]++; du[b]++;
                int[] nxt = h[dep + 1];
                int nlen = 0;
                for (int i = 0; i < len; i++) {
                    int e = lst[i];
                    if (e == id) continue;
                    if (du[U[e]] >= 2) continue;
                    if (du[V[e]] >= 2) continue;
                    nxt[nlen++] = e;
                }
                dfs(dep + 1, nlen, cnt + 1, nxt);
                du[a]--; du[b]--;
                return;
            }
        }

        int vp = 0, mn = Integer.MAX_VALUE;
        for (int v = 1; v <= n; v++) {
            if (du[v] < 2 && inc[v] > 0 && inc[v] < mn) {
                mn = inc[v];
                vp = v;
            }
        }

        if (vp == 0) {
            if (cnt > ans) ans = cnt;
            return;
        }

        int ep = -1;
        for (int i = 0; i < len; i++) {
            int e = lst[i];
            if (U[e] == vp || V[e] == vp) { ep = e; break; }
        }

        int a = U[ep], b = V[ep];
        if (du[a] < 2 && du[b] < 2) {
            du[a]++; du[b]++;
            int[] nxt = h[dep + 1];
            int nlen = 0;
            for (int i = 0; i < len; i++) {
                int e = lst[i];
                if (e == ep) continue;
                if (du[U[e]] >= 2) continue;
                if (du[V[e]] >= 2) continue;
                nxt[nlen++] = e;
            }
            dfs(dep + 1, nlen, cnt + 1, nxt);
            du[a]--; du[b]--;
        }

        int[] nxt = h[dep + 1];
        int nlen = 0;
        for (int i = 0; i < len; i++) {
            if (lst[i] != ep) nxt[nlen++] = lst[i];
        }
        dfs(dep + 1, nlen, cnt, nxt);
    }

    static class FastScanner {
        private final InputStream in;
        private final byte[] buffer = new byte[1 << 16];
        private int ptr = 0, len = 0;

        FastScanner(InputStream is) { this.in = is; }

        private int read() throws IOException {
            if (ptr >= len) {
                len = in.read(buffer);
                ptr = 0;
                if (len <= 0) return -1;
            }
            return buffer[ptr++];
        }

        int nextInt() throws IOException {
            int c;
            while ((c = read()) <= ' ') {
                if (c == -1) return Integer.MIN_VALUE;
            }
            int sign = 1;
            if (c == '-') {
                sign = -1;
                c = read();
            }
            int val = 0;
            while (c > ' ') {
                val = val * 10 + (c - '0');
                c = read();
            }
            return val * sign;
        }
    }
}
