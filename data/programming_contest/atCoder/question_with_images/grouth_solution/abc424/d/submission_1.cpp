#include<bits/stdc++.h>
using namespace std;
int T,n,m,ans;
char c[10][10];
void dfs(int x,int y,int cnt){
	if(cnt>ans) return;
	if(y==m){
		dfs(x+1,1,cnt);
	}
	if(x==n){
		ans=min(ans,cnt);
		return;
	}
	if(c[x][y]=='.'||c[x+1][y]=='.'||c[x][y+1]=='.'||c[x+1][y+1]=='.') dfs(x,y+1,cnt);
	else{
		c[x+1][y+1]='.';
		dfs(x,y+1,cnt+1);
		c[x+1][y+1]='#';
		c[x+1][y]='.';
		dfs(x,y+1,cnt+1);
		c[x+1][y]='#';		
	}
}
int main(){
	ios::sync_with_stdio(false);
	cin.tie(0),cout.tie(0);
	cin>>T;
	while(T--){
		ans=100;
		cin>>n>>m;
		for(int i=1;i<=n;i++){
			for(int j=1;j<=m;j++){
				cin>>c[i][j];
			}
		}
		dfs(1,1,0);
		cout<<ans<<endl;
	}
	return 0;
}