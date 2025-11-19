#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
const int N=40,M=510;
ll n,mod,ans[M];
ll fac[M],inv[M];
ll dp[N][M][N][N][2],g[N][N][M],t[N][N][M];
ll ksm(ll x,ll k){
	ll tmp=1;
	while(k){
		if(k&1) tmp=tmp*x%mod;
		x=x*x%mod;
		k>>=1;
	}
	return tmp;
}
void init(){
	fac[0]=1;
	for(int i=1;i<=500;i++) fac[i]=fac[i-1]*i%mod;
	inv[500]=ksm(fac[500],mod-2);
	for(int i=499;i>=0;i--) inv[i]=inv[i+1]*(i+1)%mod;
}
ll C(ll x,ll y){
	if(x<y||x<0||y<0) return 0;
	return fac[x]*inv[y]%mod*inv[x-y]%mod;
}
int main(){
	std::ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin>>n>>mod;
	init();
	for(int i=1;i<=n;i++){
		t[i][0][0]=1;
		for(int j=1;j<=n-i;j++){
			for(int k=j;k<=i*j;k++){
				for(int l=1;l<=min(k,i);l++) t[i][j][k]=(t[i][j][k]+t[i][j-1][k-l]*C(i,l)%mod)%mod;
			}
		}
	}
	
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n-i;j++){
			for(int k=j;k<=n*(n-1)/2;k++){
				for(int l=0;l<=k-j;l++) g[i][j][k]=(g[i][j][k]+t[i][j][k-l]*C(j*(j-1)/2,l)%mod)%mod;
			}
		}
	}
	
	dp[1][0][0][1][1]=1;
	for(int i=1;i<n;i++){
		for(int j=i-1;j<=i*(i-1)/2;j++){
			for(int k=0;k<=i;k++){
				for(int p=1;p<=i;p++){
					for(int q=0;q<=1;q++){
						if(!dp[i][j][k][p][q]) continue;
						for(int x=1;x<=n-i;x++){
							for(int y=x;y<=x*p+x*(x-1)/2;y++){
								if(q==0) dp[i+x][j+y][k][x][1]=(dp[i+x][j+y][k][x][1]+dp[i][j][k][p][0]*C(n-i,x)%mod*g[p][x][y]%mod)%mod;
								else dp[i+x][j+y][k+x][x][0]=(dp[i+x][j+y][k+x][x][0]+dp[i][j][k][p][1]*C(n-i,x)%mod*g[p][x][y]%mod)%mod;
							}
						}
					}
				}
			}
		}
	}
	for(int i=n-1;i<=n*(n-1)/2;i++){
		for(int j=1;j<=n;j++) ans[i]=(ans[i]+dp[n][i][n/2][j][0]+dp[n][i][n/2][j][1])%mod;
	}
	for(int i=n-1;i<=n*(n-1)/2;i++) cout<<ans[i]<<" ";
	return 0;
}