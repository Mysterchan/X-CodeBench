#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
const int mod=998244353;
inline int Mod(int x) { return x<0 ? x+mod : (x>=mod ? x-mod : x); }
inline void adm(int &x,int y) { x=Mod(x+y); }
inline int qmi(ll a,int b)
{
	ll res=1;
	for (;b;b>>=1,a=a*a%mod) if (b&1) res=res*a%mod;
	return res;
}
const int N=2000010;
int fac[N],infac[N];
void init(int n)
{
	fac[0]=1; for (int i=1;i<=n;i++) fac[i]=(ll)fac[i-1]*i%mod;
	infac[n]=qmi(fac[n],mod-2); for (int i=n-1;i>=0;i--) infac[i]=(ll)infac[i+1]*(i+1)%mod;
} 
int binom(int a,int b) 
{
	if (a<0 || b<0 || a<b) return 0;
	return (ll)fac[a]*infac[a-b]%mod*infac[b]%mod;
}
int f(int n,int m) { return Mod(binom(n+m+2,n+1)-1); }
int g(int n,int m) { return Mod(binom(n+m+4,n+2)-1ll*(n+2)*(m+2)%mod-1); }
 
int main()
{
	int n,m,l,r,d,u; cin >> n >> m >> l >> r >> d >> u;
	init(n+m+4); int ans=g(n,m);
	
	adm(ans,mod-g(r-l,u-d));
	for (int i=d;i<=u;i++)
	{
		int x=r,y=i;
		adm(ans,mod-(ll)f(x-l,y-d)*f(n-x-1,m-y)%mod);
	}
	for (int i=l;i<=r;i++)
	{
		int x=i,y=u;
		adm(ans,mod-(ll)f(x-l,y-d)*f(n-x,m-y-1)%mod);
	}
	for (int i=l;i<=r;i++)
	{
		int x=i,y=d;
		adm(ans,mod-(ll)f(x,y-1)*f(n-x,m-y)%mod);
	}
	for (int i=d;i<=u;i++)
	{
		int x=l,y=i;
		adm(ans,mod-(ll)f(x-1,y)*f(n-x,m-y)%mod);
	}
	cout << ans << "\n";
		
	return 0;
}