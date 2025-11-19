import java.io.*;
import java.util.*;

public class Main {

    static FastScanner sc = new FastScanner();
    static PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

    static class State implements Comparable<State> {
        int u;
        long fuel, w;
        State(int u, long fuel, long w) { this.u = u; this.fuel = fuel; this.w = w; }
        public int compareTo(State o) {
            if (fuel != o.fuel) return Long.compare(fuel, o.fuel);
            if (w != o.w) return Long.compare(w, o.w);
            return Integer.compare(u, o.u);
        }
    }

    static final long INF = Long.MAX_VALUE / 4;

    public static void main(String[] args) {
        solve();
        out.close();
    }

    static void solve() {
        int n = sc.nextInt();
        int m = sc.nextInt();
        long[] W = new long[n + 1];
        for (int i = 1; i <= n; i++) W[i] = sc.nextLong();

        List<Integer>[] g = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) g[i] = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt(), v = sc.nextInt();
            g[u].add(v);
            g[v].add(u);
        }

        ArrayList<long[]>[] frontier = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) frontier[i] = new ArrayList<>();

        long[] ans = new long[n + 1];
        Arrays.fill(ans, INF);

        PriorityQueue<State> pq = new PriorityQueue<>();

        addState(1, 0L, 0L, frontier, ans);
        pq.add(new State(1, 0L, 0L));

        while (!pq.isEmpty()) {
            State cur = pq.poll();
            int u = cur.u;
            long f = cur.fuel, w = cur.w;

            if (isDominated(u, f, w, frontier)) continue;

            long nw = w + W[u];
            long nf = f + nw;
            for (int v : g[u]) {

                if (wouldBeKept(v, nf, nw, frontier)) {
                    addState(v, nf, nw, frontier, ans);
                    pq.add(new State(v, nf, nw));
                }
            }
        }

        for (int i = 1; i <= n; i++) {

            out.println(ans[i] == INF ? -1 : ans[i]);
        }
    }

    static boolean isDominated(int u, long f, long w, ArrayList<long[]>[] frontier) {
        for (long[] p : frontier[u]) {
            if (p[0] <= f && p[1] <= w) return true;
        }
        return false;
    }

    static boolean wouldBeKept(int u, long f, long w, ArrayList<long[]>[] frontier) {
        return !isDominated(u, f, w, frontier);
    }

    static void addState(int u, long f, long w, ArrayList<long[]>[] frontier, long[] ans) {

        if (isDominated(u, f, w, frontier)) return;

        ArrayList<long[]> list = frontier[u];
        for (int i = list.size() - 1; i >= 0; i--) {
            long[] p = list.get(i);
            if (f <= p[0] && w <= p[1]) {
                list.remove(i);
            }
        }
        list.add(new long[]{f, w});
        if (f < ans[u]) ans[u] = f;
    }

    static class FastScanner {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        String next() {
            try {
                while (st == null || !st.hasMoreTokens()) st = new StringTokenizer(br.readLine());
            } catch (IOException e) { throw new RuntimeException(e); }
            return st.nextToken();
        }
        int nextInt() { return Integer.parseInt(next()); }
        long nextLong() { return Long.parseLong(next()); }
        double nextDouble() { return Double.parseDouble(next()); }
    }
}