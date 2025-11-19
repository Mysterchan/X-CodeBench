#include<bits/stdc++.h>
using namespace std;
#define rep(i, s, t) for(int i = (s); i <= (t); i ++)
#define per(i, s, t) for(int i = (s); i >= (t); i --)
template<typename T, typename T2>
inline void chmin(T &x, T2 &&y) { x = min(x, y); }
template<typename T, typename T2>
inline void chmax(T &x, T2 &&y) { x = max(x, y); }
typedef long long ll;

const int N = 3005;

struct dsu {
    vector<int> fa, sz;
    int find(int x) { while(x != fa[x]) x = fa[x] = fa[fa[x]]; return x; }
    bool merge(int x, int y)
    {
        x = find(x), y = find(y);
        if(x == y) return 0;
        if(sz[x] > sz[y]) swap(x, y);
        sz[y] += sz[x];
        fa[x] = y;
        return 1;
    }
    void init(int n) { fa.resize(n + 1), sz.resize(n + 1); rep(i, 0, n) fa[i] = i, sz[i] = 1; }
} f;

int n, a[N][N], lc[N][N];
bool g[N][N];
vector<int> e[N];

basic_string<int> path[N], son[N], now;

int dep[N];
int dfn[N], sz[N], fa[N], ts;

void dfs(int x, int fa)
{
    dep[x] = dep[fa] + 1;
    dfn[x] = ++ts, sz[x] = 1, son[x] = {x};
    now.push_back(x);
    path[x] = now; ::fa[x] = fa;
    for(int i : e[x]) if(i != fa)
    {
        dfs(i, x);
        sz[x] += sz[i];
        for(int j : son[x]) for(int k : son[i]) lc[j][k] = lc[k][j] = x;
        son[x] += son[i];
    }
    now.pop_back();
}

void merg(int x, int y)
{
    if(x == y) return;
    if(dep[x] > dep[y]) swap(x, y);
    if(g[x][y]) return;
    g[x][y] = 1;
    int lc = ::lc[x][y];
    if(lc == x)
    {
        merg(path[y][dep[x] + 1], fa[y]);
    }
    else merg(fa[x], fa[y]);
}

int c[N][N];
bool chk(int x, int y)
{
    if(x == y) return 1;
    if(dep[x] > dep[y]) swap(x, y);
    if(c[x][y] != -1) return c[x][y];
    if(f.find(x) != f.find(y)) return c[x][y] = 0;
    c[x][y] = 1;
    int lc = ::lc[x][y];
    if(lc == x)
    {
        return c[x][y] = chk(path[y][dep[x] + 1], fa[y]);
    }
    else return c[x][y] = chk(fa[x], fa[y]);
}

signed main()
{
    ios::sync_with_stdio(0);cin.tie(0);
    cin >> n;
    rep(i, 1, n - 1)
    {
        int x, y; cin >> x >> y;
        e[x].push_back(y);
        e[y].push_back(x);
    }
    dep[0] = -1; dfs(1, 0);
    rep(i, 1, n) rep(j, 1, n) cin >> (char&)a[i][j];
    rep(i, 1, n) g[i][i] = 1;
    f.init(n);
    rep(i, 1, n) rep(j, i + 1, n) if(a[i][j] == '1')
    {
        merg(i, j);
    }
    rep(i, 1, n) rep(j, 1, n) if(g[i][j]) f.merge(i, j);
    int ans = 0;
    memset(c, -1, sizeof c);
    rep(i, 1, n) rep(j, i + 1, n)
    {
        ans += chk(i, j);
    }
    cout << ans * 2 + n;

    return 0;
}