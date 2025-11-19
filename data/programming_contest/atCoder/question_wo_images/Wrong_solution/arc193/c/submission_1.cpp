#include<bits/stdc++.h>
using namespace std;
using i64=long long;
constexpr i64 mod=998244353;
inline i64 qpow(i64 p,i64 t){
   i64 r=1;for(;t;t>>=1,p=p*p%mod)if(t&1)(r*=p)%=mod;
   return r;
}
i64 fac[410],ifac[410],f[410][410],g[410][410],pwC[410],C;
inline i64 binom(int n,int m){
   return m<0||m>n?0:fac[n]*ifac[m]%mod*ifac[n-m]%mod;
}
int n,m;
int main(){
   scanf("%d%d%lld",&n,&m,&C),C%=mod;
   fac[0]=1;for(int i=1;i<=400;i++)fac[i]=fac[i-1]*i%mod;
   ifac[400]=qpow(fac[400],mod-2);for(int i=400;i>=1;i--)ifac[i-1]=ifac[i]*i%mod;
   pwC[0]=1;for(int i=1;i<=400;i++)pwC[i]=pwC[i-1]*C%mod;
   for(int i=1;i<=n;i++){
      for(int j=1;j<=m;j++){
         for(int y=1;y<j;y++)(g[i][j]+=f[i][j-y]*binom(j,y)%mod*(y&1?mod-1:1))%=mod;
         for(int x=1;x<i;x++)(f[i][j]+=g[i-x][j]*binom(i,x)%mod*(x&1?C:mod-C))%=mod;
         for(int x=1;x<=i;x++){
            (f[i][j]+=(i==x?1:f[i-x][j])*binom(i,x)%mod*(x+1&1?mod-pwC[x]:pwC[x]))%=mod;
         }
         for(int y=1;y<=j;y++){
            (f[i][j]+=(j==y?1:f[i][j-y])*binom(j,y)%mod*(y+1&1?mod-pwC[y]:pwC[y]))%=mod;
         }
         if(~i&1&&~j&1)(f[i][j]+=C*3)%=mod;
         else (f[i][j]+=mod-C)%=mod;
      }
   }
   i64 ans=0;
   for(int i=1;i<n;i++)for(int j=1;j<m;j++){
      (ans+=f[n-i][m-j]*binom(n,i)%mod*binom(m,j)%mod*(i+j&1?mod-C:C))%=mod;
   }
   if(~n&1&&~m&1)(ans+=5*C)%=mod;
   else (ans+=C)%=mod;
   printf("%lld",ans);
   return 0;
}