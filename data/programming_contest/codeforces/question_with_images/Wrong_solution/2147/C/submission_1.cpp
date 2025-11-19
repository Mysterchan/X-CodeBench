#include <bits/stdc++.h>
using namespace std;

#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;

typedef long long ll;
template <typename T>
using ordered_set =
    tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;

#ifdef LOCAL
#include "debug.h"
#else
#define debug(...)
#endif

#define mod 1000000007
#define mod1 998244353
#define inf (ll)1e15
#define linf (ll)2e18
#define nl '\n'

const ll N = 1e3 + 1;

void solve() {
    ll n;
    cin >> n;
    string s;
    cin >> s;

    vector<ll> dp(n, 0);
    if (s[0] == '0')
        dp[0] = 1;
    if (s[n - 1] == '0')
        dp[n - 1] = 1;
    for (int i = 1; i < n; i++) {
        if (s[i] == '0') {
            if (dp[i - 1] == 1 or s[i - 1] == '0' or dp[i - 1] == 2) {
                dp[i - 1] = 1, dp[i] = 1;
                continue;
            }
            if (i > 1) {
                if (dp[i - 2] == 1 or dp[i - 2] == 2) {
                    dp[i] = 2;
                    continue;
                }
                if (s[i - 2] == '0') {
                    dp[i - 2] = 3;
                    dp[i] = 3;
                    continue;
                }
            }
        }
    }
    for (int i = 0; i < n; i++) {
        if (s[i] == '0' and !dp[i]) {
            cout << "NO\n";
            return;
        }
    }
    cout << "YES\n";
}

int main() {
    ios_base::sync_with_stdio(false), cin.tie(nullptr);
    ll TESTS = 1;
    cin >> TESTS;

    for (int Case = 1; Case <= TESTS; Case++) {
        debug(Case);
        solve();
    }

    return 0;
}
