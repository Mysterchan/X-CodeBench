#ifdef LOCAL
    #include <bits/include_all.h>
#else
    #include <bits/stdc++.h>
    #include <ext/pb_ds/assoc_container.hpp>
    #include <ext/pb_ds/tree_policy.hpp>
#endif

#pragma GCC target ("avx2")
#pragma GCC optimize ("Ofast")
#pragma GCC optimize ("unroll-loops")

#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define int long long

using namespace std;
using namespace __gnu_pbds;

template <typename T> using oset = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;
template <typename T> inline bool umin(T &a, const T &b) { if(a > b) { a = b; return 1; } return 0; }
template <typename T> inline bool umax(T &a, const T &b) { if(a < b) { a = b; return 1; } return 0; }

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

const ll mod = 998244353;
const ll inf = 1e18;
const int MAX = 2e5 + 42;

random_device rd;
mt19937 gen(rd());
uniform_int_distribution<ll> dis(1, inf);

pair<vector<int>, vector<int>> bfs(vector<vector<int>> g, int s, int t) {
    int n = g.size() - 1;

    vector<int> d(n + 1, inf), p(n + 1);
    queue<int> q; q.push(s); d[s] = 0;
    while(!q.empty()) {
        int v = q.front(); q.pop();

        for(auto to : g[v]) {
            if(to == t) continue;
            if(umin(d[to], d[v] + 1)) {
                p[to] = v;
                q.push(to);
            }
        }
    }

    for(auto to : g[t]) {
        if(umin(d[t], d[to] + 1)) {
            p[t] = to;
        }
    }

    return {d, p};
}

void solve() {
    int n, m, s, t;
    cin >> n >> m >> s >> t;

    vector<vector<int>> g(n + 1);
    for(int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;

        g[u].push_back(v);
        g[v].push_back(u);
    }

    auto [ds, ps] = bfs(g, s, t);
    auto [dt, pt] = bfs(g, t, s);

    vector<int> path;
    int V = t;
    while(V != s) {
        path.push_back(V);
        V = ps[V];
    }
    path.push_back(V);
    reverse(all(path));

    vector<int> used(n + 1);
    for(auto v : path) used[v] = 1;

    int ans = inf;
    for(int v = 1; v <= n; v++) {
        if(!used[v]) {
            umin(ans, ds[v] + dt[v]);
        }
    }

    auto USED = used;
    for(int it = 0; it < 2; it++) {
        used = USED;
        int v = s;
        int len = 0;

        while(1) {
            int cnt = 0;
            for(auto to : g[v]) {
                if(!used[to]) cnt++;
            }

            len++;
            if(cnt > 1) {
                umin(ans, ds[t] + 4 * len);
                break;
            }
            if(cnt == 0) break;

            used[v] = 1;
            for(auto to : g[v]) {
                if(!used[to]) {
                    v = to;
                }
            }
        }

        swap(t, s); swap(ds, dt);
    }

    if(ans == inf) cout << "-1\n";
    else cout << ans + ds[t] << '\n';
}

signed main() {
    ios_base::sync_with_stdio(0); cin.tie(0);
    int ttt = 1;
    while(ttt--) {
        solve();
    }
}
