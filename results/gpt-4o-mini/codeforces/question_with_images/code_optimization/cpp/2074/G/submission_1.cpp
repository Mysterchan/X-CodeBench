#include <bits/stdc++.h>
using namespace std;

#define int int64_t

void solve() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++)
        cin >> a[i];
    
    int maxScore = 0;
    
    // We will use a dynamic programming array to store maximum scores
    vector<vector<int>> dp(n, vector<int>(n, 0));

    for (int length = 3; length <= n; ++length) {
        for (int l = 0; l <= n - length; ++l) {
            int r = l + length - 1;
            // Calculate the score for all valid triangles within bounds l and r
            for (int k = l + 1; k < r; ++k) {
                int score = a[l] * a[k] * a[r];
                int currentScore = score + (l + 1 <= k - 1 ? dp[l + 1][k - 1] : 0) 
                                             + (k + 1 <= r - 1 ? dp[k + 1][r - 1] : 0);
                dp[l][r] = max(dp[l][r], currentScore);
            }
            maxScore = max(maxScore, dp[l][r]);
        }
    }

    cout << maxScore << "\n";
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}