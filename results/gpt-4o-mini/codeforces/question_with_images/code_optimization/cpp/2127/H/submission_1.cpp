#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, m;
        cin >> n >> m;
        vector<pair<int, int>> edges(m);
        vector<int> degree(n, 0);
        
        for (int i = 0; i < m; i++) {
            int u, v;
            cin >> u >> v;
            u--; v--;
            edges[i] = {u, v};
        }

        vector<bool> taken(m, false);
        int best = 0;

        auto countCandyEdges = [&]() {
            int count = 0;
            for (int i = 0; i < n; i++) {
                if (degree[i] > 2) return -1; // if any degree exceeds 2
            }
            for (int i = 0; i < m; i++) {
                if (taken[i]) count++;
            }
            return count;
        };

        function<void(int)> dfs = [&](int i) {
            if (i == m) {
                best = max(best, countCandyEdges());
                return;
            }
            dfs(i + 1); // skip the current edge
            
            int u = edges[i].first;
            int v = edges[i].second;

            if (degree[u] < 2 && degree[v] < 2) {
                taken[i] = true;
                degree[u]++;
                degree[v]++;
                dfs(i + 1); // include the current edge
                taken[i] = false;
                degree[u]--;
                degree[v]--;
            }
        };

        dfs(0);
        cout << best << endl;
    }
    return 0;
}