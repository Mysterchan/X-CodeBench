#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    // Quick check: cycle graph must have exactly n edges
    if (m != n) {
        cout << "No\n";
        return 0;
    }

    vector<vector<int>> adj(n + 1);
    vector<int> degree(n + 1, 0);

    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        degree[u]++;
        degree[v]++;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    // Check all vertices have degree 2
    for (int i = 1; i <= n; i++) {
        if (degree[i] != 2) {
            cout << "No\n";
            return 0;
        }
    }

    // Check connectivity using DFS
    vector<bool> visited(n + 1, false);
    int stack_top = 0;
    vector<int> stack(n);
    stack[stack_top++] = 1;
    visited[1] = true;
    int visited_count = 1;

    while (stack_top > 0) {
        int u = stack[--stack_top];
        for (int w : adj[u]) {
            if (!visited[w]) {
                visited[w] = true;
                stack[stack_top++] = w;
                visited_count++;
            }
        }
    }

    cout << (visited_count == n ? "Yes\n" : "No\n");
    return 0;
}