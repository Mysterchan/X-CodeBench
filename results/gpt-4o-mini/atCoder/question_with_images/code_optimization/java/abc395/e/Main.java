import java.util.*;

public class Main {
    static class Edge {
        int to;
        Edge(int t) { to = t; }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), m = sc.nextInt(), x = sc.nextInt();

        List<Edge>[] adj = new ArrayList[n];
        List<Edge>[] revAdj = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<>();
            revAdj[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            int u = sc.nextInt() - 1;
            int v = sc.nextInt() - 1;
            adj[u].add(new Edge(v));
            revAdj[v].add(new Edge(u));
        }

        long[] dist = new long[n];
        Arrays.fill(dist, Long.MAX_VALUE);
        dist[0] = 0;

        PriorityQueue<long[]> pq = new PriorityQueue<>(Comparator.comparingLong(a -> a[1]));
        pq.offer(new long[]{0, 0}); // {node, cost}

        while (!pq.isEmpty()) {
            long[] current = pq.poll();
            int u = (int) current[0];
            long cost = current[1];

            if (cost > dist[u]) continue;

            // Move along edges
            for (Edge e : adj[u]) {
                int v = e.to;
                if (dist[v] > cost + 1) {
                    dist[v] = cost + 1;
                    pq.offer(new long[]{v, dist[v]});
                }
            }

            // Reverse edges
            if (dist[u] > cost + x) {
                dist[u] = cost + x;
                pq.offer(new long[]{u, dist[u]});
            }

            // Move along reversed edges
            for (Edge e : revAdj[u]) {
                int v = e.to;
                if (dist[v] > cost + 1) {
                    dist[v] = cost + 1;
                    pq.offer(new long[]{v, dist[v]});
                }
            }
        }

        long answer = dist[n - 1];
        System.out.println(answer);
    }
}