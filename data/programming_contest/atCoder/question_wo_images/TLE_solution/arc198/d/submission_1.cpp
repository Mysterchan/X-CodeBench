#include <bits/stdc++.h>
using namespace std;
#ifdef tabr
#include "library/debug.cpp"
#else
#define debug(...)
#endif

struct dsu {
    vector<int> p;
    vector<int> sz;
    int n;

    dsu(int _n) : n(_n) {
        p = vector<int>(n);
        iota(p.begin(), p.end(), 0);
        sz = vector<int>(n, 1);
    }

    inline int get(int x) {
        if (p[x] == x) {
            return x;
        } else {
            return p[x] = get(p[x]);
        }
    }

    inline bool unite(int x, int y) {
        x = get(x);
        y = get(y);
        if (x == y) {
            return false;
        }
        p[x] = y;
        sz[y] += sz[x];
        return true;
    }

    inline bool same(int x, int y) {
        return (get(x) == get(y));
    }

    inline int size(int x) {
        return sz[get(x)];
    }

    inline bool root(int x) {
        return (x == get(x));
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
        x--;
        y--;
        g[x].emplace_back(y);
        g[y].emplace_back(x);
    }
    vector<string> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    dsu uf(n);
    {
        vector<vector<int>> d(n, vector<int>(n));
        vector<vector<int>> p(n, vector<int>(n, -1));
        function<void(int, int)> dfs = [&](int v, int r) {
            for (int to : g[v]) {
                if (to == p[r][v]) {
                    continue;
                }
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
            f[e].resize(unique(f[e].begin(), f[e].end()) - f[e].begin());
            for (auto [x, y] : f[e]) {
                uf.unite(x, y);
                if (e - 2 >= 0) {
                    int px = p[y][x];
                    int py = p[x][y];
                    f[e - 2].emplace_back(minmax(px, py));
                }
            }
        }
    }
    int ans = 0;
    auto search2 = [&](int i, int j) {
        deque<vector<tuple<int, int, int>>> d;
        if (j == -1) {
            vector<tuple<int, int, int>> f;
            f.emplace_back(i, -1, -1);
            d.emplace_back(f);
        } else {
            if (uf.get(i) != uf.get(j)) {
                return;
            }
            vector<tuple<int, int, int>> f;
            f.emplace_back(i, j, i);
            f.emplace_back(j, i, j);
            d.emplace_back(f);
        }
        while (!d.empty()) {
            auto f = d.front();
            d.pop_front();
            int sz = int(f.size());
            vector<tuple<int, int, int, int>> nf;
            for (int x = 0; x < sz; x++) {
                auto [xv, xp, xr] = f[x];
                for (int to : g[xv]) {
                    if (to == xp) {
                        continue;
                    }
                    nf.emplace_back(uf.get(to), to, xv, xr == -1 ? to : xr);
                }
                for (int y = x + 1; y < sz; y++) {
                    auto [yv, yp, yr] = f[y];
                    if (xr != yr) {
                        ans++;
                    }
                }
            }
            sort(nf.begin(), nf.end());
            sz = int(nf.size());
            for (int x = 0, y = 0; x < sz; x = y) {
                while (y < sz && get<0>(nf[x]) == get<0>(nf[y])) {
                    y++;
                }
                vector<tuple<int, int, int>> e;
                for (int z = x; z < y; z++) {
                    e.emplace_back(get<1>(nf[z]), get<2>(nf[z]), get<3>(nf[z]));
                }
                d.emplace_back(e);
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