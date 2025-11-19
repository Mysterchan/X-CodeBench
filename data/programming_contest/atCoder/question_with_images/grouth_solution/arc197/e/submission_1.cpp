#include <bits/stdc++.h>
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
const int mod=998244353,inv2=499122177,inv24=291154603;
int n,h,w;
signed main()
{
	__BEGIN_MULTITEST__
	scanf("%d%d%d",&n,&h,&w);
	if(min(h,w)<2*n)
		printf("0\n");
	else
	{
		h-=2*n-2;
		w-=2*n-2;
		auto C2=[](int x) -> ll {return 1ll*x*(x-1)%mod*inv2%mod;};
		auto C4=[](int x) -> ll {return 1ll*x*(x-1)%mod*(x-2)%mod*(x-3)%mod*inv24%mod;};
		auto sqr=[](int x) -> ll {return 1ll*x*x%mod;};
		printf("%lld\n",(sqr(C2(h)*C2(w)%mod)-C4(h+1)*C4(w+1)%mod*2%mod+mod)%mod);
	}
	__END_MULTITEST__
	return 0;
}