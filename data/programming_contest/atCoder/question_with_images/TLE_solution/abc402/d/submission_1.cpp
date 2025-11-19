#include<bits/stdc++.h>
#define ll long long
const ll N=5e5+100;
using namespace std;
ll n,m,ans;
ll a[N],b[N];
ll D(ll x,ll y){
	if(x<y)return y-x;
	else return n-x+y;
}
int main(){
    scanf("%lld%lld",&n,&m);
    for(ll i=1;i<=m;i++){
    	scanf("%lld%lld",&a[i],&b[i]);
    	if(a[i]>b[i])swap(a[i],b[i]);
	}
	for(ll i=1;i<=m;i++){
		for(ll j=i+1;j<=m;j++){
			if(D(a[i],a[j])==D(b[j],b[i]))continue;
			ans++;
		}
	}
	printf("%lld",ans);
    return 0;
} 