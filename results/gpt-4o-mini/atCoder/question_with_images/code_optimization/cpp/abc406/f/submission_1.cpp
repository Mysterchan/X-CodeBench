#include <bits/stdc++.h>
using namespace std;
#define int long long
const int N = 3e5 + 10;

vector<int> tree[N];
int subtreeWeight[N];
int weight[N];

void dfs(int node, int parent) {
    subtreeWeight[node] = weight[node];
    for (int neighbor : tree[node]) {
        if (neighbor != parent) {
            dfs(neighbor, node);
            subtreeWeight[node] += subtreeWeight[neighbor];
        }
    }
}

signed main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    // Initialize weights
    for (int i = 1; i <= n; i++) {
        weight[i] = 1;
    }

    // Read tree structure
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        tree[u].push_back(v);
        tree[v].push_back(u);
    }

    // Process queries
    int q;
    cin >> q;
    vector<pair<int, int>> edges;
    for (int i = 0; i < q; i++) {
        int type;
        cin >> type;
        if (type == 1) {
            int x, w;
            cin >> x >> w;
            weight[x] += w;
        } else {
            int y;
            cin >> y;
            y--; // to make it 0-indexed
            edges.push_back({tree[edges[y].first][0], tree[edges[y].second][0]});
        }
    }

    // Calculate subtree weights for the first time
    dfs(1, -1);

    // Output results for query type 2
    for (auto &edge : edges) {
        int u = edge.first;
        int v = edge.second;

        // Calculate difference of subtree weights
        int totalWeight = subtreeWeight[u];
        int subtreeWeightWhenEdgeRemoved = subtreeWeight[v];

        cout << abs(totalWeight - subtreeWeightWhenEdgeRemoved) << '\n';
    }

    return 0;
}