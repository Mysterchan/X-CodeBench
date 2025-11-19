#include <bits/stdc++.h>
#define ll long long
using namespace std;
const int MOD=998244353;
ll n,x,y;
ll f[200005],inv[200005];
ll qpow(ll a,ll b)
{
	ll res=1;
	while(b)
	{
		if(b&1)res=res*a%MOD;
		a=a*a%MOD;b>>=1;
	}
	return res;
}
ll C(ll n,ll m)
{
	return f[n]*inv[m]%MOD*inv[n-m]%MOD;
}
ll mol(ll x)
{
	return x>=MOD?x-MOD:x;
}
int main() 
{ 
    ios::sync_with_stdio(0);cin.tie(0);cout.tie(0); 
	cin>>n>>x>>y;
	f[0]=1;
	for(ll i=1;i<=n;++i)f[i]=f[i-1]*i%MOD;
	inv[n]=qpow(f[n],MOD-2);
	for(ll i=n-1;i>=0;--i)inv[i]=inv[i+1]*(i+1)%MOD;
	++x;++y;
	x&=1;y&=1;
	ll av=1,aw=0,mv=0,cv=0;
	while(n--)
	{
		ll a,b;
		cin>>a>>b;
		bool f1=(x==y?((x*a+b)&1):(x&1)?(a||(b&1)):(a<=1&&(b&1)));
		bool f2=(x==y?((x*a+b)&1):(y&1)?(a||(b&1)):(a<=1&&(b&1)));
		if(!f1&&!f2)av=mol(av*2);
		if(f1&&f2)++aw;
		if(f2)++mv;
		if(f1^f2)++cv;
	}
	ll nr=cv,res=0,sv=0;
	for(ll i=0;i<=aw;++i)
	{
		while(nr>=0&&2*i+nr>mv)sv=mol(sv+C(cv,nr--));
		res=mol(res+sv*av%MOD*C(aw,i)%MOD);
	}
	cout<<res;
}