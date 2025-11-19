import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    static class DSU {
        DSU(int n) {
            init(n);
        }

        private int[] p, sz;
        List<Integer>[] el;

        void init(int n) {
            p = new int[n];
            sz = new int[n];
            for (int i = 0; i < n; i++) {
                p[i] = i;
                sz[i] = 1;
            }
            el = new List[n];
            for (int i = 0; i < n; i++) {
                el[i] = new ArrayList<>();
                el[i].add(i);
            }
        }

        void union(int x, int y, int h) {
            x = find(x);
            y = find(y);
            if (x == y) return;
            if (sz[x] > sz[y]) {
                int t = x;
                x = y;
                y = t;
            }
            for (int d : el[x]) {
                for (int[] q : query[d]) {
                    int a = q[0], b = q[1];
                    if (find(a) == y) {
                        lim[b] = h;
                    }
                }
                el[y].add(d);
            }
            el[x] = new ArrayList<>();

            sz[y] += sz[x];
            p[x] = y;
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

    static int m, n;
    static List<int[]>[] query;
    static int[] f1, f2;
    static int[] lim;

    public static void main(String[] args) {
        m = sc.nextInt();
        n = sc.nextInt();
        int[][] a = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                a[i][j] = sc.nextInt();
            }
        }
        List<int[]> ed = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i + 1 < m) {
                    ed.add(new int[]{idx(i, j), idx(i + 1, j), Math.min(a[i][j], a[i + 1][j])});
                }
                if (j + 1 < n) {
                    ed.add(new int[]{idx(i, j), idx(i, j + 1), Math.min(a[i][j], a[i][j + 1])});
                }
            }
        }
        ed.sort((o1, o2) -> o2[2] - o1[2]);

        int q = sc.nextInt();
        int len = m * n;
        query = new List[len];
        for (int i = 0; i < len; i++) {
            query[i] = new ArrayList<>();
        }
        f1 = new int[q];
        f2 = new int[q];
        lim = new int[q];
        for (int i = 0; i < q; i++) {
            int x1 = sc.nextInt() - 1, y1 = sc.nextInt() - 1;
            f1[i] = sc.nextInt();
            int x2 = sc.nextInt() - 1, y2 = sc.nextInt() - 1;
            f2[i] = sc.nextInt();
            int i1 = idx(x1, y1), i2 = idx(x2, y2);
            query[i1].add(new int[]{i2, i});
            query[i2].add(new int[]{i1, i});

        }
        DSU dsu = new DSU(len);
        Arrays.fill(lim, 1 << 30);
        for (int[] e : ed) {
            int i1 = e[0], i2 = e[1], h = e[2];
            dsu.union(i1, i2, h);
        }
        for (int i = 0; i < q; i++) {
            if (lim[i] > Math.min(f1[i], f2[i])) out.println(Math.abs(f1[i] - f2[i]));
            else out.println(f1[i] + f2[i] - 2 * lim[i]);
        }

        out.close();
    }

    static int idx(int x, int y) {
        return x * n + y;
    }

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