#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N;
vector<vector<int>> G;

// Returns the size of the largest alkane subtree rooted at 'u' with parent 'p'.
// If p == -1, 'u' is considered the root of the alkane (degree 4).
// Otherwise, 'u' is an internal node or leaf in the alkane.
int dfs(int u, int p) {
    vector<int> child_sizes;
    for (int v : G[u]) {
        if (v == p) continue;
        int res = dfs(v, u);
        if (res != -1) child_sizes.push_back(res);
    }
    sort(child_sizes.rbegin(), child_sizes.rend());

    if (p == -1) {
        // Root node: must have degree 4 in alkane
        if ((int)child_sizes.size() < 4) return -1;
        int prod = 1;
        for (int i = 0; i < 4; i++) prod *= child_sizes[i];
        return prod;
    } else {
        // Non-root node: degree 1 or 4
        // If degree 1 (leaf in alkane), no children included
        if ((int)child_sizes.size() < 3) return 1;
        // If degree 4, include top 3 children
        int prod = 1;
        for (int i = 0; i < 3; i++) prod *= child_sizes[i];
        return prod;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    G.resize(N);
    for (int i = 0; i < N - 1; i++) {
        int a, b; cin >> a >> b; a--; b--;
        G[a].push_back(b);
        G[b].push_back(a);
    }

    int ans = -1;
    // Try each node as root of alkane (degree 4)
    for (int i = 0; i < N; i++) {
        int res = dfs(i, -1);
        if (res > ans) ans = res;
    }

    cout << ans << "\n";
    return 0;
}