import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        List<List<Integer>> adj = new ArrayList<>(n + 1);
        for (int i = 0; i <= n; i++) {
            adj.add(new ArrayList<>());
        }
        
        int[] degree = new int[n + 1];

        for (int i = 0; i < n - 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            adj.get(u).add(v);
            adj.get(v).add(u);
            degree[u]++;
            degree[v]++;
        }

        long maxVertices = 0;
        boolean hasFourDegree = false;

        for (int i = 1; i <= n; i++) {
            if (degree[i] == 4) {
                hasFourDegree = true;
            }
        }

        if (!hasFourDegree) {
            System.out.println(-1);
            return;
        }

        boolean[] visited = new boolean[n + 1];
        for (int i = 1; i <= n; i++) {
            if (degree[i] >= 1 && !visited[i]) {
                long count = dfs(i, adj, degree, visited);
                if (count > 0) {
                    maxVertices = Math.max(maxVertices, count);
                }
            }
        }

        System.out.println(maxVertices > 0 ? 3 * maxVertices + 2 : -1);
    }

    private static long dfs(int cur, List<List<Integer>> adj, int[] degree, boolean[] visited) {
        visited[cur] = true;
        long count = 1;
        List<Long> children = new ArrayList<>();

        for (int nxt : adj.get(cur)) {
            if (!visited[nxt] && degree[nxt] >= 1) {
                long childCount = dfs(nxt, adj, degree, visited);
                if (degree[nxt] >= 4) {
                    children.add(childCount);
                }
                count += childCount;
            }
        }

        Collections.sort(children, Collections.reverseOrder());
        long selectCount = 0;
        for (int i = 0; i < Math.min(3, children.size()); i++) {
            selectCount += children.get(i);
        }

        return count + selectCount - 1; // -1 because cur is counted in the total
    }
}