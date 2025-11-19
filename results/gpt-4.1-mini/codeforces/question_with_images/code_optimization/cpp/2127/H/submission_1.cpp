#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    while (t--) {
        int n, m; cin >> n >> m;
        vector<vector<int>> adj(n);
        vector<pair<int,int>> edges(m);
        for (int i = 0; i < m; i++) {
            int u,v; cin >> u >> v; u--; v--;
            edges[i] = {u,v};
            adj[u].push_back(v);
            adj[v].push_back(u);
        }

        // Since each vertex belongs to at most 5 simple cycles,
        // the graph is "almost" a cactus-like structure.
        // The problem reduces to finding a maximum subgraph with max degree ≤ 2.
        // Such subgraphs are unions of paths and cycles.
        // This is equivalent to finding a maximum matching in the line graph of G,
        // but since n ≤ 30 and sum n^2 ≤ 900, we can do a backtracking with pruning.

        // Optimization:
        // Sort edges by sum of degrees ascending to try edges with less "pressure" first.
        vector<int> deg(n,0);
        vector<int> static_degree(n,0);
        for (auto &e : edges) {
            static_degree[e.first]++;
            static_degree[e.second]++;
        }
        sort(edges.begin(), edges.end(), [&](auto &a, auto &b) {
            return static_degree[a.first] + static_degree[a.second] < static_degree[b.first] + static_degree[b.second];
        });

        int best = 0;

        // Precompute prefix sums of edges to help pruning
        vector<int> suffix_max(m+1,0);
        // suffix_max[i] = max number of edges we can add from edges[i..end]
        // Since max degree is 2, max edges from remaining edges ≤ number of edges left
        // but we can do better by counting how many edges can be added without violating degree 2
        // We'll just use remaining edges count as upper bound for pruning.

        // Backtracking with pruning
        vector<int> degree(n,0);

        function<void(int,int)> dfs = [&](int i, int cur) {
            if (cur + (m - i) <= best) return; // prune if even taking all remaining edges won't beat best
            if (i == m) {
                if (cur > best) best = cur;
                return;
            }
            // Option 1: skip edge i
            dfs(i+1, cur);

            // Option 2: take edge i if possible
            int u = edges[i].first, v = edges[i].second;
            if (degree[u] < 2 && degree[v] < 2) {
                degree[u]++;
                degree[v]++;
                dfs(i+1, cur+1);
                degree[u]--;
                degree[v]--;
            }
        };

        dfs(0,0);
        cout << best << "\n";
    }
    return 0;
}