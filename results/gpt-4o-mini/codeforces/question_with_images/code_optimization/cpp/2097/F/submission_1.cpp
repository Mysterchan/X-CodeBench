#include <bits/stdc++.h>
#define int long long
using namespace std;

void solve() {
    int n, m;
    cin >> n >> m;
    vector<int> s(n), dp(n);
    for (int i = 0; i < n; i++) {
        cin >> s[i];
    }
    
    for (int day = 0; day < m; day++) {
        vector<int> a(n), b(n), c(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        for (int i = 0; i < n; i++) {
            cin >> b[i];
        }
        for (int i = 0; i < n; i++) {
            cin >> c[i];
        }
        
        vector<int> next_s(n);
        for (int i = 0; i < n; i++) {
            next_s[i] = max(0LL, s[i] - a[i] - c[(i + 1) % n]);
        }
        
        for (int i = 0; i < n; i++) {
            long long found = max(0LL, next_s[i] - b[i]);
            dp[i] = next_s[i] - found + (s[i] - next_s[i]);
        }
        
        s = next_s;

        // Calculate total unfound luggage
        int total_unfound = 0;
        for (int i = 0; i < n; i++) {
            total_unfound += s[i];
        }
        
        cout << total_unfound << endl;
    }
}

signed main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}