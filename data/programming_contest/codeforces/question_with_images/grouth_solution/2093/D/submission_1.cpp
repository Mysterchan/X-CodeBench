#pragma GCC optimize("Ofast,unroll-loops")
#pragma GCC target("avx2,popcnt")
#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using pi = pair<ll, ll>;

void solve() {
    ll N, Q;
    cin >> N >> Q;
    ll L = 1LL << N;

    auto dfs = [&](auto& dfs, ll x, ll y, ll K) -> ll {
        if (K == 0) return 0;
        ll n = 1LL << (K - 1);
        ll k = n * n;
        if (x < n && y < n) return dfs(dfs, x, y, K - 1);
        if (n <= x && n <= y) return k + dfs(dfs, x - n, y - n, K - 1);
        if (n <= x && y < n) return k + k + dfs(dfs, x - n, y, K - 1);
        return 3 * k + dfs(dfs, x, y - n, K - 1);
    };

    auto F = [&](auto& F, ll m, ll K) -> pi {
        if (K == 0) return {0, 0};
        ll n = 1LL << (K - 1);
        ll k = n * n;
        if (m < k) return F(F, m, K - 1);
        m -= k;
        if (m < k) {
            auto [x, y] = F(F, m, K - 1);
            return {x + n, y + n};
        }
        m -= k;
        if (m < k) {
            auto [x, y] = F(F, m, K - 1);
            return {x + n, y};
        }
        m -= k;
        auto [x, y] = F(F, m, K - 1);
        return {x, y + n};
    };

    while (Q--) {
        string S;
        cin >> S;
        if (S == "->") {
            ll x, y;
            cin >> x >> y;
            --x, --y;
            ll ANS = dfs(dfs, x, y, N);
            cout << 1 + ANS << '\n';
        } else {
            ll n;
            cin >> n;
            --n;
            auto [x, y] = F(F, n, N);
            cout << x + 1 << " " << y + 1 << '\n';
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;
    while (T--) solve();
    return 0;
}