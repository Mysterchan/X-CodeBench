#include<bits/stdc++.h>
using namespace std;
using i64=long long;
constexpr i64 mod=998244353;
int n,m,p[510][510],invp1[510],f[510][510],g[510][510];
bool flag[510][510];
int main(){
   scanf("%d%d",&n,&m);
   for(int i=1;i<=m;i++)for(int j=1;j<=n;j++)scanf("%d",&p[i][j]);
   for(int i=1;i<=n;i++)invp1[p[1][i]]=i;
   for(int i=2;i<=m;i++){
      int q[510];
      for(int j=1;j<=n;j++)q[j]=p[i][j];
      for(int j=1;j<=n;j++)p[i][j]=q[invp1[j]];
      int d=(1+n-p[i][1])%n;
      for(int j=1;j<=n;j++)p[i][j]=(p[i][j]-1+d)%n+1;
   }
   for(int l=1;l<=n;l++){
      int mx[510],mi[510];
      for(int i=2;i<=m;i++)mx[i]=0,mi[i]=1e9;
      for(int r=l;r<=n;r++){
         flag[l][r]=true;
         for(int i=2;i<=m;i++){
            mi[i]=min(mi[i],p[i][r]);
            mx[i]=max(mx[i],p[i][r]);
            flag[l][r]=flag[l][r]&&mx[i]-mi[i]+1==r-l+1;
         }
      }
   }
   for(int i=1;i<=n+1;i++)g[i][i-1]=1;
   for(int len=1;len<=n;len++)for(int l=1,r;(r=l+len-1)<=n;l++){
      for(int k=l;k<r;k++)(g[l][r]+=g[l][k]*f[k+1][r])%=mod;
      if(flag[l][r]){
         for(int k=l;k<=r;k++)(f[l][r]+=g[l][k-1]*g[k+1][r])%=mod;
         (g[l][r]+=f[l][r])%=mod;
      }
   }
   printf("%lld",g[2][n]);
   return 0;
}