#include <iostream>
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

using vi = vector<ll>;
#define pb push_back
#define nl '\n'
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()

const ll MOD = 1000000007;

void setIO(string name = "")
{
    cin.tie(0)->sync_with_stdio(0);
    if (sz(name))
    {
        freopen((name + ".in").c_str(), "r", stdin);
        freopen((name + ".out").c_str(), "w", stdout);
    }
}
template <typename t>
void debug(t x) { cout << x << nl; }

void read(vector<ll> &a, int n)
{
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
}

const int MAXN = 305;

bitset<MAXN> adj[MAXN];

void solve()
{
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while (t--)
    {
        int n, k;
        cin >> n >> k;

        vector<bool> is(n, false);

        vector<bool> cl(n, false);

        for (int j = 0; j < k; ++j)
        {
            for (int i = 0; i < n; ++i)
            {
                adj[i].reset();
            }

            vector<int> deg(n, 0);

            int m;
            cin >> m;
            for (int i = 0; i < m; ++i)
            {
                int u, v;
                cin >> u >> v;
                --u;
                --v;
                adj[u][v] = 1;
                adj[v][u] = 1;
                deg[u]++;
                deg[v]++;
            }

            for (int i = 0; i < n; ++i)
            {
                for (int j = i + 1; j < n; ++j)
                {

                    bitset<MAXN> ti = adj[i];
                    bitset<MAXN> tj = adj[j];

                    ti.reset(j);
                    tj.reset(i);
                    if (ti == tj)
                    {
                        if (adj[i][j])
                        {
                            if (deg[i] == n - 1 && deg[j] == n - 1)
                            {
                                cl[i] = true;
                                cl[j] = true;
                            }
                        }
                        else
                        {
                            if (deg[i] == 0 && deg[j] == 0)
                            {
                                is[i] = true;
                                is[j] = true;
                            }
                        }
                    }
                }
            }
        }

        bool ok = true;
        for (int i = 0; i < n; ++i)
        {
            if (is[i] && cl[i])
            {
                ok = false;
                break;
            }
        }

        if (ok)
        {
            cout << "Yes" << nl;
        }
        else
        {
            cout << "No" << nl;
        }
    }

    return 0;
}