#include <iostream>
using namespace std;
typedef long long ll;

const int mod = 998244353;
ll fac[5000005],inv[5000005];

ll pow(ll a, ll b) {
	ll re = 1;
	while (b) {
		if (b & 1) re = re*a%mod;
		a = a*a%mod; b >>= 1;
	}
	return re;
}
ll C(ll n, ll m) {
	return fac[n]*inv[m]%mod*inv[n-m]%mod;
}
ll f(ll n, ll m) {
	return (C(n+m+2,m+1)+mod-1)%mod;
}
ll g(ll n, ll m) {
	return ((C(n+m+4,n+2)-1-(n+2)*(m+2)%mod)%mod+mod)%mod;
}

int main() {
	fac[0] = inv[0] = 1;
	for (int i = 1; i <= 5e6; i++) {
		fac[i] = fac[i-1]*i;
		inv[i] = pow(fac[i],mod-2);
	}
	ll n,m,l,r,d,u;
	cin >> n >> m >> l >> r >> d >> u;
	ll ans = ((g(n,m)-g(r-l,u-d))%mod+mod)%mod;
	for (int i = l; i <= r; i++) ans = ((ans-f(i,d-1)*f(n-i,m-d)%mod)%mod+mod)%mod;
	for (int j = d; j <= u; j++) ans = ((ans-f(l-1,j)*f(n-l,m-j)%mod)%mod+mod)%mod;
	for (int i = l; i <= r; i++) ans = ((ans-f(n-i,m-u-1)*f(i-l,u-d)%mod)%mod+mod)%mod;
	for (int j = d; j <= u; j++) ans = ((ans-f(n-r-1,m-j)*f(r-l,j-d)%mod)%mod+mod)%mod;
	cout << ans;
	return 0;
}