import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static int[] degree;
    static boolean[] visited;
    static int[][] adj;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        // For a cycle graph, number of edges must be equal to number of vertices
        if (M != N) {
            System.out.println("No");
            return;
        }

        degree = new int[N + 1];
        adj = new int[N + 1][2]; // each vertex has exactly 2 neighbors in a cycle
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            // Increase degree and store neighbors
            if (degree[a] == 2 || degree[b] == 2) {
                // degree cannot exceed 2 in a cycle graph
                System.out.println("No");
                return;
            }

            adj[a][degree[a]++] = b;
            adj[b][degree[b]++] = a;
        }

        // Check all vertices have degree exactly 2
        for (int i = 1; i <= N; i++) {
            if (degree[i] != 2) {
                System.out.println("No");
                return;
            }
        }

        // Check connectivity and cycle property by DFS or BFS
        visited = new boolean[N + 1];
        int count = dfs(1, -1);

        // If all vertices are visited and degrees are 2, it's a cycle graph
        System.out.println(count == N ? "Yes" : "No");
    }

    static int dfs(int node, int parent) {
        visited[node] = true;
        int count = 1;
        for (int i = 0; i < 2; i++) {
            int next = adj[node][i];
            if (next == parent) continue;
            if (visited[next]) continue;
            count += dfs(next, node);
        }
        return count;
    }
}