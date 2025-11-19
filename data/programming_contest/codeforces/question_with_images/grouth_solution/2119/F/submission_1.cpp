#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<vector>
#include<set>
#include<queue>
#include<unordered_map>
#include<map>
#define int long long
using namespace std;
int n,st,dist[1000002],w[1000001],tim[1000001],ans;
vector <int> g[1000001];
int f[1000001];
queue<int> q;
void getdis(int u,int fa)
{
	for(int v:g[u])
	{
		if(v==fa) continue;
		dist[v]=dist[u]+1;
		getdis(v,u);
	}
}
void dfs(int u,int fa,int k,bool inn,int hei,int TIM,int dis)
{
	if(hei<0)
	{
		TIM=max(TIM,(-hei+1)/2*2+k*2+dis);
	}
	if(TIM<=dist[u])
	{
		ans=max(ans,dist[u]);
	}
	else
	{
		return;
	}
	for(int v:g[u])
	{
		if(v==fa) continue;
		if(inn&&w[u]!=w[v])
		{
			dfs(v,u,min(k,tim[v]),inn,hei+w[v],TIM+1,dis+1);
		}
		else
		{
			dfs(v,u,k,0,hei+w[v],TIM+1,dis+1);
		}
	}
}
int T; 
signed main()
{
	ios::sync_with_stdio(false);
	cin>>T;
	int cnt=0;
	while(T--)
	{
		cnt++;
		cin>>n>>st;
		for(int i=1;i<=n;i++)
		{
			dist[i]=0;
			tim[i]=1000000000;
			g[i].clear();
			f[i]=-10000000000000000;
		}
		ans=0;
		for(int i=1;i<=n;i++)
		{
			cin>>w[i];
		}
		for(int i=1,u,v;i<n;i++)
		{
			cin>>u>>v;
			g[u].push_back(v);
			g[v].push_back(u);
		}
		getdis(1,-1);
		for(int i=1;i<=n;i++)
		{
			for(int v:g[i])
			{
				if(w[i]==1&&w[v]==1)
				{
					tim[i]=0;
					q.push(i);
					break;
				}
			}
		}
		while(!q.empty())
		{
			int u=q.front();
			q.pop();
			for(int v:g[u])
			{
				if(tim[v]==1000000000&&w[v]!=w[u])
				{
					tim[v]=tim[u]+1;
					q.push(v);
				}
			}
		}
		dfs(st,-1,tim[st],1,w[st],1,1);
		cout<<ans+(dist[st]&1)-1<<'\n';
	}
}