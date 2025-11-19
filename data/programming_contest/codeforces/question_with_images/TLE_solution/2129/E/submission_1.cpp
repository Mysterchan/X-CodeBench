#include <iostream>
#include <vector>
#include <algorithm>
#include <cctype>
#include <iterator>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n, m;
        cin >> n >> m;
        vector<vector<int>> graph(n+1);
        vector<int> base(n+1, 0);

        for (int i = 0; i < m; i++) {
            int u, v;
            cin >> u >> v;
            graph[u].push_back(v);
            graph[v].push_back(u);
            base[u] ^= v;
            base[v] ^= u;
        }

        vector<vector<int>> neighbors_sorted(n+1);
        vector<vector<int>> prefix_xor(n+1);

        for (int u = 1; u <= n; u++) {
            vector<int> &adj = graph[u];
            sort(adj.begin(), adj.end());
            neighbors_sorted[u] = adj;
            int sz = adj.size();
            vector<int> pxor(sz, 0);
            if (sz > 0) {
                pxor[0] = adj[0];
                for (int i = 1; i < sz; i++) {
                    pxor[i] = pxor[i-1] ^ adj[i];
                }
            }
            prefix_xor[u] = pxor;
        }

        int q;
        cin >> q;
        while (q--) {
            int l, r, k;
            cin >> l >> r >> k;
            vector<int> values;
            int len = r - l + 1;
            values.reserve(len);

            for (int u = l; u <= r; u++) {
                const vector<int>& adj = neighbors_sorted[u];
                auto it_low = lower_bound(adj.begin(), adj.end(), l);
                int left_index = distance(adj.begin(), it_low);
                auto it_high = upper_bound(adj.begin(), adj.end(), r);
                int right_index = distance(adj.begin(), it_high);

                int xor_val = 0;
                if (left_index < right_index) {
                    int last_index = right_index - 1;
                    if (left_index == 0) {
                        xor_val = prefix_xor[u][last_index];
                    } else {
                        xor_val = prefix_xor[u][last_index] ^ prefix_xor[u][left_index-1];
                    }
                }
                values.push_back(xor_val);
            }

            nth_element(values.begin(), values.begin() + k - 1, values.end());
            cout << values[k-1] << '\n';
        }
    }

    return 0;
}

