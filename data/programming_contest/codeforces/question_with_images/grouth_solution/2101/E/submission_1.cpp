#include <bits/stdc++.h>
#define LL long long
int T,N,a[70009],hd[70009],vv[70009],sz[70009],siz[70009],son[70009],
k,to[140009],nxt[140009],dp[70009],as[70009];
char s[70009];
void l(int u,int v) {
    to[++k]=v;nxt[k]=hd[u];hd[u]=k;
}
struct n_t{
    int p,d,xx;
};std::vector<n_t> t2[70009];
struct v_t{
    int va,id;
    int va2,id2;
} ;std::vector<v_t> va[70009];
void chk(v_t &x,int p1,int p2) {
    if(x.id==p2) {
        if(x.va<p1) {
            x.va=p1;
        }
        return;
    }
    if(x.va<p1) {
        x.va2=x.va;x.id2=x.id;
        x.va=p1;x.id=p2;
    } else if(x.va2<p1) {
        x.va2=p1;x.id2=p2;        
    }
}
void dfs(int n,int f) {
    siz[n]=1;
    son[n]=0;
    for(int i=hd[n];i;i=nxt[i]) {
        if(to[i]==f||vv[to[i]]) continue;
        dfs(to[i],n);
        siz[n]+=siz[to[i]];
        if(siz[to[i]]>siz[son[n]]) son[n]=to[i];
    }
}
void dfs2(int n,int f,int d,int rt,int rt2) {
    if(rt2==0&&(f)) rt2=n;
    t2[n].push_back((n_t){rt,d,rt2});
    for(int i=hd[n];i;i=nxt[i]) {
        if(to[i]==f||vv[to[i]])continue;
        dfs2(to[i],n,d+1,rt,rt2);
    }
}
void sv(int n) {
    dfs(n,0);
    int g=n;
    while(son[g]&&siz[son[g]]>=(siz[n]+1)/2) {
        g=son[g];
    }
    sz[g]=siz[n];
    n=g;
    vv[n]=1;
    dfs2(n,0,0,n,0);
    for(int i=hd[n];i;i=nxt[i]) {
        if(!vv[to[i]]) sv(to[i]);
    }
}
signed main(void) {
    scanf("%d",&T);
    while(T--) {
        scanf("%d",&N);
        scanf("%s",s+1);
        for(int i=1;i<=N;i++) hd[i]=vv[i]=0,t2[i].clear();k=0;
        for(int i=1;i<N;i++) {
            int u,v;
            scanf("%d %d",&u,&v);
            l(u,v),l(v,u);
        }
        sv(1);
        for(int i=1;i<=N;i++) {
            if(s[i]=='0') {
                dp[i]=0;
                as[i]=-1;
            } else {
                dp[i]=0x3f3f3f3f;
                as[i]=1;
            }
            va[i].clear();
            va[i].resize(sz[i]);
        }
        for(int i=1;;i++) {
            int ff=0;
            for(int j=1;j<=N;j++) {
                if(s[j]=='0') {
                    dp[j]=0;
                } 
                if(dp[j]) as[j]=i,ff=1;
            }
            if(!ff) break;
            for(int j=1;j<=N;j++) {
                for(int k=0;k<sz[j];k++) {
                    va[j][k].va=-0x3f3f3f3f;
                    va[j][k].va2=-0x3f3f3f3f;
                }
            }
            for(int j=1;j<=N;j++) {
                int xx=dp[j]/2;
                if(dp[j]==0) continue;
                for(int k=0;k<t2[j].size();k++) {
                    int rt=t2[j][k].p,di=t2[j][k].d;
                    if(di>xx) continue;
                    di=xx-di;
                    di=std::min(di,sz[rt]-1);
                    chk(va[rt][di],t2[j][k].d,t2[j][k].xx);
                }
            }
            for(int j=1;j<=N;j++) {
                for(int k=sz[j]-2;k>=0;k--) {
                    chk(va[j][k],va[j][k+1].va,va[j][k+1].id);
                    chk(va[j][k],va[j][k+1].va2,va[j][k+1].id2);
                }
            }            
            for(int j=1;j<=N;j++) {
                dp[j]=0;
                for(int k=0;k<t2[j].size();k++) {
                    int rt=t2[j][k].p,di=t2[j][k].d;
                    if(t2[j][k].xx==va[rt][di].id)
                        dp[j]=std::max(dp[j],di+va[rt][di].va2);
                    else dp[j]=std::max(dp[j],di+va[rt][di].va);
                }
            }
        }
        for(int i=1;i<=N;i++) printf("%d ",as[i]);printf("\n");
    }
}