import java.io.*;
import java.util.*;

public class Main {
    static PrintWriter pw;
    static MScanner sc;

    public static void main(String[] args) throws IOException {
        sc = new MScanner(System.in);
        pw = new PrintWriter(System.out);
        int t = sc.nextInt();

        for (int i = 0; i < t; i++) {
            solver();
        }
        pw.flush();
    }

    public static void solver() throws IOException {
        int n = sc.nextInt();
        int m = sc.nextInt();
        int x = sc.nextInt();
        int y = sc.nextInt();

        List<Integer>[] graph = new List[n + 1];
        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            graph[u].add(v);
            graph[v].add(u);
        }

        // Sort adjacency lists to ensure lex order traversal
        for (int i = 1; i <= n; i++) {
            Collections.sort(graph[i]);
        }

        // BFS to find shortest lexicographically smallest path
        int[] parent = new int[n + 1];
        Arrays.fill(parent, -1);
        parent[x] = 0;

        PriorityQueue<Integer> pq = new PriorityQueue<>();
        pq.add(x);

        while (!pq.isEmpty()) {
            int cur = pq.poll();
            if (cur == y) break;
            for (int nxt : graph[cur]) {
                if (parent[nxt] == -1) {
                    parent[nxt] = cur;
                    pq.add(nxt);
                }
            }
        }

        // Reconstruct path from y to x
        List<Integer> path = new ArrayList<>();
        int cur = y;
        while (cur != 0) {
            path.add(cur);
            cur = parent[cur];
        }
        Collections.reverse(path);

        for (int v : path) {
            pw.print(v);
            pw.print(' ');
        }
        pw.println();
    }

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
}