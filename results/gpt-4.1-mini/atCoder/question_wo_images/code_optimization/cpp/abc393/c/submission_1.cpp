#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    // Use unordered_set to track unique edges efficiently
    // Store edges as pairs (min(u,v), max(u,v)) to handle undirected edges
    unordered_set<long long> seen;
    int to_remove = 0;

    for (int i = 0; i < M; i++) {
        int u, v;
        cin >> u >> v;
        if (u == v) {
            // Self-loop, must remove
            to_remove++;
            continue;
        }
        int a = min(u, v);
        int b = max(u, v);
        long long key = (long long)a * 200000 + b; // 200000 > max N to avoid collisions
        if (seen.count(key)) {
            // Multi-edge, must remove
            to_remove++;
        } else {
            seen.insert(key);
        }
    }

    cout << to_remove << "\n";

    return 0;
}