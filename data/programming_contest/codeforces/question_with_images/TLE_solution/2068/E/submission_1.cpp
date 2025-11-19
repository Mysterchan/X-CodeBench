
#ifdef DEBUG
#include "debug.hpp"
#elif DeBuG
#include "debug.h"
#else
#include "bits/stdc++.h"
#define dbg(...)
#endif

using namespace std;

#define rep(i, a, b) for (int i = (a); i < (b); ++i)
#define all(a) begin(a), end(a)
#define sz(a) int(size(a))

using ll = long long; using vi = vector<int>;
using pii = pair<int,int>; using pll = pair<ll,ll>;

template<class T> using V = vector<T>;

const int MX = 2e5;

int n, m;
vector<int> G[MX + 1];

int dist0[MX + 1], dist1[MX + 1], level[MX + 1];

void bfs (int source, int dist[MX + 1], int cost_bound) {
    fill(dist + 1, dist + (1 + n), -1);
    queue<int> q;

    dist[source] = 0;
    q.push(source);

    while (!q.empty()) {
        int u = q.front(); q.pop();
        if (dist1[u] == -1) continue;
        for (int v : G[u]) {
            if (dist[v] != -1) continue;
            if (cost_bound != -1 && dist[u]+dist1[u] > cost_bound) continue;
            dist[v] = 1 + dist[u];
            q.push(v);
        }
    }
}

bool visited[MX + 1];
set<int> sub[MX + 1];
set<pair<int,int>> back_edges[MX + 1];

void dfs (int u, int p = -1) {
    sub[u].insert(u);
    for (int v : G[u]) if (v != p)
        back_edges[u].emplace(dist0[u] + dist0[v], v);

    for (int v : G[u]) {
        if (visited[v] || dist0[v] != dist0[u] + 1) continue;

        dfs(v, u);

        if (sz(sub[u]) < sz(sub[v])) sub[u].swap(sub[v]);
        sub[u].merge(sub[v]); // test

        if (sz(back_edges[u]) < sz(back_edges[v])) back_edges[u].swap(back_edges[v]);
        back_edges[u].merge(back_edges[v]);
    }

    while (sz(back_edges[u]) && sub[u].count(back_edges[u].begin()->second))
        back_edges[u].erase(back_edges[u].begin());

    if (!sz(back_edges[u])) return;

    ll cost = back_edges[u].begin()->first + 1 - dist0[u];

    if (dist1[u] == -1 || dist1[u] > cost)
        dist1[u] = cost;
}

void build_dist1 () {
    vector<pair<int,int>> vertices(n);
    rep (i, 0, n - 1) vertices[i] = {dist0[i+1], i+1};
    sort(all(vertices));
    reverse(all(vertices));

    fill(dist1 + 1, dist1 + (n + 1), -1);
    dist1[n] = 0;
    for (auto [d, u] : vertices) {
        if (dist0[u] == -1) continue;

        int v_u = -1;
        for (int v : G[u]) {
            if (dist0[v] != dist0[u] - 1) continue;
            v_u = v;
            break;
        }

        for (int v : G[u]) {
            if (v == v_u || dist0[v] == -1) continue;

            if (dist0[v] == dist0[u] - 1) {
                dist1[u] = dist0[u];
                break;
            } else if (dist0[v] == dist0[u]) {
                dist1[u] = 1 + dist0[v];
            } else if (dist1[v] != -1 && (dist1[u] == -1 || dist1[u] > 1 + dist1[v])) {
                dist1[u] = 1 + dist1[v];
            }
        }
    }

    fill(visited + 1, visited + (1 + n), false);
    fill(sub + 1, sub + (1 + n), set<int>());
    fill(back_edges + 1, back_edges + (1 + n), set<pair<int,int>>());
    dfs(n);
}

int solve () {
    bfs(n, dist0, -1);

    build_dist1();

    int lo = 1, hi = 3 * n;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        bfs(1, level, mid);
        if (level[n] != -1) hi = mid;
        else lo = mid + 1;
    }

    return lo == 3 * n ? -1 : lo;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    while (cin >> n >> m) {
        fill(G + 1, G + (1 + n), vector<int>());
        rep (i, 0, m) {
            int u, v; cin >> u >> v;
            G[u].push_back(v);
            G[v].push_back(u);
        }

        cout << solve() << "\n";
    }
}
