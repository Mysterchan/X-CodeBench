#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll INF = 1LL << 60;
const int MAXN = 200000 + 10;

int n, m;
ll X;
vector<int> g[2][MAXN]; // g[0]: original edges, g[1]: reversed edges

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m >> X;
    for (int i = 0; i < m; i++) {
        int u, v; cin >> u >> v;
        g[0][u].push_back(v);
        g[1][v].push_back(u);
    }

    // dist[flip][node]: minimal cost to reach node with flip state
    // flip=0 means edges as original, flip=1 means edges reversed
    vector<vector<ll>> dist(2, vector<ll>(n + 1, INF));
    dist[0][1] = 0;

    // Use 0-1 BFS with deque because edges cost 1 and flip cost X (large)
    // But since flip cost can be large, we use Dijkstra instead
    using pli = pair<ll, pair<int,int>>; // cost, (flip, node)
    priority_queue<pli, vector<pli>, greater<pli>> pq;
    pq.push({0, {0, 1}});

    while (!pq.empty()) {
        auto [cost, state] = pq.top(); pq.pop();
        int flip = state.first, u = state.second;
        if (dist[flip][u] < cost) continue;
        if (u == n) {
            cout << cost << "\n";
            return 0;
        }

        // Move along edges in current flip state
        for (int nxt : g[flip][u]) {
            ll ncost = cost + 1;
            if (ncost < dist[flip][nxt]) {
                dist[flip][nxt] = ncost;
                pq.push({ncost, {flip, nxt}});
            }
        }

        // Flip edges direction
        int nflip = 1 - flip;
        ll ncost = cost + X;
        if (ncost < dist[nflip][u]) {
            dist[nflip][u] = ncost;
            pq.push({ncost, {nflip, u}});
        }
    }

    // Should never reach here because problem guarantees reachability
    cout << -1 << "\n";
    return 0;
}