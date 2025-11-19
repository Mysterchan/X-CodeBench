#include<bits/stdc++.h>
using namespace std;
int dp[200000][2],lockx[200000];
vector<int>line[200000];
void dfs(int t,int tag){
	vector<int>::iterator it;
	if(dp[t][tag])return;
	dp[t][tag]=1;
	for(it=line[t].begin();it!=line[t].end();it++)
	{
		if(tag==0)dfs(*it,1);
		else
		{
			lockx[*it]--;
			if(!lockx[*it])dfs(*it,0);
		}
	}
}
int main(){
	ios::sync_with_stdio(false),cin.tie(0);
	int T,n,m,q,i,u,v,op;
	for(cin>>T;T>0;T--)
	{
		cin>>n>>m>>q;
		for(i=0;i<n;i++)
		{
			lockx[i]=0;
			dp[i][0]=0;
			dp[i][1]=0;
		}
		for(i=0;i<m;i++)
		{
			cin>>u>>v;
			line[v-1].push_back(u-1);
			lockx[u-1]++;
		}
		for(;q>0;q--)
		{
			cin>>op>>u;
			u--;
			if(op==1)
			{
				dfs(u,0);
				dfs(u,1);
			}
			else
			{
				if(dp[u][0]==0)cout<<"YES\n";
				else cout<<"NO\n";
			}
		}
		for(i=0;i<n;i++)line[i].clear();
	}
	return 0;
}