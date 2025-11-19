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
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static MyScanner sc = new MyScanner();
    static int N, K;
    static final int MAXN = (int) 2E6 + 10;
    static int[] a = new int[MAXN];
    static int[] v = new int[MAXN];
    static ArrayList<Integer>[] gcd = new ArrayList[MAXN];
    public static void main(String[] args) throws IOException {
        N = sc.nextInt();
        K = sc.nextInt();
        for (int i = 1; i < MAXN; i++) {
            gcd[i] = new ArrayList<>();
        }

        for (int i = 1; i <= N; i++) {
            a[i] = sc.nextInt();
            for (int j = 1; j <= a[i] / j; j++) if (a[i] % j == 0) {
                gcd[i].add(j);
                v[j]++;
                if (j != a[i] / j) {
                    v[a[i] / j]++;
                    gcd[i].add(a[i] / j);
                }
            }
        }

        for (int i = 1; i <= N; i++) {
            gcd[i].sort((o1, o2) -> o2 - o1);
            for (var x : gcd[i]) {
                if (v[x] >= K) {
                    bw.write(x + "\n");
                    break;
                }
            }
        }
        bw.flush();
    }
}