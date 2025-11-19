#include <bits/stdc++.h>
using namespace std;

struct dsu {
    vector<int> p;
    dsu(int n) : p(n) {
        iota(p.begin(), p.end(), 0);
    }

    int find(int x) {
        return p[x] == x ? x : (p[x] = find(p[x]));
    }

    void unite(int x, int y) {
        p[find(x)] = find(y);
    }

    bool same(int x, int y) {
        return find(x) == find(y);
    }
};

void dfs(int v, int parent, vector<vector<int>>& g, vector<int>& depth, vector<int>& parentArr) {
    for (int to : g[v]) {
        if (to != parent) {
            depth[to] = depth[v] + 1;
            parentArr[to] = v;
            dfs(to, v, g, depth, parentArr);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;

    vector<vector<int>> g(n);
    for (int i = 0; i < n - 1; i++) {
        int x, y;
        cin >> x >> y;
        x--; y--;
        g[x].emplace_back(y);
        g[y].emplace_back(x);
    }

    vector<string> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    dsu uf(n);
    
    vector<vector<int>> depth(n, vector<int>(n));
    vector<vector<int>> parent(n, vector<int>(n, -1));

    for (int i = 0; i < n; i++) {
        depth[i] = vector<int>(n, 0);
        parent[i][i] = -1;
        dfs(i, -1, g, depth[i], parent[i]);
    }

    vector<vector<pair<int, int>>> edges(n);
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (a[i][j] == '1') {
                edges[depth[i][j]].emplace_back(i, j);
            }
        }
    }
    
    for (int e = n - 1; e >= 0; e--) {
        sort(edges[e].begin(), edges[e].end());
        edges[e].erase(unique(edges[e].begin(), edges[e].end()), edges[e].end());
        for (auto [x, y] : edges[e]) {
            uf.unite(x, y);
            if (e - 2 >= 0) {
                int px = parent[y][x];
                int py = parent[x][y];
                edges[e - 2].emplace_back(min(px, py), max(px, py));
            }
        }
    }

    int ans = 0;
    
    auto search = [&](int i, int j) {
        vector<int> distinctVertices;
        if (j == -1) {
            distinctVertices = {i};
        } else {
            if (uf.same(i, j)) {
                distinctVertices = {i, j};
            } else {
                return;
            }
        }
        vector<pair<int, int>> visited;
        for (int x : distinctVertices) {
            for (int to : g[x]) {
                if (to != j) {
                    visited.emplace_back(uf.find(to), x);
                }
            }
        }
        for (size_t p = 0; p < visited.size(); p++) {
            for (size_t q = p + 1; q < visited.size(); q++) {
                if (visited[p].first != visited[q].first) {
                    ans++;
                }
            }
        }
    };

    for (int i = 0; i < n; i++) {
        search(i, -1);
        for (int j : g[i]) {
            if (i < j) {
                search(i, j);
            }
        }
    }
    cout << ans * 2 + n << '\n';
    return 0;
}
