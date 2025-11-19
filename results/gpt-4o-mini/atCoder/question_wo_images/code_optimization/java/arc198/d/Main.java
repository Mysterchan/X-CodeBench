import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        FastReader sc = new FastReader();
        int n = sc.nextInt();
        List<Integer>[] ed = new ArrayList[n];
        for (int i = 0; i < n; i++) ed[i] = new ArrayList<>();
        
        // Read edges
        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt() - 1;
            int v = sc.nextInt() - 1;
            ed[u].add(v);
            ed[v].add(u);
        }

        // Read adjacency matrix
        char[][] s = new char[n][];
        for (int i = 0; i < n; i++) {
            s[i] = sc.next().toCharArray();
        }
        
        // Pre-compute parent and depth using DFS
        int[] parent = new int[n];
        int[] depth = new int[n];
        Arrays.fill(parent, -1);
        dfs(0, ed, parent, depth);

        // Create a union-find structure to detect non-palindromic pairs
        UnionFind uf = new UnionFind(n);
        boolean[][] visited = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (s[i][j] == '1' && !visited[i][j]) {
                    visited[i][j] = visited[j][i] = true;
                    int lca = lca(i, j, parent, depth);
                    List<Integer> path = getPath(i, j, lca, parent);
                    if (!isPalindrome(path, n, uf)) {
                        System.out.println((long) Math.pow(10, 100));
                        return;
                    }
                }
            }
        }
        
        // Count palindromic pairs
        int ans = n; // Count (i, i) pairs
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (isPalindrome(getPath(i, j, lca(i, j, parent), parent), n, uf)) {
                    ans += 2;
                }
            }
        }
        System.out.println(ans);
    }

    private static void dfs(int u, List<Integer>[] ed, int[] parent, int[] depth) {
        for (int v : ed[u]) {
            if (v != parent[u]) {
                parent[v] = u;
                depth[v] = depth[u] + 1;
                dfs(v, ed, parent, depth);
            }
        }
    }

    private static int lca(int u, int v, int[] parent, int[] depth) {
        while (u != v) {
            if (depth[u] > depth[v]) u = parent[u];
            else v = parent[v];
        }
        return u;
    }

    private static List<Integer> getPath(int u, int v, int lca, int[] parent) {
        List<Integer> path = new ArrayList<>();
        while (u != lca) {
            path.add(u);
            u = parent[u];
        }
        path.add(lca);
        List<Integer> path2 = new ArrayList<>();
        while (v != lca) {
            path2.add(v);
            v = parent[v];
        }
        Collections.reverse(path2);
        path.addAll(path2);
        return path;
    }

    private static boolean isPalindrome(List<Integer> path, int n, UnionFind uf) {
        int size = path.size();
        for (int i = 0; i < size / 2; i++) {
            if (uf.find(path.get(i)) != uf.find(path.get(size - 1 - i))) {
                return false;
            }
        }
        return true;
    }

    static class UnionFind {
        private int[] parent;

        UnionFind(int n) {
            parent = new int[n];
            for (int i = 0; i < n; i++) parent[i] = i;
        }

        int find(int x) {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        }

        void union(int x, int y) {
            parent[find(x)] = find(y);
        }
    }

    static class FastReader {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        String nextLine() {
            try {
                return br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
                return null;
            }
        }
    }
}