#include <bits/stdc++.h>
using namespace std;

#define int long long

void solve() {
    int n, w;
    cin >> n >> w;
    
    vector<vector<int>> items(60);
    
    for (int i = 0; i < n; i++) {
        int x, y;
        cin >> x >> y;
        items[x].push_back(y);
    }
    
    // Sort and compute prefix sums
    vector<vector<int>> prefixSum(60);
    for (int i = 0; i < 60; i++) {
        if (!items[i].empty()) {
            sort(items[i].rbegin(), items[i].rend());
            prefixSum[i].push_back(0);
            for (int val : items[i]) {
                prefixSum[i].push_back(prefixSum[i].back() + val);
            }
        } else {
            prefixSum[i].push_back(0);
        }
    }
    
    map<pair<int, int>, int> memo;
    
    function<int(int, int)> dp = [&](int bit, int capacity) -> int {
        if (bit < 0 || capacity <= 0) return 0;
        
        auto key = make_pair(bit, capacity);
        if (memo.count(key)) return memo[key];
        
        int maxVal = 0;
        int maxTake = min(capacity >> bit, (int)items[bit].size());
        
        for (int take = 0; take <= maxTake; take++) {
            int usedWeight = take * (1LL << bit);
            int value = prefixSum[bit][take];
            maxVal = max(maxVal, value + dp(bit - 1, capacity - usedWeight));
        }
        
        return memo[key] = maxVal;
    };
    
    cout << dp(59, w) << "\n";
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