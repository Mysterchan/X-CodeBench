#include <bits/stdc++.h>
using namespace std;
using i64=long long;

struct In{
    static const int S=1<<20;
    int i=0,l=0; char b[S];
    inline char gc(){ if(i>=l){ l=fread(b,1,S,stdin); i=0; if(!l) return 0; } return b[i++]; }
    template<class T> bool rd(T& x){ char c=gc(); if(!c) return false; while(c<=' ') if(!(c=gc())) return false; int s=1; if(c=='-'){ s=-1; c=gc(); } long long v=0; while(c>' '){ v=v*10+(c-'0'); c=gc(); } x=T(v*s); return true; }
} inw;

const int MN=300000+5, ME=600000+5;
int n,head[MN],to[ME],nx_[ME],ec,eu[MN],ev[MN];
int par[MN],in_[MN],sz[MN],cur[MN],stk[MN],top,child_[MN];
i64 ft[MN],S;
char outb[1<<23]; int op;

inline void ae(int u,int v){ to[++ec]=v; nx_[ec]=head[u]; head[u]=ec; }
inline void add(int i,i64 v){ for(;i<=n;i+=i&-i) ft[i]+=v; }
inline i64 sum(int i){ i64 r=0; for(;i;i-=i&-i) r+=ft[i]; return r; }
inline i64 range(int l,int r){ return sum(r)-sum(l-1); }
inline void wi(i64 x){ if(x==0){ outb[op++]='0'; outb[op++]='\n'; return; } if(x<0){ outb[op++]='-'; x=-x; } char s[24]; int k=0; while(x){ s[k++]=char('0'+x%10); x/=10; } while(k) outb[op++]=s[--k]; outb[op++]='\n'; }

int main(){
    memset(head,-1,sizeof(head));
    if(!inw.rd(n)) return 0;
    for(int i=1;i<=n-1;i++){
        int u,v; inw.rd(u); inw.rd(v);
        eu[i]=u; ev[i]=v; ae(u,v); ae(v,u);
    }
    par[1]=0; stk[top++]=1; cur[1]=head[1];
    int tim=0;
    while(top){
        int v=stk[top-1];
        if(!sz[v]){ in_[v]=++tim; sz[v]=1; }
        int e=cur[v];
        if(e!=-1){
            cur[v]=nx_[e]; int u=to[e];
            if(u==par[v]) continue;
            par[u]=v; cur[u]=head[u]; stk[top++]=u;
        }else{
            if(par[v]) sz[par[v]]+=sz[v];
            top--;
        }
    }
    for(int i=1;i<=n-1;i++) child_[i]=(par[eu[i]]==ev[i]?eu[i]:ev[i]);
    for(int v=1;v<=n;v++) add(in_[v],1);
    S=n;
    int q; inw.rd(q);
    while(q--){
        int t; inw.rd(t);
        if(t==1){
            int x,w; inw.rd(x); inw.rd(w);
            add(in_[x],w); S+=w;
        }else{
            int y; inw.rd(y);
            int c=child_[y];
            i64 sub=range(in_[c],in_[c]+sz[c]-1);
            i64 ans=S-(sub<<1); if(ans<0) ans=-ans;
            wi(ans);
        }
    }
    fwrite(outb,1,op,stdout);
    return 0;
}