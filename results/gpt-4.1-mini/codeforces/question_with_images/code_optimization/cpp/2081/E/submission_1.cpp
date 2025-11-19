#include <bits/stdc++.h>
using namespace std;
const int N = 5005, mod = 998244353;

int fac[N], inv[N];
int n, m;
int fa[N], col[N], lim[N];
vector<int> G[N];
int sc[N][2];
int f[N][2][N], g[N][2], sf[N][2], se[N][2];
int si[N][2], sz[N];

inline int inc(int a, int b) {
    a += b;
    return a >= mod ? a - mod : a;
}
inline int mul(int a, int b) {
    return (int)((long long)a * b % mod);
}
int powe(int a, int b) {
    int res = 1;
    while (b) {
        if (b & 1) res = mul(res, a);
        a = mul(a, a);
        b >>= 1;
    }
    return res;
}
int C(int n, int m) {
    if (n < 0 || m < 0 || n < m) return 0;
    return mul(fac[n], mul(inv[m], inv[n - m]));
}
int P(int a, int b) {
    return C(a + b, b);
}

void DFS(int u) {
    for (int e : G[u]) {
        DFS(e);
        if (!sz[e]) {
            for (int i = 1; i <= sz[e]; i++) {
                f[u][0][i] = f[e][0][i];
                f[u][1][i] = f[e][1][i];
            }
            sz[u] += sz[e];
            si[u][0] += si[e][0];
            si[u][1] += si[e][1];
            continue;
        }
        int maxsz = sz[u] + sz[e] + 1;
        for (int i = 0; i <= maxsz; i++) {
            sf[i][0] = sf[i][1] = se[i][0] = se[i][1] = g[i][0] = g[i][1] = 0;
        }
        for (int i = sz[u]; i >= 0; i--) {
            sf[i][0] = inc(sf[i + 1][0], f[u][0][i]);
            sf[i][1] = inc(sf[i + 1][1], f[u][1][i]);
        }
        for (int i = sz[e]; i >= 0; i--) {
            se[i][0] = inc(se[i + 1][0], f[e][0][i]);
            se[i][1] = inc(se[i + 1][1], f[e][1][i]);
        }
        int S[2] = {0, 0}, H[2] = {0, 0};
        for (int i = 1; i <= sz[e]; i++) {
            S[0] = inc(S[0], f[e][0][i]);
            S[1] = inc(S[1], f[e][1][i]);
        }
        for (int i = 1; i <= sz[u]; i++) {
            H[0] = inc(H[0], f[u][0][i]);
            H[1] = inc(H[1], f[u][1][i]);
        }
        for (int i = 1; i <= sz[u]; i++) {
            for (int c = 0; c <= 1; c++) {
                g[i][c] = inc(g[i][c], mul(mul(S[c ^ 1], P(sz[u] - i, sz[e] - 1)), sf[i + 1][c]));
                g[i][c] = inc(g[i][c], mul(S[c ^ 1], mul(P(sz[u] - i, sz[e]), f[u][c][i])));
            }
        }
        for (int i = 1; i <= sz[e]; i++) {
            for (int c = 0; c <= 1; c++) {
                g[i][c] = inc(g[i][c], mul(H[c ^ 1], mul(P(sz[e] - i, sz[u] - 1), se[i + 1][c])));
                g[i][c] = inc(g[i][c], mul(H[c ^ 1], mul(P(sz[e] - i, sz[u]), f[e][c][i])));
            }
        }
        for (int c = 0; c <= 1; c++) {
            bool flg = false;
            if (si[e][c ^ 1]) {
                flg = true;
                for (int i = 0; i <= sz[u]; i++) {
                    for (int j = 1; j <= sz[e] - 1; j++) {
                        g[i + j][c] = inc(g[i + j][c], mul(mul(sf[i][c], f[e][c][j]), mul(P(i, j), P(sz[u] - i, sz[e] - j - 1))));
                    }
                }
            }
            if (si[u][c ^ 1]) {
                flg = true;
                for (int i = 1; i <= sz[u] - 1; i++) {
                    for (int j = 0; j <= sz[e]; j++) {
                        g[i + j][c] = inc(g[i + j][c], mul(mul(f[u][c][i], se[j][c]), mul(P(i, j), P(sz[u] - i - 1, sz[e] - j))));
                    }
                }
            }
            if (!flg) {
                int x = si[u][c] + si[e][c];
                if (x) g[x][c] = inc(g[x][c], fac[x]);
            }
        }
        sz[u] += sz[e];
        si[u][0] += si[e][0];
        si[u][1] += si[e][1];
        for (int c = 0; c <= 1; c++) {
            for (int i = 1; i <= sz[u]; i++) {
                f[u][c][i] = g[i][c];
            }
        }
    }
    // Add chips at node u
    int ps = (int)G[u].size();
    if (ps) {
        int it = G[u][0], now = 0, fc = 1;
        while (now < ps && G[u][now] == it) now++;
        for (int j = 0; j < ps;) {
            int p = j, ct = 1;
            while (p + 1 < ps && G[u][p + 1] == G[u][j]) p++, ct++;
            fc = mul(fc, fac[ct]);
            j = p + 1;
        }
        if (sz[u] == 0) {
            f[u][it][now] = fc;
        } else {
            int ln = 0, pos = ps - 1;
            while (pos >= 0 && G[u].back() == G[u][pos]) ln++, pos--;
            for (int i = 0; i <= sz[u] + ps; i++) g[i][0] = g[i][1] = 0;
            for (int c = 0; c <= 1; c++) {
                if (G[u].back() == c) {
                    for (int i = 1; i <= sz[u]; i++) {
                        if (ps == ln && f[u][c][i]) g[ln + i][it] = inc(g[ln + i][it], mul(fc, mul(P(ln, i), f[u][c][i])));
                        else g[now][it] = inc(g[now][it], mul(fc, mul(P(ln, i), f[u][c][i])));
                    }
                } else {
                    for (int i = 1; i <= sz[u]; i++) g[now][it] = inc(g[now][it], mul(fc, f[u][c][i]));
                }
            }
            for (int i = 1; i <= sz[u] + ps; i++) {
                f[u][0][i] = g[i][0];
                f[u][1][i] = g[i][1];
            }
        }
    }
    for (int c : G[u]) {
        sz[u]++;
        si[u][c]++;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    fac[0] = inv[0] = 1;
    for (int i = 1; i < N; i++) fac[i] = mul(fac[i - 1], i);
    inv[N - 1] = powe(fac[N - 1], mod - 2);
    for (int i = N - 2; i >= 1; i--) inv[i] = mul(inv[i + 1], i + 1);

    int T; cin >> T;
    while (T--) {
        cin >> n >> m;
        for (int i = 0; i <= max(n, m); i++) {
            G[i].clear();
            sz[i] = 0;
            si[i][0] = si[i][1] = 0;
            sc[i][0] = sc[i][1] = 0;
            for (int c = 0; c <= 1; c++) {
                for (int j = 0; j <= m; j++) f[i][c][j] = 0;
            }
        }
        for (int i = 1; i <= n; i++) cin >> fa[i];
        for (int i = 1; i <= n; i++) if (fa[i]) G[fa[i]].push_back(i);
        for (int i = 1; i <= m; i++) cin >> col[i];
        for (int i = 1; i <= m; i++) cin >> lim[i];

        // Assign chips to nodes with pruning
        static int st[N];
        for (int i = m; i >= 1; i--) {
            int u = lim[i], C = col[i], tp = 0;
            while (u) st[++tp] = u, u = fa[u];
            bool flg = false;
            for (int j = tp; j >= 2; j--) {
                u = st[j];
                if ((sc[u][0] && C == 1) || (sc[u][1] && C == 0)) {
                    flg = true;
                    break;
                }
            }
            u = st[1];
            G[u].push_back(i);
            sc[u][C]++;
        }

        for (int i = 1; i <= n; i++) {
            if (G[i].empty()) continue;
            sort(G[i].begin(), G[i].end());
            for (int &x : G[i]) x = col[x];
        }

        DFS(1);

        int ans = 0;
        for (int i = 1; i <= m; i++) {
            ans = inc(ans, f[1][0][i]);
            ans = inc(ans, f[1][1][i]);
        }
        cout << ans << "\n";
    }
    return 0;
}