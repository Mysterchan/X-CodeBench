import java.io.*;
import java.util.*;

public class Main {
    static class MScanner {
        StringTokenizer st;
        BufferedReader br;

        public MScanner(InputStream system) {
            br = new BufferedReader(new InputStreamReader(system));
        }

        public String next() throws IOException {
            while (st == null || !st.hasMoreTokens())
                st = new StringTokenizer(br.readLine());
            return st.nextToken();
        }

        public int nextInt() throws IOException {
            return Integer.parseInt(next());
        }
    }

    static void bfs(int start, int target, List<Integer>[] graph, PrintWriter pw) {
        Queue<Integer> queue = new LinkedList<>();
        Map<Integer, Integer> parentMap = new HashMap<>();
        boolean[] visited = new boolean[graph.length];

        queue.offer(start);
        visited[start] = true;

        while (!queue.isEmpty()) {
            int node = queue.poll();
            if (node == target) break;

            for (int neighbor : graph[node]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    parentMap.put(neighbor, node);
                    queue.offer(neighbor);
                }
            }
        }

        List<Integer> path = new ArrayList<>();
        for (Integer curr = target; curr != null; curr = parentMap.get(curr)) {
            path.add(curr);
        }
        Collections.reverse(path);
        for (int v : path) {
            pw.print(v + " ");
        }
        pw.println();
    }

    public static void main(String[] args) throws IOException {
        MScanner sc = new MScanner(System.in);
        PrintWriter pw = new PrintWriter(System.out);
        int t = sc.nextInt();

        for (int i = 0; i < t; i++) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int x = sc.nextInt();
            int y = sc.nextInt();
            List<Integer>[] graph = new ArrayList[n + 1];
            for (int j = 1; j <= n; j++) {
                graph[j] = new ArrayList<>();
            }
            for (int j = 0; j < m; j++) {
                int u = sc.nextInt();
                int v = sc.nextInt();
                graph[u].add(v);
                graph[v].add(u);
            }
            for (int j = 1; j <= n; j++) {
                Collections.sort(graph[j]);
            }

            bfs(x, y, graph, pw);
        }

        pw.flush();
    }
}