import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        char[][] matrix = new char[n][];
        for (int i = 0; i < n; i++) {
            matrix[i] = br.readLine().toCharArray();
        }

        int maxNode = n * n;
        ArrayList<int[]>[] g = new ArrayList[maxNode + 1];
        for (int i = 0; i <= maxNode; i++) {
            g[i] = new ArrayList<>();
        }

        // Node maxNode is the special start node
        for (int i = 0; i < n; i++) {
            g[maxNode].add(new int[]{i * n + i, 0});
        }

        Map<Character, ArrayList<Integer>> edge = new HashMap<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                char c = matrix[i][j];
                if (c == '-') continue;
                
                ArrayList<Integer> list = edge.get(c);
                if (list != null) {
                    for (int k : list) {
                        int a = k / n, b = k % n;
                        g[j * n + a].add(new int[]{i * n + b, 2});
                        g[b * n + i].add(new int[]{a * n + j, 2});
                    }
                }
                edge.computeIfAbsent(c, k -> new ArrayList<>()).add(i * n + j);
                
                if (i != j) {
                    g[maxNode].add(new int[]{i * n + j, 1});
                }
            }
        }

        int[] dist = new int[maxNode];
        Arrays.fill(dist, Integer.MAX_VALUE);
        
        Deque<Integer> q = new ArrayDeque<>();
        q.add(maxNode);
        dist[maxNode] = 0;

        while (!q.isEmpty()) {
            int u = q.poll();
            int d = u == maxNode ? 0 : dist[u];
            
            for (int[] edge_info : g[u]) {
                int v = edge_info[0];
                int w = edge_info[1];
                int newDist = d + w;
                
                if (newDist < dist[v]) {
                    dist[v] = newDist;
                    q.add(v);
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int d = dist[i * n + j];
                sb.append(d == Integer.MAX_VALUE ? -1 : d);
                if (j < n - 1) sb.append(' ');
            }
            sb.append('\n');
        }
        System.out.print(sb);
    }
}