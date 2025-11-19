#include <bits/stdc++.h>
#define int long long
using namespace std;

vector<vector<int>> graph;
vector<int> degree;

void dfs(int node, int parent, int& total) {
    if (degree[node] == 1) return;
    for (auto neighbor : graph[node]) {
        if (neighbor == parent) continue;
        dfs(neighbor, node, total);
        total += degree[neighbor] == 1 ? 0 : (1 + degree[neighbor]);
    }
}

void solve() {
    int n;
    cin >> n;
    graph.assign(n + 1, vector<int>());
    degree.assign(n + 1, 0);

    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
        degree[u]++;
        degree[v]++;
    }

    if (n == 2) {
        cout << 0 << endl;
        return;
    }

    int result = LLONG_MAX;

    for (int i = 1; i <= n; i++) {
        int mid = 0;
        for (auto neighbor : graph[i]) {
            if (degree[neighbor] > 1) {
                int temp = 0;
                dfs(neighbor, i, temp);
                mid += temp;
            }
        }
        result = min(result, mid);
    }

    cout << result << endl;
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}