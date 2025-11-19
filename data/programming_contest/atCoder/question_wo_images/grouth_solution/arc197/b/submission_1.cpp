#include<bits/stdc++.h>
#define int long long
using namespace std;
const int N=2e5+10;
int T,n,a[N],sum[N];
signed main()
{
	cin.tie(0)->sync_with_stdio(0);
	cin>>T;
	while(T--)
	{
		cin>>n;
		for(int i=1; i<=n; i++)cin>>a[i];
		sort(a+1,a+n+1);
		for(int i=1; i<=n; i++)sum[i]=sum[i-1]+a[i];
		int ans=0;
		for(int i=1; i<=n; i++)
		{
			int l=i-1,r=n+1,mid;
			while(l+1<r)
			{
				int mid=l+r>>1;
				if(sum[mid]<a[i]*mid)l=mid;
				else r=mid;
			}
			ans=max(ans,l-i+1);
		}
		cout<<ans<<'\n';
	}
	return 0;
}