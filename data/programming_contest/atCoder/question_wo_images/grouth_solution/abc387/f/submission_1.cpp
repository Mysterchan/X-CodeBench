#include<bits/stdc++.h>
#define int long long
using namespace std;

const int M=3e3+10,mod=998244353;
int n,m,a[M];
int dfn[M],low[M],st[M],cnt,tp,scc[M],tot;
bitset<M> in,vis,rd;
vector<int> e[M],tr[M];
int ans=1,f[M][M],dp[M][M];

void tarjan(int u)
{
	dfn[u]=low[u]=++tot;
	in[u]=1,st[++tp]=u;
	for(auto v:e[u])
	{
		if(dfn[v]==0)
		{
			tarjan(v);
			low[u]=min(low[u],low[v]);
		}
		else if(in[v])
			low[u]=min(low[u],dfn[v]);
	}
	
	if(dfn[u]==low[u])
	{
		int now;
		cnt++;
		do
		{
			now=st[tp--];
			in[now]=0;
			scc[now]=cnt;
		}while(now!=u);
	}
}

void dfs(int u)
{
	for(int i=1;i<=m;i++)
		dp[u][i]=1;
	for(auto v:tr[u])
	{
		dfs(v);
		for(int i=1;i<=m;i++)
			dp[u][i]=(dp[u][i]*f[v][i])%mod;
	}
	for(int i=1;i<=m;i++)
		f[u][i]=(f[u][i-1]+dp[u][i])%mod;
}

signed main()
{
	cin>>n>>m;
	for(int i=1;i<=n;i++)
	{
		scanf("%lld",&a[i]);
		e[a[i]].push_back(i);
	}
	
	for(int i=1;i<=n;i++)
		if(!dfn[i])
			tarjan(i);
	
	for(int i=1;i<=n;i++)
	{
		int fu=scc[i];
		for(auto v:e[i])
		{
			int fv=scc[v];
			if(fu!=fv)
			{
				tr[fu].push_back(fv);
				rd[fv]=1;
			}
		}
	}
	
	for(int i=1;i<=cnt;i++)
	{
		if(rd[i]==0)
		{
			dfs(i);
			ans=(ans*f[i][m])%mod;
		}
	}
	
	cout<<ans;
	
	return 0;
}