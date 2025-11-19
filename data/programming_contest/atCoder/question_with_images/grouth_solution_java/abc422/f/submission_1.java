import java.io.*;
import java.util.*;

public class Main {

    static FastScanner sc = new FastScanner();
    static PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

    public static void main(String[] args) {
        int t = 1;
        while (t-- > 0) {
            solve();
        }
        out.close();
    }

    record State(int u, long f, long w) {}

    record FW(long f, long w) {}

    static void solve() {
        int n = sc.nextInt(), m = sc.nextInt();
        int[] W = new int[n+1];
        for (int i = 1; i <= n; ++i){
            W[i] = sc.nextInt();
        }
        List<Integer>[] adj = new List[n+1];
        for (int i = 1; i <= n; ++i){
            adj[i] = new ArrayList<>();
        }
        for (int i = 1; i <= m; ++i){
            int u = sc.nextInt(), v = sc.nextInt();
            adj[u].add(v);
            adj[v].add(u);
        }
        List<FW>[] frontiers = new List[n+1];
        for (int i = 1; i <= n; ++i){
            frontiers[i] = new ArrayList<>();
        }
        long[] dist = new long[n+1];
        final long INF = Long.MAX_VALUE >> 1;
        Arrays.fill(dist, INF);
        PriorityQueue<State> pq = new PriorityQueue<>(Comparator.comparingLong(State::f).thenComparingLong(State::w));
        pq.add(new State(1, 0, 0));
        while (!pq.isEmpty()) {
            State cur = pq.poll();
            int u = cur.u;
            long f = cur.f, w = cur.w;
            if (check(u, f, w, frontiers)) continue;
            if (f < dist[u]) dist[u] = f;
            insert(u, f, w, frontiers);
            long nw = w + W[u];
            long nf = f + nw;
            for (int v : adj[u]) {
                pq.add(new State(v, nf, nw));
            }
        }
        for (int i = 1; i <= n; ++i){
            out.println(dist[i]);
        }
    }

    static boolean check(int u, long f, long w, List<FW>[] frontiers) {
        List<FW> list = frontiers[u];
        for (FW fw : list) {
            if (f >= fw.f && w >= fw.w) return true;
        }
        return false;
    }

    static void insert(int u, long f, long w, List<FW>[] frontiers) {
        List<FW> list = frontiers[u];
        list.removeIf(fw -> f <= fw.f && w <= fw.w);
        list.add(new FW(f, w));
    }

    static class FastScanner {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        String next() {
            try {
                while (st == null || !st.hasMoreTokens()) {
                    st = new StringTokenizer(br.readLine());
                }
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
            return st.nextToken();
        }
        int nextInt() {
            return Integer.parseInt(next());
        }
        long nextLong() {
            return Long.parseLong(next());
        }
        double nextDouble() {
            return Double.parseDouble(next());
        }
    }
}