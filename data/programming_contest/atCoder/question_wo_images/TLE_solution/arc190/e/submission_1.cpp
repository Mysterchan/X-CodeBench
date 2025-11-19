#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,n) for (int i=a;i<n;i++)
#define per(i,a,n) for (int i=n-1;i>=a;i--)
#define pb push_back
#define eb emplace_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define fi first
#define se second
#define SZ(x) ((int)(x).size())
typedef vector<int> VI;
typedef basic_string<int> BI;
typedef long long ll;
typedef pair<int,int> PII;
typedef double db;
mt19937 mrand(random_device{}()); 
ll mod;
int rnd(int x) { return mrand() % x;}
ll gcd(ll a,ll b) { return b?gcd(b,a%b):a;}

const int N=201000;
int n,q,a[N];
ll dp[5][5],pd[5][5];
int main() {
	scanf("%d%d",&n,&q);
	for (int i=1;i<=n;i++) {
		scanf("%d",&a[i]);
	}
	rep(i,0,q) {
		int l,r;
		scanf("%d%d",&l,&r);
		memset(dp,0,sizeof(dp));
		rep(j,l,r+1) {
			rep(c1,0,3) rep(c2,0,3) pd[c1][c2]=dp[c1][c2],dp[c1][c2]=1ll<<60;
			rep(c1,0,3) rep(c2,0,3) rep(c3,0,3) if (c1+c3>=2&&c2+c3>=2) {
				dp[c2][c3]=min(dp[c2][c3],pd[c1][c2]+c3*a[j]);
			}
		}
		ll ans=1ll<<60;
		rep(c1,0,3) rep(c2,0,3) ans=min(ans,dp[c1][c2]);
		printf("%lld\n",ans/2);
	}
}