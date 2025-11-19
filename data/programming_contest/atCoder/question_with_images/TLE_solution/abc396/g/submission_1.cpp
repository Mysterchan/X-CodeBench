#include<bits/stdc++.h>
using namespace std;
using ll = long long;
const ll N=200005;
ll n,m,a[N],f[N*2];
string s;
inline ll cntbit(ll x){
	ll ret=0;
	while(x){
		if(x&1)ret++;
		x>>=1;
	}
	return ret;
}
int main(){
	cin>>n>>m;
	for(ll i=1;i<=n;++i){
		cin>>s;
		for(ll j=1;j<=m;++j){
			a[i]<<=1;
			a[i]+=(s[j-1]-'0');
		}
	}
	for(ll num=0;num<(1<<m);++num){
		f[num]=min(cntbit(num),m-cntbit(num));
	}
	ll ans=n*m;
	for(ll num=0;num<(1<<m);++num){
		if((num^((1<<m)-1))<num)continue;
		ll sum=0;
		for(ll i=1;i<=n;++i){
			sum+=f[a[i]^num];
		}
		ans=min(ans,sum);
	}
	cout<<ans<<"\n";
	return 0;
}