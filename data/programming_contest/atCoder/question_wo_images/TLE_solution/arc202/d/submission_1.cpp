#include <bits/stdc++.h>

#define N 2000005
#define mod 998244353

typedef long long ll;

using namespace std;

ll ft[N],ftv[N],iv[N],f[N],g[N];
ll C(int n,int m){return n>=m&&m>=0?ft[n]*ftv[m]%mod*ftv[n-m]%mod:0;}
void Cinit()
{
	ft[0]=ftv[0]=1;
	for(int i=1;i<N;++i)
	{
		ft[i]=ft[i-1]*i%mod;
		iv[i]=i==1?1:(mod-mod/i)*iv[mod%i]%mod;
		ftv[i]=ftv[i-1]*iv[i]%mod;
	}
}
ll qpow(ll a,int b){ll ans=1;b=(b+mod-1)%(mod-1);while(b){if(b&1)ans=ans*a%mod;a=a*a%mod;b>>=1;}return ans;}
void ntt(vector<ll>& a,int n,int fl)
{
	int i,k,l;
	static int rv[N*4];a.resize(n);
	for(i=1;i<n;++i){rv[i]=(rv[i>>1]>>1)|(i&1)*(n/2);if(i<rv[i])swap(a[i],a[rv[i]]);}
	for(k=1;k<n;k*=2)
	{
		ll w=qpow(3,fl*(mod-1)/k/2);
		for(l=0;l<n;l+=2*k)
		{
			ll wk=1;
			for(i=l;i<l+k;++i)
			{
				a[i+k]=(a[i]-a[i+k]*wk%mod+mod)%mod;
				a[i]=(2*a[i]-a[i+k]+mod)%mod;
				wk=wk*w%mod;
			}
		}
	}
}
vector<ll> operator*(vector<ll> a,vector<ll> b)
{
	int n=1<<__lg(a.size()+b.size()-2)+1;
	ntt(a,n,1);ntt(b,n,1);ll in=qpow(n,mod-2);
	for(int i=0;i<n;++i)a[i]=a[i]*b[i]%mod*in%mod;ntt(a,n,-1);
	while(!a.empty()&&a.back()==0)a.pop_back();
	return a;
}
void pmod(vector<ll>& a,int s){while(a.size()>s){(*(a.end()-s-1)+=a.back())%=mod;a.pop_back();}}
vector<ll> qpow(vector<ll> a,int b,int s=N)
{
	vector<ll> ans={1};
	while(b)
	{
		if(b&1){ans=ans*a;pmod(ans,s);}
		a=a*a;pmod(a,s);b>>=1;
	}
	return ans;
}
void calc(int l,int r,int ps,int sz,vector<ll> A,int d,ll* f)
{
	vector<ll>B,C;
	auto a=[&](int x){x=(x%sz+sz)%sz;return x>=A.size()?0:A[x];};
	if(l==r){f[l]=a(ps-d);return;}
	int m=(l+r)>>1,dl,dr;

	if(2*(m-l)+1>=sz){B=A;dl=d;}
	else{dl=ps-(m-l);for(int i=ps-(m-l);i<=ps+(m-l);++i)B.push_back(a(i-d));}
	calc(l,m,ps,sz,B,dl,f);

	A=A*qpow({1,1,1},m-l+1,sz);pmod(A,sz);d-=(m-l+1);

	if(2*(r-m-1)+1>=sz){C=A;dr=d;}
	else{dr=ps-(r-m-1);for(int i=ps-(r-m-1);i<=ps+(r-m-1);++i)C.push_back(a(i-d));}
	calc(m+1,r,ps,sz,C,dr,f);
}

void sol(int n,int m,int s,int t,ll* f)
{
	static ll a[N],b[N];
	vector<ll>A;A.push_back(1);for(int i=1;i<2*n+2;++i)A.push_back(0);
	calc(0,m,abs(s-t),2*n+2,A,0,a);
	calc(0,m,abs(s+t-2*n-2),2*n+2,A,0,b);
	for(int i=0;i<=m;++i)f[i]=(a[i]-b[i]+mod)%mod;
}

int main()
{
	ll ans=0;
	int i,n,m,T,x1,y1,x2,y2;
	scanf("%d %d %d %d %d %d %d",&n,&m,&T,&x1,&y1,&x2,&y2);
	Cinit();sol(n,T,x1,x2,f);sol(m,T,y1,y2,g);
	for(i=0;i<=T;++i)(ans+=((T-i)&1?-1:1)*f[i]*g[i]%mod*C(T,i))%=mod;
	printf("%lld\n",(ans+mod)%mod);
	return 0;
}
