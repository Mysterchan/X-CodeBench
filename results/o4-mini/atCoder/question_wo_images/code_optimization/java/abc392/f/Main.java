import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static class FastReader {
        BufferedReader br;
        StringTokenizer st;
        public FastReader() { br = new BufferedReader(new InputStreamReader(System.in)); }
        String next() {
            while (st == null || !st.hasMoreTokens()) {
                try { st = new StringTokenizer(br.readLine()); }
                catch (IOException e) { e.printStackTrace(); }
            }
            return st.nextToken();
        }
        int nextInt() { return Integer.parseInt(next()); }
    }

    static class Fenwick {
        int n;
        int[] bit;
        int maxPow;
        public Fenwick(int n) {
            this.n = n;
            bit = new int[n + 1];
            for (int i = 1; i <= n; i++) {
                bit[i] += 1;
                int j = i + (i & -i);
                if (j <= n) bit[j] += bit[i];
            }
            maxPow = 1;
            while ((maxPow << 1) <= n) maxPow <<= 1;
        }
        // find smallest idx such that prefix sum >= k
        public int findKth(int k) {
            int pos = 0;
            for (int pw = maxPow; pw > 0; pw >>= 1) {
                int nxt = pos + pw;
                if (nxt <= n && bit[nxt] < k) {
                    pos = nxt;
                    k -= bit[nxt];
                }
            }
            return pos + 1;
        }
        public void update(int idx, int delta) {
            for (int i = idx; i <= n; i += i & -i) {
                bit[i] += delta;
            }
        }
    }

    public static void main(String[] args) {
        FastReader fr = new FastReader();
        int N = fr.nextInt();
        int[] P = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            P[i] = fr.nextInt();
        }
        int[] ans = new int[N];
        Fenwick fw = new Fenwick(N);
        for (int i = N; i >= 1; i--) {
            int k = P[i];
            int pos = fw.findKth(k);
            ans[pos - 1] = i;
            fw.update(pos, -1);
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            sb.append(ans[i]);
            if (i + 1 < N) sb.append(' ');
        }
        System.out.println(sb.toString());
    }
}