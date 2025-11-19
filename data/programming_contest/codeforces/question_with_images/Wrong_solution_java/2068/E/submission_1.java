import java.io.*;
import java.util.*;

public class Main {
    static int n, m;
    static ArrayList<Integer>[] graph;
    static int[] distFromStart, distFromEnd;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        graph = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) graph[i] = new ArrayList<>();

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            graph[u].add(v);
            graph[v].add(u);
        }

        distFromStart = bfs(1);
        distFromEnd = bfs(n);

        int shortestPathLength = distFromStart[n];
        if (shortestPathLength == Integer.MAX_VALUE) {
            System.out.println(-1);
            return;
        }

        int maxDist = shortestPathLength;

        for (int u = 1; u <= n; u++) {
            for (int v : graph[u]) {
                if (distFromStart[u] + 1 + distFromEnd[v] == shortestPathLength) {
                    int detour = distFromStart[u] + 1 + distFromEnd[v];
                    maxDist = Math.max(maxDist, shortestPathLength + 1);
                }
            }
        }
        System.out.println(maxDist);
    }

    static int[] bfs(int start) {
        int[] dist = new int[n + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[start] = 0;
        Queue<Integer> q = new ArrayDeque<>();
        q.add(start);
        while (!q.isEmpty()) {
            int u = q.poll();
            for (int v : graph[u]) {
                if (dist[v] == Integer.MAX_VALUE) {
                    dist[v] = dist[u] + 1;
                    q.add(v);
                }
            }
        }
        return dist;
    }
}
