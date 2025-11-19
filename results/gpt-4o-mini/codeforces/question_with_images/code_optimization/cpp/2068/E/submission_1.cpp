#include <bits/stdc++.h>
using namespace std;

const int MX = 200000;

int n, m;
vector<int> G[MX + 1];

vector<int> bfs(int source) {
    vector<int> dist(n + 1, -1);
    queue<int> q;
    dist[source] = 0;
    q.push(source);

    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int v : G[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }
    return dist;
}

int solve() {
    // Get shortest path from n (Porto) to all nodes
    vector<int> dist_to_porto = bfs(n);

    // Calculate the shortest distance from 1 (Lisbon) to all nodes
    vector<int> dist_to_lisbon = bfs(1);

    // Check which roads to block and the minimum route the supporters can take
    int min_dist = INT_MAX;
    
    for (int u = 1; u <= n; ++u) {
        for (int v : G[u]) {
            // Block the edge u-v if it's not going to Porto
            if (dist_to_porto[v] == dist_to_porto[u] - 1) continue;

            // Compare the distance with the blocked edge
            if (dist_to_lisbon[u] != -1 && dist_to_porto[v] != -1) {
                min_dist = min(min_dist, dist_to_lisbon[u] + dist_to_porto[v] + 1);
            }
        }
    }

    return min_dist == INT_MAX ? -1 : min_dist;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    
    while (cin >> n >> m) {
        for (int i = 1; i <= n; ++i) G[i].clear();
        
        for (int i = 0; i < m; ++i) {
            int u, v; cin >> u >> v;
            G[u].push_back(v);
            G[v].push_back(u);
        }

        cout << solve() << "\n";
    }
}