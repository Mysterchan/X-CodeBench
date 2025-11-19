#include<bits/stdc++.h>
typedef long long LL;
#define int LL
#ifdef WIN32
#define getchar _getchar_nolock
#define putchar _putchar_nolock
#else
#define getchar getchar_unlocked
#define putchar putchar_unlocked
#endif
using namespace std;
namespace my
{
	namespace fastIO
	{
		inline char get_char()
		{
			char c=getchar();
			for(;c<=32&&c!=EOF;c=getchar());
			return c;
		}
		inline int read()
		{
			int x=0,f=1;
			char c=getchar();
			for(;c<'0'||c>'9';c=getchar()){if(c=='-') f=-1;if(c==EOF) return c;}
			for(;c>='0'&&c<='9';c=getchar()) x=(x<<3)+(x<<1)+c-48;
			return x*f;
		}
		inline void write(int x)
		{
			if(x<0) putchar('-'),x=-x;
			if(x>9) write(x/10);
			putchar(x%10+48);
		}
		inline void file()
		{
			freopen(".in","r",stdin);
			freopen(".out","w",stdout);
		}
		inline void close()
		{
			fclose(stdin);
			fclose(stdout);
		}
		inline void fast()
		{
			ios::sync_with_stdio(false);
			cin.tie(NULL);
			cout.tie(NULL);
		}
	}
	using namespace fastIO;
	const int N=1e6+1;
	int n=5,ans=0,a[N];
	int main()
	{
		for(int i=1;i<=n;++i) a[i]=read();
		bool ok=false;
		for(;!ok;){
			for(int i=1;i<n&&ans>1;++i)
				if(a[i]>a[i+1]){
					++ans;
					swap(a[i],a[i+1]);
					ok=false;
				}
		}
		if(ans!=1){
			printf("No");
			return 0;
		}
		printf("Yes");
		return 0;
	}
}
signed main()
{
	my::main();
	return 0;
}
