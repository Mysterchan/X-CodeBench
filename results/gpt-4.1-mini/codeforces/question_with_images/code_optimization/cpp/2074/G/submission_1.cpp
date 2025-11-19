#include <bits/stdc++.h>
using namespace std;

#define int int64_t

int dp[405][405];

void solve() {
    int n; cin >> n;
    vector<int> a(n);
    for (int &x : a) cin >> x;

    // dp[i][j]: max score for polygon vertices from i to j (inclusive)
    // i < j, indices modulo n, but we use linear indexing with offset
    // We'll use 0-based indexing and consider intervals [i, j] with j > i

    // Since polygon is circular, we duplicate array to handle wrap-around
    vector<int> vals(2 * n);
    for (int i = 0; i < 2 * n; i++) vals[i] = a[i % n];

    // Reset dp
    for (int i = 0; i < 2 * n; i++)
        for (int j = 0; j < 2 * n; j++)
            dp[i][j] = 0;

    // We only consider intervals of length >= 3 (triangles)
    for (int length = 3; length <= n; length++) {
        for (int l = 0; l + length - 1 < 2 * n; l++) {
            int r = l + length - 1;
            int &res = dp[l][r];
            res = 0;
            // Try all possible k between l+1 and r-1 to form triangle (l, k, r)
            for (int k = l + 1; k < r; k++) {
                int val = dp[l][k] + dp[k][r] + vals[l] * vals[k] * vals[r];
                if (val > res) res = val;
            }
        }
    }

    int ans = 0;
    // The polygon is circular, so max over all intervals of length n
    for (int i = 0; i < n; i++) {
        ans = max(ans, dp[i][i + n - 1]);
    }
    cout << ans << "\n";
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    while (t--) solve();

    return 0;
}