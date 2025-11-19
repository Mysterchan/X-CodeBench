#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (n); ++i)
#define rep1(i, n) for (int i = 1; i < (n); ++i)
#define rep1n(i, n) for (int i = 1; i <= (n); ++i)
#define repr(i, n) for (int i = (n) - 1; i >= 0; --i)
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define each(x, a) for (auto &x : a)
#define range(i, n) rep(i, n)
#define pii pair<ll, ll>
#define ll long long
#define ld long double
#define ull unsigned long long
#define pb push_back
#define eb emplace_back
#define mp make_pair
#define F first
#define S second
#define ar array
#define vec vector

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--)
    {
        int n, m;
        ll k;
        cin >> n >> m >> k;
        vector<vector<int>> adj(n + 1);
        vector<int> deg(n + 1);
        rep(i, m)
        {
            int u, v;
            cin >> u >> v;
            adj[u].pb(v);
            adj[v].pb(u);
            deg[u]++;
            deg[v]++;
        }
        vector<int> odd;
        rep1n(i, n) if (deg[i] & 1) odd.pb(i);
        if (odd.empty())
        {
            cout << "YES\n";
            continue;
        }
        int a = odd[0], b = odd[1];
        if (k >= m)
        {
            cout << "YES\n";
            continue;
        }
        bool ab_edge = false;
        each(v, adj[a]) if (v == b) ab_edge = true;
        if (k == 1)
        {
            int cut = deg[a] + deg[b] - (ab_edge ? 1 : 0);
            cout << (cut <= 2 ? "YES\n" : "NO\n");
            continue;
        }
        if (deg[a] == 1 && deg[b] == 1)
        {
            int prev, curr, steps, La, Lb;
            prev = a;
            curr = adj[a][0];
            steps = 0;
            while (deg[curr] == 2)
            {
                int n1 = adj[curr][0], n2 = adj[curr][1];
                int nxt = (n1 == prev ? n2 : n1);
                prev = curr;
                curr = nxt;
                steps++;
            }
            La = steps + 1;
            prev = b;
            curr = adj[b][0];
            steps = 0;
            while (deg[curr] == 2)
            {
                int n1 = adj[curr][0], n2 = adj[curr][1];
                int nxt = (n1 == prev ? n2 : n1);
                prev = curr;
                curr = nxt;
                steps++;
            }
            Lb = steps + 1;
            ll lim = min<ll>(La, Lb);
            cout << (k <= lim ? "YES\n" : "NO\n");
        }
        else
        {
            cout << "NO\n";
        }
    }
    return 0;
}