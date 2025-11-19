#include <bits/stdc++.h>

using namespace std;

using i64 = long long;

using PII = pair<int, int>;

void dijkstra(vector<vector<PII>> &adj) {
    int n = adj.size();
    vector<int> dist(n, INT_MAX);
    dist[0] = 0;
    vector<int> vis(n);

    priority_queue<PII, vector<PII>, greater<PII>> pq;
    pq.emplace(0, 0);
    while (!pq.empty()) {
        auto [dis, u] = pq.top();
        pq.pop();

        if (vis[u]) continue;
        vis[u] = true;

        for (auto [v, w] : adj[u]) {
            if (dist[v] > dis + w) {
                dist[v] = dis + w;
                pq.emplace(dist[v], v);
            }
        }
    }

    cout << min(dist[n - 1], dist[n / 2 - 1]);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, x;
    cin >> n >> m >> x;

    vector<vector<PII>> adj(2 * n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        u--;
        v--;
        adj[u].emplace_back(v, 1);
        adj[u + n].emplace_back(v + n, 1);
    }

    for (int u = 0; u < n; u++) {
        adj[u].emplace_back(u + n, x);
        adj[u + n].emplace_back(u, x);
    }

    dijkstra(adj);

    return 0;
}