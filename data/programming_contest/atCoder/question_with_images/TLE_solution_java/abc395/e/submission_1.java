import java.util.*;

public class Main {
    static class Edge {
        int to, cost;
        Edge(int t, int c) { to = t; cost = c; }
    }

    static class State {
        int node;
        boolean parity;
        long cost;
        State(int node, boolean parity, long cost) {
            this.node = node;
            this.parity = parity;
            this.cost = cost;
        }
    }

    static List<Edge>[] adj;
    static List<Edge>[] revAdj;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), m = sc.nextInt(), x = sc.nextInt();

        adj = new ArrayList[n];
        revAdj = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<>();
            revAdj[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            int u = sc.nextInt() - 1;
            int v = sc.nextInt() - 1;
            adj[u].add(new Edge(v, 1));
            revAdj[v].add(new Edge(u, 1));
        }

        long[][] dist = new long[n][2];
        for (long[] row : dist) Arrays.fill(row, Long.MAX_VALUE);
        dist[0][0] = 0;

        Deque<State> dq = new ArrayDeque<>();
        dq.addFirst(new State(0, false, 0));

        while (!dq.isEmpty()) {
            State cur = dq.pollFirst();
            int u = cur.node;
            boolean p = cur.parity;
            long cost = cur.cost;

            if (cost > dist[u][p ? 1 : 0]) continue;

            List<Edge>[] graph = p ? revAdj : adj;

            for (Edge e : graph[u]) {
                int v = e.to;
                if (dist[v][p ? 1 : 0] > cost + 1) {
                    dist[v][p ? 1 : 0] = cost + 1;
                    dq.addFirst(new State(v, p, cost + 1));
                }
            }

            if (dist[u][!p ? 1 : 0] > cost + x) {
                dist[u][!p ? 1 : 0] = cost + x;
                dq.addLast(new State(u, !p, cost + x));
            }
        }

        long answer = Math.min(dist[n - 1][0], dist[n - 1][1]);
        System.out.println(answer);
    }
}