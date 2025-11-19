import java.io.*;
import java.util.*;

public class Main {
    static class MyScanner {
        static BufferedReader r;
        static StringTokenizer st;
        public MyScanner() {
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
    static class Pair <K, V> {
        K X;
        V Y;

        public Pair(K x, V y) {
            X = x;
            Y = y;
        }

        public Pair() {}

        @Override
        public String toString() {
            return "Pair{" + "X=" + X + ", Y=" + Y + '}';
        }
    }
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static MyScanner sc = new MyScanner();
    static int N, Q;
    static final int MAXN = 200010;
    static int[] a = new int[MAXN], ans = new int[MAXN], f = new int[MAXN];
    static ArrayList<Pair<Integer, Integer>>[] query = new ArrayList[MAXN];
    public static void main(String[] args) throws IOException {
        N = sc.nextInt();
        Q = sc.nextInt();
        for (int i = 1; i <= N; i++) {
            a[i] = sc.nextInt();
            query[i] = new ArrayList<>();
        }
        for (int i = 1; i <= Q; i++) {
            int r = sc.nextInt(), x = sc.nextInt();
            query[r].add(new Pair<>(x, i));
        }
        int R = 0;
        for (int i = 1; i <= N; i++) {
            int l = 0, r = R;
            while (l < r) {
                int mid = (l + r + 1) >> 1;
                if (a[mid] < a[i]) l = mid;
                else r = mid - 1;
            }
            R = Math.max(R, l + 1);
            f[l + 1] = a[i];

            for (var X : query[i]) {
                int x = X.X, id = X.Y;
                l = 0;
                r = R;
                while (l < r) {
                    int mid = (l + r + 1) >> 1;
                    if (f[mid] <= x) l = mid;
                    else r = mid - 1;
                }
                ans[id] = l;
            }
        }
        for (int i = 1; i <= Q; i++) {
            bw.write(ans[i] + "\n");
        }
        bw.flush();
    }
}