#include <bits/stdc++.h>
using namespace std;

int n, m, x, y;
vector<vector<int>> graph;
vector<int> parent;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    while (t--) {
        cin >> n >> m >> x >> y;
        x--, y--;

        graph.assign(n, vector<int>());
        parent.assign(n, -1);

        for (int i = 0; i < m; i++) {
            int u, v; cin >> u >> v;
            u--, v--;
            graph[u].push_back(v);
            graph[v].push_back(u);
        }

        // Sort adjacency lists to ensure lex smallest path
        for (int i = 0; i < n; i++) {
            sort(graph[i].begin(), graph[i].end());
        }

        // BFS to find shortest lex smallest path from x to y
        queue<int> q;
        q.push(x);
        parent[x] = x;

        while (!q.empty()) {
            int cur = q.front(); q.pop();
            if (cur == y) break;
            for (int nxt : graph[cur]) {
                if (parent[nxt] == -1) {
                    parent[nxt] = cur;
                    q.push(nxt);
                }
            }
        }

        // Reconstruct path from y to x
        vector<int> path;
        for (int cur = y; cur != x; cur = parent[cur]) {
            path.push_back(cur);
        }
        path.push_back(x);
        reverse(path.begin(), path.end());

        for (int v : path) cout << v + 1 << " ";
        cout << "\n";
    }
}