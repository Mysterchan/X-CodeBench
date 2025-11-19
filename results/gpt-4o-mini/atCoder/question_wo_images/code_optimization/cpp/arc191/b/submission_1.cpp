#include <bits/stdc++.h>
using namespace std;

#define int long long

void solve() {
    int n, k;
    cin >> n >> k;

    vector<int> compatible;
    
    for (int i = n; compatible.size() < k; i++) {
        if ((i ^ n) % n == (i ^ n)) {
            compatible.push_back(i);
        }
    }

    if (compatible.size() < k) {
        cout << -1 << '\n';
    } else {
        cout << compatible[k - 1] << '\n';
    }
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
