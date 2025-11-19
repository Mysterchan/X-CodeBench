#include<bits/stdc++.h>
#define int long long 
#define MAXN 200005 
const int mod=998244353;
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
template<class T>void inc(T&a,T b){a=a+b>=mod?a+b-mod:a+b;}
template<class T>void dec(T&a,T b){a=a>=b?a-b:a+mod-b;}
template<class T>int sub(T a,T b){return a>=b?a-b:a+mod-b;}
int n,a[MAXN],pw[MAXN],p[MAXN],ans;
namespace segtr{
#define ls x<<1
#define rs x<<1|1
#define mid (l+r>>1)
	int seg[MAXN<<2],tag[MAXN<<2];
	void up(int x){seg[x]=(seg[ls]+seg[rs])%mod;}
	void addtag(int x,int w){tag[x]=tag[x]*w%mod,seg[x]=seg[x]*w%mod;}
	void down(int x){
		if(tag[x]==1)return;
		addtag(ls,tag[x]),addtag(rs,tag[x]);
		tag[x]=1;
	}
	void build(int x,int l,int r){
		tag[x]=1;
		if(l==r)return seg[x]=1,void();
		build(ls,l,mid),build(rs,mid+1,r);
		up(x);
	}
	void upd(int x,int l,int r,int ql,int qr,int w){
		if(l>qr||r<ql)return;
		if(l>=ql&&r<=qr)return addtag(x,w),void();
		down(x);if(ql<=mid)upd(ls,l,mid,ql,qr,w);
		if(mid<qr)upd(rs,mid+1,r,ql,qr,w);
		up(x);
	}
#undef ls 
#undef rs 
#undef mid 
}using namespace segtr;
void calc(){
	build(1,1,n-1);
	for(int i=1;i<n;i++){
		upd(1,1,n-1,a[i],n-1,2ll);
		inc(ans,seg[1]);
	}
	for(int i=1;i<n;i++)dec(ans,(n-1)*pw[i]%mod);
}
signed main(){
	n=gi();pw[0]=1;
	for(int i=1;i<=n;i++)a[i]=gi(),p[a[i]]=i,pw[i]=pw[i-1]*2ll%mod;
	calc();
	std::reverse(a+1,a+n+1);calc();
	for(int i=1;i<=n;i++)a[i]=n-a[i]+1;calc();
	std::reverse(a+1,a+n+1);calc();
	inc(ans,(n-1)*(n-1)%mod*sub(pw[n],1ll)%mod);
	printf("%lld\n",ans);
	return 0;
}
