import java.util.*;
import java.io.*;

public class Main {
    static final int MAXN = 200000;
    static int[][] dp;
    static int[] inDegree;
    static ArrayList<Integer>[] graph;

    static void dfs(int node, int state) {
        if (dp[node][state] != 0) return;
        dp[node][state] = 1;

        for (int neighbor : graph[node]) {
            if (state == 0) {
                dfs(neighbor, 1);
            } else {
                inDegree[neighbor]--;
                if (inDegree[neighbor] == 0) {
                    dfs(neighbor, 0);
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);

        int T = Integer.parseInt(br.readLine());

        while (T-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int q = Integer.parseInt(st.nextToken());

            dp = new int[n][2];
            inDegree = new int[n];
            graph = new ArrayList[n];

            for (int i = 0; i < n; i++) {
                graph[i] = new ArrayList<>();
                inDegree[i] = 0;
                dp[i][0] = 0;
                dp[i][1] = 0;
            }

            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                int u = Integer.parseInt(st.nextToken()) - 1;
                int v = Integer.parseInt(st.nextToken()) - 1;
                graph[v].add(u);
                inDegree[u]++;
            }

            for (int i = 0; i < q; i++) {
                st = new StringTokenizer(br.readLine());
                int op = Integer.parseInt(st.nextToken());
                int u = Integer.parseInt(st.nextToken()) - 1;

                if (op == 1) {
                    dfs(u, 0);
                    dfs(u, 1);
                } else {
                    if (dp[u][0] == 0) {
                        pw.println("YES");
                    } else {
                        pw.println("NO");
                    }
                }
            }
        }

        pw.flush();
        pw.close();
    }
}
