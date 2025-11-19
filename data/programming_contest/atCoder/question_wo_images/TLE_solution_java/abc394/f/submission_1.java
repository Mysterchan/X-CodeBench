import java.io.*;
import java.util.*;

public class Main {
    static class Key {
        int node, parent, limit;

        Key(int node, int parent, int limit) {
            this.node = node;
            this.parent = parent;
            this.limit = limit;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (!(o instanceof Key)) return false;
            Key key = (Key) o;
            return node == key.node && parent == key.parent && limit == key.limit;
        }

    }

    static HashMap<Key, Long> memo = new HashMap<>();

    static long dfs(int cur, int parent, List<List<Integer>> adj, int[] degree, int limit) {
        Key key = new Key(cur, parent, limit);
        if (memo.containsKey(key)) {
            return memo.get(key);
        }
        long count = 1;
        List<Long> childrenVals = new ArrayList<>();

        for (int nxt : adj.get(cur)) {
            if (nxt == parent) continue;
            if (degree[nxt] >= 4) {

                childrenVals.add(dfs(nxt, cur, adj, degree, 3));
            }
        }

        Collections.sort(childrenVals, Collections.reverseOrder());
        for (int i = 0; i < limit && i < childrenVals.size(); i++) {
            count += childrenVals.get(i);
        }
        memo.put(key, count);
        return count;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            adj.add(new ArrayList<>());
        }
        int[] degree = new int[n + 1];

        for (int i = 0; i < n - 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            adj.get(u).add(v);
            adj.get(v).add(u);
            degree[u]++;
            degree[v]++;
        }

        long best = 0;

        for (int i = 1; i <= n; i++) {
            if (degree[i] >= 4) {
                best = Math.max(best, dfs(i, -1, adj, degree, 4));
            }
        }

        if (best == 0) {
            System.out.println(-1);
        } else {
            System.out.println(3 * best + 2);
        }
    }
}