#include<bits/stdc++.h>
using namespace std;
#define mod 998244353
#define N 1011
#define int long long
bool ip(int x)
{
	for(int i=2;i*i<=x;i++) if(x%i==0) return 0;
	return 1;
}
int i,n,dp[N][N][2],j,k,ans=1,po[N],a[N],b[N];
string s;
signed main()
{
	cin.tie(0)->sync_with_stdio(0);cout.tie(0);
	cin>>n;
	for(i=1;i<n;i++) cin>>a[i];
	for(int p=2;p<1000;p++) if(ip(p))
	{
		int all=0,an=0;
		for(i=1;i<n;i++)
		{
			b[i]=0;
			while(a[i]%p==0) a[i]/=p,b[i]++,all++;
		}
		memset(dp,0,sizeof dp);
		dp[1][0][1]=po[0]=1;
		for(i=1;i<=all;i++) dp[1][i][0]=po[i]=po[i-1]*p%mod;
		for(i=1;i<n;i++)
			for(j=0;j<=all;j++)
				for(int ze=0;ze<2;ze++) if(dp[i][j][ze])
				{
					(dp[i+1][j+b[i]][ze]+=dp[i][j][ze]*po[j+b[i]])%=mod;
					if(j-b[i]>=0&&b[i]) (dp[i+1][j-b[i]][ze|(!(j-b[i]))]+=dp[i][j][ze]*po[j-b[i]])%=mod;
				}
		for(j=0;j<=all;j++) (an+=dp[n][j][1])%=mod;
		ans=ans*an%mod;		
	}
	cout<<ans;
}