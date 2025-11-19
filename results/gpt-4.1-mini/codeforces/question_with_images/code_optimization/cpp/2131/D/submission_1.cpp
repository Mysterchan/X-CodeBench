#include <bits/stdc++.h>
using namespace std;

int deg[200005];
vector<int> vec[200005];

void solve() {
    int n; cin >> n;
    for (int i = 1; i <= n; i++) {
        vec[i].clear();
        deg[i] = 0;
    }
    for (int i = 1; i < n; i++) {
        int u, v; cin >> u >> v;
        vec[u].push_back(v);
        vec[v].push_back(u);
        deg[u]++;
        deg[v]++;
    }
    if (n == 2) {
        cout << 0 << "\n";
        return;
    }
    int ans = 1e9;
    // For each node, count how many neighbors are not leaves
    for (int i = 1; i <= n; i++) {
        int cnt = 0;
        for (auto v : vec[i]) {
            if (deg[v] > 1) cnt++;
        }
        ans = min(ans, cnt);
    }
    cout << ans << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t; cin >> t;
    while (t--) solve();
    return 0;
}