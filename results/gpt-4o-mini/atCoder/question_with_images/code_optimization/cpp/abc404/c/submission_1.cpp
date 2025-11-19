#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    // A cycle graph must have exactly N edges
    if (m != n) {
        cout << "No";
        return 0;
    }

    // Degree count
    vector<int> degree(n + 1, 0);
    vector<vector<int>> adj(n + 1);

    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
        degree[u]++;
        degree[v]++;
    }

    // Check if all vertices have degree 2
    for (int i = 1; i <= n; i++) {
        if (degree[i] != 2) {
            cout << "No";
            return 0;
        }
    }

    // Check for a single cycle
    vector<bool> visited(n + 1, false);
    int start = 1;
    int current = start;
    int count = 0;

    do {
        visited[current] = true;
        count++;
        for (int neighbor : adj[current]) {
            if (!visited[neighbor]) {
                current = neighbor;
                break;
            }
        }
    } while (current != start);

    // Check if we visited all nodes exactly once
    if (count == n) {
        cout << "Yes";
    } else {
        cout << "No";
    }

    return 0;
}