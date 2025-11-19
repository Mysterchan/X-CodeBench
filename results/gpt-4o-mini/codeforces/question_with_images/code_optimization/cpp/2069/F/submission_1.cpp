#include <bits/stdc++.h>
using namespace std;

const int mxN = 4e5;
int n, q;

struct UnionFind {
    vector<int> parent, rank;

    UnionFind(int size) {
        parent.resize(size);
        rank.resize(size, 0);
        iota(parent.begin(), parent.end(), 0);
    }

    int find(int x) {
        return (x == parent[x]) ? x : parent[x] = find(parent[x]);
    }

    bool unite(int x, int y) {
        x = find(x), y = find(y);
        if (x == y) return false;

        if (rank[x] < rank[y])
            swap(x, y);
        parent[y] = x;
        if (rank[x] == rank[y])
            rank[x]++;
        return true;
    }
};

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    cin >> n >> q;
    
    vector<bool> addedA(n * n, false), addedB(n * n, false);
    UnionFind ufA(n), ufB(n), ufDB(n);
    
    auto edgeHash = [&](int x, int y) {
        return x * n + y;  // unique hash for vertices
    };
    
    int componentCountA = 0, componentCountB = 0;

    for (int i = 0; i < q; ++i) {
        char c;
        int x, y;
        cin >> c >> x >> y;
        --x; --y;
        if (x > y) swap(x, y);
        
        bool isGraphA = (c == 'A');
        int* edgesTracker = isGraphA ? addedA.data() : addedB.data();
        UnionFind& uf = isGraphA ? ufA : ufB;
        UnionFind& ufD = ufDB;

        int edgeIndex = edgeHash(x, y);
        
        if (edgesTracker[edgeIndex]) {
            edgesTracker[edgeIndex] = false;
            uf.unite(x, y);
            if (isGraphA && !ufD.unite(x, y)) {
                componentCountA--;
            } else if (!isGraphA && ufD.unite(x, y)) {
                componentCountB--;
            }
        } else {
            edgesTracker[edgeIndex] = true;
            if (uf.unite(x, y)) {
                if (isGraphA) {
                    componentCountA++;
                } else {
                    componentCountB--;
                }
            }
        }
        
        // Now we calculate the number of edges needed
        int result = max(0, componentCountB - componentCountA);
        cout << result << "\n";
    }
    
    return 0;
}