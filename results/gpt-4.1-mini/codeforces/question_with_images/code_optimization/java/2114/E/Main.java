import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int[] a;
    static List<List<Integer>> adj;
    static long[] dp0, dp1; // dp0[u]: max alternating sum starting at u with + sign at u, dp1[u]: with - sign at u

    static void dfs(int u, int p) {
        dp0[u] = a[u];
        dp1[u] = -a[u];
        for (int v : adj.get(u)) {
            if (v == p) continue;
            dfs(v, u);
            // If we continue path from u to v, sign flips
            dp0[u] = Math.max(dp0[u], a[u] + dp1[v]);
            dp1[u] = Math.min(dp1[u], -a[u] + dp0[v]);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder output = new StringBuilder();

        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            n = Integer.parseInt(br.readLine());
            a = new int[n + 1];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 1; i <= n; i++) {
                a[i] = Integer.parseInt(st.nextToken());
            }

            adj = new ArrayList<>();
            for (int i = 0; i <= n; i++) adj.add(new ArrayList<>());

            for (int i = 0; i < n - 1; i++) {
                st = new StringTokenizer(br.readLine());
                int u = Integer.parseInt(st.nextToken());
                int v = Integer.parseInt(st.nextToken());
                adj.get(u).add(v);
                adj.get(v).add(u);
            }

            dp0 = new long[n + 1];
            dp1 = new long[n + 1];

            dfs(1, 0);

            for (int i = 1; i <= n; i++) {
                output.append(dp0[i]).append(' ');
            }
            output.append('\n');
        }

        bw.write(output.toString());
        bw.flush();
        bw.close();
    }
}