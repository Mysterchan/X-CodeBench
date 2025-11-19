#include <bits/stdc++.h>
using namespace std;
#define int long long
#define ld long double
#define pll pair<int, int>
#define pdd pair<double, double>
#define tlll tuple<int, int, int>
#define ls id<<1
#define rs (id<<1) + 1
const int N = 3e7 + 10;
const int M = 1e5 + 10;
const int MX = 1e17;
const int MOD = 998244353;
const int LOGN = 20;
int dirs[4][2] = {{1, 0}, {-1, 0}, {0, -1}, {0, 1}};

int n,m,q,k;
int qpow(int a, int b, int p)
{
    int ans = 1 % p;
    while (b)
    {
        if (b & 1)
            ans = ans * a % p;
        a = a * a % p;
        b >>= 1;
    }
    return ans % p;
}

void solve() {
    cin >> n >> m;
    vector<int> id(2*n+1);
    for(int i=1;i<=m;i++) {
        int u,v;cin>>u>>v;
        id[u] = id[v] = i;
    }
    vector<int> min_cov(2*n+1);
    int K=1;
    while((1<<K) <= m) K++;
    vector<vector<int>> par(K+1,vector<int>(m+1,-1));
    vector<int> dep(m+1);
    stack<int> sta;
    sta.push(0);
    for(int i=1;i<=2*n;i++) {
        if(i%2 == 0) {
            if(!id[i]) continue;
            if(sta.top() == id[i]) {
                sta.pop();
                par[0][id[i]] = sta.top();
                dep[id[i]] = sta.size();
            } else {
                sta.push(id[i]);
            }
        } else {
            min_cov[i] = sta.top();
        }
    }

    for(int j=1;j<=K;j++) {
        for(int i=0;i<=m;i++) {
            par[j][i] = (par[j-1][i]==-1 ? -1 : par[j-1][par[j-1][i]]);
        }
    }

    auto lca = [&] (int u,int v) -> int{
        if(dep[u] > dep[v]) swap(u,v);
        int d = dep[v] - dep[u];
        for(int k = 0 ; k < K ; k++) {
            if((d>>k)&1)
                v = par[k][v];
        }
        if(u == v) return u;
        for(int k=K-1;k>=0;k--) {
            if(par[k][u] != par[k][v]) {
                u = par[k][u];
                v = par[k][v];
            }
        }
        return par[0][u];
    };
    int q;
    cin >> q;
    while (q--) {
        int c, d;
        cin >> c >> d;
        int u = min_cov[c];
        int v = min_cov[d];
        int l = lca(u, v);
        cout << dep[u] + dep[v] - dep[l] * 2 << '\n';
    }
}

signed main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int _ = 1;
    while (_--)
        solve();
    return 0;
}