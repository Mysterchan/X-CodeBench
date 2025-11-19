#include<bits/stdc++.h>
using namespace std;
const long long mod=998244353;
int p[300000],dep[300000];
long long dp[300000],dps[300000];
vector<int>v[300000];
int main(){
	ios::sync_with_stdio(false),cin.tie(0);
	int T,n,i,j,x;
	long long ans;
	for(cin>>T;T>0;T--)
	{
		cin>>n;
		dep[0]=0;
		for(i=1;i<n;i++)
		{
			cin>>p[i];
			p[i]--;
			dep[i]=dep[p[i]]+1;
		}
		for(i=0;i<n;i++)
		{
			v[dep[i]].push_back(i);
			dp[i]=0;
			dps[i]=0;
		}
		dp[0]=1;
		dps[0]=1;
		for(i=1;i<n;i++)
		{
			for(j=0;j<v[i].size();j++)
			{
				x=v[i][j];
				if(i==1)dp[x]=dps[i-1];
				else dp[x]=(dps[i-1]+mod-dp[p[i]])%mod;
				dps[i]=(dps[i]+dp[x])%mod;
			}
		}
		ans=0;
		for(i=0;i<n;i++)ans=(ans+dp[i])%mod;
		cout<<ans<<'\n';
		for(i=0;i<n;i++)v[i].clear();
	}
	return 0;
}