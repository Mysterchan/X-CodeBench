#include <bits/stdc++.h>
using namespace std;

int n, m, q;
int f[505][505];
int parent[250005];
int sz[250005];

inline int get(int u, int v) {
    return (u - 1) * m + v;
}

int find(int u) {
    if (parent[u] != u) parent[u] = find(parent[u]);
    return parent[u];
}

void merge(int u, int v) {
    u = find(u);
    v = find(v);
    if (u == v) return;
    if (sz[u] < sz[v]) swap(u, v);
    parent[v] = u;
    sz[u] += sz[v];
}

void reset(int total) {
    for (int i = 0; i < total; i++) {
        parent[i] = i;
        sz[i] = 1;
    }
}

int sx[] = {0, 0, 1, -1};
int sy[] = {1, -1, 0, 0};

struct Query {
    int a, b, c, d, e, g, id;
};

void solve() {
    cin >> n >> m;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            cin >> f[i][j];
        }
    }
    
    cin >> q;
    vector<Query> queries(q);
    vector<int> ans(q);
    
    for (int i = 0; i < q; i++) {
        cin >> queries[i].a >> queries[i].b >> queries[i].c 
            >> queries[i].d >> queries[i].e >> queries[i].g;
        queries[i].id = i;
    }
    
    function<void(int, int, vector<Query>&)> dfs = [&](int l, int r, vector<Query>& x) {
        if (x.empty()) return;
        
        int md = (l + r) >> 1;
        
        if (l == r) {
            for (auto& q : x) {
                if (l > max(q.c, q.g)) {
                    ans[q.id] = abs(q.c - q.g);
                } else {
                    ans[q.id] = abs(q.c - l) + abs(q.g - l);
                }
            }
            return;
        }
        
        reset(n * m + 1);
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (f[i][j] <= md) continue;
                
                for (int k = 0; k < 4; k++) {
                    int u = i + sx[k];
                    int v = j + sy[k];
                    if (u >= 1 && u <= n && v >= 1 && v <= m && f[u][v] > md) {
                        merge(get(u, v), get(i, j));
                    }
                }
            }
        }
        
        vector<Query> L, R;
        L.reserve(x.size());
        R.reserve(x.size());
        
        for (auto& q : x) {
            if (find(get(q.a, q.b)) == find(get(q.d, q.e))) {
                R.push_back(q);
            } else {
                L.push_back(q);
            }
        }
        
        if (!L.empty() && l <= md) {
            dfs(l, md, L);
        }
        if (!R.empty() && r > md) {
            dfs(md + 1, r, R);
        }
    };
    
    dfs(0, 1000000, queries);
    
    for (int i = 0; i < q; i++) {
        cout << ans[i] << "\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    solve();
    
    return 0;
}