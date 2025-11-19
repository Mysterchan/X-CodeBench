#include<bits/stdc++.h>
using namespace std;

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int N, Q;
    cin >> N >> Q;
    vector<int> A(N);
    for (int i = 0; i < N; ++i) cin >> A[i];
    
    // Coordinate compression
    vector<int> vals = A;
    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());
    int M = vals.size();
    
    for (int i = 0; i < N; ++i) {
        A[i] = lower_bound(vals.begin(), vals.end(), A[i]) - vals.begin();
    }
    
    // Precompute LIS length at each position for each possible X value
    vector<vector<int>> dp(N + 1, vector<int>(M + 1, 0));
    
    for (int r = 1; r <= N; ++r) {
        for (int x = 0; x <= M; ++x) {
            dp[r][x] = dp[r-1][x];
        }
        
        int val = A[r-1];
        for (int x = val; x < M; ++x) {
            int max_len = 0;
            for (int prev = 0; prev < val; ++prev) {
                max_len = max(max_len, dp[r-1][prev]);
            }
            dp[r][x] = max(dp[r][x], max_len + 1);
        }
    }
    
    for (int i = 0; i < Q; ++i) {
        int R, X;
        cin >> R >> X;
        
        int x_idx = upper_bound(vals.begin(), vals.end(), X) - vals.begin();
        
        int result = 0;
        for (int j = 0; j < x_idx; ++j) {
            result = max(result, dp[R][j]);
        }
        
        cout << result << "\n";
    }
    
    return 0;
}