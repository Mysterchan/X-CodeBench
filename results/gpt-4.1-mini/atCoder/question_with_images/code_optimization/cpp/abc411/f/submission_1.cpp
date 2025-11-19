#include <bits/stdc++.h>
using namespace std;

struct UF {
    vector<int> parent, size;
    UF(int n) : parent(n), size(n, 1) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int x) {
        while (x != parent[x]) x = parent[x] = parent[parent[x]];
        return x;
    }
    bool unite(int a, int b) {
        a = find(a), b = find(b);
        if (a == b) return false;
        if (size[a] < size[b]) swap(a, b);
        parent[b] = a;
        size[a] += size[b];
        return true;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M; cin >> N >> M;
    vector<int> U(M), V(M);
    for (int i = 0; i < M; i++) {
        cin >> U[i] >> V[i];
        U[i]--; V[i]--;
    }

    int Q; cin >> Q;
    vector<int> X(Q);
    for (int i = 0; i < Q; i++) {
        cin >> X[i];
        X[i]--;
    }

    // DSU for vertices (pieces)
    UF uf(N);

    // For each vertex, store adjacency as unordered_set for O(1) insert/erase
    vector<unordered_set<int>> adj(N);
    for (int i = 0; i < M; i++) {
        adj[U[i]].insert(V[i]);
        adj[V[i]].insert(U[i]);
    }

    int edge_count = M;

    // To merge adjacency sets efficiently, always merge smaller into larger
    auto merge = [&](int a, int b) {
        // a is bigger set, b is smaller set
        // For each neighbor x of b:
        //   - Remove b from adj[x], add a to adj[x] if not present
        //   - Add x to adj[a] if not present
        //   - Adjust edge_count accordingly
        for (int x : adj[b]) {
            if (x == a) {
                // edge between a and b is removed after contraction
                edge_count--;
                continue;
            }
            // Remove b from adj[x]
            adj[x].erase(b);
            // Add a to adj[x] if not present
            if (adj[x].insert(a).second) {
                edge_count++;
            }
            // Add x to adj[a] if not present
            if (adj[a].insert(x).second) {
                edge_count++;
            }
        }
        // Remove b's adjacency set (clear)
        adj[b].clear();
    };

    for (int i = 0; i < Q; i++) {
        int e = X[i];
        int a = uf.find(U[e]);
        int b = uf.find(V[e]);
        if (a != b) {
            // Check if edge exists between a and b
            if (adj[a].count(b)) {
                // Union sets
                if (adj[a].size() < adj[b].size()) swap(a, b);
                uf.parent[b] = a;
                uf.size[a] += uf.size[b];

                // Remove edge between a and b
                adj[a].erase(b);
                adj[b].erase(a);
                edge_count--;

                // Merge adjacency sets
                merge(a, b);
            }
        }
        cout << edge_count << "\n";
    }

    return 0;
}