#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define N 10000005
const int mod=998244353;
int n,a,b,q;
int fac[N],ifac[N],inv[N],rr[N],f[N][2],g[N][2];
int C(int n,int k){
    return 1ll*fac[n]*ifac[k]%mod*ifac[n-k]%mod;
}
int main(){
    scanf("%d%d%d%d",&n,&a,&b,&q);
    fac[0]=fac[1]=inv[0]=inv[1]=ifac[0]=ifac[1]=rr[0]=1;
    rr[1]=1;
    for(int i=2;i<=n;++i){
        rr[i]=rr[i-1]*4ll%mod;
        fac[i]=1ll*fac[i-1]*i%mod;
        inv[i]=1ll*(mod-mod/i)*inv[mod%i]%mod;
        ifac[i]=1ll*ifac[i-1]*inv[i]%mod;
    }
    f[0][0]=g[0][0]=1;
    int ds=a,dx=n-a+1,dy=n-b+1,dz=b;
    for(int i=1;i<=n;++i){
        if(ds<=i)f[i][1]=C(i-1,ds-1);
        if(dx<=i&&ds-1+dx-1!=i-1)f[i][1]=(f[i][1]+C(i-1,dx-1))%mod;
        if(i<n)f[i][0]=(f[i-1][0]*2ll%mod-f[i][1]+mod)%mod;
        if(dz<=i)g[i][1]=C(i-1,dz-1);
        if(dy<=i&&dz-1+dy-1!=i-1)g[i][1]=(g[i][1]+C(i-1,dy-1))%mod;
        if(i<n)g[i][0]=(g[i-1][0]*2ll%mod-g[i][1]+mod)%mod;
    }
    while(q--){
        int k;scanf("%d",&k);
        int kk=n-k+1;
        printf("%d\n",(((1ll*f[kk][1]*g[kk][1]%mod+1ll*f[kk][1]*g[kk][0]%mod)%mod+1ll*g[kk][1]*f[kk][0]%mod)%mod));
    }
    return 0;
}