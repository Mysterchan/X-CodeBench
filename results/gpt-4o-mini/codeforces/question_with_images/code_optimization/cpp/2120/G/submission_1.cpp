#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    cin >> t;

    while (t--) {
        int n, m, k;
        cin >> n >> m >> k;
        
        vector<int> degree(n, 0);
        map<int, vector<int>> vertexEdges;

        for (int i = 0; i < m; i++) {
            int u, v;
            cin >> u >> v;
            u--; v--;
            degree[u]++;
            degree[v]++;
            vertexEdges[u].push_back(v);
            vertexEdges[v].push_back(u);
        }

        int oddDegreeCount = 0;
        for (int d : degree) {
            if (d % 2 == 1) {
                oddDegreeCount++;
            }
        }

        // For the original graph G to have an Euler trail, check the odd degree count
        if (oddDegreeCount > 2) {
            cout << "NO\n";
            continue;
        }

        // Check the conditions for L^k(G)
        // If k is odd, we have to keep the odd degree property
        if (k % 2 == 1) {
            cout << (oddDegreeCount == 0 ? "YES\n" : "NO\n");
        } else {
            // If k is even, the resulting graph will have even degree vertices
            cout << "YES\n";
        }
    }

    return 0;
}