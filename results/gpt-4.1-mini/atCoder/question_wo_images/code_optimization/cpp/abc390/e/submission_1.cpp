#pragma GCC optimize("O3")
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, X; cin >> N >> X;
    vector<array<ll, 3>> dp(X + 1, {LLONG_MIN, LLONG_MIN, LLONG_MIN});
    dp[0] = {0, 0, 0};

    for (int _ = 0; _ < N; ++_) {
        int V, C; ll A; cin >> V >> A >> C;
        int idx = V - 1;
        for (int cal = X - C; cal >= 0; --cal) {
            if (dp[cal][0] == LLONG_MIN) continue;
            auto &cur = dp[cal];
            auto &nxt = dp[cal + C];
            ll ni = cur[0], nj = cur[1], nk = cur[2];
            if (idx == 0) ni += A;
            else if (idx == 1) nj += A;
            else nk += A;
            // Update dp[cal + C] if better
            if (nxt[0] < ni || nxt[1] < nj || nxt[2] < nk) {
                // We want to maximize the minimum of the three vitamins
                // So update only if min is improved or if equal min but better in some vitamin
                ll old_min = min({nxt[0], nxt[1], nxt[2]});
                ll new_min = min({ni, nj, nk});
                if (new_min > old_min) {
                    nxt = {ni, nj, nk};
                } else if (new_min == old_min) {
                    // If min equal, update if any vitamin is better
                    if (ni > nxt[0] || nj > nxt[1] || nk > nxt[2]) {
                        nxt = {ni, nj, nk};
                    }
                }
            }
        }
    }

    ll res = 0;
    for (int cal = 0; cal <= X; ++cal) {
        if (dp[cal][0] == LLONG_MIN) continue;
        ll cur_min = min({dp[cal][0], dp[cal][1], dp[cal][2]});
        if (cur_min > res) res = cur_min;
    }
    cout << res << "\n";

    return 0;
}