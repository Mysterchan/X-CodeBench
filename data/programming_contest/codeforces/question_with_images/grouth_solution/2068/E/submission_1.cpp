#include <bits/stdc++.h>

using namespace std;
#define int long long
const int p=998244353;
int po(int a,int b) {if(b==0) return 1; if(b==1) return a; if(b%2==0) {int u=po(a,b/2);return (u*1LL*u)%p;} else {int u=po(a,b-1);return (a*1LL*u)%p;}}
int inv(int x) {return po(x,p-2);}
mt19937 rnd;
#define app push_back
#define all(x) (x).begin(),(x).end()
#ifdef LOCAL
#define debug(...) [](auto...a){ ((cout << a << ' '), ...) << endl;}(#__VA_ARGS__, ":", __VA_ARGS__)
#define debugv(v) do {cout<< #v <<" : {"; for(int izxc=0;izxc<v.size();++izxc) {cout << v[izxc];if(izxc+1!=v.size()) cout << ","; }cout <<"}"<< endl;} while(0)
#else
#define debug(...)
#define debugv(v)
#endif
#define lob(a,x) lower_bound(all(a),x)
#define upb(a,x) upper_bound(all(a),x)
const int N = 107;
bool dp[N][N];
int32_t main()
{
    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    int n, m;
    cin >> n >> m;
    vector <vector <int>> g(n);
    for (int i = 0; i <m; ++i){
        int u, v; cin >> u >> v;
        u--; v--;
        g[u].app(v); g[v].app(u);
    }

    vector <vector <int> > tree(n);
    vector <int> dist(n, n), par(n, n - 1);
    queue <int> q;
    q.push(n - 1); dist[n - 1] = 0;
    while (!q.empty()) {
        int  u = q.front(); q.pop();
        for (int v : g[u]) {
            if (dist[v] >dist[u] + 1) {
                dist[v] = dist[u] + 1;
                par[v] = u;
                tree[u].app(v);
                q.push(v);
            }
        }
    }

    const int inf = 1e9+7;

    auto h = dist;

    vector <int> l(n), r(n);
    int ptr = 0;
    const int L = 20;
    vector <vector <int> > go(n, vector <int> (L)), mn(n, vector <int> (L, inf));
    function <void(int)> dfs = [&] (int u) {
        l[u] = ptr++;
        go[u].front() = par[u];
        for (int i = 0; i + 1 < L; ++i) {
            go[u][i+1] = go[go[u][i]][i];
        }
        for (int v : tree[u]) {
            dfs(v);
        }
        r[u] = ptr;
    };
    dfs(n-1);

    auto anc = [&] (int u, int v) {
        return l[u] <= l[v] && r[v] <= r[u];
    };

    auto lca = [&] (int u, int v) {
        if (anc(u,v)) {
            return u;
        }
        for (int i = L - 1; i >= 0; --i) {
            if (!anc(go[u][i],v)) {
                u =go[u][i];
            }
        }
        return go[u].front();
    };

    auto make = [&] (int s, int h, int v) {
        for (int i = 0; i < L; ++i) {
            if ((h >> i) & 1) {
                mn[s][i] = min(mn[s][i], v);
                s = go[s][i];

            }
        }
    };

    for (int x = 0; x < n; ++x) {
        for (int y : g[x]) {
            if (par[x] != y && par[y] != x) {
                int lc = lca(x, y);
                if (h[lc] < h[y]) {
                    make(y, h[y] - h[lc], h[x] + h[y] + 1);
                }
            }
        }
    }



    for (int i = L - 1; i; --i) {
        for (int u = 0; u < n; ++u) {
            if (mn[u][i] != inf) {
                mn[u][i - 1] = min(mn[u][i - 1], mn[u][i]);
                mn[go[u][i - 1]][i - 1] = min(mn[go[u][i - 1]][i - 1], mn[u][i]);
            }
        }
    }



    vector <int> min2(n);
    for (int i = 0; i + 1 < n; ++i) {
        if (mn[i][0] == inf) {
            min2[i] = inf;
        }
        else {
            min2[i] = mn[i][0] - h[i];
        }
    }



    auto check = [&] (int T) {
        fill(all(dist), inf);

        if (min2[0] <= T) {
            dist[0] = 0;
            q.push(0);
        }

        while(!q.empty()) {
            int u = q.front(); q.pop();

            for (int v : g[u]) {
                if (dist[v] == inf && min2[v] + dist[u] + 1 <= T) {
                    dist[v] = dist[u] + 1;
                    q.push(v);
                }
            }
        }
        return dist.back() < inf;
    };

    if (!check(2 * n)) {
        cout << -1 << '\n';
    }
    else {
        int lo = 0, hi = 2 * n;
        while (lo < hi - 1) {
            int T = (lo + hi) / 2;
            if (check(T)) {
                hi = T;
            }
            else {
                lo = T;
            }
        }
        cout << hi << '\n';
    }
    return 0;
}
