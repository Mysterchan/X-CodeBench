#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<ll> a(n);
    for (auto &x : a) cin >> x;

    const ll NEG = -4e18;
    vector<ll> dp(n + 1, NEG);
    dp[0] = 0;

    for (int i = 0; i < n; ++i) {
        vector<ll> newdp = dp;
        for (int k = 0; k <= n; ++k) {
            if (dp[k] == NEG) continue;
            newdp[k + 1] = max(newdp[k + 1], dp[k] + a[i]);
            if (k > 0)
                newdp[k - 1] = max(newdp[k - 1], dp[k]);
        }
        dp.swap(newdp);
    }

    cout << *max_element(dp.begin(), dp.end()) << "\n";
    return 0;
}
