#include <bits/stdc++.h>
using namespace std;

const int MAXN = 70005;
const int MAXLOG = 17;
const int INF = 1e9;

int n, t;
char s[MAXN];
vector<int> g[MAXN];
int f[MAXN][MAXLOG + 1];
int sz[MAXN], p[MAXN], tcnt;
bool vist[MAXN];
int dep[MAXN], vc[MAXN], kcnt;

int M = 100000; // segment tree max index

// Segment tree for max queries and updates
struct SegTree {
    int n;
    vector<int> tree;
    SegTree(int size) : n(size) {
        tree.assign(4 * n, -INF);
    }
    void update(int idx, int val, int v=1, int tl=0, int tr=-1) {
        if (tr == -1) tr = n - 1;
        if (tl == tr) {
            tree[v] = max(tree[v], val);
            return;
        }
        int tm = (tl + tr) >> 1;
        if (idx <= tm) update(idx, val, v << 1, tl, tm);
        else update(idx, val, v << 1 | 1, tm + 1, tr);
        tree[v] = max(tree[v << 1], tree[v << 1 | 1]);
    }
    void clear(int idx, int v=1, int tl=0, int tr=-1) {
        if (tr == -1) tr = n - 1;
        if (tl == tr) {
            tree[v] = -INF;
            return;
        }
        int tm = (tl + tr) >> 1;
        if (idx <= tm) clear(idx, v << 1, tl, tm);
        else clear(idx, v << 1 | 1, tm + 1, tr);
        tree[v] = max(tree[v << 1], tree[v << 1 | 1]);
    }
    int query(int l, int r, int v=1, int tl=0, int tr=-1) {
        if (tr == -1) tr = n - 1;
        if (l > r) return -INF;
        if (l <= tl && tr <= r) return tree[v];
        int tm = (tl + tr) >> 1;
        int res = -INF;
        if (l <= tm) res = max(res, query(l, r, v << 1, tl, tm));
        if (r > tm) res = max(res, query(l, r, v << 1 | 1, tm + 1, tr));
        return res;
    }
};

SegTree seg(M + 1);

// DFS to get subtree sizes and order for centroid decomposition
void dfs0(int x, int p_) {
    p[++tcnt] = x;
    sz[x] = 1;
    for (auto &nx : g[x]) {
        if (nx == p_ || vist[nx]) continue;
        dfs0(nx, x);
        sz[x] += sz[nx];
    }
}

// DFS to compute depths from centroid root
void dfs1(int x, int p_) {
    for (auto &nx : g[x]) {
        if (nx == p_ || vist[nx]) continue;
        dep[nx] = dep[x] + 1;
        dfs1(nx, x);
    }
}

// DFS to collect nodes in a subtree for processing
void dfs2(int x, int p_) {
    vc[++kcnt] = x;
    for (auto &nx : g[x]) {
        if (nx == p_ || vist[nx]) continue;
        dfs2(nx, x);
    }
}

// Add value to segment tree if index >= 0
inline void seg_add(int x, int y) {
    if (x >= 0) seg.update(x, y);
}

// Remove value from segment tree (reset to -INF)
inline void seg_remove(int x) {
    if (x >= 0) seg.clear(x);
}

void solve(int x, int j) {
    tcnt = 0;
    dfs0(x, 0);
    int total = tcnt;
    int centroid = -1;
    for (int i = 1; i <= total; i++) {
        int y = p[i];
        int mx = 0;
        for (auto &nx : g[y]) {
            if (vist[nx]) continue;
            if (sz[nx] > sz[y]) mx = max(mx, total - sz[y]);
            else mx = max(mx, sz[nx]);
        }
        if (mx <= total / 2) {
            centroid = y;
            break;
        }
    }
    dep[centroid] = 0;
    dfs1(centroid, 0);

    // Insert centroid itself
    seg_add(f[centroid][j - 1] / 2 - dep[centroid], dep[centroid]);

    // Process subtrees of centroid
    for (auto &nx : g[centroid]) {
        if (vist[nx]) continue;
        kcnt = 0;
        dfs2(nx, centroid);
        for (int i = 1; i <= kcnt; i++) {
            int z = vc[i];
            int ql = dep[z];
            int qr = M;
            int val = seg.query(ql, qr);
            if (val != -INF) {
                f[z][j] = max(f[z][j], dep[z] + val);
            }
        }
        for (int i = 1; i <= kcnt; i++) {
            int z = vc[i];
            seg_add(f[z][j - 1] / 2 - dep[z], dep[z]);
        }
    }

    // Remove centroid itself
    seg_remove(f[centroid][j - 1] / 2 - dep[centroid]);

    // Remove subtree contributions
    for (auto &nx : g[centroid]) {
        if (vist[nx]) continue;
        kcnt = 0;
        dfs2(nx, centroid);
        for (int i = 1; i <= kcnt; i++) {
            int z = vc[i];
            seg_remove(f[z][j - 1] / 2 - dep[z]);
        }
    }

    // Reverse order to consider paths in opposite direction
    reverse(g[centroid].begin(), g[centroid].end());

    for (auto &nx : g[centroid]) {
        if (vist[nx]) continue;
        kcnt = 0;
        dfs2(nx, centroid);
        for (int i = 1; i <= kcnt; i++) {
            int z = vc[i];
            int ql = dep[z];
            int qr = M;
            int val = seg.query(ql, qr);
            if (val != -INF) {
                f[z][j] = max(f[z][j], dep[z] + val);
            }
        }
        for (int i = 1; i <= kcnt; i++) {
            int z = vc[i];
            seg_add(f[z][j - 1] / 2 - dep[z], dep[z]);
        }
    }

    f[centroid][j] = max(f[centroid][j], dep[centroid] + seg.query(dep[centroid], M));
    seg_remove(f[centroid][j - 1] / 2 - dep[centroid]);

    for (auto &nx : g[centroid]) {
        if (vist[nx]) continue;
        kcnt = 0;
        dfs2(nx, centroid);
        for (int i = 1; i <= kcnt; i++) {
            int z = vc[i];
            seg_remove(f[z][j - 1] / 2 - dep[z]);
        }
    }

    vist[centroid] = true;
    for (auto &nx : g[centroid]) {
        if (!vist[nx]) solve(nx, j);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;
    seg = SegTree(M + 1);

    while (T--) {
        cin >> n;
        cin >> (s + 1);
        for (int i = 1; i <= n; i++) {
            g[i].clear();
            for (int j = 0; j <= MAXLOG; j++) f[i][j] = 0;
            vist[i] = false;
        }
        for (int i = 1; i < n; i++) {
            int u, v; cin >> u >> v;
            g[u].push_back(v);
            g[v].push_back(u);
        }

        // Initialize f[i][0]
        for (int i = 1; i <= n; i++) {
            if (s[i] == '1') f[i][0] = 2 * n;
            else f[i][0] = 0;
        }

        for (int j = 1; j <= MAXLOG; j++) {
            for (int i = 1; i <= n; i++) vist[i] = false;
            solve(1, j);
            for (int i = 1; i <= n; i++) {
                if (s[i] == '0') f[i][j] = 0;
            }
        }

        for (int i = 1; i <= n; i++) {
            if (s[i] == '0') {
                cout << -1 << " ";
            } else {
                int res = MAXLOG + 1;
                for (int j = 0; j <= MAXLOG; j++) {
                    if (f[i][j] == 0) {
                        res = j;
                        break;
                    }
                }
                cout << res << " ";
            }
        }
        cout << "\n";
    }

    return 0;
}