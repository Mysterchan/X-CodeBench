#include <bits/stdc++.h>
using namespace std;

enum Color {
    RED,
    BLUE
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    while(t--) {
        int n, m, q;
        cin >> n >> m >> q;

        vector<vector<int>> adj(n + 1);
        vector<int> out_degree(n + 1, 0);
        vector<Color> colors(n + 1, BLUE);
        
        for (int i = 0; i < m; i++) {
            int u, v;
            cin >> u >> v;
            adj[u].push_back(v);
            out_degree[u]++;
        }

        vector<bool> cryWin(n + 1, false);
        stack<int> nodesToProcess;

        for (int i = 1; i <= n; i++) {
            if (out_degree[i] == 0) {
                cryWin[i] = true; // terminal nodes
                nodesToProcess.push(i);
            }
        }

        while (!nodesToProcess.empty()) {
            int curr = nodesToProcess.top();
            nodesToProcess.pop();

            if (colors[curr] == RED) {
                cryWin[curr] = false; // River wins
                continue;
            }

            for (int prev : adj[curr]) {
                cryWin[prev] = cryWin[prev] || !cryWin[curr];

                out_degree[prev]--;
                if (out_degree[prev] == 0) {
                    nodesToProcess.push(prev);
                }
            }
        }

        for (int i = 0; i < q; i++) {
            int type, u;
            cin >> type >> u;

            if (type == 1) {
                if (colors[u] == RED) continue; // already red
                colors[u] = RED; // update color to red
                cryWin[u] = false; // River wins if token at red node

                // Backtrack to adjust win states for ancestors
                for (int j = 1; j <= n; j++) {
                    for (int prev : adj[j]) {
                        if (prev == u) {
                            if (!cryWin[j]) {
                                cryWin[j] = true; // update parent state
                            }
                        }
                    }
                }
            } else { // Query type 2
                cout << (cryWin[u] ? "YES" : "NO") << '\n';
            }
        }
    }

    return 0;
}