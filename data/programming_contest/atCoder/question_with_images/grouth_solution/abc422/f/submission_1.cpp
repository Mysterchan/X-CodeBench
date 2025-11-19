#include<bits/stdc++.h>
using namespace std;
const int N=5010;
vector<int>edges[N];
long long dp[N][N];
long long sto[N];
int main()
{
	int n,m;
	cin>>n>>m;
	for(int i=1;i<=n;i++)cin>>sto[i];
	for(int i=1;i<=m;i++)
	{
		int a,b;
		cin>>a>>b;
		edges[a].push_back(b);
		edges[b].push_back(a);
	}
	memset(dp,127,sizeof(dp));
	for(int i=0;i<=n;i++)dp[1][i]=i*sto[1];
	for(int i=n-1;i>=0;i--)
	{
		for(int j=1;j<=n;j++)
		{
			for(auto y:edges[j])
			{
				dp[y][i]=min(dp[y][i],dp[j][i+1]+sto[y]*i);
			}
		}
	}
	for(int i=1;i<=n;i++)cout<<dp[i][0]<<endl;
	return 0;
}