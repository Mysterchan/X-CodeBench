#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ull = unsigned long long;
using db = double;
using i128 = __int128;
using u128 = unsigned __int128;
#define I return
#define WILL
#define AK 0
#define XCPC ;
#define AL(X) (X).begin() + 1, (X).end()
#define ALL(X) (X).begin(), (X).end()
#define l first
#define r second
int n, m, k, q;
struct DSU
{
    vector<int> f;
    stack<pair<int, int>> sk;
    vector<int> sz;
    DSU(int n)
    {
        f.resize(n);
        sz.resize(n, 1);
        iota(ALL(f), 0);
    }
    int find(int u)
    {
        return (f[u] == u ? u : find(f[u]));
    }
    void merge(int u, int v)
    {
        u = find(u);
        v = find(v);
        if (u == v)
            return;
        if (sz[u] < sz[v])
            swap(u, v);
        sk.push({u, v});
        f[v] = u;
        sz[u] += sz[v];
    }
    void back(int n)
    {
        while (sk.size() > n)
        {
            auto [u, v] = sk.top();
            sk.pop();
            f[v] = v;
            sz[u] -= sz[v];
        }
    }
};
int get(int u, int v)
{
    return (u - 1) * m + v;
}
int sx[] = {0, 0, 1, -1};
int sy[] = {1, -1, 0, 0};
void solve()
{
    cin >> n >> m;
    vector f(n + 1, vector<int>(m + 1));
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            cin >> f[i][j];
        }
    }
    DSU dsu(n * m + 1);
    cin >> q;
    vector<array<int, 7>> query(q);
    vector<int> ans(q);
    for (int i = 0; i < q; i++)
    {
        int x, y, z, x1, y1, z1;
        cin >> x >> y >> z >> x1 >> y1 >> z1;
        query[i] = {x, y, z, x1, y1, z1, i};
    }
    auto dfs = [&](auto &&dfs, int l, int r, vector<array<int, 7>> x)
    {
        int md = (l + r) >> 1;
        if (l == r)
        {
            for (auto [a, b, c, d, e, g, id] : x)
            {
                if (l > max(c, g))
                {
                    ans[id] = abs(c - g);
                }
                else
                    ans[id] = abs(c - l) + abs(g - l);
            }
            return;
        }
        int sz = dsu.sk.size();
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= m; j++)
            {
                if (f[i][j] <= md)
                    continue;
                for (int k = 0; k < 4; k++)
                {
                    int u = i + sx[k];
                    int v = j + sy[k];
                    if (u <= 0 || u > n || v <= 0 || v > m || f[u][v] <= md)
                        continue;
                    dsu.merge(get(u, v), get(i, j));
                }
            }
        }
        vector<array<int, 7>> L, R;
        for (int i = 0; i < x.size(); i++)
        {
            auto [a, b, c, d, e, f, id] = x[i];
            if (dsu.find(get(a, b)) == dsu.find(get(d, e)))
            {
                R.push_back({a, b, c, d, e, f, id});
            }
            else
            {
                L.push_back({a, b, c, d, e, f, id});
            }
        }
        vector<array<int, 7>>().swap(x);
        if (L.size() && l <= md)
        {
            dfs(dfs, l, md, L);
        }
        dsu.back(sz);
        if (R.size() && r > md)
        {
            dfs(dfs, md + 1, r, R);
        }
    };
    dfs(dfs, 0, 1e6, query);
    for (int i = 0; i < q; i++)
    {
        cout << ans[i] << "\n";
    }
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int tt = 1;
    while (tt--)
    {
        solve();
    }
    I WILL AK XCPC
}