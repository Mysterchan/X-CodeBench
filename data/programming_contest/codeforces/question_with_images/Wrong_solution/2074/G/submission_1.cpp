#include<bits/stdc++.h>
#define rep(i,a,b) for(int i=(a);i<=(b);++i)
using namespace std;
#define int long long
const int mxn=888;
int dp[mxn][mxn],n,a[mxn];
void Max(int&x,int y){x=max(x,y);}
inline void solve(){
	cin>>n;
	for(int i=0;i<=n*2+2;++i)for(int j=0;j<=n*2+2;++j)dp[i][j]=-1145141919810ll,a[i]=0;
	for(int i=1;i<=n;++i)cin>>a[i];
	for(int i=n+1;i<=n*2;++i)a[i]=a[i-n];
	for(int i=1;i<=n*2+1;++i)dp[i][i]=0,dp[i][i-1]=0;
	for(int l=n*2;l;--l){
		for(int r=l;r<=min(2*n,l+n-1);++r){
			Max(dp[l][r],dp[l+1][r]);
			Max(dp[l][r],dp[l][r-1]);
			for(int k=l+1;k<=r-1;++k){
				Max(dp[l][r],a[l]*a[k]*a[r]+dp[l+1][k-1]+dp[k+1][r-1]);
			}

		}
	}
	int ans=0;
	for(int i=1;i<=n+1;++i)Max(ans,dp[i][i+n-1]);
	cout<<ans<<'\n';
}
signed main(){
	int T=1;
	cin>>T;
	for(;T--;)solve();
	return 0;  
}
