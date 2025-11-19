#include<bits/stdc++.h>
#define rep(i, j, k) for(int i=(j); i<=(k); ++i)
#define per(i, j, k) for(int i=(j); i>=(k); --i)
using namespace std;
namespace DEBUG{
    template<class T> void _debug(const char *s, T x) {cout<<s<<'='<<x<<endl;}
    template<class F, class... Nxt> void _debug(const char *s, F x, Nxt... nxt){
        while(*s!=',') cout<<*s++;
        cout<<'='<<x<<',';
        _debug(s+1, nxt...);
    }
    template<class T> ostream& operator<<(ostream c, vector<T> x){
        c<<'[';
        for(auto v:x) c<<v<<", ";
        return c<<']';
    }
    #ifdef ck
    #define debug(...) 0
    #else
    #define debug(...) _debug(#__VA_ARGS__, __VA_ARGS__)
    #endif
} using namespace DEBUG;
const int N=10007, mod=998244353, up=1e4;
int n, a[N], f[2][N][2], maxn, p[N], ans=1, sum, d, pw[N];
void pls(int &a, long long b){a=(a+b)%mod;}

bool is_prime(int n){
    for(int i=2; i*i<=n; ++i) if(n%i==0) return 0;
    return 1;
}

signed main(){
    cin.tie(0)->sync_with_stdio(0);
    cin>>n;
    rep(i, 1, n-1) cin>>a[i], maxn=max(maxn, a[i]);
    rep(x, 2, maxn) if(is_prime(x)){
        rep(i, 1, n-1){
            p[i]=0;
            while(a[i]%x==0) a[i]/=x, ++p[i];
        }
        pw[0]=1;
        rep(i, 1, up) pw[i]=1ll*pw[i-1]*x%mod;
        rep(i, 0, up) f[d][i][0]=f[d][i][1]=0;
        rep(i, 0, up) f[d][i][!i]=pw[i];
        rep(i, 1, n-1){
            if(!p[i]){
                rep(j, 0, up){
                    pls(f[!d][j][0], 1ll*f[d][j][0]*pw[j]);
                    pls(f[!d][j][1], 1ll*f[d][j][1]*pw[j]);
                }
            } else{
                rep(j, 0, up){
                    pls(f[!d][j+p[i]][0], 1ll*f[d][j][0]*pw[j+p[i]]);
                    pls(f[!d][j+p[i]][1], 1ll*f[d][j][1]*pw[j+p[i]]);
                }
                pls(f[!d][0][1], f[d][p[i]][0]+f[d][p[i]][1]);
                rep(j, p[i]+1, up){
                    pls(f[!d][j-p[i]][0], 1ll*f[d][j][0]*pw[j-p[i]]);
                    pls(f[!d][j-p[i]][1], 1ll*f[d][j][1]*pw[j-p[i]]);
                }
            }
            rep(j, 0, up) f[d][j][0]=f[d][j][1]=0;
            d^=1;
        }
        sum=0;
        rep(i, 0, up) pls(sum, f[d][i][1]), f[d][i][0]=f[d][i][1]=0;
        ans=1ll*ans*sum%mod;
    }
    cout<<ans;
}
