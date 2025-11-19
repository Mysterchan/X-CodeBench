#include <bits/stdc++.h>
using namespace std;

void findLexicographicallySmallestPath(int n, int m, int x, int y, vector<vector<int>>& graph) {
    vector<int> parent(n, -1); // To store the parents of each node in the path
    vector<bool> visited(n, false);
    priority_queue<int, vector<int>, greater<int>> pq; // Min-heap for lexicographic ordering
    pq.push(x);
    visited[x] = true;

    while (!pq.empty()) {
        int v = pq.top();
        pq.pop();
        
        if (v == y) break; // If we reached the destination, stop

        for (int nv : graph[v]) {
            if (!visited[nv]) {
                visited[nv] = true;
                parent[nv] = v; // Set parent to reconstruct the path
                pq.push(nv);
            }
        }
    }

    // Reconstruct path from Y to X
    vector<int> path;
    for (int at = y; at != -1; at = parent[at]) {
        path.push_back(at + 1); // Switching index to 1-based
    }
    reverse(path.begin(), path.end()); // Reverse to get path from X to Y

    for (int ans_v : path) {
        cout << ans_v << " ";
    }
    cout << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n, m, x, y;
        cin >> n >> m >> x >> y;
        x--, y--; // Convert to 0-based index

        vector<vector<int>> graph(n);
        for (int i = 0; i < m; i++) {
            int u, v;
            cin >> u >> v;
            u--, v--; // Convert to 0-based index
            graph[u].push_back(v);
            graph[v].push_back(u);
        }

        // Sort the graph adjacency list
        for (auto& neighbors : graph) {
            sort(neighbors.begin(), neighbors.end());
        }

        findLexicographicallySmallestPath(n, m, x, y, graph);
    }

    return 0;
}