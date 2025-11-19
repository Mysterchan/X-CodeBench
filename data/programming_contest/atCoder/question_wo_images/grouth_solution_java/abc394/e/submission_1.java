import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.IOException;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);

        int N = Integer.parseInt(br.readLine().trim());

        char[][] adj = new char[N][N];
        for (int i = 0; i < N; i++) {
            String line = br.readLine().trim();
            for (int j = 0; j < N; j++) {
                adj[i][j] = line.charAt(j);
            }
        }

        int[][] ans = new int[N][N];
        for (int i = 0; i < N; i++) {
            Arrays.fill(ans[i], -1);
        }

        Queue<int[]> q = new ArrayDeque<>();

        for (int i = 0; i < N; i++) {
            ans[i][i] = 0;
            q.add(new int[]{i, i});
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (adj[i][j] != '-') {

                    if (ans[i][j] == -1) {
                        ans[i][j] = 1;
                        q.add(new int[]{i, j});
                    }
                }
            }
        }

        while (!q.isEmpty()) {
            int[] curr = q.poll();
            int u = curr[0];
            int v = curr[1];
            int d = ans[u][v];

            for (int u_prev = 0; u_prev < N; u_prev++) {
                char c1 = adj[u_prev][u];
                if (c1 == '-') {
                    continue;
                }

                for (int v_succ = 0; v_succ < N; v_succ++) {
                    char c2 = adj[v][v_succ];

                    if (c1 == c2 && ans[u_prev][v_succ] == -1) {
                        ans[u_prev][v_succ] = d + 2;
                        q.add(new int[]{u_prev, v_succ});
                    }
                }
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                out.print(ans[i][j]);
                if (j < N - 1) {
                    out.print(" ");
                }
            }
            out.println();
        }

        out.flush();
    }
}