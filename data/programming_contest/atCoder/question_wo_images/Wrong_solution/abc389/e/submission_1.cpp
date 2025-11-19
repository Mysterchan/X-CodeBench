#include<bits/stdc++.h>
#include<ext/pb_ds/assoc_container.hpp>
#include<ext/pb_ds/tree_policy.hpp>
 
using namespace std;
using namespace __gnu_pbds;
 
#define ll long long
#define pll pair<long long,long long> 
#define INF 1e18
#define pii pair<int,int>
#define vi vector<int>
#define infi 1e9
#define vvi vector<vector<int> >
#define vll vector<ll>
#define vvll vector<vector<ll> >
#define vvii vector<vector<int> >
 
 ll M=1e9+7;
 
typedef tree<ll, null_type, less<ll>, rb_tree_tag, tree_order_statistics_node_update> pbds; 
 
 
bool cmp(const pair<int,int> &a, const pair<int,int> &b) {
    if (a.first == b.first)
        return a.second > b.second; 
    return a.first < b.first;
}




bool func(ll M,vll& p,ll x){
    ll val=M;
    for(int i=0;i<p.size();i++){
        ll k=(x/p[i]+1)/2;
        ll z=sqrt(M/p[i]);
        if(k>z) return 0;
        val-=k*k*p[i];
    }

    if(val>=0) return 1;
    return 0;
    
}


 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); 
    
    ll n,m;
    cin>>n>>m;

    vll p(n);
    for(int i=0;i<n;i++) cin>>p[i];

    ll lo=0,hi=1e18;

    while(hi-lo>1){
        ll mid=(lo+hi)/2;
        bool b1=func(m,p,mid);
        bool b2=func(m,p,mid+1);

        if(b1==1 && b2==1){
            lo=mid+1;
        }
        else{
            hi=mid;
        }
    }
    ll x1=0;
    bool b1=func(m,p,hi);
    bool b2=func(m,p,hi+1);
    if((b1==1) && (b2==0)){
        x1=hi;
    }
    else x1=lo;

    ll ans=0;
    for(int i=0;i<n;i++){
        ans+=(x1/p[i]+1)/2;
        ll k=(x1/p[i]+1)/2;
        m-=k*k*p[i];
    }

    ans+=m/(x1+1);
    cout<<ans<<endl;





 
 }
 