#include<bits/stdc++.h>
#define rep(i, j, k) for(int i=(j); i<=(k); ++i)
using namespace std;

const int N=1007, mod=998244353;
int n, a[N], maxn, ans=1;

void pls(int &a, long long b){a=(a+b)%mod;}

int power(int a, int b){
    int res=1;
    for(; b; b>>=1, a=1ll*a*a%mod)
        if(b&1) res=1ll*res*a%mod;
    return res;
}

signed main(){
    cin.tie(0)->sync_with_stdio(0);
    cin>>n;
    rep(i, 1, n-1) cin>>a[i], maxn=max(maxn, a[i]);
    
    vector<int> primes;
    vector<bool> is_prime(maxn+1, true);
    for(int i=2; i<=maxn; ++i){
        if(is_prime[i]){
            primes.push_back(i);
            for(int j=i*2; j<=maxn; j+=i)
                is_prime[j]=false;
        }
    }
    
    for(int x : primes){
        vector<int> p(n);
        rep(i, 1, n-1){
            while(a[i]%x==0) a[i]/=x, ++p[i];
        }
        
        int maxp=*max_element(p.begin(), p.end());
        
        vector<int> pw(maxp+n+1);
        pw[0]=1;
        rep(i, 1, maxp+n) pw[i]=1ll*pw[i-1]*x%mod;
        
        vector<vector<int>> f(maxp+n+1, vector<int>(2));
        rep(i, 0, maxp+n) f[i][!i?1:0]=pw[i];
        
        rep(i, 1, n-1){
            vector<vector<int>> nf(maxp+n+1, vector<int>(2));
            if(!p[i]){
                rep(j, 0, maxp+n){
                    pls(nf[j][0], 1ll*f[j][0]*pw[j]);
                    pls(nf[j][1], 1ll*f[j][1]*pw[j]);
                }
            } else{
                rep(j, 0, maxp+n-p[i]){
                    pls(nf[j+p[i]][0], 1ll*f[j][0]*pw[j+p[i]]);
                    pls(nf[j+p[i]][1], 1ll*f[j][1]*pw[j+p[i]]);
                }
                pls(nf[0][1], f[p[i]][0]+f[p[i]][1]);
                rep(j, p[i]+1, maxp+n){
                    pls(nf[j-p[i]][0], 1ll*f[j][0]*pw[j-p[i]]);
                    pls(nf[j-p[i]][1], 1ll*f[j][1]*pw[j-p[i]]);
                }
            }
            f=move(nf);
        }
        
        int sum=0;
        rep(i, 0, maxp+n) pls(sum, f[i][1]);
        ans=1ll*ans*sum%mod;
    }
    cout<<ans;
}