#include<bits/stdc++.h>
#define int long long 
#define MAXN 1000005 
int gi(){
	char c;int x=0,f=0;
	while(!isdigit(c=getchar()))f|=(c=='-');
	while(isdigit(c))x=(x*10)+(c^48),c=getchar();
	return f?-x:x;
}
std::mt19937 rnd(std::random_device{}());
#define pr std::pair<int,int>
#define all(x) (x).begin(),(x).end()
#define mem(x,w) memset(x,w,sizeof(x))
#define sz(x) (int)((x).size())
#define eb emplace_back
#define fi first
#define se second
template<class T>void cxk(T&a,T b){a=a>b?a:b;}
template<class T>void cnk(T&a,T b){a=a<b?a:b;}
int n,m,a[MAXN],b[MAXN];
bool chk(int x){
	for(int i=1;i<=n;i++)if(b[i+x]<a[i])return 0;
	return 1;
}
void work(){
	n=gi(),m=gi();
	for(int i=1;i<=n;i++)a[i]=gi(),a[i]=(-a[i]%m+m)%m;
	for(int i=1;i<=n;i++)b[i]=gi();
	std::sort(a+1,a+n+1),std::sort(b+1,b+n+1);
	for(int i=1;i<=n;i++)b[i+n]=b[i]+m;
	int l=0,r=n+1,mid,p=0;
	while(l+1<r)mid=l+r>>1,chk(mid)?r=p=mid:l=mid;
	int ans=0;for(int i=1;i<=n;i++)cxk(ans,(b[i+p]-a[i])%m);
	printf("%lld\n",ans);
}
signed main(){
	int t=gi();while(t--)work();
	return 0;
}
