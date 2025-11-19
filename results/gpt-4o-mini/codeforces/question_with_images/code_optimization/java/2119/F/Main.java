import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public final class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringBuilder output = new StringBuilder();
        
        while (T-- > 0) {
            String[] input = br.readLine().split(" ");
            int n = Integer.parseInt(input[0]);
            int start = Integer.parseInt(input[1]);
            String[] weights = br.readLine().split(" ");
            int[] w = new int[n + 1];
            for (int i = 1; i <= n; ++i) {
                w[i] = Integer.parseInt(weights[i - 1]);
            }
  
            List<List<Integer>> edges = new ArrayList<>();
            for (int i = 0; i <= n; ++i) {
                edges.add(new ArrayList<>());
            }
  
            for (int i = 1; i < n; ++i) {
                String[] edge = br.readLine().split(" ");
                int u = Integer.parseInt(edge[0]);
                int v = Integer.parseInt(edge[1]);
                edges.get(u).add(v);
                edges.get(v).add(u);
            }
  
            int moves = simulateLavaFlood(n, start, w, edges);
            output.append(moves).append("\n");
        }
        System.out.print(output);
    }

    private static int simulateLavaFlood(int n, int start, int[] w, List<List<Integer>> edges) {
        boolean[] visited = new boolean[n + 1];
        visited[start] = true;

        int moves = 0;
        int life = 1;
        int time = 0;
        int current = start;
        int depth = 0;

        List<Integer> currentDepth = new ArrayList<>();
        currentDepth.add(current);
  
        while (depth <= n) {
            List<Integer> nextDepth = new ArrayList<>();
            for (int node : currentDepth) {
                if (life <= 0) {
                    return moves;
                }
                life += w[node];
                if (life <= 0) {
                    return moves;
                }

                for (int neighbor : edges.get(node)) {
                    if (!visited[neighbor] && (depth + 1 < n)) {
                        visited[neighbor] = true;
                        nextDepth.add(neighbor);
                    }
                }
            }

            moves += nextDepth.size();
            currentDepth = nextDepth;
            depth++;
        }
        
        return moves;
    }
}