#include<iostream>//Are dreams merely lost wings in the concrete jungle？
#include<algorithm>
#include<cmath>
#include<iomanip>
#include<cstdio>
#include<string>
#include<deque>
#include<stack>
#include<queue>
#include<vector>
#include<stdio.h>
#include<map>
#include<set>
#include<string.h>
#include<random>
#include<time.h>
#include<stdlib.h>
#include<bitset>
#define il inline
#define reg register
#define ll long long
#define popcount __builtin_popcount
using namespace std;
inline void read(int &n){int x=0,f=1;char ch=getchar();while(ch<'0'||ch>'9'){if(ch=='-') f=-1;ch=getchar();}
	while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}n=x*f;}
inline void read(ll &n){ll x=0,f=1;char ch=getchar();while(ch<'0'||ch>'9'){if(ch=='-') f=-1;ch=getchar();}
	while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}n=x*f;}
const int N=2e5+5,mod=998244353;
int n,m;
vector<ll>g[N],f[N],a[N];
void upd1(int x,int y){
	if(x==y&&x==1)g[x][y]=1;
	else g[x][y]=(g[x-1][y]*a[x-1][y]%mod+g[x][y-1]*a[x][y-1]%mod)%mod;
}
void upd2(int x,int y){
	if(x==n&&y==m)f[x][y]=1;
	else f[x][y]=(f[x+1][y]*a[x+1][y]%mod+f[x][y+1]*a[x][y+1]%mod)%mod;
}
void upd(int x,int y){
	upd1(x,y);upd2(x,y);
}
void update(int x,int y){
	if(n>m){
		for(int j=1;j<=m;j++)upd(x,j);
	}else{
		for(int i=1;i<=n;i++)upd(i,y);
	}
}
int nowx,nowy,q;
ll ans;
int main(){
	cin>>n>>m;
	for(int i=0;i<=n+1;i++){
		a[i].resize(m+2);f[i].resize(m+2);g[i].resize(m+2);
	}
	for(int i=1;i<=n;i++){
		for(int j=1;j<=m;j++){
			cin>>a[i][j];
		}
	}
	for(int i=1;i<=n;i++){
		for(int j=1;j<=m;j++){
			upd1(i,j);
		}
	}
	for(int i=n;i>=1;i--){
		for(int j=m;j>=1;j--){
			upd2(i,j);
		}
	}
	ans=g[n][m]*a[n][m]%mod;
	read(q);read(nowx);read(nowy);
	while(q--){
		char c;int w;
		cin>>c;cin>>w;
		if(c=='U')nowx--;
		else if(c=='L')nowy--;
		else if(c=='R')nowy++;
		else if(c=='D')nowx++;
		update(nowx,nowy);
		ans=(ans-g[nowx][nowy]*f[nowx][nowy]%mod*a[nowx][nowy]%mod+mod)%mod;
		a[nowx][nowy]=w;
		update(nowx,nowy);
		ans=(ans+g[nowx][nowy]*f[nowx][nowy]%mod*a[nowx][nowy]%mod+mod)%mod;
		printf("%d\n",ans);
	}
	return 0;
}

