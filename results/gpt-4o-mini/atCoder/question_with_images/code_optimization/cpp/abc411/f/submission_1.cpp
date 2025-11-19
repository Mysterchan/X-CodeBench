#include <bits/stdc++.h>
#define pii pair<int, int>
using namespace std;

const int MAX = 300007;
vector<int> G[MAX];
pii E[MAX];

struct UnionFind {
    int parent[MAX], size[MAX];
    UnionFind() {
        iota(parent, parent + MAX, 0);
        fill(size, size + MAX, 1);
    }

    int Find(int x) {
        if (parent[x] != x) {
            parent[x] = Find(parent[x]);
        }
        return parent[x];
    }

    void Union(int x, int y) {
        x = Find(x);
        y = Find(y);
        if (x != y) {
            if (size[x] < size[y]) swap(x, y);
            parent[y] = x;
            size[x] += size[y];
        }
    }
} uf;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, M, Q;
    cin >> N >> M;

    unordered_map<int, unordered_set<int>> adj;

    for (int i = 1; i <= M; ++i) {
        int a, b;
        cin >> a >> b;
        E[i] = {a, b};
        adj[a].insert(b);
        adj[b].insert(a);
    }

    cin >> Q;
    int edgeCount = M;

    while (Q--) {
        int en;
        cin >> en;
        int a = E[en].first, b = E[en].second;

        int rootA = uf.Find(a), rootB = uf.Find(b);

        if (rootA != rootB) {
            if (adj[rootA].size() < adj[rootB].size()) {
                swap(rootA, rootB);
            }

            uf.Union(rootA, rootB);

            for (int neighbor : adj[rootB]) {
                if (neighbor != rootA) {
                    if (adj[rootA].insert(neighbor).second) { // Only add if it was not already present
                        edgeCount++;
                    }
                }
            }

            adj[rootB].clear();
            edgeCount -= (adj[rootB].size() + 1);
        }

        cout << edgeCount << '\n';
    }
    
    return 0;
}