#include<bits/stdc++.h>
#define mod 998244353
using namespace std;
int powdv(int x,int y=mod-2){
	int ans=1;
	while(y){
		if(y&1)ans=1ll*ans*x%mod;
		y>>=1,x=1ll*x*x%mod;
	}
	return ans;
}
char s[70005];
vector<int>g[70005];
int f[70005][25],j;
int vist[70005],sz[70005];
int p[70005],t;
void dfs0(int x,int la){
	p[++t]=x;sz[x]=1;
	for(auto cu:g[x]){
		if(cu==la||vist[cu])continue;
		dfs0(cu,x);sz[x]+=sz[cu];
	}
}
int sm[800005];
void build(int l,int r,int o){
	if(l==r){
		sm[o]=-1e9;
		return;
	}
	int mid=(l+r)>>1;
	build(l,mid,o<<1);build(mid+1,r,o<<1|1);
	sm[o]=-1e9;
}
void add(int l,int r,int o,int x,int y){
	if(l==r){
		sm[o]=max(sm[o],y);
		return;
	}
	int mid=(l+r)>>1;
	if(x<=mid)add(l,mid,o<<1,x,y);
	else add(mid+1,r,o<<1|1,x,y);
	sm[o]=max(sm[o<<1],sm[o<<1|1]);
}
void gai(int l,int r,int o,int x){
	if(l==r){
		sm[o]=-1e9;
		return;
	}
	int mid=(l+r)>>1;
	if(x<=mid)gai(l,mid,o<<1,x);
	else gai(mid+1,r,o<<1|1,x);
	sm[o]=max(sm[o<<1],sm[o<<1|1]);
}
int query(int l,int r,int o,int ll,int rr){
	if(l>=ll&&r<=rr)return sm[o];
	int mid=(l+r)>>1,ans=-1e9;
	if(mid>=ll)ans=max(ans,query(l,mid,o<<1,ll,rr));
	if(mid<rr)ans=max(ans,query(mid+1,r,o<<1|1,ll,rr));
	return ans;
}
int M=1e5;
int vc[100005],dep[100005],kk;
void dfs1(int x,int la){
	for(auto cu:g[x]){
		if(cu==la||vist[cu])continue;
		dep[cu]=dep[x]+1;dfs1(cu,x);
	}
}
void dfs2(int x,int la){
	vc[++kk]=x;
	for(auto cu:g[x]){
		if(cu==la||vist[cu])continue;
		dfs2(cu,x);
	}
}
void jia(int x,int y){
	if(x>=0)add(0,M,1,x,y);
}
void shan(int x){
	if(x>=0)gai(0,M,1,x);
}
void solve(int x){
	t=0;dfs0(x,0);
	int r=0;
	for(int i=1;i<=t;++i){
		int y=p[i],mx=0;
		for(auto cu:g[y])if(!vist[cu]){
			if(sz[cu]>sz[y])mx=max(mx,t-sz[y]);
			else mx=max(mx,sz[cu]);
		}
		if(mx<=t/2)r=y;
	}
	dep[r]=0;kk=0;dfs1(r,0);
	jia(f[r][j-1]/2-dep[r],dep[r]);
	for(auto cu:g[r])if(!vist[cu]){
		kk=0;dfs2(cu,r);
		for(int i=1;i<=kk;++i){
			int z=vc[i];
			f[z][j]=max(f[z][j],dep[z]+query(0,M,1,dep[z],M));
		}
		for(int i=1;i<=kk;++i){
			int z=vc[i];
			jia(f[z][j-1]/2-dep[z],dep[z]);
		}
	}
	shan(f[r][j-1]/2-dep[r]);
	for(auto cu:g[r])if(!vist[cu]){
		kk=0;dfs2(cu,r);
		for(int i=1;i<=kk;++i){
			int z=vc[i];
			shan(f[z][j-1]/2-dep[z]);
		}
	}
	reverse(g[r].begin(),g[r].end());
	for(auto cu:g[r])if(!vist[cu]){
		kk=0;dfs2(cu,r);
		for(int i=1;i<=kk;++i){
			int z=vc[i];
			f[z][j]=max(f[z][j],dep[z]+query(0,M,1,dep[z],M));
		}
		for(int i=1;i<=kk;++i){
			int z=vc[i];
			jia(f[z][j-1]/2-dep[z],dep[z]);
		}
	}
	f[r][j]=max(f[r][j],dep[r]+query(0,M,1,dep[r],M));
	shan(f[r][j-1]/2-dep[r]);
	for(auto cu:g[r])if(!vist[cu]){
		kk=0;dfs2(cu,r);
		for(int i=1;i<=kk;++i){
			int z=vc[i];
			shan(f[z][j-1]/2-dep[z]);
		}
	}
	vist[r]=1;
	for(auto cu:g[r])if(!vist[cu])solve(cu);
}
int main(){
	build(0,M,1);
	int T;
	scanf("%d",&T);
	while(T--){
		int n;
		scanf("%d",&n);
		scanf("%s",s+1);
		for(int i=1;i<=n;++i)g[i].clear();
		for(int i=1;i<n;++i){
			int u,v;
			scanf("%d%d",&u,&v);
			g[u].emplace_back(v);
			g[v].emplace_back(u);
		}
		for(int i=1;i<=n;++i)for(int j=0;j<=20;++j)f[i][j]=0;
		for(int i=1;i<=n;++i)if(s[i]=='1')f[i][0]=2*n;
		for(j=1;j<=17;++j){
			for(int i=1;i<=n;++i)vist[i]=0;
			solve(1);
			for(int i=1;i<=n;++i)if(s[i]=='0')f[i][j]=0;
		}
		for(int i=1;i<=n;++i){
			if(s[i]=='0')printf("%d ",-1);
			else{
				int wz=18;
				for(int j=0;j<=17;++j)if(f[i][j]==0){
					wz=j;break;
				}
				printf("%d ",wz);
			}
		}
		printf("\n");
	}
	return 0;
}