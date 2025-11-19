import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;

public class Main {
    private static void dfs(int node, int parent, long currentSum, int currentDepth, long[] threats, int[] values, List<List<Integer>> adj) {
        threats[node] = currentSum + values[node] * (currentDepth % 2 == 0 ? 1 : -1);
        for (int neighbor : adj.get(node)) {
            if (neighbor != parent) {
                dfs(neighbor, node, threats[node], currentDepth + 1, threats, values, adj);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder output = new StringBuilder();

        int t = Integer.parseInt(br.readLine());

        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine());

            String[] input = br.readLine().split(" ");
            int[] values = new int[n + 1];
            for (int i = 1; i <= n; i++) {
                values[i] = Integer.parseInt(input[i - 1]);
            }

            List<List<Integer>> adj = new ArrayList<>(n + 1);
            for (int i = 0; i <= n; i++) {
                adj.add(new ArrayList<>());
            }

            for (int i = 0; i < n - 1; i++) {
                input = br.readLine().split(" ");
                int u = Integer.parseInt(input[0]);
                int v = Integer.parseInt(input[1]);
                adj.get(u).add(v);
                adj.get(v).add(u);
            }

            long[] threats = new long[n + 1];
            dfs(1, -1, 0, 0, threats, values, adj); // Node 1 is the root, parent is -1

            for (int i = 1; i <= n; i++) {
                output.append(threats[i]).append(" ");
            }
            output.append("\n");
        }

        bw.write(output.toString());
        bw.close();
    }
}