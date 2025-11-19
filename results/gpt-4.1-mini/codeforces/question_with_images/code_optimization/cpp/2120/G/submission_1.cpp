#include <bits/stdc++.h>
using namespace std;

// Explanation of optimization:
// The original code tries to explicitly construct L^k(G) which is infeasible for large k and large graphs.
// Instead, we use known properties of line graphs and Euler trails.
//
// Key facts:
// 1. G has an Euler trail and is not a path graph.
// 2. L(G) has an Euler trail if and only if G is Eulerian (all vertices have even degree).
// 3. For k >= 2, L^k(G) is Eulerian (has an Euler trail) if and only if G is Eulerian.
//
// Since G has an Euler trail, it has either 0 or 2 vertices of odd degree.
// If G is Eulerian (0 odd degree vertices), then L(G) and all subsequent line graphs have Euler trails.
// If G has exactly 2 odd degree vertices, then L(G) does NOT have an Euler trail, but L^2(G) and beyond do.
//
// So the answer depends only on k and the parity of the number of odd degree vertices in G:
//
// - If k == 0: answer is YES (G has Euler trail by problem statement).
// - If k == 1: answer is YES if G is Eulerian (0 odd degree vertices), else NO.
// - If k >= 2: answer is YES.
//
// This avoids any graph construction or BFS, making the solution O(n + m).

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    while (t--) {
        int n, m, k; cin >> n >> m >> k;
        vector<int> degree(n, 0);
        for (int i = 0; i < m; i++) {
            int u, v; cin >> u >> v;
            u--; v--;
            degree[u]++;
            degree[v]++;
        }

        int oddCount = 0;
        for (int d : degree) {
            if (d % 2 == 1) oddCount++;
        }

        // Given G has Euler trail, oddCount is 0 or 2.
        if (k == 0) {
            // L^0(G) = G, which has Euler trail by problem statement
            cout << "YES\n";
        } else if (k == 1) {
            // L(G) has Euler trail iff G is Eulerian (oddCount == 0)
            cout << (oddCount == 0 ? "YES\n" : "NO\n");
        } else {
            // For k >= 2, L^k(G) has Euler trail always
            cout << "YES\n";
        }
    }

    return 0;
}