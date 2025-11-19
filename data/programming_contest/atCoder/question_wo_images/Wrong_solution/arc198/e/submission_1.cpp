#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    int size = 1 << n;
    vector<int> cnt(size, 0);
    for (int i = 0; i < m; ++i) {
        int s;
        cin >> s;
        cnt[s] = 1;
    }

    vector<int> f = cnt;
    for (int i = 0; i < n; ++i) {
        for (int mask = 0; mask < size; ++mask) {
            if (mask & (1 << i)) {
                f[mask] = (f[mask] + f[mask ^ (1 << i)]) % MOD;
            }
        }
    }

    int max_x = 1 << n;
    vector<long long> dp(max_x + 1, 0);
    dp[0] = 1;

    for (int x = 0; x < max_x; ++x) {
        if (dp[x] == 0) continue;
        int ways = f[x];
        dp[x + 1] = (dp[x + 1] + dp[x] * ways) % MOD;
    }

    cout << dp[max_x] % MOD << '\n';
    return 0;
}