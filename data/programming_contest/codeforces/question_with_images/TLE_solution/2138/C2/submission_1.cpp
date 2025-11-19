#include <bits/stdc++.h>
using namespace std;
mt19937 rd(chrono::steady_clock::now().time_since_epoch().count());
long long rand(long long l, long long r) {
	return uniform_int_distribution<long long>(l, r)(rd);
}
const int N = 2e5 + 1;
int n, k, p[N], deg[N], h[N], cnt[N];
vector<int> adj[N];
bitset<N> cur, fix;
void reinit() {
	for (int i = 0; i <= n; ++i) {
		cnt[i] = deg[i] = 0;
	}
	cur.reset();
	fix.reset();
}
void solve() {
	cin >> n >> k;
	for (int i = 2; i <= n; ++i) {
		cin >> p[i];
		++deg[p[i]];
	}
	++cnt[0];
	int mnh = n;
	for (int i = 0; i <= k; ++i) {
		fix[i] = 1;
	}
	for (int i = 2; i <= n; ++i) {
		h[i] = h[p[i]] + 1;
		++cnt[h[i]];
		if (!deg[i]) mnh = min(mnh, h[i]);
	}
	cur[0] = 1;
	int now = n, ans = 0;
	for (int i = 0; i <= mnh; ++i) {
		cur |= (cur << cnt[i]);
		now -= cnt[i];
		int mn = max(0, k - now);
		if ((cur >> mn << (N - 1 - k + mn)).count()) ans = i + 1;
		else break;
	}
	cout << ans << '\n';
}
signed main() {
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	#ifdef LOCAL
	#else
	#endif
	int t;
	cin >> t;
	while (t--) {
		solve();
		reinit();
	}
	return 0;
}