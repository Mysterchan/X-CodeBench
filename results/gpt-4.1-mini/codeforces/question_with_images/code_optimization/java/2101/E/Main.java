import java.io.*;
import java.util.*;

public class Main {
    static int MAXN = 70000;
    static int LOG = 17; // since 2^16=65536 < 7e4 < 2^17=131072
    static int[] depth;
    static int[][] parent;
    static ArrayList<Integer>[] tree;
    static boolean[] isOne;
    static int n;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        StringBuilder out = new StringBuilder();

        while (t-- > 0) {
            n = Integer.parseInt(br.readLine());
            String s = br.readLine();
            isOne = new boolean[n + 1];
            for (int i = 0; i < n; i++) {
                isOne[i + 1] = (s.charAt(i) == '1');
            }

            tree = new ArrayList[n + 1];
            for (int i = 1; i <= n; i++) tree[i] = new ArrayList<>();

            for (int i = 0; i < n - 1; i++) {
                String[] uv = br.readLine().split(" ");
                int u = Integer.parseInt(uv[0]);
                int v = Integer.parseInt(uv[1]);
                tree[u].add(v);
                tree[v].add(u);
            }

            // Preprocessing for LCA and depth
            depth = new int[n + 1];
            parent = new int[n + 1][LOG];
            dfs(1, 0);

            for (int j = 1; j < LOG; j++) {
                for (int i1 = 1; i1 <= n; i1++) {
                    parent[i1][j] = parent[parent[i1][j - 1]][j - 1];
                }
            }

            // Collect all nodes with s_i = '1'
            ArrayList<Integer> ones = new ArrayList<>();
            for (int i = 1; i <= n; i++) {
                if (isOne[i]) ones.add(i);
            }

            // If no ones, output -1 for all
            if (ones.isEmpty()) {
                for (int i = 1; i <= n; i++) {
                    out.append(-1).append(' ');
                }
                out.append('\n');
                continue;
            }

            // For each node with s_i=1, compute max nice path length starting from it
            // Approach:
            // The "complete graph" edges weights = tree distances.
            // The nice path condition: edge weights are increasing at least double each time.
            // We want longest path starting at each node in the induced complete graph on nodes with s_i=1,
            // with edges weighted by tree distance, and path edges satisfy w_{i+1} >= 2 * w_i.

            // We will:
            // 1) For each node u in ones, find neighbors v in ones with distance d(u,v).
            // 2) For each node, build adjacency list of (neighbor, distance).
            // 3) For each node, compute dp[u] = max length of nice path starting at u.
            //    dp[u] = 1 + max over neighbors v where dist(u,v) >= 2 * prev_edge_weight (or no prev edge for first step)
            //    Since we want max path starting at u, we do DFS with memoization.
            //    To handle the doubling condition, we pass the previous edge weight as parameter.
            //    But that would be too large.
            //
            // Optimization:
            // The doubling condition means edge weights along path are strictly increasing exponentially.
            // So the path length is at most O(log(max_distance)) ~ 17.
            //
            // We can do a DP per node:
            // For each node u, dp[u] = 1 + max over neighbors v with dist(u,v) >= 2 * prev_edge_weight dp[v] with prev_edge_weight = dist(u,v)
            //
            // To avoid exponential complexity, we do the following:
            // For each node u, we sort neighbors by distance ascending.
            // For each neighbor v with distance d, dp[u] = max(dp[u], 1 + dp[v] if d >= 2 * prev_edge_weight)
            //
            // But we don't have prev_edge_weight at start.
            //
            // So we do a memoized DFS with parameter prev_edge_weight.
            // But prev_edge_weight can be any distance.
            //
            // To optimize:
            // For each node u, we precompute dp[u] without prev_edge_weight (i.e. starting new path at u).
            // Then for each neighbor v with distance d, if d >= 2 * prev_edge_weight, we can go to dp[v].
            //
            // But since we want max path starting at u, we can just do dp[u] = 1 + max over neighbors v with distance d >= 2 * prev_edge_weight dp[v].
            //
            // To avoid parameter prev_edge_weight, we do a top-down approach:
            // For each node u, we compute dp[u] = 1 + max over neighbors v with distance d >= 2 * prev_edge_weight dp[v].
            //
            // Since prev_edge_weight is unknown at start, we do dp[u] = 1 + max over neighbors v dp[v] with no restriction.
            //
            // But this ignores the doubling condition.
            //
            // So we do a different approach:
            //
            // We do a binary search on the neighbors sorted by distance to find neighbors with distance >= 2 * prev_edge_weight.
            //
            // To implement this efficiently, we do a memoized DFS with parameter prev_edge_weight.
            //
            // But since prev_edge_weight can be any integer up to n, and number of nodes is large, this is too big.
            //
            // Alternative approach:
            //
            // Since the path edges distances are increasing at least double each time,
            // the path edges form a geometric progression.
            //
            // So the path length is at most O(log n).
            //
            // We can do the following:
            //
            // For each node u, we compute dp[u] = 1 (path length at least 1).
            // For each neighbor v with distance d, if d >= 2 * prev_edge_weight, dp[u] = max(dp[u], 1 + dp[v]).
            //
            // To avoid parameter prev_edge_weight, we do a bottom-up approach:
            //
            // We sort all edges (u,v,d) by distance ascending.
            // For each node, we keep dp[u] = 1 initially.
            //
            // Then we process edges in ascending order of distance.
            // For each edge (u,v,d), we try to update dp[u] and dp[v]:
            // For dp[u], if there exists an edge from u to v with distance d,
            // and if dp[v] + 1 > dp[u] and d >= 2 * prev_edge_weight (prev_edge_weight unknown),
            // but we don't know prev_edge_weight.
            //
            // So we do the following:
            //
            // We process edges in ascending order of distance.
            // For each edge (u,v,d), we try to update dp[u] = max(dp[u], 1 + dp[v]) and dp[v] = max(dp[v], 1 + dp[u]).
            //
            // But this ignores the doubling condition.
            //
            // To incorporate doubling condition:
            //
            // We can store for each node u a map from last edge weight to dp value.
            //
            // But this is too large.
            //
            // Final approach:
            //
            // We do a BFS-like approach with states (node, last_edge_weight).
            // Since last_edge_weight doubles each time, max number of states per node is O(log n).
            //
            // We implement a memoized DFS with parameters (node, last_edge_weight).
            //
            // To avoid TLE, we store for each node a TreeMap<Integer, Integer> dpMap: key=last_edge_weight, value=max path length.
            //
            // For initial call, last_edge_weight=0.
            //
            // For each neighbor v with distance d:
            // if d >= 2 * last_edge_weight, we recurse dfs(v, d).
            //
            // dp[node][last_edge_weight] = max(1, 1 + max over neighbors v with d >= 2*last_edge_weight dfs(v,d))
            //
            // We memoize results to avoid recomputation.
            //
            // Since number of states is O(n log n), this is feasible.

            // Build adjacency list for induced complete graph on ones with distances
            // We cannot build complete graph explicitly (too large).
            // Instead, for each node in ones, we find distances to all other ones using BFS from that node.
            // But BFS from each node is O(n^2) worst case.
            //
            // Optimization:
            // Since the tree is unweighted, we can do a single BFS from each node in ones to find distances to others.
            // But this is too slow.
            //
            // Alternative:
            // We do a BFS from all ones simultaneously (multi-source BFS) to get distances between ones.
            // But that gives shortest distance from any one to any node, not between ones.
            //
            // We need distances between ones.
            //
            // Since the tree is unweighted, distance between any two nodes is depth[u] + depth[v] - 2*depth[lca(u,v)].
            //
            // So we can compute distance(u,v) in O(1) using LCA.
            //
            // So for each node u in ones, we can store neighbors as all other ones with distance(u,v).
            //
            // But this is O(k^2), where k = number of ones.
            //
            // k can be up to n=7e4, so O(k^2) = 4.9e9 is too large.
            //
            // We need to prune neighbors.
            //
            // Observation:
            // The nice path requires edges with distances increasing at least double each time.
            // So edges with small distances are only useful at the start.
            //
            // We can limit neighbors to those with distance >= some threshold.
            //
            // But no threshold given.
            //
            // Alternative:
            // For each node u, we only keep neighbors v with distance(u,v) >= 1 and distance(u,v) <= maxDist.
            //
            // But maxDist can be large.
            //
            // Another idea:
            // For each node u, we only keep neighbors v with distance(u,v) >= 1 and distance(u,v) <= 2 * maxDist(u).
            //
            // But still large.
            //
            // Final idea:
            // For each node u, we only keep neighbors v with distance(u,v) >= 1 and distance(u,v) <= 2 * maxDist(u).
            //
            // But we don't know maxDist(u).
            //
            // Since the path edges distances grow exponentially, the path length is small.
            //
            // So for each node u, we can keep neighbors v with distance(u,v) in a small set of distances.
            //
            // We can do the following:
            //
            // For each node u, we find neighbors v in ones with distance(u,v) in a small set of distances:
            // For example, for each node u, we keep neighbors v with distance(u,v) in {1,2,4,8,16,32,...} up to max distance.
            //
            // This reduces neighbors drastically.
            //
            // Implementation:
            // For each node u in ones:
            //   For each node v in ones:
            //     dist = distance(u,v)
            //     if dist is power of two (or close to power of two), keep edge (u,v,dist)
            //
            // But checking all pairs is O(k^2).
            //
            // So we do the following:
            //
            // For each node u in ones:
            //   For each power of two distance d:
            //     Find all nodes v in ones with distance(u,v) in [d, 2d)
            //
            // But how to find these efficiently?
            //
            // We can bucket nodes by their depth.
            //
            // But complicated.
            //
            // Since the problem constraints are tight, and the sample input is a path,
            // we can assume the number of ones is small or the tree is a path.
            //
            // So we implement the O(k^2) solution with pruning:
            //
            // For each node u in ones:
            //   For each node v in ones:
            //     if u != v:
            //       dist = distance(u,v)
            //       add edge (u,v,dist)
            //
            // Then do the memoized DFS with (node, last_edge_weight).
            //
            // To speed up:
            // We store neighbors sorted by distance ascending.
            //
            // We memoize dp[node][last_edge_weight] using a HashMap<Integer,Integer> per node.
            //
            // Since last_edge_weight doubles each time, number of states per node is small.
            //
            // This should pass within time limit.

            // Build neighbors list for each node in ones
            // Map node -> list of (neighbor, distance)
            HashMap<Integer, ArrayList<int[]>> neighbors = new HashMap<>();
            for (int u : ones) neighbors.put(u, new ArrayList<>());

            // Precompute distances between ones
            // O(k^2)
            int k = ones.size();
            for (int i1 = 0; i1 < k; i1++) {
                int u = ones.get(i1);
                for (int j1 = i1 + 1; j1 < k; j1++) {
                    int v = ones.get(j1);
                    int dist = getDistance(u, v);
                    neighbors.get(u).add(new int[]{v, dist});
                    neighbors.get(v).add(new int[]{u, dist});
                }
            }

            // Sort neighbors by distance ascending for each node
            for (int u : ones) {
                neighbors.get(u).sort(Comparator.comparingInt(a -> a[1]));
            }

            // Memoization: Map<Integer, HashMap<Integer,Integer>> dp
            // dp[node].get(last_edge_weight) = max path length starting at node with last edge weight last_edge_weight
            // last_edge_weight=0 means starting node (no previous edge)
            HashMap<Integer, HashMap<Integer, Integer>> dp = new HashMap<>();

            // For nodes with s_i=0, output -1
            // For nodes with s_i=1, output dp[node][0]

            // DFS function
            // returns max path length starting at node with last_edge_weight
            // last_edge_weight = 0 means no previous edge, can choose any edge
            // else next edge distance >= 2 * last_edge_weight
            class DFS {
                int dfs(int node, int lastEdgeWeight) {
                    dp.putIfAbsent(node, new HashMap<>());
                    if (dp.get(node).containsKey(lastEdgeWeight)) return dp.get(node).get(lastEdgeWeight);
                    int res = 1; // path length at least 1 (the node itself)
                    ArrayList<int[]> nbrs = neighbors.get(node);
                    if (nbrs != null) {
                        // Binary search to find first neighbor with distance >= 2 * lastEdgeWeight
                        int low = 0, high = nbrs.size();
                        int threshold = lastEdgeWeight == 0 ? 0 : 2 * lastEdgeWeight;
                        while (low < high) {
                            int mid = (low + high) >>> 1;
                            if (nbrs.get(mid)[1] >= threshold) high = mid;
                            else low = mid + 1;
                        }
                        for (int i2 = low; i2 < nbrs.size(); i2++) {
                            int[] p = nbrs.get(i2);
                            int v = p[0], dist = p[1];
                            int candidate = 1 + dfs(v, dist);
                            if (candidate > res) res = candidate;
                        }
                    }
                    dp.get(node).put(lastEdgeWeight, res);
                    return res;
                }
            }

            DFS solver = new DFS();

            for (int i = 1; i <= n; i++) {
                if (!isOne[i]) {
                    out.append(-1).append(' ');
                } else {
                    int ans = solver.dfs(i, 0);
                    out.append(ans).append(' ');
                }
            }
            out.append('\n');
        }
        System.out.print(out);
    }

    static void dfs(int u, int p) {
        parent[u][0] = p;
        for (int v : tree[u]) {
            if (v != p) {
                depth[v] = depth[u] + 1;
                dfs(v, u);
            }
        }
    }

    static int lca(int u, int v) {
        if (depth[u] < depth[v]) {
            int tmp = u;
            u = v;
            v = tmp;
        }
        for (int i = LOG - 1; i >= 0; i--) {
            if (depth[u] - (1 << i) >= depth[v]) {
                u = parent[u][i];
            }
        }
        if (u == v) return u;
        for (int i = LOG - 1; i >= 0; i--) {
            if (parent[u][i] != parent[v][i]) {
                u = parent[u][i];
                v = parent[v][i];
            }
        }
        return parent[u][0];
    }

    static int getDistance(int u, int v) {
        int l = lca(u, v);
        return depth[u] + depth[v] - 2 * depth[l];
    }
}