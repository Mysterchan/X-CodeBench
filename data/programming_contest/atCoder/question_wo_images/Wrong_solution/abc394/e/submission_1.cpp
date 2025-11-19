#include<bits/stdc++.h>
using namespace std;
int n,vis[103][103],ans;
string s[103],cr[103][103];
bool flat;

void dfs(int x,int y,int sm,string z){
	if(x==y){
		for(int i=0;i<z.size();i++){
			if(z[i]==z[z.size()-1-i]&&i==z.size()-1){
				ans=sm,flat=1;
				return;
			}
		}
	}
	for(int i=1;i<=n;i++){
		if(vis[x][i]==0&&s[x][i]!='-'){
			vis[x][i]=1;
			vis[x][0]=1;
			dfs(i,y,sm+1,z+s[x][i]);
			if(flat) return ;
			vis[x][i]=0;
			vis[x][0]=0;
		}
	}
	ans=0; 
}

int main(){
	cin>>n;
	for(int i=1;i<=n;i++) cin>>s[i],s[i]=" "+s[i];
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			if(i==j){
				cout<<0<<" ";
				continue;
			}
			ans=0,flat=0;
			dfs(i,j,ans,"");
			if(!flat) cout<<-1<<" ";
			else cout<<ans<<" ";
			for(int ii=1;ii<=n;ii++){
				if(vis[ii][0]==1){
					for(int jj=1;jj<=n;jj++) vis[ii][jj]=0;
				}
			}
		}
		cout<<endl;
	}
	return 0;
} 