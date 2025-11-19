#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
const int N=5010,mod=998244353 ;
ll n,a[N],b[N],l,r,f[N][N];
void add(ll &a,ll b){a=(a+b)%mod;}
ll solve(ll x){
    memset(f,0,sizeof f);
    f[0][0]=1;
    for(int i=1; i<=n; i++){
        for(int j=0; j<i; j++)
            if(b[j]-a[i]>=x)
                add(f[i][j],f[i-1][j]+f[i][j-1]);
        if(b[i]-a[i]>=x) add(f[i][i], f[i][i-1]);
    }
    return f[n][n];
}
int main(){
    cin>>n>>l>>r;
    for(int i=1; i<=n; i++) cin>>a[i], a[i]+=a[i-1];
    for(int i=1; i<=n; i++) cin>>b[i], b[i]+=b[i-1];
    cout<<((solve(b[n]-a[n]-r) - solve(b[n]-a[n]-l+1))%mod+mod)%mod;
    return 0;
}
