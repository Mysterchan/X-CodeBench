#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <limits>

using namespace std;
typedef long long ll;

const int N = 2e5 + 10;
vector<pair<int, int>> graph[N]; // Adjacency list for the original graph
vector<pair<int, int>> reverseGraph[N]; // Adjacency list for the reverse graph

ll d[N]; // Minimum cost to reach each node
const ll INF = numeric_limits<ll>::max();

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    ll x;
    cin >> n >> m >> x;

    // Reading the graph edges
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        graph[u].emplace_back(v, 0); // Original graph edge
        reverseGraph[v].emplace_back(u, 1); // Reverse graph edge
    }

    // Priority queue for Dijkstra's algorithm
    priority_queue<tuple<ll, int>, vector<tuple<ll, int>>, greater<tuple<ll, int>>> pq;

    // Initial cost to start from vertex 1
    fill(d, d + n + 1, INF);
    d[1] = 0;
    pq.emplace(0, 1); // (cost, vertex)

    while (!pq.empty()) {
        auto [cost, u] = pq.top(); pq.pop();

        // If we reach vertex N, print the cost
        if (u == n) {
            cout << cost << '\n';
            return 0;
        }

        // Move along the original directed edges
        for (auto &[v, _] : graph[u]) {
            if (cost + 1 < d[v]) {
                d[v] = cost + 1;
                pq.emplace(d[v], v);
            }
        }

        // Reverse all edges
        if (cost + x < d[n]) {
            for (auto &[v, _] : reverseGraph[u]) {
                if (cost + x + 1 < d[v]) {
                    d[v] = cost + x + 1;
                    pq.emplace(d[v], v);
                }
            }
        }
    }
    return 0;
}