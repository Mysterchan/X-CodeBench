#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const int MAX_N = 5010;
const ll INF = 1e18;

vector<ll> W(MAX_N);
vector<vector<int>> adj(MAX_N);

ll dijkstra(int n) {
    vector<ll> fuel(n, INF);
    priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<>> pq;

    fuel[0] = 0; // Starting point
    pq.push({0, 0});

    while (!pq.empty()) {
        auto [curr_fuel, node] = pq.top();
        pq.pop();

        if (curr_fuel > fuel[node]) continue;

        for (int neighbor : adj[node]) {
            ll new_fuel = curr_fuel + W[neighbor] * (curr_fuel / W[node]);
            if (new_fuel < fuel[neighbor]) {
                fuel[neighbor] = new_fuel;
                pq.push({new_fuel, neighbor});
            }
        }
    }

    return fuel;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    for (int i = 0; i < n; ++i) {
        cin >> W[i];
    }

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u - 1].push_back(v - 1);
        adj[v - 1].push_back(u - 1);
    }

    vector<ll> result = dijkstra(n);
    for (int i = 0; i < n; ++i) {
        cout << result[i] << "\n";
    }

    return 0;
}