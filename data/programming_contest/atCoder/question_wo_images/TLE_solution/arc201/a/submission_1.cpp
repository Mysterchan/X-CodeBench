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
struct e
{
    int v;
    ll w;
    int id;
};
struct D
{
    vector<vector<e>> edge;
    vector<int> dis;
    vector<int> cur;
    int s, t;
    ll maxflow;
    D(int n)
    {
        edge.resize(n);
        dis.resize(n);
        cur.resize(n);
        maxflow = 1e9;
    }
    void add_edge(int u, int v, ll w)
    {
        int su = edge[u].size();
        int sv = edge[v].size();
        edge[u].push_back({v, w, sv});
        edge[v].push_back({u, 0, su});
    }
    int bfs()
    {
        queue<int> q;
        fill(ALL(dis), 0);
        q.push(s);
        dis[s] = 1;
        while (q.size())
        {
            auto u = q.front();
            q.pop();
            for (auto &[v, w, id] : edge[u])
            {
                if (w && dis[v] == 0)
                {
                    dis[v] = dis[u] + 1;
                    q.push(v);
                }
            }
        }
        fill(ALL(cur), 0);
        return dis[t] != 0;
    }
    ll dfs(int u, ll flow)
    {
        if (u == t || !flow)
            return flow;
        ll rest = flow;
        for (int i = cur[u]; i < edge[u].size(); i++)
        {
            cur[u] = i;
            auto &[v, w, id] = edge[u][i];
            if (dis[v] == dis[u] + 1 && w)
            {
                ll t = dfs(v, min(w, flow));
                if (t)
                {
                    w -= t;
                    edge[v][id].w += t;
                    return t;
                }
                else
                    dis[v] = 0;
            }
        }
        return 0;
    }
    ll dinic()
    {
        ll ans = 0;
        while (bfs())
        {
            ll d = 0;
            while (d = dfs(s, maxflow))
            {
                ans += d;
            }
        }
        return ans;
    }
};
void solve()
{
    cin >> n;
    vector<int> a(n + 1), b(n + 1), c(n + 1);
    ll sum = 0;
    for (int i = 1; i <= n; i++)
    {
        cin >> a[i] >> b[i] >> c[i];
        sum += b[i];
    }
    ll l = 0, r = sum;
    auto check = [&](ll u)
    {
        D d(n + 5);
        d.s = 1;
        d.t = n + 4;
        for (int i = 1; i <= n; i++)
        {
            d.add_edge(1, i + 1, b[i]);
            d.add_edge(i + 1, n + 2, a[i]);
            d.add_edge(i + 1, n + 3, c[i]);
        }
        d.add_edge(n + 2, n + 4, u);
        d.add_edge(n + 3, n + 4, u);
        return d.dinic() == u * 2;
    };
    while (l < r)
    {
        ll md = (l + r + 1) >> 1;
        if (check(md))
        {
            l = md;
        }
        else
        {
            r = md - 1;
        }
    }
    cout << l << "\n";
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int tt = 1;
    cin >> tt;
    while (tt--)
    {
        solve();
    }
    I WILL AK XCPC
}