#include <bits/stdc++.h>
#define int long long
using namespace std;
const int MOD = 998244353;

int modular_add(int x, int y) {
    return (x + y) % MOD;
}

int modular_mult(int x, int y) {
    return (x * y) % MOD;
}

int sum_of_first_n(int x) {
    return (x * (x + 1) / 2) % MOD;
}

void solve() {
    int n, h, w;
    cin >> n >> h >> w;
    
    if (h < 2 * n || w < 2 * n) {
        cout << 0 << '\n';
        return;
    }

    int valid_positions_h = h - 2 * n + 1;
    int valid_positions_w = w - 2 * n + 1;

    int total_ways = modular_mult(modular_mult(sum_of_first_n(valid_positions_w), sum_of_first_n(valid_positions_w)), modular_mult(sum_of_first_n(valid_positions_h), sum_of_first_n(valid_positions_h)));

    int subtract_h = 0, subtract_w = 0;

    for (int j = 1; j <= valid_positions_h; j++) {
        subtract_h = modular_add(subtract_h, modular_mult(j, sum_of_first_n(valid_positions_h - j)));
    }
    for (int j = 1; j <= valid_positions_w; j++) {
        subtract_w = modular_add(subtract_w, modular_mult(j, sum_of_first_n(valid_positions_w - j)));
    }

    total_ways = modular_add(total_ways, MOD - modular_mult(2, modular_mult(subtract_h, subtract_w)));
    cout << total_ways << '\n';
}

signed main() {
    ios_base::sync_with_stdio(0); 
    cin.tie(0);

    int t;
    cin >> t;
    while (t--) solve();
}