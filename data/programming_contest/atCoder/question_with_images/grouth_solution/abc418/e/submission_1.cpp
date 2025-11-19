#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll N=2009,NN=4000009;
struct xl{ll kx,ky;} k[NN];
struct xlcd{ll kx,ky,l;} c[NN];
ll x[N],y[N];
bool cmp1(const xl&a,const xl&b){
	return a.kx<b.kx||(a.kx==b.kx&&a.ky<b.ky);
}
bool cmp2(const xlcd&a,const xlcd&b){
	return a.kx<b.kx||(a.kx==b.kx&&a.ky<b.ky)||(a.kx==b.kx&&a.ky==b.ky&&a.l<b.l);
}
int main(){
	ll n;
	cin>>n;
	for(ll i=1;i<=n;i++)cin>>x[i]>>y[i];
	ll cnt=0;
	for(ll i=1;i<n;i++){
		for(ll j=i+1;j<=n;j++){
			ll kx=x[i]-x[j],ky=y[i]-y[j];
			ll l=kx*kx+ky*ky;
			ll g=__gcd(kx,ky);
			kx/=g,ky/=g;
			cnt++;
			k[cnt]=(xl){kx,ky};
			c[cnt]=(xlcd){kx,ky,l};
		}
	}
	sort(k+1,k+1+cnt,cmp1);
	sort(c+1,c+1+cnt,cmp2);
	ll ans1=0,ans2=0,yb=1;
	while(yb<=cnt){
		ll x=yb;
		while(yb<=cnt&&k[x].kx==k[yb].kx&&k[x].ky==k[yb].ky)yb++;
		ans1+=(yb-x)*(yb-x-1)/2;
	}
	yb=1;
	while(yb<=cnt){
		ll x=yb;
		while(yb<=cnt&&c[x].kx==c[yb].kx&&c[x].ky==c[yb].ky&&c[x].l==c[yb].l)yb++;
		ans2+=(yb-x)*(yb-x-1)/2;
	}
	cout<<(ans1-ans2/2);
	return 0;
}