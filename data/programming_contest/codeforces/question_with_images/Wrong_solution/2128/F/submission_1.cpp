#include <bits/stdc++.h>

#define pb push_back
#define sz(x) (int)(x).size()
#define all(x) (x).begin(), (x).end()

using namespace std;

using ll = long long;

const int N = 1e6 + 5;
const int inf = 2e9;
const long long INF = 4e18;

void solve (int test) {
    int n, m, k;
    cin >> n >> m >> k;

    vector < vector < array < int , 3 > > > g (n + 1);
    for (int i = 1; i <= m; ++ i) {
        int u, v, l, r;
        cin >> u >> v >> l >> r;

        g[u].pb ({v, l, r});
        g[v].pb ({u, l, r});
    }


    auto calc = [&] (int v, bool mn) -> vector < ll > {
        vector < ll > dist (n + 1, INF);
        dist[v] = 0;
        set < pair < int , int > > st;
        st.insert ({0, v});
        while (sz(st)) {
            auto it = st.begin();
            int v = it->second, w = it->first;
            st.erase (it);
            for (auto& [to, l, r] : g[v]) {
                int w = (mn ? l : r);
                if (dist[to] > dist[v] + w) {
                    dist[to] = dist[v] + w;
                    st.insert ({dist[to], to});
                }
            }
        }

        return dist;
    };

    vector < ll > dist1 = calc (1, true);
    vector < ll > distk = calc (k, true);
    vector < ll > distmx1 = calc (1, false);
    vector < ll > distmxk = calc (k, false);

    vector < ll > distn = calc (n, true);
    vector < ll > distmxn = calc (n, false);

    vector < vector < pair < int , int > > > gn(n + 1);
    vector < vector < pair < int , int > > > gn1(n + 1);
    for (int i = 1; i <= n; ++ i) {
        for (auto&[to, l, r] : g[i]) {
            bool ok = true;
            bool ok1 = true;
            ok &= (dist1[to] + distk[i] + l == dist1[k] || dist1[i] + distk[to] + l == dist1[k]);
            ok &= (distmx1[to] + distmxk[i] + r == distmx1[k] || distmx1[i] + distmxk[to] + r == distmx1[k]);

            ok1 &= (distn[to] + distk[i] + l == distn[k] || distn[i] + distk[to] + l == distn[k]);
            ok1 &= (distmxn[to] + distmxk[i] + r == distmxn[k] || distmxn[i] + distmxk[to] + r == distmxn[k]);

            if (ok || ok1) {
                gn[i].pb({to, r});
            } else {
                gn[i].pb ({to, l});
            }
            if (!ok || !ok1) {
                gn1[i].pb({to, r});
            } else {
                gn1[i].pb ({to, l});
            }

        }
    }

    auto calc1 = [&] (int v) -> vector < ll > {
        vector < ll > dist (n + 1, INF);
        dist[v] = 0;
        set < pair < int , int > > st;
        st.insert ({0, v});
        while (sz(st)) {
            auto it = st.begin();
            int v = it->second, w = it->first;
            st.erase (it);
            for (auto& [to, w] : gn[v]) {
                if (dist[to] > dist[v] + w) {
                    dist[to] = dist[v] + w;
                    st.insert ({dist[to], to});
                }
            }
        }
        return dist;
    };    auto calc2 = [&] (int v) -> vector < ll > {
        vector < ll > dist (n + 1, INF);
        dist[v] = 0;
        set < pair < int , int > > st;
        st.insert ({0, v});
        while (sz(st)) {
            auto it = st.begin();
            int v = it->second, w = it->first;
            st.erase (it);
            for (auto& [to, w] : gn1[v]) {
                if (dist[to] > dist[v] + w) {
                    dist[to] = dist[v] + w;
                    st.insert ({dist[to], to});
                }
            }
        }
        return dist;
    };

    vector < ll > dist = calc1(1);
    vector < ll > distk1 = calc1(k);
    vector < ll > dist2 = calc2(1);
    vector < ll > distk2 = calc2(k);

    bool ok = false;
    ok |= dist[k] + distk1[n] != dist[n];
    ok |= dist2[k] + distk2[n] != dist2[n];

    cout << (!ok ? "NO\n" : "YES\n");

}

int main () {
#ifdef __APPLE__
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
#endif // __APPLE__
    ios_base::sync_with_stdio(false); cin.tie(nullptr);

    int tt = 1;
    cin >> tt;
    for (int i = 1; i <= tt; ++ i) {
        solve (i);
    }

    return 0;
}