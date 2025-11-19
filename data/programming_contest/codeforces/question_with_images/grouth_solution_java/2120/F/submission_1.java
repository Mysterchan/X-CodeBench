import java.io.*;
import java.util.*;

public class Main {
    static ArrayList<Integer>[] g;
    static ArrayList<Integer>[] gr;
    static boolean[] visited;
    static List<Integer> order;
    static int[] comp;

    static int idx(int v, boolean pos) {
        return 2 * v + (pos ? 0 : 1);
    }

    static void dfs1(int v) {
        visited[v] = true;
        for (int nv : g[v])
            if (!visited[nv])
                dfs1(nv);
        order.add(v);
    }

    static void dfs2(int v, int label) {
        comp[v] = label;
        visited[v] = true;
        for (int nv : gr[v])
            if (!visited[nv])
                dfs2(nv, label);
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);
        int T = Integer.parseInt(br.readLine().trim());
        for (int tc = 0; tc < T; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());
            int total = 2 * n;
            g = new ArrayList[total];
            gr = new ArrayList[total];
            for (int i = 0; i < total; i++) {
                g[i] = new ArrayList<>();
                gr[i] = new ArrayList<>();
            }
            for (int group = 0; group < k; group++) {
                int m = Integer.parseInt(br.readLine().trim());
                BitSet[] adj = new BitSet[n];
                for (int i = 0; i < n; i++)
                    adj[i] = new BitSet(n);
                for (int i = 0; i < m; i++) {
                    st = new StringTokenizer(br.readLine());
                    int u = Integer.parseInt(st.nextToken()) - 1;
                    int v = Integer.parseInt(st.nextToken()) - 1;
                    adj[u].set(v);
                    adj[v].set(u);
                }
                for (int u = 0; u < n; u++) {
                    for (int v = u + 1; v < n; v++) {
                        BitSet setU = (BitSet) adj[u].clone();
                        BitSet setV = (BitSet) adj[v].clone();
                        setU.clear(u); setU.clear(v);
                        setV.clear(u); setV.clear(v);
                        if (!setU.equals(setV))
                            continue;
                        if (adj[u].get(v)) {
                            int a = idx(u, true), b = idx(v, false);
                            g[a].add(b); gr[b].add(a);
                            a = idx(v, true); b = idx(u, false);
                            g[a].add(b); gr[b].add(a);
                        } else {
                            int a = idx(u, false), b = idx(v, true);
                            g[a].add(b); gr[b].add(a);
                            a = idx(v, false); b = idx(u, true);
                            g[a].add(b); gr[b].add(a);
                        }
                    }
                }
            }
            order = new ArrayList<>();
            visited = new boolean[total];
            for (int i = 0; i < total; i++)
                if (!visited[i])
                    dfs1(i);
            Arrays.fill(visited, false);
            comp = new int[total];
            int label = 0;
            for (int i = order.size() - 1; i >= 0; i--) {
                int v = order.get(i);
                if (!visited[v]) {
                    dfs2(v, label);
                    label++;
                }
            }
            boolean can = true;
            for (int i = 0; i < n; i++) {
                if (comp[idx(i, true)] == comp[idx(i, false)]) {
                    can = false;
                    break;
                }
            }
            pw.println(can ? "Yes" : "No");
        }
        pw.flush();
    }
}
