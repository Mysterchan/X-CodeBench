import java.io.*;
import java.util.*;

public class Main {
    static Map<Long, Long> memo = new HashMap<>();
    
    static long makeKey(int node, int parent, int limit) {
        return ((long)node << 32) | ((long)(parent + 1) << 8) | limit;
    }

    static long dfs(int cur, int parent, List<List<Integer>> adj, int[] degree, int limit) {
        long key = makeKey(cur, parent, limit);
        Long cached = memo.get(key);
        if (cached != null) {
            return cached;
        }
        
        long count = 1;
        List<Integer> childrenIdx = new ArrayList<>();
        
        for (int nxt : adj.get(cur)) {
            if (nxt == parent) continue;
            if (degree[nxt] >= 4) {
                childrenIdx.add(nxt);
            }
        }
        
        if (childrenIdx.size() <= limit) {
            for (int nxt : childrenIdx) {
                count += dfs(nxt, cur, adj, degree, 3);
            }
        } else {
            long[] childrenVals = new long[childrenIdx.size()];
            for (int i = 0; i < childrenIdx.size(); i++) {
                childrenVals[i] = dfs(childrenIdx.get(i), cur, adj, degree, 3);
            }
            Arrays.sort(childrenVals);
            for (int i = childrenVals.length - 1; i >= childrenVals.length - limit; i--) {
                count += childrenVals[i];
            }
        }
        
        memo.put(key, count);
        return count;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        List<List<Integer>> adj = new ArrayList<>(n + 1);
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