#include<bits/stdc++.h>
using namespace std;
#define int long long 
const int N=2e5+10,mod=998244353;
int pw(int a,int b){
    if(!b)return 1;
    if(b&1)return pw(a*a%mod,b>>1)%mod*a%mod;
    return pw(a*a%mod,b>>1)%mod;
}
int f[N],g[N],a[N],n,q,sum=0;
signed main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>n>>q;
    for(int i=2;i<=n;i++)cin>>a[i];
    f[1]=g[1]=0;
    sum=0;
    for(int i=2;i<=n;i++)f[i]=(a[i]+pw(i-1,mod-2)*sum)%mod,sum=(sum+f[i])%mod;
    sum=0;
    for(int i=2;i<=n;i++)g[i]=pw(i,mod-2)*(f[i]+sum)%mod,sum=(sum+g[i])%mod;
    int ret=1;
    for(int i=1;i<n;i++)ret=ret*i%mod;
    while(q--){
        int x,y;cin>>x>>y;
        if(x>y)swap(x,y);
        cout<<((f[x]+f[y]-g[x]*2)%mod+mod)%mod*ret%mod<<"\n";
    }
    return 0;
}