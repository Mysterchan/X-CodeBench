import java.io.*;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) {
        int T = sc.nextInt();
        while (T-- > 0) {
            solve();
        }
        out.close();
    }

    static void solve() {
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        long ans = 0;
        int pt = -1;
        int[] val = new int[n + 1];
        int[] cnt = new int[n + 1];
        int cc = 0;
        for (int i = 0; i < n; i++) {
            cc = 0;
            while (pt > -1 && val[pt] <= a[i]) {
                if (pt == 0) {
                    int[] f = f(val[pt], cnt[pt], a[i]);
                    ans += f[0];
                    pt--;
                    cc += f[1];
                    break;
                } else {
                    if (val[pt - 1] == a[i]) {
                        int[] f = f(val[pt], cnt[pt], a[i]);
                        ans += f[0];
                        pt--;
                        cc += f[1] + cnt[pt];
                        pt--;
                        break;
                    } else if (val[pt - 1] > a[i]) {
                        int[] f = f(val[pt], cnt[pt], a[i]);
                        ans += f[0];
                        pt--;
                        cc += f[1];
                        break;
                    } else {
                        int[] f = f(val[pt], cnt[pt], val[pt - 1]);
                        ans += f[0];
                        pt--;
                        cnt[pt] += f[1];
                    }
                }
            }
            pt++;
            val[pt] = a[i];
            cnt[pt] = cc + 1;

        }

        while (pt >= 0) {
            if (pt > 0) {
                int[] z = f(val[pt], cnt[pt], val[pt - 1]);
                ans += z[0];
                cnt[pt - 1] += z[1];
                pt--;
            } else {
                ans += g(cnt[pt]);
                pt--;
            }
        }
        out.println(ans);
    }

    static int g(int c) {
        int ans = 0;
        while (c > 1) {
            ans += c % 2;
            c = (c + 1) / 2;
        }
        return ans;
    }

    static int[] f(int v, int c, int v2) {
        int ans = 0;
        while (v < v2 && c > 1) {
            ans += c % 2;
            v++;
            c = (c + 1) / 2;
        }
        ans += v2 - v;
        return new int[]{ans, c};
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