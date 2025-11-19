#include<bits/stdc++.h>
#define emp emplace_back
using namespace std;
using ll=long long;
const int kn = 4e5 + 45, mod = 998244353;
int n, a[kn];
ll f[1024][1024];
signed main(){
    cin.tie(0)->ios::sync_with_stdio(false);
    cin >> n;
    for(int i=0; i<1024; ++i) for(int j=0; j<1024; ++j) f[i][j] = 1;
    for(int i=1; i<=n; ++i){
        cin >> a[i];
        for(int j=0, b0=(a[i]>>10); j<1024; ++j){
            if((j | a[i]) == j) (f[b0][j] *= a[i]) %= mod;
        }
        ll ans = 1;
        for(int j=0, b1=(a[i]&(1<<10)-1); j<1024; ++j){
            if((a[i] | j) == a[i]) (ans *= f[j][b1]) %= mod;
        }
        printf("%lld\n", ans);
    }
    return 0;
}