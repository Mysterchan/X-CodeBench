#include <iostream>
#include <vector>
using namespace std;

const long long MOD = 998244353;
const int MAXN = 2025;

int N, M, A[MAXN];
int color[MAXN];
int cycle_id[MAXN];
int comp_root[MAXN];
vector<int> ch[MAXN];

// dp[node][max_val]: number of ways to assign subtree rooted at node with max value ≤ max_val
// We'll optimize solve by using prefix sums to avoid O(M^2) per node.

long long dp[MAXN][MAXN];
bool vis[MAXN];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M;
    for (int i = 1; i <= N; i++) {
        cin >> A[i];
        cycle_id[i] = -1;
        comp_root[i] = -1;
        color[i] = 0;
        ch[i].clear();
    }

    for (int i = 1; i <= N; i++) {
        ch[A[i]].push_back(i);
    }

    // Detect cycles and assign cycle_id and comp_root
    // color: 0=unvisited,1=visiting,2=visited
    for (int i = 1; i <= N; i++) {
        if (color[i] != 0) continue;
        int cur = i;
        vector<int> stack;
        while (true) {
            if (color[cur] == 0) {
                color[cur] = 1;
                stack.push_back(cur);
                cur = A[cur];
            } else if (color[cur] == 1) {
                // Found cycle start at cur
                int cyc_id = cur;
                int idx = (int)stack.size() - 1;
                // Mark cycle nodes
                while (stack[idx] != cur) idx--;
                for (int j = idx; j < (int)stack.size(); j++) {
                    cycle_id[stack[j]] = cyc_id;
                    comp_root[stack[j]] = cyc_id;
                }
                // For nodes before cycle in stack, assign comp_root to cycle root
                for (int j = 0; j < idx; j++) {
                    comp_root[stack[j]] = cyc_id;
                }
                // Mark all visited
                for (int node : stack) color[node] = 2;
                break;
            } else {
                // color[cur] == 2
                // Assign comp_root for nodes in stack to comp_root[cur]
                int root = comp_root[cur];
                for (int node : stack) comp_root[node] = root;
                for (int node : stack) color[node] = 2;
                break;
            }
        }
    }

    // For any node without comp_root (should not happen), assign comp_root by following A
    for (int i = 1; i <= N; i++) {
        if (comp_root[i] == -1) {
            int cur = i;
            while (comp_root[cur] == -1) cur = A[cur];
            comp_root[i] = comp_root[cur];
        }
    }

    vector<bool> done(N + 1, false);
    long long ans = 1;

    // We'll implement a bottom-up DP for trees rooted at cycle nodes or single nodes.

    // solve subtree rooted at node with max_val ≤ M
    // We'll compute dp[node][val] for val=1..M
    // dp[node][val] = sum_{x=1}^{val} product over children c of dp[c][x]

    // To optimize:
    // For each node, we compute dp[node][val] using prefix sums of children's dp arrays.

    // We'll write a function to compute dp for a subtree rooted at node,
    // excluding children that are in the same cycle (to avoid infinite recursion).

    // Precompute dp for all nodes outside cycles first.

    // We'll process components one by one.

    // For each cycle component:
    // - Extract cycle nodes
    // - For each val=1..M:
    //     ways = product over cycle nodes of (product over children not in cycle of dp[c][val])
    // - total ways = sum over val=1..M of ways

    // For nodes not in any cycle (comp_root == -1), treat them as single-node cycles.

    // We'll implement a memoized DP for nodes outside cycles.

    // To avoid recursion overhead, we'll do iterative DP with topological order.

    // First, build reverse graph ignoring edges inside cycles.

    // Mark nodes in cycles
    vector<bool> in_cycle(N + 1, false);
    for (int i = 1; i <= N; i++) {
        if (cycle_id[i] != -1) in_cycle[i] = true;
    }

    // Build graph ignoring edges inside cycles
    // For DP, we need to process nodes in order so that children are processed before parents.

    // We'll do a post-order DFS for each node outside cycles.

    vector<bool> dp_done(N + 1, false);

    // dp[node][val] for node outside cycle
    // We'll store dp[node][val] for val=1..M

    // To save memory, we can store dp arrays only for nodes outside cycles.

    // For nodes in cycles, we only need dp for their children outside cycles.

    // Implement DP for nodes outside cycles:

    // We'll implement a function to compute dp[node][val] for node outside cycle.

    // Use iterative DFS with stack to avoid recursion overhead.

    // Since N and M are up to 2025, memory usage is acceptable.

    // We'll implement a function compute_dp(node):

    // For each node outside cycle:
    //   dp[node][val] = sum_{x=1}^{val} product over children c of dp[c][x]

    // We'll precompute prefix sums for children dp arrays to speed up.

    // Let's implement:

    // Store dp arrays for all nodes (including cycle nodes) for children outside cycles.

    // For cycle nodes, we only compute dp for their children outside cycles.

    // For nodes outside cycles, we compute dp fully.

    // We'll implement compute_dp(node) with memoization.

    // To avoid recursion, we'll do a topological order.

    // Build graph ignoring edges inside cycles:

    vector<int> g[MAXN];
    int indeg[MAXN] = {0};

    for (int u = 1; u <= N; u++) {
        for (int c : ch[u]) {
            if (in_cycle[u] && in_cycle[c] && cycle_id[u] == cycle_id[c]) {
                // edge inside cycle, ignore for dp graph
                continue;
            }
            g[c].push_back(u);
            indeg[u]++;
        }
    }

    // We'll process nodes with indeg=0 first (leaves in dp graph)

    vector<int> order;
    vector<int> q;
    for (int i = 1; i <= N; i++) {
        if (indeg[i] == 0) q.push_back(i);
    }

    while (!q.empty()) {
        int u = q.back();
        q.pop_back();
        order.push_back(u);
        for (int v : g[u]) {
            indeg[v]--;
            if (indeg[v] == 0) q.push_back(v);
        }
    }

    // Now order is a topological order for dp computation

    // For each node, dp[node][val] = sum_{x=1}^{val} product over children c of dp[c][x]

    // For leaves (no children outside cycle), dp[node][val] = val

    // We'll store dp arrays for all nodes.

    // To optimize memory, we can store dp arrays as int arrays.

    // Implement dp computation in topological order:

    for (int u : order) {
        // children outside cycle:
        vector<int> children;
        for (int c : ch[u]) {
            if (in_cycle[u] && in_cycle[c] && cycle_id[u] == cycle_id[c]) continue;
            children.push_back(c);
        }

        if (children.empty()) {
            // dp[u][val] = val
            for (int val = 1; val <= M; val++) {
                dp[u][val] = val;
            }
        } else {
            // For each child, we have dp[c][val]
            // We'll compute prefix sums for each child to get sum_{x=1}^{val} dp[c][x]

            // For each child c, precompute prefix sums:
            // prefix_c[val] = sum_{x=1}^{val} dp[c][x]

            // We'll store prefix sums temporarily.

            static long long prefix[MAXN];
            vector<long long*> prefix_children;
            vector<long long> prefix_storage;

            // To avoid dynamic allocation, we'll reuse prefix array for each child.

            // We'll store prefix sums for each child in a vector of pointers to prefix arrays.

            // But since M is up to 2025, and number of children can be up to N, we can store prefix sums in a vector.

            // We'll store prefix sums for all children in a vector<vector<long long>>

            vector<vector<long long>> prefix_all(children.size(), vector<long long>(M + 1, 0));

            for (size_t i = 0; i < children.size(); i++) {
                int c = children[i];
                prefix_all[i][0] = 0;
                for (int val = 1; val <= M; val++) {
                    prefix_all[i][val] = (prefix_all[i][val - 1] + dp[c][val]) % MOD;
                }
            }

            // Now compute dp[u][val] for val=1..M:
            // dp[u][val] = sum_{x=1}^{val} product over children c of dp[c][x]
            // = sum_{x=1}^{val} prod_{c} dp[c][x]

            // We'll compute dp[u][val] using prefix sums over val.

            // To do this efficiently, we can compute dp[u][val] incrementally:

            // For val=1:
            // dp[u][1] = product over c of dp[c][1]

            // For val>1:
            // dp[u][val] = dp[u][val-1] + product over c of dp[c][val]

            // So we can compute product over c of dp[c][val] for val=1..M, then prefix sum over val.

            // Let's precompute prod_dp_val[val] = product over c of dp[c][val]

            static long long prod_dp_val[MAXN];
            for (int val = 1; val <= M; val++) {
                long long prod = 1;
                for (size_t i = 0; i < children.size(); i++) {
                    prod = (prod * dp[children[i]][val]) % MOD;
                }
                prod_dp_val[val] = prod;
            }

            dp[u][0] = 0;
            for (int val = 1; val <= M; val++) {
                dp[u][val] = (dp[u][val - 1] + prod_dp_val[val]) % MOD;
            }
        }
    }

    // Now process each cycle component:

    vector<bool> done_cycle(N + 1, false);

    for (int i = 1; i <= N; i++) {
        if (comp_root[i] == -1) continue;
        int root = comp_root[i];
        if (done_cycle[root]) continue;

        // Extract cycle nodes
        vector<int> cyc;
        int cur = root;
        do {
            cyc.push_back(cur);
            done_cycle[cur] = true;
            cur = A[cur];
        } while (cur != root);

        // For val=1..M:
        // ways[val] = product over cycle nodes of (product over children outside cycle of dp[c][val])

        // For each cycle node, compute product of dp[c][val] over children outside cycle

        // We'll precompute for each cycle node an array prod_children[val]

        vector<long long> ways(M + 1, 1);

        for (int node : cyc) {
            // children outside cycle
            vector<int> children_out;
            for (int c : ch[node]) {
                if (in_cycle[node] && in_cycle[c] && cycle_id[node] == cycle_id[c]) continue;
                children_out.push_back(c);
            }

            if (children_out.empty()) {
                // product over children dp[c][val] = 1 for all val
                // multiply ways[val] by 1, no change
                continue;
            }

            // For each val, compute product over children dp[c][val]
            // We'll compute prod_children[val] for val=1..M

            static long long prod_children[MAXN];
            for (int val = 1; val <= M; val++) {
                long long prod = 1;
                for (int c : children_out) {
                    prod = (prod * dp[c][val]) % MOD;
                }
                prod_children[val] = prod;
            }

            for (int val = 1; val <= M; val++) {
                ways[val] = (ways[val] * prod_children[val]) % MOD;
            }
        }

        // total ways = sum over val=1..M of ways[val]
        long long total = 0;
        for (int val = 1; val <= M; val++) {
            total = (total + ways[val]) % MOD;
        }

        ans = (ans * total) % MOD;
    }

    cout << ans << "\n";

    return 0;
}