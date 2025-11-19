#include<bits/stdc++.h>
using namespace std;
#define lowbit(x) (x&(-x))
const int maxn=3e5+10;
int n,p[maxn],c[maxn],ans;
void add(int x,int v){
    for(int i=x;i<=n;i+=lowbit(i))
        c[i]+=v;
}
int query(int x){
    int ans=0;
    for(int i=x;i;i-=lowbit(i))
        ans+=c[i];
    return ans;
}
int main(){
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
        scanf("%d",&p[i]);
    for(int i=1;i<=n;i++){
        ans+=max(0,-(query(p[i])+1)*query(p[i])/2+i*(i+1)/2)-i;
        add(p[i],1);
    }
    printf("%d",ans);
    return 0;
}