#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
const int N=5005,L=5000,mod=998244353;
int f[N][2][N],sf[N][2],g[N][2];
int sz[N],se[N][2],si[N][2],sc[N][2];
int col[N],fa[N],lim[N],h[N],st[N];
int n,m,S[2],H[2];
int cnt,Ans;
int fac[N],inv[N];
vector<int>G[N];
struct Edge{int to,next;}w[N<<1];
void Add(int x,int y){cnt++;w[cnt].to=y,w[cnt].next=h[x],h[x]=cnt;}
int inc(int a,int b){a+=b;return a>=mod?a-mod:a;}
int mul(int a,int b){return 1ll*a*b%mod;}
int C(int n,int m){if(n<0||m<0||n<m)return 0;return mul(fac[n],mul(inv[m],inv[n-m]));}
int powe(int a,int b){int v=1;while(b){if(b&1)v=mul(v,a);a=mul(a,a),b>>=1;}return v;}
int P(int a,int b){return C(a+b,b);}
void DFS(int u){
	int i,j,c,I;
	for(I=h[u];I;I=w[I].next){
		int e=w[I].to;DFS(e);
		if(!sz[e])continue;
		if(!sz[u]){
			for(i=1;i<=sz[e];i++)f[u][0][i]=f[e][0][i],f[u][1][i]=f[e][1][i];
			sz[u]+=sz[e];si[u][0]+=si[e][0],si[u][1]+=si[e][1];continue;
		}
		for(i=0;i<=sz[u]+sz[e]+1;i++)sf[i][1]=sf[i][0]=g[i][1]=g[i][0]=se[i][0]=se[i][1]=0;
		for(i=sz[u];i>=0;i--)sf[i][0]=inc(sf[i+1][0],f[u][0][i]),sf[i][1]=inc(sf[i+1][1],f[u][1][i]);
		for(i=sz[e];i>=0;i--)se[i][0]=inc(se[i+1][0],f[e][0][i]),se[i][1]=inc(se[i+1][1],f[e][1][i]);
		S[0]=S[1]=H[0]=H[1]=0;
		for(i=1;i<=sz[e];i++)S[0]=inc(S[0],f[e][0][i]),S[1]=inc(S[1],f[e][1][i]);
		for(i=1;i<=sz[u];i++)H[0]=inc(H[0],f[u][0][i]),H[1]=inc(H[1],f[u][1][i]);
		for(i=1;i<=sz[u];i++){
			for(c=0;c<=1;c++){
				g[i][c]=inc(g[i][c],mul(mul(S[c^1],P(sz[u]-i,sz[e]-1)),sf[i+1][c]));
				g[i][c]=inc(g[i][c],mul(S[c^1],mul(P(sz[u]-i,sz[e]),f[u][c][i])));
			}
		}
		for(i=1;i<=sz[e];i++){
			for(c=0;c<=1;c++){
				g[i][c]=inc(g[i][c],mul(H[c^1],mul(P(sz[e]-i,sz[u]-1),se[i+1][c])));
				g[i][c]=inc(g[i][c],mul(H[c^1],mul(P(sz[e]-i,sz[u]),f[e][c][i])));
			}
		}		
		for(c=0;c<=1;c++){
			int flg=0;
			if(si[e][c^1]){flg=1;
				for(i=0;i<=sz[u];i++){
					for(j=1;j<=sz[e]-1;j++)
					g[i+j][c]=inc(g[i+j][c],mul(mul(sf[i][c],f[e][c][j]),mul(P(i,j),P(sz[u]-i,sz[e]-j-1))));
				}
			}
			if(si[u][c^1]){flg=1;
				for(i=1;i<=sz[u]-1;i++){
					for(j=0;j<=sz[e];j++)
					g[i+j][c]=inc(g[i+j][c],mul(mul(f[u][c][i],se[j][c]),mul(P(i,j),P(sz[u]-i-1,sz[e]-j))));
				}
			}
			if(!flg){
				int x=si[u][c]+si[e][c];
				if(x)g[x][c]=inc(g[x][c],fac[x]);
			}
		}
		sz[u]+=sz[e];si[u][0]+=si[e][0],si[u][1]+=si[e][1];
		for(c=0;c<=1;c++){for(i=1;i<=sz[u];i++)f[u][c][i]=g[i][c];}
	}
	int ps=G[u].size();
	if(ps){
		
		int it=G[u][0],now=0,fc=1;
		while(now<ps&&G[u][now]==it)now++;
		for(j=0;j<ps;j++){
			int p=j,ct=1;
			while(p+1<ps&&G[u][p+1]==G[u][j])p++,ct++;
			fc=mul(fc,fac[ct]);j=p;
		}
		if(sz[u]==0)f[u][it][now]=fc;
		else{
			int ln=0,pos=ps-1;
			while(pos>=0&&G[u].back()==G[u][pos])ln++,pos--;
			for(i=0;i<=sz[u]+G[u].size();i++)g[i][0]=g[i][1]=0;
			for(c=0;c<=1;c++){
				if(G[u].back()==c){
					for(i=1;i<=sz[u];i++){
						if(ps==ln&&f[u][c][i])g[ln+i][it]=inc(g[ln+i][it],mul(fc,mul(P(ln,i),f[u][c][i])));
						else g[now][it]=inc(g[now][it],mul(fc,mul(P(ln,i),f[u][c][i])));
					}
				}
				else{for(i=1;i<=sz[u];i++)g[now][it]=inc(g[now][it],mul(fc,f[u][c][i]));}
			}
			for(i=1;i<=sz[u]+G[u].size();i++)f[u][0][i]=g[i][0],f[u][1][i]=g[i][1];
		}
	}
	for(int c:G[u]){sz[u]++;si[u][c]++;}
}
int main(){
	int i,j,c,T;inv[0]=fac[0]=1;
	for(i=1;i<=L;i++)fac[i]=mul(fac[i-1],i);inv[L]=powe(fac[L],mod-2);
	for(i=L-1;i>=1;i--)inv[i]=mul(inv[i+1],i+1);
	scanf("%d",&T);
	while(T--){
		scanf("%d%d",&n,&m);cnt=Ans=0;
		for(i=0;i<=max(n,m);i++){
			h[i]=sz[i]=0;G[i].clear();
			for(c=0;c<=1;c++){
				sc[i][c]=se[i][c]=si[i][c]=0;	
				for(j=0;j<=m;j++)f[i][c][j]=0;
			}
		}
		for(i=1;i<=n;i++){scanf("%d",&fa[i]);if(fa[i])Add(fa[i],i);}
		for(i=1;i<=m;i++)scanf("%d",&col[i]);
		for(i=1;i<=m;i++)scanf("%d",&lim[i]);
		for(i=m;i>=1;i--){
			int u=lim[i],flg=0,C=col[i],tp=0;
			while(u){st[++tp]=u;u=fa[u];}
			for(j=tp;j>=1;j--){
				u=st[j];flg=0;
				if(j==1)break;
				if(sc[u][0]&&C==1)flg=1;
				if(sc[u][1]&&C==0)flg=1;
				if(flg==1)break;
			}
			G[u].push_back(i);sc[u][C]++;
		}
		for(i=1;i<=n;i++){
			int ps=G[i].size();if(!ps)continue;
			sort(G[i].begin(),G[i].end());
			for(j=0;j<ps;j++)G[i][j]=col[G[i][j]];
		}
		DFS(1);int Ans=0;
		for(i=1;i<=m;i++){for(c=0;c<=1;c++)Ans=inc(Ans,f[1][c][i]);}
		printf("%d\n",Ans);
	}
}