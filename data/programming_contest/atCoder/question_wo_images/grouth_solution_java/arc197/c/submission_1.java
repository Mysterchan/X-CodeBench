import java.io.*;
import java.util.StringTokenizer;

public class Main {

    static void init(int n) {
        int len = 4 * n;
        sum = new long[len];

        build(1, 0, n - 1);
    }

    static void build(int u, int le, int ri) {
        if (le == ri) {
            sum[u] = 1;
            return;
        }
        int mid = le + ri >> 1;
        build(u << 1, le, mid);
        build(u << 1 | 1, mid + 1, ri);
        pushUp(u);
    }

    static void pushUp(int u) {
        sum[u] = sum[u << 1] + sum[u << 1 | 1];
    }

    static void update1(int u, int idx, int v, int l, int r) {
        if (l == idx && r == idx) {
            sum[u] = v;
            return;
        }
        int mid = l + r >> 1;
        if (mid >= idx) update1(u << 1, idx, v, l, mid);
        else update1(u << 1 | 1, idx, v, mid + 1, r);
        pushUp(u);
    }

    static long queryRangeSum(int u, int le, int ri, int l, int r) {
        if (le <= l && r <= ri) {
            return sum[u];
        }
        int mid = l + r >> 1;
        long ret = 0;
        if (mid >= le) ret += queryRangeSum(u << 1, le, ri, l, mid);
        if (mid < ri) ret += queryRangeSum(u << 1 | 1, le, ri, mid + 1, r);
        return ret;
    }

    static long[] sum;

    public static void main(String[] args) {
        int N = (int) 3e6;
        init(N);
        boolean[] del = new boolean[N];
        boolean[] nDel = new boolean[N];

        int q = sc.nextInt();
        for (int i = 0; i < q; i++) {
            int a = sc.nextInt(), b = sc.nextInt();
            if (a < N && !del[a]) {
                del[a] = true;
                for (int j = a; j < N; j += a) {
                    if (!nDel[j]) {
                        update1(1, j, 0, 0, N - 1);
                        nDel[j] = true;
                    }
                }
            }

            int l = 0, r = N - 1, ans = -1;
            while (l <= r) {
                int mid = l + r >> 1;
                long v = queryRangeSum(1, 0, mid, 0, N - 1);
                if (v >= b + 1) {
                    ans = mid;
                    r = mid - 1;

                } else  l = mid + 1;
            }
            out.println(ans);

        }

        out.close();
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