#include <bits/stdc++.h>
using namespace std;
using ll = long long;

inline ll powmod(ll b, ll e, ll m) {
    ll res = 1;
    while (e) {
        if (e & 1) res = res * b % m;
        b = b * b % m;
        e >>= 1;
    }
    return res;
}

void solve() {
    int n, m, k;
    cin >> n >> m >> k;

    int edge = 0;
    int edge_col = 0;
    for (int i = 0; i < k; i++) {
        int x, y, c;
        cin >> x >> y >> c;
        // Check if the cell is at the edge
        if ((x == 1 || x == n) ^ (y == 1 || y == m)) {
            edge++;
            edge_col += c;
        }
    }

    edge_col %= 2;

    constexpr ll mod = 1e9 + 7;
    ll total_cells = n * m;
    
    // Number of edge cells
    int total_edge_cells = (n - 2) * 2 + (m - 2) * 2;

    if (edge == total_edge_cells) { // All edge cells are colored
        if (edge_col == 1) {
            cout << "0\n"; // Odd number of edges with different colors
            return;
        }
        // All cells can be painted freely 
        cout << powmod(2, total_cells - k, mod) << '\n';
    } else {
        // At least one edge cell is green
        cout << powmod(2, total_cells - k - 1, mod) << '\n'; // There is one less degree of freedom
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        solve();
    }
}