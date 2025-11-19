import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        // A cycle graph must have exactly n edges and n vertices
        if (m != n) {
            System.out.println("No");
            return;
        }

        // Adjacency list
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        Set<Integer> visited = new HashSet<>();

        // Reading edges and building the graph
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        // Check degree of each vertex
        for (int i = 1; i <= n; i++) {
            if (graph.get(i).size() != 2) {
                System.out.println("No");
                return;
            }
        }

        // Start a DFS or BFS from vertex 1 to check connectivity
        if (!dfs(1, -1, visited, graph)) {
            System.out.println("No");
            return;
        }

        // Check if we visited all vertices
        if (visited.size() == n) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
        br.close();
    }

    private static boolean dfs(int node, int parent, Set<Integer> visited, List<List<Integer>> graph) {
        visited.add(node);
        for (int neighbor : graph.get(node)) {
            if (!visited.contains(neighbor)) {
                if (!dfs(neighbor, node, visited, graph)) {
                    return false;
                }
            } else if (neighbor != parent) {
                // If we visit a visited vertex that is not the parent, it's a cycle
                return false;
            }
        }
        return true;
    }
}