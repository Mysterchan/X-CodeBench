#include<bits/stdc++.h>
#define ll long long
using namespace std;
const int MAXN=5e4+5;
const ll inf=1e18;
int n; ll a[4][MAXN],b[MAXN],h[4],L[4][MAXN],R[4][MAXN],c[4][MAXN],d[4][MAXN];
ll Q(int u,int v) {
	int p=min_element(a[v]+1,a[v]+n+1)-a[v];
	ll x=inf,y=inf,f=inf,g=inf,z=inf;
	for(int i=1;i<p;++i) f=min(f,x+a[v][i]),z=min(z,f+a[u][i]),x=min(x,a[u][i]),f=min(f,x+a[v][i]);
	for(int i=n;i>p;--i) g=min(g,y+a[v][i]),z=min(z,g+a[u][i]),y=min(y,a[u][i]),g=min(g,y+a[v][i]);
	z=min(z+a[v][p],a[v][0]+min(x,y)+min(max(x,y),a[u][p]));
	for(int i=2;i<=n-2;++i) z=min(z,a[u][i]+a[v][i+1]+c[u][i-1]+d[v][i+2]);
	return z;
}
void solve() {
	cin>>n,n-=2;
	for(int o:{0,1,2,3}) {
		ll x=inf,y=inf;
		for(int i=1;i<=n;++i) cin>>a[o][i],b[i]=a[o][i],y=min(y,max(x,b[i])),x=min(x,b[i]),L[o][i]=x+y,c[o][i]=x;
		a[o][0]=x+y,x=y=inf;
		for(int i=n;i>=1;--i) y=min(y,max(x,b[i])),x=min(x,b[i]),R[o][i]=x+y,d[o][i]=x;
		if(n>2) nth_element(b+1,b+3,b+n+1),h[o]=b[1]+b[2]+b[3];
	}
	ll z=min(min(Q(0,1),Q(1,0))+a[2][0]+a[3][0],min(Q(2,3),Q(3,2))+a[0][0]+a[1][0]);
	if(n==2) return cout<<z<<"\n",void();
	ll w1=inf,w2=inf,w3=inf,w4=inf;
	for(int i=3;i<=n-2;++i) w1=min(w1,L[0][i-1]+R[1][i+1]),w2=min(w2,L[2][i-1]+R[3][i+1]),w3=min(w3,R[0][i+1]+L[1][i-1]),w4=min(w4,R[2][i+1]+L[3][i-1]);
	cout<<min({z,h[0]+h[1]+a[2][0]+a[3][0],h[2]+h[3]+a[0][0]+a[1][0],w1+w2,w3+w4})<<"\n";
}
signed main() {
	ios::sync_with_stdio(false),cin.tie(0),cout.tie(0);
	int _; cin>>_;
	while(_--) solve();
	return 0;
}