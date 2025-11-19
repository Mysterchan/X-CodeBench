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
    ll n, m, k;
    cin >> n >> m >> k;

    int edge = 0;
    int edge_col = 0;
    for (int i = 0; i < k; i++) {
        ll x, y, c;
        cin >> x >> y >> c;
        // Check if cell is on the border excluding corners
        // Border cells are those with x==1 or x==n or y==1 or y==m
        // Corners are (1,1), (1,m), (n,1), (n,m)
        // The problem's original code checks (x==1 || x==n) XOR (y==1 || y==m)
        // which is true for border cells excluding corners.
        if ((x == 1 || x == n) ^ (y == 1 || y == m)) {
            edge++;
            edge_col ^= c; // use XOR instead of addition mod 2 for speed
        }
    }

    constexpr ll mod = 1'000'000'007;
    ll border_count = 2 * (n + m - 4); // number of border cells excluding corners

    if (edge == border_count) {
        if (edge_col == 1) {
            cout << 0 << "\n";
            return;
        }
        cout << powmod(2, n * m - k, mod) << "\n";
    } else {
        cout << powmod(2, n * m - k - 1, mod) << "\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t; cin >> t;
    while (t--) solve();
}