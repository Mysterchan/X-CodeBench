#include <bits/stdc++.h>
using namespace std;
int n,m;
vector<int> ed[200010];
int cnt[200010];
int dis1[200010],dis2[200010],dis3[200010];
int fro1[200010],fro2[200010];

struct Info{
	int u,d,fro;
};
bool operator<(Info A,Info B)
{
	return A.d>B.d;
}
priority_queue<Info>Q;
priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>>Q_;
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0),cout.tie(0);

	cin>>n>>m;
	for(int i=1,u,v;i<=m;i++)
	{
		cin>>u>>v;
		ed[u].push_back(v);
		ed[v].push_back(u);
	}

	memset(dis1,0x3f,sizeof(dis1));
	memset(dis2,0x3f,sizeof(dis2));
	dis1[n]=0;
	Q.push(Info{n,0,0});
	while(!Q.empty())
	{
		Info t=Q.top();Q.pop();

		if(cnt[t.u]>=2) continue;
		cnt[t.u]++;
		for(int v:ed[t.u]) if(v!=t.fro)
		{
			if(dis1[v]>t.d+1)
			{
				if(fro1[v]!=t.u) dis2[v]=dis1[v],fro2[v]=fro1[v];
				dis1[v]=t.d+1,fro1[v]=t.u,Q.push(Info{v,t.d+1,t.u});
			}
			else if(fro1[v]!=t.u&&dis2[v]>t.d+1)
				dis2[v]=t.d+1,fro2[v]=t.u,Q.push(Info{v,t.d+1,t.u});	
		}
	}

	dis2[n]=0;

	memset(cnt,0,sizeof(cnt));
	memset(dis3,0x3f,sizeof(dis3));
	dis3[n]=0;
	Q_.push(make_pair(0,n));
	int u,d;
	while(!Q_.empty())
	{
		u=Q_.top().second,d=Q_.top().first;Q_.pop();
		if(d<dis2[u])
		{
			dis3[u]=dis2[u];Q_.push(make_pair(dis2[u],u));
			continue;
		}
		if(cnt[u]) continue;
	
		cnt[u]=1;
		for(int v:ed[u])
			if(dis3[v]>d+1)
				dis3[v]=d+1,Q_.push(make_pair(d+1,v));
	}

	cout<<dis3[1]<<endl;
	return 0;
}