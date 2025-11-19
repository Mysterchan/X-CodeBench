import java.io.*;
import java.util.*;

public class Main {
    static int N, LOG;
    static List<Integer>[] tree;
    static int[][] A;
    static int[][] up;
    static int[] depth;
    static DSU dsu;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        tree = new ArrayList[N];
        for (int i = 0; i < N; i++) tree[i] = new ArrayList<>();

        for (int i = 0; i < N - 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken()) - 1;
            int v = Integer.parseInt(st.nextToken()) - 1;
            tree[u].add(v);
            tree[v].add(u);
        }

        A = new int[N][N];
        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < N; j++) {
                A[i][j] = line.charAt(j) - '0';
            }
        }

        LOG = 1;
        while ((1 << LOG) <= N) LOG++;

        up = new int[N][LOG];
        depth = new int[N];
        dfs(0, 0, -1);

        dsu = new DSU(N);

        for (int i = 0; i < N; i++) {
            for (int j = i+1; j < N; j++) {
                if (A[i][j] == 1) {
                    int lca = lca(i, j);
                    unionSymmetric(i, j, lca);
                }
            }
        }

        long score = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (isPalindromePath(i, j)) score++;
            }
        }

        System.out.println(score);
    }

    static void dfs(int u, int d, int p) {
        depth[u] = d;
        up[u][0] = p == -1 ? u : p;
        for (int i = 1; i < LOG; i++) {
            up[u][i] = up[up[u][i - 1]][i - 1];
        }
        for (int v : tree[u]) {
            if (v != p) {
                dfs(v, d + 1, u);
            }
        }
    }

    static int lca(int u, int v) {
        if (depth[u] < depth[v]) {
            int temp = u; u = v; v = temp;
        }
        for (int i = LOG - 1; i >= 0; i--) {
            if (depth[u] - (1 << i) >= depth[v]) {
                u = up[u][i];
            }
        }
        if (u == v) return u;
        for (int i = LOG - 1; i >= 0; i--) {
            if (up[u][i] != up[v][i]) {
                u = up[u][i];
                v = up[v][i];
            }
        }
        return up[u][0];
    }

    static void unionSymmetric(int u, int v, int lca) {
        List<Integer> pathU = new ArrayList<>();
        List<Integer> pathV = new ArrayList<>();
        int currU = u;
        int currV = v;

        while (currU != lca) {
            pathU.add(currU);
            currU = up[currU][0];
        }
        pathU.add(lca);

        while (currV != lca) {
            pathV.add(currV);
            currV = up[currV][0];
        }

        int len = pathU.size() + pathV.size();
        for (int k = 0; k < len / 2; k++) {
            int leftNode = (k < pathU.size()) ? pathU.get(k) : pathV.get(len - 1 - k);
            int rightNode = (k < pathU.size()) ?
                ( (len - 1 - k) < pathU.size() ? pathU.get(len - 1 - k) : pathV.get(len - 1 - k - pathU.size()) ) :
                pathV.get(len - 1 - k);

            if (k < pathU.size() && k < pathV.size()) {
                dsu.union(pathU.get(k), pathV.get(pathV.size() - 1 - k));
            }
        }
    }

    static boolean isPalindromePath(int i, int j) {
        int lca = lca(i, j);
        List<Integer> pathNodes = new ArrayList<>();
        int curr = i;
        while (curr != lca) {
            pathNodes.add(curr);
            curr = up[curr][0];
        }
        pathNodes.add(lca);
        List<Integer> temp = new ArrayList<>();
        curr = j;
        while (curr != lca) {
            temp.add(curr);
            curr = up[curr][0];
        }

        for (int k = temp.size() - 1; k >= 0; k--) {
            pathNodes.add(temp.get(k));
        }

        int len = pathNodes.size();
        for (int k = 0; k < len / 2; k++) {
            if (dsu.find(pathNodes.get(k)) != dsu.find(pathNodes.get(len - 1 - k))) return false;
        }
        return true;
    }

    static class DSU {
        int[] parent;
        int[] rank;

        DSU(int n) {
            parent = new int[n];
            rank = new int[n];
            for (int i = 0; i < n; i++) parent[i] = i;
        }

        int find(int x) {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        }

        void union(int x, int y) {
            x = find(x);
            y = find(y);
            if (x != y) {
                if (rank[x] < rank[y]) {
                    parent[x] = y;
                } else {
                    parent[y] = x;
                    if (rank[x] == rank[y]) rank[x]++;
                }
            }
        }
    }
}