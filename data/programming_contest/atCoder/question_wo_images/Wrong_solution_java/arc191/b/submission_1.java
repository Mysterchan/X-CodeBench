import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) {
        int T = sc.nextInt();
        while (T-- > 0) {
            int n = sc.nextInt(), k = sc.nextInt() - 1;
            if (k == 0) {
                out.println(n);
                continue;
            }
            char[] s = Integer.toBinaryString(n).toCharArray();
            int cnt = 0;
            int len = s.length;
            List<Integer> l = new ArrayList<>();
            for (int i = len - 1, j = 0; i >= 0; i--, j++) {
                if (s[i] == '0') {
                    l.add(j);
                    cnt++;
                }
            }
            if (k > 1 << cnt) {
                out.println(-1);
                continue;
            }
            int ans = 0;
            int p = 0;

            for (int i = 0; i < cnt; i++) {
                if ((k >> i & 1) == 1) {
                    ans |= 1 << l.get(p);
                }
                p++;
            }
            for (int i = 0, j = len - 1; i < len; i++, j--) {
                if (s[i] == '1') ans |= 1 << j;
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