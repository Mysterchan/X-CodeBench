import java.io.*;
import java.util.*;

public class Main{
    static int[] parent;
    static Set<Integer>[] edges;
    static int edgeCount = 0;

    static int find(int x) {
        return parent[x] == x ? x : (parent[x] = find(parent[x]));
    }

    static void union(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) return;

        if (edges[a].size() > edges[b].size()) {
            int tmp = a; a = b; b = tmp;
        }

        for (int neighbor : edges[a]) {
            int nRoot = find(neighbor);
            if (nRoot == b) {
                edgeCount--;
                continue;
            }

            if (!edges[b].contains(nRoot)) {
                edges[b].add(nRoot);
                edges[nRoot].add(b);
            } else {
                edgeCount--;
            }

            edges[nRoot].remove(a);
        }

        edges[a].clear();
        parent[a] = b;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        PrintWriter out = new PrintWriter(System.out);

        in.nextToken(); int n = (int) in.nval;
        in.nextToken(); int m = (int) in.nval;

        parent = new int[n + 1];
        edges = new HashSet[n + 1];

        for (int i = 1; i <= n; i++) {
            parent[i] = i;
            edges[i] = new HashSet<>();
        }

        int[] u = new int[m + 1];
        int[] v = new int[m + 1];

        for (int i = 1; i <= m; i++) {
            in.nextToken(); u[i] = (int) in.nval;
            in.nextToken(); v[i] = (int) in.nval;

            edges[u[i]].add(v[i]);
            edges[v[i]].add(u[i]);
            edgeCount++;
        }

        in.nextToken(); int q = (int) in.nval;
        int[] x = new int[q];
        for (int i = 0; i < q; i++) {
            in.nextToken(); x[i] = (int) in.nval;
        }

        for (int i = 0; i < q; i++) {
            int a = find(u[x[i]]);
            int b = find(v[x[i]]);

            if (a != b && edges[a].contains(b)) {
                union(a, b);
            }
            out.println(edgeCount);
        }

        out.flush();
    }
}