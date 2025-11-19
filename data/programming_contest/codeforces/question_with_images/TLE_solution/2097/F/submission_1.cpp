
#include <bits/stdc++.h>
#define int long long
using namespace std;
const int inf=1e18;
int dp[1005][1<<12];
int f[1<<12][13][2][2],n,m,s[20];
int a[1005][20],b[1005][20],c[1005][20];
void chk(int &x,int y){
	if(x>=y)x=y;
}
void solve(){
	cin>>n>>m;
	for(int i=0;i<(1<<n);i++)dp[0][i]=0;
	for(int i=0;i<n;i++){
		cin>>s[i];
		for(int j=0;j<(1<<n);j++)if(!(j>>i&1))dp[0][j]+=s[i];
	}
	for(int i=1;i<=m;i++){
		for(int j=0;j<n;j++)cin>>a[i][j];
		for(int j=0;j<n;j++)cin>>b[i][j];
		for(int j=0;j<n;j++)cin>>c[i][j];
		for(int j=0;j<(1<<n);j++)for(int k=0;k<n;k++)for(int x=0;x<2;x++)f[j][k][x][0]=f[j][k][x][1]=inf;
		for(int j=0;j<(1<<n);j++){
			chk(f[j^(j&1)][0][j&1][j&1],dp[i-1][j]+a[i][1]*(j>>1&1)+b[i][0]*(j&1)+c[i][n-1]*(j>>(n-1)&1));
			chk(f[j|1][0][j&1][j&1],dp[i-1][j]);
		}
		for(int k=1;k<n;k++){
			for(int j=0;j<(1<<n);j++){
				for(int x=0;x<2;x++){
					for(int y=0;y<2;y++){
						chk(f[j|(1<<k)][k][x][j>>k&1],f[j][k-1][x][y]);
						if(k<n-1)chk(f[j^(j&(1<<k))][k][x][j>>k&1],f[j][k-1][x][y]+a[i][k+1]*(j>>(k+1)&1)+b[i][k]*(j>>k&1)+c[i][k-1]*y);
						else chk(f[j^(j&(1<<k))][k][x][j>>k&1],f[j][k-1][x][y]+a[i][0]*x+b[i][k]*(j>>k&1)+c[i][k-1]*y);
					}
				}
			}
		}
		for(int j=0;j<(1<<n);j++)dp[i][j]=inf;
		for(int j=0;j<(1<<n);j++)for(int x=0;x<2;x++)for(int y=0;y<2;y++)chk(dp[i][j],f[j][n-1][x][y]);
		cout<<dp[i][0]<<'\n';
	}
}
signed main(){
#ifdef FILE
    freopen(".in","r",stdin);
    freopen(".out","w",stdout);
#endif
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc;
    cin>>tc;
    while(tc--)solve();
    return 0;
}

