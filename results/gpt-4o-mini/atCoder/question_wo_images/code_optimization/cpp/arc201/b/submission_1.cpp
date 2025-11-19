#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl "\n"

void solve() {
    int n, w;
    cin >> n >> w;

    vector<pair<int, int>> items(n);
    
    for (int i = 0; i < n; i++) {
        int x, y;
        cin >> x >> y;
        items[i] = {1LL << x, y}; // Store weight as 2^X and value
    }

    // Sort items by weight (to apply a modified knapsack approach)
    sort(items.begin(), items.end());

    // dp[w] will store the maximum value we can obtain with a weight limit w
    vector<int> dp(w + 1, 0);

    for (const auto& item : items) {
        auto weight = item.first;
        auto value = item.second;

        // Process this item in a reversed manner for the current weight limit
        for (int j = w; j >= weight; j--) {
            dp[j] = max(dp[j], dp[j - weight] + value);
        }
    }

    // The maximum achievable value with the maximum weight limit w
    cout << dp[w] << endl;
}

int32_t main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    
    return 0;
}
