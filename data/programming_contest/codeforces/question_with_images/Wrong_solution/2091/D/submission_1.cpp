#include<bits/stdc++.h>
#define umap unordered_map
#define pr pair
#define st first
#define nd second
#define pc putchar
#define pb push_back
#define rep(i,x,y)for(int i=x;i<=y;i++)
#define per(i,x,y)for(int i=y;i>=x;i--)
#define ws(x) (write(x),pc(' '))
#define we(x) (write(x),pc('\n'))
using namespace std;
const int N=1e5,M=1e5,mod=998244353;
inline void read(register int &a)
{
	a=0;register char c;
	register int f=1;
	while((c=getchar())<48)if(c==45)f=-1;
	do a=(a<<3)+(a<<1)+(c^48);
	while((c=getchar())>47);
	a*=f;
}
inline void write(register int x)
{
    if(x<0)putchar('-'),x=-x;
    if(x>9)write(x/10);
    putchar(x%10+'0');
}
signed main()
{
	int T;
	read(T);
	while(T--)
	{
		int n,m,k;
		read(n),read(m),read(k);
		swap(n,m);
		int l=1,r=n,ans=0;
		while(l<=r)
		{
			int mid=l+r>>1;
			if((n/(mid+1)*mid+n%(mid+1))*m>=k)
			{
				r=mid-1;
				ans=mid;
			}
			else l=mid+1;
		}
		we(ans);
	}
}