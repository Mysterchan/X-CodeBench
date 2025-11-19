#include <bits/stdc++.h>
using namespace std;

constexpr int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;
    while (T--) {
        int H, W; cin >> H >> W;
        vector<string> grid(H);
        for (auto &row : grid) cin >> row;

        // Check rows: if no 'B' in row and W is odd => 0 ways
        // else if no 'B' in row and W even => multiply ans by 2
        // else rows with 'B' => multiply ans by 2 once per connected component of rows linked by columns with 'B'

        // Similarly for columns.

        // The problem reduces to:
        // For rows without 'B':
        //   if W odd => no solution
        //   else ways *= 2
        // For columns without 'B':
        //   if H odd => no solution
        //   else ways *= 2
        // For rows and columns with 'B':
        //   The rows and columns with 'B' form a bipartite graph.
        //   Each connected component contributes factor 2.
        //   If any conflict arises, answer = 0.

        // Build bipartite graph between rows and columns with 'B'
        vector<vector<int>> adj(H + W);
        vector<bool> rowHasB(H, false), colHasB(W, false);

        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                if (grid[i][j] == 'B') {
                    rowHasB[i] = true;
                    colHasB[j] = true;
                    adj[i].push_back(H + j);
                    adj[H + j].push_back(i);
                }
            }
        }

        vector<int> color(H + W, -1);
        auto modpow = [](long long base, long long exp, int mod) {
            long long res = 1;
            while (exp > 0) {
                if (exp & 1) res = res * base % mod;
                base = base * base % mod;
                exp >>= 1;
            }
            return res;
        };

        long long ans = 1;
        // Check rows without B
        for (int i = 0; i < H; i++) {
            if (!rowHasB[i]) {
                if (W % 2 == 1) {
                    ans = 0;
                    break;
                }
                ans = (ans * 2) % MOD;
            }
        }
        if (ans == 0) {
            cout << 0 << "\n";
            continue;
        }
        // Check columns without B
        for (int j = 0; j < W; j++) {
            if (!colHasB[j]) {
                if (H % 2 == 1) {
                    ans = 0;
                    break;
                }
                ans = (ans * 2) % MOD;
            }
        }
        if (ans == 0) {
            cout << 0 << "\n";
            continue;
        }

        // Now count connected components in bipartite graph of rows and columns with B
        // Each component contributes factor 2
        // Also check bipartite coloring to detect conflicts (should be bipartite by construction)
        for (int i = 0; i < H + W; i++) {
            if (color[i] == -1 && ((i < H && rowHasB[i]) || (i >= H && colHasB[i - H]))) {
                // BFS to color component
                queue<int> q;
                q.push(i);
                color[i] = 0;
                while (!q.empty()) {
                    int u = q.front(); q.pop();
                    for (int v : adj[u]) {
                        if (color[v] == -1) {
                            color[v] = color[u] ^ 1;
                            q.push(v);
                        } else if (color[v] == color[u]) {
                            // Not bipartite => no solution
                            ans = 0;
                            break;
                        }
                    }
                    if (ans == 0) break;
                }
                if (ans == 0) break;
                ans = (ans * 2) % MOD;
            }
        }

        cout << ans << "\n";
    }

    return 0;
}