import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        StringBuilder result = new StringBuilder();

        while (t-- > 0) {
            int n = scanner.nextInt();
            String s = scanner.next();
            List<List<Integer>> adj = new ArrayList<>(n + 1);
            for (int i = 0; i <= n; i++) {
                adj.add(new ArrayList<>());
            }

            for (int i = 0; i < n - 1; i++) {
                int u = scanner.nextInt();
                int v = scanner.nextInt();
                adj.get(u).add(v);
                adj.get(v).add(u);
            }

            int[] maxNicePath = new int[n + 1];
            int[] distFromRoot = new int[n + 1];
            boolean[] visited = new boolean[n + 1];

            for (int i = 1; i <= n; i++) {
                if (s.charAt(i - 1) == '1') {
                    Arrays.fill(visited, false);
                    Arrays.fill(maxNicePath, -1);
                    dfs(i, 0, 1, visited, distFromRoot, maxNicePath, adj, s);
                }
            }

            for (int i = 1; i <= n; i++) {
                result.append(maxNicePath[i]).append(" ");
            }
            result.append("\n");
        }
        System.out.print(result);
        scanner.close();
    }

    private static void dfs(int node, int parentDistance, int currentPathLength, boolean[] visited,
                            int[] distFromRoot, int[] maxNicePath, List<List<Integer>> adj, String s) {
        visited[node] = true;
        maxNicePath[node] = Math.max(maxNicePath[node], currentPathLength);

        for (int neighbor : adj.get(node)) {
            if (!visited[neighbor]) {
                int edgeWeight = 1; // All edges in the tree have weight 1
                int nextPathLength = (2 * edgeWeight <= parentDistance) ? currentPathLength + 1 : 1; // Reset at the first step
                dfs(neighbor, edgeWeight, nextPathLength, visited, distFromRoot, maxNicePath, adj, s);
            }
        }
    }
}