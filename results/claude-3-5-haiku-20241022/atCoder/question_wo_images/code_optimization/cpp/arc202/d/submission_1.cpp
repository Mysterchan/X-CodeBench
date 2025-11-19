#include <bits/stdc++.h>

#define N 2000005
#define mod 998244353

typedef long long ll;

using namespace std;

ll ft[N],ftv[N],iv[N],f[N],g[N];
int rv[N];

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

ll qpow(ll a,int b)
{
	ll ans=1;
	b=(b+mod-1)%(mod-1);
	while(b){if(b&1)ans=ans*a%mod;a=a*a%mod;b>>=1;}
	return ans;
}

void ntt(ll* a,int n,int fl)
{
	for(int i=1;i<n;++i)if(i<rv[i])swap(a[i],a[rv[i]]);
	for(int k=1;k<n;k*=2)
	{
		ll w=qpow(3,fl*(mod-1)/k/2);
		for(int l=0;l<n;l+=2*k)
		{
			ll wk=1;
			for(int i=l;i<l+k;++i)
			{
				ll t=a[i+k]*wk%mod;
				a[i+k]=(a[i]-t+mod)%mod;
				a[i]=(a[i]+t)%mod;
				wk=wk*w%mod;
			}
		}
	}
}

void poly_mul(ll* a,int na,ll* b,int nb,ll* c)
{
	int n=1,lg=0;
	while(n<na+nb-1){n<<=1;lg++;}
	for(int i=1;i<n;++i)rv[i]=(rv[i>>1]>>1)|((i&1)<<(lg-1));
	
	static ll ta[N],tb[N];
	memset(ta,0,n*sizeof(ll));
	memset(tb,0,n*sizeof(ll));
	memcpy(ta,a,na*sizeof(ll));
	memcpy(tb,b,nb*sizeof(ll));
	
	ntt(ta,n,1);ntt(tb,n,1);
	ll in=qpow(n,mod-2);
	for(int i=0;i<n;++i)ta[i]=ta[i]*tb[i]%mod*in%mod;
	ntt(ta,n,-1);
	memcpy(c,ta,(na+nb-1)*sizeof(ll));
}

void calc(int l,int r,int ps,int sz,ll* A,int na,int d,ll* f)
{
	static ll B[N],C[N],tmp[N];
	auto a=[&](int x){x=(x%sz+sz)%sz;return x>=na?0:A[x];};
	
	if(l==r){f[l]=a(ps-d);return;}
	int m=(l+r)>>1;
	
	int nb;
	if(2*(m-l)+1>=sz){
		memcpy(B,A,na*sizeof(ll));
		nb=na;
	}else{
		nb=0;
		for(int i=ps-(m-l);i<=ps+(m-l);++i)B[nb++]=a(i-d);
	}
	calc(l,m,ps,sz,B,nb,2*(m-l)+1>=sz?d:ps-(m-l),f);
	
	int steps=m-l+1;
	static ll pow3[N];
	int npow=min(steps+1,sz);
	for(int i=0;i<npow;++i)pow3[i]=C(steps,i);
	
	int nres=min(na+npow-1,sz);
	poly_mul(A,na,pow3,npow,tmp);
	for(int i=nres;i<na+npow-1;++i)(tmp[i-sz]+=tmp[i])%=mod;
	
	int nc;
	if(2*(r-m-1)+1>=sz){
		memcpy(C,tmp,nres*sizeof(ll));
		nc=nres;
	}else{
		nc=0;
		int dd=d-steps;
		for(int i=ps-(r-m-1);i<=ps+(r-m-1);++i){
			int idx=(i-dd%sz+sz)%sz;
			C[nc++]=idx<nres?tmp[idx]:0;
		}
	}
	calc(m+1,r,ps,sz,C,nc,2*(r-m-1)+1>=sz?d-steps:ps-(r-m-1),f);
}

void sol(int n,int m,int s,int t,ll* f)
{
	static ll a[N],b[N],A[N];
	A[0]=1;
	for(int i=1;i<2*n+2;++i)A[i]=0;
	
	calc(0,m,abs(s-t),2*n+2,A,2*n+2,0,a);
	calc(0,m,abs(s+t-2*n-2),2*n+2,A,2*n+2,0,b);
	for(int i=0;i<=m;++i)f[i]=(a[i]-b[i]+mod)%mod;
}

int main()
{
	ll ans=0;
	int n,m,T,x1,y1,x2,y2;
	scanf("%d %d %d %d %d %d %d",&n,&m,&T,&x1,&y1,&x2,&y2);
	Cinit();
	sol(n,T,x1,x2,f);
	sol(m,T,y1,y2,g);
	for(int i=0;i<=T;++i)(ans+=((T-i)&1?-1:1)*f[i]*g[i]%mod*C(T,i))%=mod;
	printf("%lld\n",(ans+mod)%mod);
	return 0;
}