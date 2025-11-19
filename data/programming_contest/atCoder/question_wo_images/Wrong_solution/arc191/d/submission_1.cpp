#include<bits/stdc++.h>
#define pb push_back
using namespace std;
const int maxn=400005;
int N,M,S,T,Que[maxn*10],Cnt[maxn*10],DD[maxn];
vector<int> E[maxn];
struct YYZ{
    int Min,cMin;
    YYZ operator +(const YYZ &B){
        YYZ C;
        C.Min=min(Min,B.Min);
        C.cMin=min(cMin,B.cMin);
        if(C.Min!=Min) C.cMin=min(C.cMin,Min);
        if(C.Min!=B.Min) C.cMin=min(C.cMin,B.Min);
        return C;
    }
}Dis[maxn];
int fm[maxn];
void BFS(int x){
    Cnt[x]=1;
    memset(DD,63,sizeof DD);
    DD[x]=0;int hed=0,til=1;Que[til]=x;
    while(hed^til)
     for(int v:E[Que[++hed]]){
        if(DD[Que[hed]]+1==DD[v]) Cnt[v]=min(Cnt[v]+Cnt[Que[hed]],2);
        else if(DD[Que[hed]]+1<DD[v]) Cnt[v]=Cnt[Que[hed]],Que[++til]=v,DD[v]=DD[Que[hed]]+1,fm[v]=Que[hed];
     }


    for(int i=1;i<=N;i++) Dis[i]=(YYZ){(int)1e9,(int)1e9};
    Dis[x]=(YYZ){0,(int)1e9};hed=0,til=1;Que[til]=x;
    while(hed^til)
     for(int v:E[Que[++hed]])if(v!=fm[Que[hed]]){
        YYZ Now=Dis[Que[hed]];Now.Min++,Now.cMin++;
        YYZ Lst=Dis[v];
        Dis[v]=Dis[v]+Now;
        if(Dis[v].Min!=Lst.Min||Dis[v].cMin!=Lst.cMin) Que[++til]=v;
     }
}
int main(){
    cin.tie(0)->sync_with_stdio(0);
    cin>>N>>M>>S>>T;
    for(int i=1,x,y;i<=M;i++) cin>>x>>y,E[x].pb(y),E[y].pb(x);
    BFS(S);
    if(Dis[T].cMin>5e8&&Cnt[T]<=1) cout<<-1<<'\n';
    else {
        int Ans=min(Dis[T].Min+Dis[T].cMin,Dis[T].Min*2+2);
        if(Cnt[T]>1) Ans=min(Ans,Dis[T].Min*2);
        cout<<Ans<<'\n';
    }
    return 0;
}