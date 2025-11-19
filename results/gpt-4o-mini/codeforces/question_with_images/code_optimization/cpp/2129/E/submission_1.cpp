#include <iostream>
#include <vector>
#include <algorithm>
#include <bitset>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n, m;
        cin >> n >> m;
        vector<vector<int>> graph(n + 1);

        for (int i = 0; i < m; i++) {
            int u, v;
            cin >> u >> v;
            graph[u].push_back(v);
            graph[v].push_back(u);
        }

        int q;
        cin >> q;
        while (q--) {
            int l, r, k;
            cin >> l >> r >> k;
            vector<int> values(r - l + 1);

            for (int u = l; u <= r; u++) {
                int xor_val = 0;
                for (int v : graph[u]) {
                    if (v >= l && v <= r) {
                        xor_val ^= v;
                    }
                }
                values[u - l] = xor_val;
            }

            nth_element(values.begin(), values.begin() + k - 1, values.end());
            cout << values[k - 1] << '\n';
        }
    }

    return 0;
}