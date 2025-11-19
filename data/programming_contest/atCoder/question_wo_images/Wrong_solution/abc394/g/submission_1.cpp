#include <bits/stdc++.h>
#define int long long
#define N 501
#define M 500005
#define mod 998244353
#define all(a) a.begin(),a.end()
#define uniqueu(a) a.erase(unique(all(a)), a.end())
using namespace std;
mt19937_64 mrand(random_device{}());

int h, w, q;
int F[N][N], id[N][N], f[M][31], dist[M], dep[M];
int cnt, len;

struct Edge {
    int u, v, w;
    bool operator < (const Edge &A) const {
        return w > A.w;
    }
} adj[M];

vector<int> edges[M];

struct DSU {
    int fa[20 * M];
    int find(int x) {
        return fa[x] == x ? x : fa[x] = find(fa[x]);
    }
    inline void merge(int x, int y, int w) {
        int fx = find(x), fy = find(y);
        if (fx == fy)
            return;
        cnt++;
        fa[cnt] = cnt;
        edges[cnt].push_back(fx);
        edges[cnt].push_back(fy);
        fa[fx] = fa[fy] = cnt;
        dist[cnt] = min(dist[cnt], w);
    }
} dsu;

inline void dfs(int p, int fa) {
    dep[p] = dep[fa] + 1;
    f[p][0] = fa;
    for (int i = 1; i <= 30; i++)
        f[p][i] = f[f[p][i - 1]][i - 1];
    for (auto &i : edges[p])
        dfs(i, p);
}

int LCA(int u, int v) {
    if (dep[u] < dep[v])
        swap(u, v);
    int c = dep[u] - dep[v];
    for (int i = 0; c; c /= 2, i++)
        if (c & 1)
            u = f[u][i];
    if (u == v)
        return u;
    for (int i = 30; i; i--)
        if (f[u][i] != f[v][i]) {
            u = f[u][i];
            v = f[v][i];
        }
    return f[u][0];
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    cin >> h >> w;
    for (int i = 1; i <= h; i++)
        for (int j = 1; j <= w; j++) {
            cin >> F[i][j];
            id[i][j] = ++cnt;
            if (i - 1 >= 1) {
                adj[++len].u = id[i][j];
                adj[len].v = id[i - 1][j];
                adj[len].w = min(F[i][j], F[i - 1][j]);
            }
            if (j - 1 >= 1) {
                adj[++len].u = id[i][j];
                adj[len].v = id[i][j - 1];
                adj[len].w = min(F[i][j], F[i][j - 1]);
            }
        }
    sort(adj + 1, adj + len + 1);
    for (int i = 1; i <= cnt; i++) {
        dsu.fa[i] = i;
        dist[i] = LONG_LONG_MAX;
    }
    for (int i = 1; i <= len; i++)
        dsu.merge(adj[i].u, adj[i].v, adj[i].w);
    dfs(cnt, 0);
    cin >> q;
    for ( ; q--; ) {
        int a, b, y, c, d, z;
        cin >> a >> b >> y >> c >> d >> z;
        if (a == c && b == d) {
            cout << abs(y - z) << "\n";
            continue;
        }
        int u = id[a][b], v = id[c][d];
        int lca = LCA(u, v);
        lca = min({dist[lca], 1ll * y, 1ll * z});
        cout << abs(y - lca) + abs(z - lca) << "\n";
    }
}