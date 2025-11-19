#include <bits/stdc++.h>
using namespace std;

struct dsu {
    vector<int> p;
    vector<int> sz;
    int n;

    dsu(int _n) : n(_n) {
        p.resize(n);
        iota(p.begin(), p.end(), 0);
        sz.assign(n, 1);
    }

    inline int get(int x) {
        return p[x] == x ? x : (p[x] = get(p[x]));
    }

    inline bool unite(int x, int y) {
        x = get(x);
        y = get(y);
        if (x == y) return false;
        p[x] = y;
        sz[y] += sz[x];
        return true;
    }
};

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
        g[x].push_back(y);
        g[y].push_back(x);
    }
    vector<string> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    dsu uf(n);
    
    vector<vector<int>> d(n, vector<int>(n));
    vector<vector<int>> p(n, vector<int>(n, -1));
    
    function<void(int, int)> dfs = [&](int v, int r) {
        for (int to : g[v]) {
            if (to == p[r][v]) continue;
            p[r][to] = v;
            d[r][to] = d[r][v] + 1;
            dfs(to, r);
        }
    };
    
    for (int i = 0; i < n; i++) {
        dfs(i, i);
    }
    
    vector<vector<pair<int, int>>> f(n);
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (a[i][j] == '1') {
                f[d[i][j]].emplace_back(i, j);
            }
        }
    }
    
    for (int e = n - 1; e >= 0; e--) {
        sort(f[e].begin(), f[e].end());
        f[e].erase(unique(f[e].begin(), f[e].end()), f[e].end());
        for (auto [x, y] : f[e]) {
            uf.unite(x, y);
            if (e >= 2) {
                int px = p[y][x];
                int py = p[x][y];
                f[e - 2].emplace_back(min(px, py), max(px, py));
            }
        }
    }
    
    long long ans = 0;
    
    auto search2 = [&](int i, int j) {
        deque<vector<pair<int, pair<int, int>>>> d;
        if (j == -1) {
            d.push_back({{i, {-1, -1}}});
        } else {
            if (uf.get(i) != uf.get(j)) return;
            d.push_back({{i, {j, i}}, {j, {i, j}}});
        }
        
        while (!d.empty()) {
            auto f = move(d.front());
            d.pop_front();
            int sz = f.size();
            
            for (int x = 0; x < sz; x++) {
                for (int y = x + 1; y < sz; y++) {
                    if (f[x].second.second != f[y].second.second) {
                        ans++;
                    }
                }
            }
            
            vector<tuple<int, int, int, int>> nf;
            nf.reserve(sz * 3);
            
            for (auto& [xv, pp] : f) {
                int xp = pp.first;
                int xr = pp.second;
                for (int to : g[xv]) {
                    if (to != xp) {
                        nf.emplace_back(uf.get(to), to, xv, xr == -1 ? to : xr);
                    }
                }
            }
            
            if (nf.empty()) break;
            
            sort(nf.begin(), nf.end());
            int nsz = nf.size();
            
            for (int x = 0; x < nsz; ) {
                int y = x;
                int grp = get<0>(nf[x]);
                while (y < nsz && get<0>(nf[y]) == grp) y++;
                
                vector<pair<int, pair<int, int>>> e;
                e.reserve(y - x);
                for (int z = x; z < y; z++) {
                    e.push_back({get<1>(nf[z]), {get<2>(nf[z]), get<3>(nf[z])}});
                }
                d.push_back(move(e));
                x = y;
            }
        }
    };
    
    for (int i = 0; i < n; i++) {
        search2(i, -1);
        for (int j : g[i]) {
            if (i < j) {
                search2(i, j);
            }
        }
    }
    
    cout << ans * 2 + n << '\n';
    return 0;
}