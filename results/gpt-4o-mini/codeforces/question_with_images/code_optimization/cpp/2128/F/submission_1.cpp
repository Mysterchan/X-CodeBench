#include <bits/stdc++.h>
using namespace std;
#define int long long
const int N = 200005;
const int inf = 1e18;
vector<array<int, 3>> adj[N];

void Solve() {
    int n, m, k;
    cin >> n >> m >> k;
    
    for (int i = 1; i <= n; ++i) {
        adj[i].clear();
    }

    for (int i = 1; i <= m; ++i) {
        int u, v, l, r;
        cin >> u >> v >> l >> r;
        adj[u].push_back({v, l, r});
        adj[v].push_back({u, l, r});
    }

    vector<int> dist(n + 1, inf);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    dist[k] = 0;
    pq.push({0, k});

    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d > dist[u]) continue;

        for (const auto& [v, l, r] : adj[u]) {
            if (dist[v] > dist[u] + l) {
                dist[v] = dist[u] + l;
                pq.push({dist[v], v});
            }
        }
    }

    int d1 = dist[1], dk = dist[k], dn = dist[n];
    if (dk == inf || dn == inf) {
        cout << "NO\n";
        return;
    }

    vector<int> maxPath(n + 1, -inf);
    maxPath[1] = d1;

    pq.push({-d1, 1});
    while (!pq.empty()) {
        auto [neg_d, u] = pq.top(); pq.pop();
        int d = -neg_d;

        if (d < maxPath[u]) continue;

        for (const auto& [v, l, r] : adj[u]) {
            int newMax = max(maxPath[u] + r, dist[v]);
            if (newMax > maxPath[v]) {
                maxPath[v] = newMax;
                pq.push({-maxPath[v], v});
            }
        }
    }

    cout << (maxPath[n] < dn ? "YES\n" : "NO\n");
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) Solve();
    return 0;
}