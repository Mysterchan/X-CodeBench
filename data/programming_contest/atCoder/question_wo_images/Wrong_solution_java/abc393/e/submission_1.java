import java.io.*;
import java.util.*;

public class Main {
    static final int N = 1200005;
    static final int M = 1000005;

    static int n, k;
    static int[] a = new int[N];
    static int[] cnt = new int[M];
    static int[] ans = new int[N];
    static int[] prime = new int[M];
    static boolean[] vis = new boolean[M];
    static int tot;

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        PrintWriter pw = new PrintWriter(System.out);
        n = sc.nextInt();
        k = sc.nextInt();
        for (int i = 1; i <= n; i++) {
            a[i] = sc.nextInt();
            cnt[a[i]]++;
        }
        for (int i = 2; i <= M - 5; i++) {
            if (!vis[i]) prime[++tot] = i;
            for (int j = 1; j <= tot && i * prime[j] <= M - 5; j++) {
                vis[i * prime[j]] = true;
                if (i % prime[j] == 0) break;
            }
        }
        for (int i = M - 5; i >= 1; i--) {
            for (int j = 1; j <= tot && i * prime[j] <= M - 5; j++) {
                cnt[i] += cnt[i * prime[j]];
            }
        }
        for (int i = 1; i <= n; i++) {
            int x = a[i], res = 0;
            for (int j = 1; j * j <= x; j++) {
                if (x % j == 0) {
                    if (cnt[j] >= k) res = Math.max(res, j);
                    if (cnt[x / j] >= k) res = Math.max(res, x / j);
                }
            }
            ans[i] = res;
        }
        for (int i = 1; i <= n; i++) {
            pw.println(ans[i]);
        }
        pw.close();
    }

    static class Scanner {
        BufferedReader br;
        StringTokenizer st;

        public Scanner(InputStream s) {
            br = new BufferedReader(new InputStreamReader(s));
        }

        public Scanner(FileReader f) {
            br = new BufferedReader(f);
        }

        public String next() throws IOException {
            while (st == null || !st.hasMoreTokens())
                st = new StringTokenizer(br.readLine());
            return st.nextToken();
        }

        public int nextInt() throws IOException {
            return Integer.parseInt(next());
        }

        public long nextLong() throws IOException {
            return Long.parseLong(next());
        }

        public double nextDouble() throws IOException {
            return Double.parseDouble(next());
        }

        public int[] nextIntArr(int n) throws IOException {
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(next());
            }
            return arr;
        }

    }
}