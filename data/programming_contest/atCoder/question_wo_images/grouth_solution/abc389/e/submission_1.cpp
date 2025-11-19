#include<bits/stdc++.h>
using namespace std;
#define ll long long
const ll N=2e5+10;
ll n,m,a[N],l,r,mid,res,ans;
bool check(ll x,ll ct=0){
    for(int i=1;i<=n;i++){
        ll k=(x+a[i])/(2*a[i]);
        if(m/a[i]<k||(k&&m/k<k)||m/a[i]<k*k||(ct+=k*k*a[i])>m) return 0;
    }
    return 1;
}
int main(){
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    cin>>n>>m;r=m;
    for(int i=1;i<=n;i++) cin>>a[i];
    while(l<=r){
        mid=l+r>>1;
        if(check(mid)) res=mid,l=mid+1;
        else r=mid-1;
    }
    for(int i=1;i<=n;i++){
        ll k=(res+a[i])/(2*a[i]);
        ans+=k,m-=k*k*a[i];
    }
    cout<<ans+m/(res+1);
    return 0;
}