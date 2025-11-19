#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, X; 
    cin >> N >> X;
    
    vector<vector<ll>> dp(4, vector<ll>(X + 1, 0)); // dp[v][c] -> max vitamin v with c calories
    for (int i = 1; i <= 3; ++i) {
        dp[i][0] = LLONG_MIN; // Cannot get any vitamin with 0 calories
    }

    for (int i = 0; i < N; ++i) {
        int V, C;
        ll A;
        cin >> V >> A >> C;
        for (int j = 3; j >= V; --j) {
            for (int k = X; k >= C; --k) {
                if (dp[j - V][k - C] != LLONG_MIN) {
                    dp[j][k] = max(dp[j][k], dp[j - V][k - C] + A);
                }
            }
        }
    }

    ll res = 0;
    for (int c = 0; c <= X; ++c) {
        ll minV = LLONG_MAX;
        for (int v = 1; v <= 3; ++v) {
            if (dp[v][c] <= 0) {
                minV = 0;
                break;
            }
            minV = min(minV, dp[v][c]);
        }
        res = max(res, minV);
    }

    cout << res << endl;

    return 0;
}