#include<bits/stdc++.h>
using namespace std;
using ll=long long;
const ll M=1e7+10,mod=998244353;
ll n,q,a,b,fac[M],facinv[M],cm[M],ans[M];
ll pw(ll x,ll y){
	ll res=1;
	while(y){
		if(y&1)res=res*x%mod;
		x=x*x%mod,y>>=1;
	}
	return res;
}
ll c(ll x,ll y){
	if(y>x)return 0;
	return fac[x]*facinv[y]%mod*facinv[x-y]%mod;
}
void solve(ll x,ll y){
	ll s=0;
	for(int i=n;i;i--){
		ll t=n-i;
		if(i<n){
			s=(s*2-c(t-1,y-1)+mod)%mod;
			if(y-i>=1)s=(s-c(t-1,y-i-1)+mod)%mod;
		}else s=1;
		ans[i]=(ans[i]+s*c(t,x-1)%mod)%mod;
		ans[i]=(ans[i]-c(t,x-1)*c(t,y-1)%mod+mod)%mod;
	}
	s=0;
	for(int i=n;i;i--){
		ll t=n-i;
		if(i<n){
			s=(s*2-c(t-1,x-1)+mod)%mod;
			if(x-i>=1)s=(s-c(t-1,x-i-1)+mod)%mod;
		}else s=1;
		ans[i]=(ans[i]+s*c(t,y-1)%mod)%mod;
	}
}
int main(){
	cin>>n>>a>>b;
	fac[0]=facinv[0]=1;
	for(int i=1;i<=n;i++)fac[i]=fac[i-1]*i%mod;
	facinv[n]=pw(fac[n],mod-2);
	for(int i=n-1;i;i--)facinv[i]=facinv[i+1]*(i+1)%mod;
	cm[0]=pw(4,mod-2);
	for(int i=1;i<=n;i++)cm[i]=cm[i-1]*4%mod;
	solve(a,b),solve(a,n-b+1),solve(n-a+1,b),solve(n-a+1,n-b+1);
	cin>>q;
	while(q--){
		int x;cin>>x;
		cout<<ans[x]*cm[x-1]%mod<<'\n';
	}
}