#include <bits/stdc++.h>
#include <cassert>

using namespace std;
using ll = long long;

#define all(x) (x).begin(), (x).end()
#define sz(x) (int)(x).size()
#define pb push_back

mt19937 rnd(chrono::steady_clock::now().time_since_epoch().count());
template<typename T>
void shuf(vector<T>& a) {
    for (int i = 1; i < sz(a); i++) swap(a[i], a[rnd() % (i + 1)]);
}

void solve() {
    int s, k; cin >> s >> k;
    if (s % k == 0) {
        cout << k << '\n';
        return;
    }
    if (s >= k * (k - 2)) {
        cout << max(1, k - 2) << '\n';
        return;
    }
    vector<int> dp(k, s + 1);
    dp[0] = 0;
    for (int ns = k - 1; ns >= 2; ns--) {
        if ((k - ns) % 2 == 1) {
            vector<int> ndp(ns, -1);
            for (int j = 0; j < (ns + 1); j++) {
                for (int steps = 1; dp[j] + steps * (ns + 1) <= s; steps++) {
                    ndp[(dp[j] + steps * (ns + 1)) % ns] = max(ndp[(dp[j] + steps * (ns + 1)) % ns], dp[j] + steps * (ns + 1));
                }
            }
            swap(dp, ndp);
        } else {
            vector<int> ndp(ns, s + 1);
            for (int j = 0; j < (ns + 1); j++) {
                for (int steps = 1; dp[j] - steps * (ns + 1) >= 0; steps++) {
                    ndp[(dp[j] - steps * (ns + 1)) % ns] = min(ndp[(dp[j] - steps * (ns + 1)) % ns], dp[j] - steps * (ns + 1));
                }
            }
            swap(dp, ndp);
            if (dp[s % ns] != s + 1) {
                cout << ns << '\n';
                return;
            }
        }
    }
    cout << 1 << '\n';
}

signed main() {
    int tt = 1;
    #ifdef LOCAL
        freopen("in.txt", "r", stdin);
        freopen("out.txt", "w", stdout);
    #else
        ios::sync_with_stdio(false);
        cin.tie(0); cout.tie(0);
    #endif
    cin >> tt;

    while (tt--) {
        solve();
    }

    return 0;
}
