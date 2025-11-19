#include <cstdio>
#include <functional>
#include <algorithm>

using namespace std;

const int N=6.3e5;

int a[N],b[N];

int main()
{
	int T;scanf("%d",&T);while(T--){
		int n,M,ans=0;scanf("%d%d",&n,&M);
		for(int i=1;i<=n;++i) scanf("%d",a+i);
		for(int i=1;i<=n;++i) scanf("%d",b+i);
		sort(a+1,a+n+1,greater<int>());sort(b+1,b+n+1);
		for(int i=1;i<=n;++i) a[i+n]=a[i]-M;
		int l=1,r=n+1,p;while(l<=r){
			int m=l+r>>1;bool flg=1;
			for(int i=n-m+2;i<=n;++i) flg&=b[i]+a[i+m-1]>=0;
			flg?(p=m,l=m+1):r=m-1;
		}
		for(int i=1;i<=n;++i) ans=max(ans,a[i+p-1]+b[i]);
		printf("%d\n",ans);
	}
}