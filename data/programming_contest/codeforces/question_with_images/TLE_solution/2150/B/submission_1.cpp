#include<bits/stdc++.h>
using namespace std;
#define ll long long
const int MAXN=2e5+5,MOD=998244353;
ll ksm(ll a,int b){ll r=1;while(b){if(b&1)r=r*a%MOD;a=a*a%MOD,b>>=1;}return r;}
int n,a[MAXN],b[MAXN];ll inf[MAXN],fac[MAXN];
void solve(){
	cin>>n;
	for(int i=1;i<=n;i++) cin>>a[i],b[i]=0;
	for(int i=1;i<=n;i++) b[min(i,n+1-i)]++;
	ll ans=1,c=0;
	for(int i=n;i>=1;i--){
		c+=b[i];
		(ans*=inf[a[i]])%=MOD;
		while(a[i]>0) (ans*=(c--))%=MOD,a[i]--;

	}
	cout<<(c==0?ans:0)<<'\n';
}
int main(){
	ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
	inf[0]=fac[0]=1;
	for(int i=1;i<MAXN;i++) inf[i]=ksm(fac[i]=fac[i-1]*i%MOD,MOD-2);
	int T;cin>>T;
	while(T--) solve();
	return 0;
}
