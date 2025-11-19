#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    unordered_map<int, unordered_set<int>> edges;
    
    int duplicates = 0, self_loops = 0;

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        if (u == v) {
            self_loops++;
        } else {
            // Count the multi-edges
            if (edges[u].count(v)) {
                duplicates++;
            }
            // Store the edge in the set to avoid multi-edges
            edges[u].insert(v);
            edges[v].insert(u);
        }
    }

    int result = duplicates + self_loops;
    cout << result << endl;

    return 0;
}