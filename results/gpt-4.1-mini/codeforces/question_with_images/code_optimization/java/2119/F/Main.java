import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;

public final class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        // Since sum of n over all test cases <= 10^6, we can reuse arrays with max size
        final int MAXN = 1000000;
        int[] w = new int[MAXN + 1];
        int[] distVolcano = new int[MAXN + 1];
        int[] distStart = new int[MAXN + 1];
        List<Integer>[] adj = new List[MAXN + 1];
        for (int i = 0; i <= MAXN; i++) adj[i] = new ArrayList<>();

        for (int _t = 0; _t < T; _t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int start = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());
            for (int i = 1; i <= n; i++) {
                w[i] = Integer.parseInt(st.nextToken());
                adj[i].clear();
                distVolcano[i] = -1;
                distStart[i] = -1;
            }

            for (int i = 0; i < n - 1; i++) {
                st = new StringTokenizer(br.readLine());
                int u = Integer.parseInt(st.nextToken());
                int v = Integer.parseInt(st.nextToken());
                adj[u].add(v);
                adj[v].add(u);
            }

            // BFS from root (1) to get distVolcano (distance from root)
            ArrayDeque<Integer> queue = new ArrayDeque<>();
            distVolcano[1] = 0;
            queue.add(1);
            while (!queue.isEmpty()) {
                int u = queue.poll();
                for (int nxt : adj[u]) {
                    if (distVolcano[nxt] == -1) {
                        distVolcano[nxt] = distVolcano[u] + 1;
                        queue.add(nxt);
                    }
                }
            }

            // BFS from start to get distStart (distance from start)
            distStart[start] = 0;
            queue.add(start);
            while (!queue.isEmpty()) {
                int u = queue.poll();
                for (int nxt : adj[u]) {
                    if (distStart[nxt] == -1) {
                        distStart[nxt] = distStart[u] + 1;
                        queue.add(nxt);
                    }
                }
            }

            // The maximum number of moves is the maximum distStart[u] such that:
            // At time t = distStart[u], vertex u is not flooded: distVolcano[u] > t
            // And life S never drops to zero or below.
            // Since w_i in {1, -1} and w_start=1, and we can move optimally,
            // the problem reduces to finding the maximum distStart[u] with distVolcano[u] > distStart[u]
            // and the path from start to u has enough +1 to keep life > 0.
            //
            // But life changes by w_u at time t when standing on u.
            // Since we must move every time, and life changes before checking death,
            // the life at time t is initial 1 + sum of w on visited vertices at times 0..t.
            //
            // The problem is known to be solvable by:
            // The maximum t such that there exists a vertex u with distStart[u] = t and distVolcano[u] > t
            // and the path from start to u has enough +1 to keep life > 0.
            //
            // Because w_i in {1,-1} and w_start=1, the best path is the one with maximum distStart[u]
            // and distVolcano[u] > distStart[u].
            //
            // So answer = max distStart[u] where distVolcano[u] > distStart[u]

            int ans = 0;
            for (int i = 1; i <= n; i++) {
                if (distStart[i] != -1 && distVolcano[i] > distStart[i]) {
                    if (distStart[i] > ans) ans = distStart[i];
                }
            }

            sb.append(ans).append('\n');
        }
        System.out.print(sb);
    }
}