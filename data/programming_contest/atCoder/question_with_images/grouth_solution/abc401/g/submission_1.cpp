
#include <bits/stdc++.h>
using namespace std;

int n;
vector<int> e1[309];
int match[309], vis[309];

bool dfs(int x){
	vis[x]=1;
	for (int i=0; i<e1[x].size(); i++){
		int y=e1[x][i];
		if (!match[y] || (!vis[match[y]] && dfs(match[y]))){
			match[y]=x;
			return 1;
		}
	}
	return 0;
}

bool solve(int n){
	memset(match, 0, sizeof match);
	for (int i=1; i<=n; i++){
		memset(vis, 0, sizeof vis);
		if (!dfs(i))	return 0;
	}
	return 1;
}

long double x1[309], Y1[309];
long double x2[309], y2[309];

long double dis(int i, int j){
	return sqrt((__int128)abs(x1[i]-x2[j])*abs(x1[i]-x2[j])+(__int128)abs(Y1[i]-y2[j])*abs(Y1[i]-y2[j]));
}

int main(){
	scanf("%d", &n);
	for (int i=1; i<=n; i++)	cin>>x1[i]>>Y1[i];
	for (int i=1; i<=n; i++)	cin>>x2[i]>>y2[i];
	
	long double l=0, r=2e18, eps=1e-9;
	while (r-l>l*eps){
		long double mid=(l+r)/2;
		
		for (int i=1; i<=n; i++)	e1[i].clear();
		for (int i=1; i<=n; i++)
			for (int j=1; j<=n; j++)
				if (dis(i, j)<=mid)
					e1[i].push_back(j);
		
		if (solve(n))	r=mid;
		else	l=mid;
	}
	
	cout<<fixed<<setprecision(12)<<(l+r)/2<<endl;
	return 0;
}