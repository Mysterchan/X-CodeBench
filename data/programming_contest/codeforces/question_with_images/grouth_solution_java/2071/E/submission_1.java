import java.io.*;
import java.util.*;

public class Main {
    static final long m = 998244353L;

    static long pwr(long b, long e) {
        long r = 1;
        b %= m;
        while(e > 0) {
            if((e & 1) == 1) r = (r * b) % m;
            b = (b * b) % m;
            e >>= 1;
        }
        return r;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(new BufferedOutputStream(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());
        for (int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            long[] pr = new long[n];
            long[] ip = new long[n];
            for (int j = 0; j < n; j++) {
                st = new StringTokenizer(br.readLine());
                long a = Long.parseLong(st.nextToken());
                long b = Long.parseLong(st.nextToken());
                long v = (a * pwr(b, m - 2)) % m;
                ip[j] = (1 - v + m) % m;
                pr[j] = ip[j];
                ip[j] = v;
            }
            ArrayList<Integer>[] g = new ArrayList[n];
            for (int j = 0; j < n; j++) {
                g[j] = new ArrayList<>();
            }
            for (int j = 0; j < n - 1; j++) {
                st = new StringTokenizer(br.readLine());
                int u = Integer.parseInt(st.nextToken()) - 1;
                int v = Integer.parseInt(st.nextToken()) - 1;
                g[u].add(v);
                g[v].add(u);
            }
            long[] pl = new long[n];
            long[] iprod = new long[n];
            for (int j = 0; j < n; j++) {
                iprod[j] = 1;
                for (int k : g[j]) iprod[j] = (iprod[j] * ip[k]) % m;
                long s = 0;
                for (int k : g[j]) {
                    long t = (iprod[j] * pwr(ip[k], m - 2)) % m;
                    t = (t * pr[k]) % m;
                    s = (s + t) % m;
                }
                pl[j] = (s * pr[j]) % m;
            }
            long sp = 0;
            for (int j = 0; j < n; j++) sp = (sp + pl[j]) % m;
            long ans = (sp * sp) % m;
            for (int j = 0; j < n; j++) ans = (ans - (pl[j] * pl[j]) % m + m) % m;
            for (int j = 0; j < n; j++)
                for (int k : g[j]) ans = (ans - (pl[j] * pl[k]) % m + m) % m;
            for (int j = 0; j < n; j++) {
                for (int k : g[j]) {
                    long c = (iprod[j] * iprod[k]) % m;
                    c = (c * pwr(ip[k], m - 2)) % m;
                    c = (c * pwr(ip[j], m - 2)) % m;
                    c = (c * pr[k]) % m;
                    c = (c * pr[j]) % m;
                    ans = (ans + c) % m;
                }
            }
            for (int j = 0; j < n; j++) {
                long sumN = 0;
                for (int k : g[j]) sumN = (sumN + pl[k]) % m;
                ans = (ans - (sumN * sumN) % m + m) % m;
                for (int k : g[j]) ans = (ans + (pl[k] * pl[k]) % m) % m;
                long s1 = 0, s2 = 0, s1sq = 0, s2sq = 0;
                for (int k : g[j]) {
                    long t1 = (iprod[k] * pwr(ip[j], m - 2)) % m;
                    t1 = (t1 * pr[k]) % m;
                    long t2 = (pl[k] - (t1 * pr[j]) % m + m) % m;
                    t2 = (t2 * pwr(ip[j], m - 2)) % m;
                    s1 = (s1 + t1) % m;
                    s2 = (s2 + t2) % m;
                    s1sq = (s1sq + (t1 * t1) % m) % m;
                    s2sq = (s2sq + (t2 * t2) % m) % m;
                }
                long tmp = ((s1 * s1) % m - s1sq + m) % m;
                ans = (ans + (tmp * pr[j]) % m) % m;
                tmp = ((s2 * s2) % m - s2sq + m) % m;
                ans = (ans + (tmp * ip[j]) % m) % m;
            }
            ans = (ans * pwr(2, m - 2)) % m;
            out.println(ans);
        }
        out.flush();
        out.close();
    }
}
