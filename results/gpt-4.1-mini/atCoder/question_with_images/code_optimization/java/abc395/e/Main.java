import java.io.*;
import java.util.*;

public class Main {
    static class Edge {
        int to;
        Edge(int t) { to = t; }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());
        long x = Long.parseLong(st.nextToken());

        List<Edge>[] adj = new ArrayList[n];
        List<Edge>[] revAdj = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<>();
            revAdj[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken()) - 1;
            int v = Integer.parseInt(st.nextToken()) - 1;
            adj[u].add(new Edge(v));
            revAdj[v].add(new Edge(u));
        }

        // dist[node][parity] = minimum cost to reach node with parity of reversals
        long[][] dist = new long[n][2];
        for (int i = 0; i < n; i++) {
            dist[i][0] = Long.MAX_VALUE;
            dist[i][1] = Long.MAX_VALUE;
        }
        dist[0][0] = 0;

        // Use a deque for 0-1 BFS
        Deque<int[]> dq = new ArrayDeque<>();
        // Each element: {node, parity}
        dq.addFirst(new int[]{0, 0});

        while (!dq.isEmpty()) {
            int[] cur = dq.pollFirst();
            int u = cur[0], p = cur[1];
            long cost = dist[u][p];

            // Move along edges in current direction
            List<Edge>[] graph = (p == 0) ? adj : revAdj;
            for (Edge e : graph[u]) {
                int v = e.to;
                if (dist[v][p] > cost + 1) {
                    dist[v][p] = cost + 1;
                    dq.addLast(new int[]{v, p});
                }
            }

            // Reverse edges (toggle parity)
            int np = 1 - p;
            if (dist[u][np] > cost + x) {
                dist[u][np] = cost + x;
                // Reversing edges is a costly operation, add to back
                dq.addLast(new int[]{u, np});
            }
        }

        long answer = Math.min(dist[n - 1][0], dist[n - 1][1]);
        System.out.println(answer);
    }
}