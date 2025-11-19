#include <bits/stdc++.h>
using namespace std;
const long long mod=998244353;
int col[5000],d[5000],p[5001],dep[5001],lca[5001][5001],siz[5001];
vector<int>line[5001],vec[5001];
long long dp[5001][5001][2],tdp[5001][2],C[5011][5011];
void dfs(int t){
	vector<int>::iterator it;
	int i,j,p,x;
	long long csum;
	siz[t]=0;
	dp[t][0][0]=1;
	dp[t][0][1]=1;
	for(it=line[t].begin();it!=line[t].end();it++)
	{
		dfs(*it);
		for(x=0;x<=1;x++)
		{
			tdp[siz[t]+siz[*it]][x]=(tdp[siz[t]+siz[*it]][x]+dp[t][siz[t]][x]*dp[*it][siz[*it]][x]%mod*C[siz[t]+siz[*it]][siz[t]])%mod;
			for(i=0;i<siz[t];i++)
			{
				csum=0;
				for(j=0;j<=siz[*it];j++)csum=(csum+dp[*it][j][x])%mod;
				for(j=0;j<=siz[*it];j++)
				{
					tdp[i+j][x]=(tdp[i+j][x]+dp[t][i][x]*csum%mod*C[i+j][i]%mod*C[siz[t]-i-1+siz[*it]-j][siz[t]-i-1])%mod;
					csum=(csum+mod-dp[*it][j][x])%mod;
				}
			}
			csum=0;
			for(i=0;i<=siz[t];i++)csum=(csum+dp[t][i][x])%mod;
			for(i=0;i<=siz[t];i++)
			{
				for(j=0;j<siz[*it];j++)tdp[i+j][x]=(tdp[i+j][x]+dp[*it][j][x]*csum%mod*C[i+j][i]%mod*C[siz[t]-i+siz[*it]-j-1][siz[t]-i])%mod;
				csum=(csum+mod-dp[t][i][x])%mod;
			}
		}
		siz[t]+=siz[*it];
		for(i=0;i<=siz[t];i++)
		{
			dp[t][i][0]=tdp[i][0];
			dp[t][i][1]=tdp[i][1];
			tdp[i][0]=0;
			tdp[i][1]=0;
		}
	}
	for(j=0;j<vec[t].size();j++)
	{
		x=vec[t][j];
		for(i=0;i<=siz[t];i++)
		{
			tdp[i+1][x]=(tdp[i+1][x]+dp[t][i][x]*(i+1))%mod;
			tdp[0][x^1]=(tdp[0][x^1]+dp[t][i][x]*(i+1))%mod;
		}
		siz[t]++;
		for(i=0;i<=siz[t];i++)
		{
			dp[t][i][0]=tdp[i][0];
			dp[t][i][1]=tdp[i][1];
			tdp[i][0]=0;
			tdp[i][1]=0;
		}
	}
}
int main(){
	ios::sync_with_stdio(false),cin.tie(0);
	int T,n,m,i,j;
	for(i=0;i<=5010;i++)
	{
		C[i][0]=1;
		C[i][i]=1;
		for(j=1;j<i;j++)C[i][j]=(C[i-1][j-1]+C[i-1][j])%mod;
	}
	for(cin>>T;T>0;T--)
	{
		cin>>n>>m;
		n++;
		p[0]=-1;
		dep[0]=0;
		for(i=1;i<n;i++)
		{
			cin>>p[i];
			line[p[i]].push_back(i);
			dep[i]=dep[p[i]]+1;
		}
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
			{
				if(i==j)lca[i][j]=i;
				else
				{
					if(dep[i]>=dep[j])lca[i][j]=lca[p[i]][j];
					else lca[i][j]=lca[i][p[j]];
				}
			}
		}
		for(i=0;i<m;i++)cin>>col[i];
		for(i=0;i<m;i++)cin>>d[i];
		for(i=m-1;i>-1;i--)
		{
			for(j=i+1;j<m;j++)
			{
				if(col[i]==col[j])continue;
				if(lca[d[i]][d[j]]==d[j])d[i]=d[j];
			}
		}
		for(i=m-1;i>-1;i--)vec[d[i]].push_back(col[i]);
		for(i=0;i<n;i++)
		{
			for(j=0;j<=m;j++)
			{
				dp[i][j][0]=0;
				dp[i][j][1]=0;
			}
		}
		dfs(0);
		for(i=0;i<n;i++)
		{
			line[i].clear();
			vec[i].clear();
		}
		cout<<(dp[0][0][0]+dp[0][0][1])%mod<<'\n';
	}
	return 0;
}