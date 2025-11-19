
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int T,n,x;
ll w,ans,z,y;
vector<ll> s[62];
int main(){
    scanf("%d",&T);
    while(T--){
        scanf("%d%lld",&n,&w);
        for(int i=1;i<=n;i++){
            scanf("%d%lld",&x,&y);
            s[x].emplace_back(y);
        }
        ans=0;
        for(ll i=0;i<=61;i++){
            s[i].emplace_back(0);
            sort(s[i].begin(),s[i].end(),greater<int>());
            auto j=s[i].begin();
            if(w>>i&1){
                ans+=s[i].front();
                j++;
            }
            if(i<61)
                while(j!=s[i].end()){
                    z=*j;
                    j++;
                    if(j!=s[i].end()){
                        s[i+1].emplace_back(z+*j);
                        j++;
                    }
                }
            s[i].clear();
        }
        printf("%lld\n",ans);
    }
    return 0;
}