#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;
    vector<ll> W(N);
    for (int i = 0; i < N; i++) cin >> W[i];

    vector<vector<int>> adj(N);
    for (int i = 0; i < M; i++) {
        int u, v; cin >> u >> v;
        u--; v--;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    // dist[v] = minimal fuel cost to reach v
    vector<ll> dist(N, LLONG_MAX);
    // weight[v] = weight after visiting v on minimal fuel path
    vector<ll> weight(N, LLONG_MAX);

    // Start at vertex 0 (vertex 1 in 1-based)
    dist[0] = 0;
    weight[0] = W[0];

    // priority_queue of (dist, vertex)
    using pli = pair<ll, int>;
    priority_queue<pli, vector<pli>, greater<>> pq;
    pq.emplace(0, 0);

    while (!pq.empty()) {
        auto [cur_dist, v] = pq.top();
        pq.pop();
        if (cur_dist > dist[v]) continue;

        ll cur_weight = weight[v];
        for (int to : adj[v]) {
            // Moving from v to to:
            // fuel cost = cur_weight
            // new weight = cur_weight + W[to]
            ll ndist = cur_dist + cur_weight;
            ll nweight = cur_weight + W[to];
            if (ndist < dist[to] || (ndist == dist[to] && nweight < weight[to])) {
                dist[to] = ndist;
                weight[to] = nweight;
                pq.emplace(ndist, to);
            }
        }
    }

    // Output results
    // For vertex 1 (index 0), fuel cost is 0 as per problem statement
    for (int i = 0; i < N; i++) {
        cout << (i == 0 ? 0 : dist[i]) << "\n";
    }

    return 0;
}