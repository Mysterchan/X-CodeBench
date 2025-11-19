#include <bits/stdc++.h>
using namespace std;
using ll = long long;

using i64 = ll;

inline i64 powmod(i64 b, i64 e, i64 m) {
    i64 res = 1;
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
        if ((x == 1 || x == n) ^ (y == 1 || y == m)) {
            edge++;
            edge_col += c;
        }
    }
    edge_col %= 2;

    constexpr ll mod = 1e9 + 7;
    if (edge == (n - 2) * 2 + (m - 2) * 2) {
        if (edge_col == 1) {
            cout << "0" << endl;
            return;
        }
        auto res = powmod(2, n * m - k, mod);
        cout << res << endl;
        return;
    }
    auto res = powmod(2, n * m - k - 1, mod);
    cout << res << endl;
}

int main() {
    cin.tie(0);
    ios::sync_with_stdio(0);
    for (int t = (cin >> t, t); t--;) {
        solve();
    }
}
