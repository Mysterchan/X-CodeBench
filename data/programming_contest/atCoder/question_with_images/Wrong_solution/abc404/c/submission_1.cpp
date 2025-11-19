#include <bits/stdc++.h>
using namespace std;

vector<int> vis;
vector<vector<int>> adj;
int n;
bool cycle = false;

bool dfs(int node, int parent) {
    vis[node] = 1;

    if (cycle) return true;

    for (auto it : adj[node]) {
        if (it == parent) continue;

        if (!vis[it]) {
            if (dfs(it, node)) return true;
        } 
        else {
            cycle = true;
            return true;
        }
    }

    return false;
}

int main() {
    cin >> n;
    int m;
    cin >> m;

    adj.resize(n + 1);
    vis.assign(n + 1, 0);

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    for (int i = 1; i <= n; i++) {   // ✅ fixed range
        if (cycle) break;
        if (!vis[i]) dfs(i, -1);
    }

    if (cycle) cout << "Yes\n";
    else cout << "No\n";

    return 0;
}