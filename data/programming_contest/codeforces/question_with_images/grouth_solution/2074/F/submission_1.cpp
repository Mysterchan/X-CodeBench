#include <bits/stdc++.h>
using namespace std;

using ll = int64_t;

void solve(){
	ll lx, rx, ly, ry;
	cin >> lx >> rx >> ly >> ry;
	ll ans = 0;
	while(true){
		if(lx == rx || ly == ry) break;
		if(lx & 1){
			ans += (ry - ly);
			lx += 1;
		}
		if(lx == rx || ly == ry) break;
		if(rx & 1){
			ans += (ry - ly);
			rx -= 1;
		}
		if(lx == rx || ly == ry) break;
		if(ly & 1){
			ans += (rx - lx);
			ly += 1;
		}
		if(lx == rx || ly == ry) break;
		if(ry & 1){
			ans += (rx - lx);
			ry -= 1;
		}
		if(lx == rx || ly == ry) break;
		lx /= 2; rx /= 2; ly /= 2; ry /= 2;
	}
	cout << ans << '\n';
}

int main(){
	ios_base::sync_with_stdio(false), cin.tie(nullptr);
	int T;
	cin >> T;
	while(T--) solve();
}
