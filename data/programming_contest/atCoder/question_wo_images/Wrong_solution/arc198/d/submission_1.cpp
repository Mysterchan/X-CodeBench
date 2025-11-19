#include<bits/stdc++.h>
#define int long long 
const int base=13331,mod=1e9+7; 
int gi(){
	char c;int x=0,f=0;
	while(!isdigit(c=getchar()))f|=(c=='-');
	while(isdigit(c))x=(x*10)+(c^48),c=getchar();
	return f?-x:x;
}
std::mt19937 rnd(std::random_device{}());
#define pr std::pair<int,int>
#define all(x) (x).begin(),(x).end()
#define mem(x,w) memset(x,w,sizeof(x))
#define sz(x) (int)((x).size())
#define eb emplace_back
#define fi first
#define se second
template<class T>void cxk(T&a,T b){a=a>b?a:b;}
template<class T>void cnk(T&a,T b){a=a<b?a:b;}
int n,fa[3005],F[3005],dfn[3005],siz[3005],dep[3005],num;
char a[3005][3005];
int col[3005],cnt,W[3005],hs[3005][3005];
std::vector<int>G[3005],g[3005];
void link(int u,int v){G[u].eb(v),G[v].eb(u);}
void init(int N){for(int i=1;i<=N;i++)F[i]=i;}
int find(int x){return F[x]==x?x:F[x]=find(F[x]);}
void dfs(int u,int FA){
	fa[u]=FA;dep[u]=dep[FA]+1,dfn[u]=++num,siz[u]=1;
	for(int v:G[u])if(v^FA)dfs(v,u),siz[u]+=siz[v];
}
void dfs2(int u,int FA,int rt){
	hs[rt][u]=(hs[rt][FA]*base%mod+col[u])%mod;
	for(int v:G[u])if(v^FA)dfs2(v,u,rt);
}
signed main(){
	std::ios::sync_with_stdio(0),std::cin.tie(0);
	std::cin>>n;init(n);
	for(int i=1,u,v;i<n;i++)std::cin>>u>>v,link(u,v);
	for(int i=1;i<=n;i++)for(int j=1;j<=n;j++)std::cin>>a[i][j];
	for(int i=1;i<=n;i++)for(int j=i+1;j<=n;j++)if(a[i][j]=='1')g[i].eb(j);
	for(int u=1;u<=n;u++){
		for(int i=1;i<=n;i++)fa[i]=dfn[i]=siz[i]=dep[i]=0;
		num=0,dfs(u,0);fa[u]=0;
		for(int v:g[u]){
			int l=v,r=v,mb=(dep[v]+1)/2;
			while(dep[r]^mb)r=fa[r];
			int mb2=dep[v]&1?mb:mb+1;
			while(dep[l]^mb2)l=fa[l];
			while(r){
				int fl=find(l),fr=find(r);
				if(fl==fr&&l^r)break;
				F[fl]=fr;
				r=fa[r];
				for(int v2:G[l])if(v2^fa[l]&&dfn[v2]<=dfn[v]&&dfn[v]<dfn[v2]+siz[v2]){l=v2;break;}
			}
		}
	}
	for(int i=1,fi;i<=n;i++){
		if(find(i)^i||col[i])continue;
		fi=find(i);++cnt;
		for(int j=1;j<=n;j++)if(find(j)==fi)col[j]=cnt;
	}
	for(int i=1;i<=n;i++)dfs2(i,0,i);
	int ans=0;
	for(int i=1;i<=n;i++)for(int j=1;j<=n;j++)if(hs[i][j]==hs[j][i])++ans;
	std::cout<<ans<<'\n';
	return 0;
}
