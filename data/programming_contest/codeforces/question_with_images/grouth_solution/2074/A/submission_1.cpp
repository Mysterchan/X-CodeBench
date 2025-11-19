#include <bits/stdc++.h>
using namespace std;

void solve(){
	vector<int> a(4);
	for(int i = 0; i < 4; i++) cin >> a[i];
	bool ok = a == vector<int>(4, a[0]);
	cout << (ok ? "YES" : "NO") << '\n';
}

int main(){
	ios_base::sync_with_stdio(false), cin.tie(nullptr);
	int T;
	cin >> T;
	while(T--) solve();
}
