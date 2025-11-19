#include <bits/stdc++.h>
using namespace std;
using ll=long long;
const int S=200000+5;
int n,p[S],c[S],cnt[S],st[S],cur[S],a[S],b[S];
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if(!(cin>>n))return 0;
    for(int i=1;i<=n;i++) cin>>p[i];
    for(int i=1;i<=n;i++){cin>>c[i]; cnt[c[i]]++;}
    int pos=1;
    for(int x=1;x<=n;x++){st[x]=pos; cur[x]=pos; pos+=cnt[x];}
    for(int i=1;i<=n;i++){int x=c[i]; a[cur[x]++]=p[i];}
    ll ans=0;
    for(int x=1;x<=n;x++) if(cnt[x]){
        int L=st[x], R=st[x]+cnt[x], d=0;
        for(int i=L;i<R;i++){
            int v=a[i];
            int k=lower_bound(b,b+d,v)-b;
            b[k]=v;
            if(k==d)d++;
        }
        ans+=1ll*(cnt[x]-d)*x;
    }
    cout<<ans<<"\n";
    return 0;
}
