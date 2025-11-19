#include <bits/stdc++.h>
using namespace std;
#define int long long
using pr = pair<int, int>;
const int N = 200000 + 5, inf = 1e18;

int n, m, k;
vector<array<int, 3>> e[N];
int dis[N], dp[N];

void Solve() {
    cin >> n >> m >> k;
    for (int i = 1; i <= n; i++) {
        dis[i] = inf;
        dp[i] = inf;
        e[i].clear();
    }
    for (int i = 0; i < m; i++) {
        int u, v, l, r;
        cin >> u >> v >> l >> r;
        e[u].push_back({v, l, r});
        e[v].push_back({u, l, r});
    }

    // Dijkstra from k with edge weights = r_i (max weights)
    priority_queue<pr, vector<pr>, greater<pr>> pq;
    dis[k] = 0;
    pq.push({0, k});
    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d != dis[u]) continue;
        for (auto &[v, l, r] : e[u]) {
            int nd = dis[u] + r;
            if (nd < dis[v]) {
                dis[v] = nd;
                pq.push({nd, v});
            }
        }
    }

    // Modified Dijkstra from 1 with edge weights = l_i (min weights)
    // dp[u] = minimal distance from 1 to u using l_i weights
    dp[1] = 0;
    pq.push({0, 1});
    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d != dp[u]) continue;
        if (dp[u] >= dis[u]) continue; // prune states that can't improve answer
        for (auto &[v, l, r] : e[u]) {
            int nd = dp[u] + l;
            if (nd < dp[v]) {
                dp[v] = nd;
                pq.push({nd, v});
            }
        }
    }

    // If dp[n] < dis[n], then YES, else NO
    cout << (dp[n] < dis[n] ? "YES\n" : "NO\n");
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T; cin >> T;
    while (T--) Solve();
    return 0;
}