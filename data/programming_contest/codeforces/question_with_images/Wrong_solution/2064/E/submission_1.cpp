#include <bits/stdc++.h>
#pragma GCC target("avx2")
#pragma GCC optimize("O3,unroll-loops")
using namespace std;
#define int long long
#define pii pair<int,int>
#define ff first
#define ss second
#define sp << " " <<    
#define all(cont) cont.begin(),cont.end()
#define vi vector<int>

const int inf = 1e17,N = 2e6+1,MOD = 998244353,B = 600;


int mult(int x,int y) {
    return (x*y)%MOD;
}

int expo(int x,int y) {
    if (!y) return 1;
    int e = expo(x,y/2);
    e = mult(e,e);
    if (y&1) e = mult(e,x);
    return e;
}

int f[N],finv[N];
void solve() {
    int n;
    cin >> n;
    vi p(n+1),c(n+1);
    for (int i=1;i<=n;i++) cin >> p[i];
    for (int i=1;i<=n;i++) cin >> c[i];
    vi pos(n+1);
    for (int i=1;i<=n;i++) pos[p[i]] = i;
    vi a(n+1);
    int blocks = n/B+1;
    vi same(blocks,1),val(blocks,0),put(blocks,0);
    int ans = 1;
    for (int i = n;i>=1;i--) {
        int ins = c[pos[i]];
        int b = pos[i]/B;
        int sol = 0,sag = 0;
        for (int j = pos[i];j>=b*B;j--) {
            if (a[j] && a[j] != ins) break;
            if (a[j]) sol++;
        }
        for (int j = pos[i];j<(b+1)*B;j++) {
            if (a[j] && a[j] != ins) break;
            if (a[j]) sag++;
        }
        int cb = b-1,db = b+1;
        while (cb >= 0) {
            if (same[cb]) {
                if (val[cb]) sol+=put[cb];
                cb--;
                continue;
            }
            else {
                for (int j = B*(cb+1)-1;j>=b*cb;j--) {
                    if (a[j] && a[j] != ins) break;
                    if (a[j]) sol++;
                }
                break;
            }
        }
        while (db < blocks) {
            if (same[db]) {
                if (val[db]) sag+=put[db];
                db++;
                continue;
            }
            else {
                for (int j = B*db;j<B*(db+1);j++) {
                    if (a[j] && a[j] != ins) break;
                    if (a[j]) sag++;
                }
                break;
            }
        }
        ans = mult(ans,sol+sag+1);
        a[pos[i]] = c[pos[i]];
        put[b]++;
        if (same[b] && val[b]) {
            same[b] = 0;
        }
        else if (same[b]) {
            val[b] = c[pos[i]];
        }
    }
    cout << ans << '\n';
}

int32_t main() { 
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    #ifdef Dodi 
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    #endif
    f[0] = 1;
    for (int i=1;i<N;i++) f[i] = mult(f[i-1],i); 
    finv[N-1] = expo(f[N-1],MOD-2);
    for (int i = N-2;i>=0;i--) finv[i] = mult(finv[i+1],i+1);
    int t = 1;
    cin >> t;
    while (t --> 0) solve();
}