#include <bits/stdc++.h>
#define eb emplace_back
#define pb push_back
#define int long long
using namespace std;
using ldb = long double;
using ll = long long;
using pii = pair<int, int>;
using ull = unsigned long long;
map<pii, bool> mp;
int n, m;
signed main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr), cout.tie(nullptr);
	cin >> n >> m;
	int ans = 0;
	for (int u, v, i = 0; i < m; ++i) {
		cin >> u >> v;
		if (mp[{u, v}] || u == v) ++ans;
		else mp[{u, v}] = mp[{v, u}] = true;
	}
	cout << ans;
	return 0;
} 