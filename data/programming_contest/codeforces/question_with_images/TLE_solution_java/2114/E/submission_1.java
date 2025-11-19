import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class Main {
    private static void getLevel(int n, int[] level, List<List<Integer>> adj) {
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{1, 0});
        boolean[] vis = new boolean[n+1];
        vis[1] = true;

        while(!q.isEmpty()) {
            int[] top = q.poll();
            int node = top[0];
            int lvl = top[1];

            level[node] = lvl;

            for(int itr: adj.get(node)) {
                if(!vis[itr]) {
                    q.add(new int[]{itr, lvl+1});
                    vis[itr] = true;
                }
            }
        }
    }

    private static long BFS(int node, int[] val, List<List<Integer>> adj, int[] level) {
        Queue<long[]> q = new LinkedList<>();
        q.add(new long[]{node, val[node]});

        long threat = val[node], move = 1;

        while(!q.isEmpty()) {
            long[] top = q.poll();
            int vertex = (int)top[0];
            long value = top[1];

            for(int itr: adj.get(vertex)) {
                if(level[itr] < level[vertex]) {
                    // System.out.println("here");
                    move *= -1;
                    threat = Math.max(threat, value + move*val[itr]);
                    q.add(new long[]{itr, value + move*val[itr]});
                }
            }
        }

        return threat;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder output = new StringBuilder();

        int t = Integer.parseInt(br.readLine());

        while(t-- > 0) {
            int n = Integer.parseInt(br.readLine());

            String[] ip = br.readLine().split(" ");
            int[] val = new int[n+1];
            for(int i=1;i<=n;i++) {
                val[i] = Integer.parseInt(ip[i-1]);
            }

            List<List<Integer>> adj = new ArrayList<>();
            for(int i=0;i<=n;i++) {
                adj.add(new ArrayList<>());
            }

            for(int i=0;i<n-1;i++) {
                ip = br.readLine().split(" ");
                int u = Integer.parseInt(ip[0]);
                int v = Integer.parseInt(ip[1]);
                adj.get(u).add(v);
                adj.get(v).add(u);
            }

            long[] ans = new long[n+1];
            for(int i=1;i<=n;i++) {
                ans[i] = val[i];
            }

            int[] level = new int[n+1];
            getLevel(n, level, adj);

            boolean[] vis = new boolean[n+1];
            Queue<Integer> q = new LinkedList<>();
            q.add(1);
            vis[1] = true;

            while(!q.isEmpty()) {
                int top = q.poll();
                ans[top] = Math.max(ans[top], BFS(top, val, adj, level));

                for(int itr: adj.get(top)) {
                    if(!vis[itr]) {
                        q.add(itr);
                        vis[itr] = true;
                    }
                }
            }

            for(int i=1;i<=n;i++) {
                output.append(ans[i] + " ");
            }
            output.append("\n");
        }

        bw.write(output.toString());
        bw.close();
    }
}
