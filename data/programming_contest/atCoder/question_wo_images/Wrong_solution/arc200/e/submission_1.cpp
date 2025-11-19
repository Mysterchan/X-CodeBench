#include <bits/stdc++.h>
#define int long long
#define INLINE inline __attribute__((always_inline))
#define __BEGIN_MULTITEST__ \
		signed T; \
		scanf("%d",&T); \
		while(T--) \
		{
#define __END_MULTITEST__ }
using ll=long long;
using i128=__int128;
using namespace std;
const int mod=998244353,inv2=mod+1>>1,inv3=(mod+1)/3;
int n,m;
auto quick_pow=[](int a,int b)
{
	int ret=1;
	while(b)
	{
		if(b&1)
			ret=1ll*ret*a%mod;
		a=1ll*a*a%mod;
		b>>=1;
	}
	return ret;
};
signed main()
{
	__BEGIN_MULTITEST__
	scanf("%lld%lld",&n,&m);
	n--;
	int pw=quick_pow(2,n),pw3=quick_pow(3,n),pw4=quick_pow(4,n);
	int ans=((m+1)*m%mod*inv2%mod*(pw-1)+1)%mod;
	if(n>=3)
		(ans+=(m+1)*((quick_pow(m+1,n)-m*(pw-1)%mod-1+mod)%mod)%mod+(m+1)*m%mod*(m-1)%mod*inv2%mod*inv3%mod*((pw4%mod-3*(pw3-pw)%mod-1+mod)%mod)%mod)%=mod;
	printf("%lld\n",ans*quick_pow(2,m)%mod);
	__END_MULTITEST__
	return 0;
}