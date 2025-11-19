#include<bits/stdc++.h>
using namespace std ;
#define ll long long
#define ii pair<int,int>
#define lll pair<ll,ll>
#define vi vector<int>
#define vvi vector<vector<int>>
#define vii vector<ii>
#define fileIO(x) if(fopen(x".inp","r")){freopen(x".inp","r",stdin);freopen(x".out","w",stdout);}
#define all(x) x.begin(),x.end()
int n,a[1000005];
int pre[1000005],aft[1000005];
void sc()
{
    set<ii>st;
    cin>>n;
    for(int i=1;i<=n;i++){
        cin>>a[i];
        st.insert({a[i],i});
        pre[i]=i-1;
        aft[i]=i+1;
    }
    aft[n]=0;
    ll ans=0;
    while(st.size()>1){
        int x=(*st.begin()).second;st.erase(st.begin());
        if(a[x]==a[aft[x]]){
            int y=aft[x];
            st.erase({a[y],y});
            st.insert({++a[x],x});
            aft[x]=aft[y];
            pre[aft[y]]=x;
            continue;
        }
        int mn=1e9;
        if(pre[x]!=0)mn=min(mn,a[pre[x]]);
        if(aft[x]!=0)mn=min(mn,a[aft[x]]);
        ans+=max(0,mn-a[x]);
        a[x]=mn;
        st.insert({a[x],x});
    }
    cout<<ans<<'\n';
    for(int i=1;i<=n;i++){
        pre[i]=0;aft[i]=0;
    }
}
int main()
{
    fileIO("task")
    ios_base :: sync_with_stdio(false) ; cin.tie(0) ; cout.tie(0) ;
    int t;cin>>t;while(t--)sc() ;
    return 0 ;
}
