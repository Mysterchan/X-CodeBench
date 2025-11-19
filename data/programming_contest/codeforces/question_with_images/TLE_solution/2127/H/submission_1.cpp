#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, m;
        cin >> n >> m;
        vector<pair<int, int>> edges;
        vector<int> static_degree(n, 0);
        for (int i = 0; i < m; i++) {
            int u, v;
            cin >> u >> v;
            u--; v--;
            edges.push_back({u, v});
            static_degree[u]++;
            static_degree[v]++;
        }

        sort(edges.begin(), edges.end(), [&](const pair<int, int>& a, const pair<int, int>& b) {
            int asum = static_degree[a.first] + static_degree[a.second];
            int bsum = static_degree[b.first] + static_degree[b.second];
            return asum < bsum;
        });

        vector<int> degree(n, 0);
        int best = 0;

        auto bound = [&]() {
            int s = 0;
            for (int i = 0; i < n; i++) {
                s += (2 - degree[i]);
            }
            return s / 2;
        };

        function<void(int, int)> dfs = [&](int i, int current_edges) {
            if (current_edges + bound() <= best) {
                return;
            }
            if (i == m) {
                if (current_edges > best) {
                    best = current_edges;
                }
                return;
            }
            dfs(i + 1, current_edges);
            int u = edges[i].first;
            int v = edges[i].second;
            if (degree[u] < 2 && degree[v] < 2) {
                degree[u]++;
                degree[v]++;
                dfs(i + 1, current_edges + 1);
                degree[u]--;
                degree[v]--;
            }
        };

        dfs(0, 0);
        cout << best << endl;
    }
    return 0;
}

