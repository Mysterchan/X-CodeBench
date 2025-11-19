#include <bits/stdc++.h>
#define int long long
using namespace std;
const int N = 4e5 + 10;
const int inf = 1e18;
int n, q;
int pre[N], suf[N];
struct node { int l, r, w, id; } a[N];
inline bool check(node x, node y) {
	if (x.l > y.r || y.l > x.r) return true;
	return false;
}
inline bool in(node x, node y) {
	if (x.l <= y.l && y.r <= x.r) return true;
	if (y.l <= x.l && x.r <= y.r) return true;
	return false;
}
signed main() {
	freopen("tangua.in", "r", stdin);
	freopen("tangua.out", "w", stdout);
	ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
	cin >> n;
	for (int i = 1; i <= n; i++) cin >> a[i].w, a[i].id = i;
	for (int i = 1; i <= n; i++) cin >> a[i].l >> a[i].r;
	for (int i = 0; i <= n + n + 1; i++) pre[i] = suf[i] = inf;
	for (int i = 1; i <= n; i++) {
		pre[a[i].r] = min(pre[a[i].r], a[i].w);
		suf[a[i].l] = min(suf[a[i].l], a[i].w);
	}
	for (int i = 1; i <= n + n; i++) pre[i] = min(pre[i], pre[i - 1]);
	for (int i = n + n; i >= 1; i--) suf[i] = min(suf[i + 1], suf[i]);
	cin >> q;
	for (int s, t; q--;) {
		cin >> s >> t;
		if (check(a[s], a[t])) cout << a[s].w + a[t].w << '\n';
		else if (in(a[s], a[t])) {
			int L = min(a[s].l, a[t].l) - 1, R = max(a[s].r, a[t].r) + 1;
			int ans = min(pre[L], suf[R]);
			if (ans < inf) cout << ans + a[s].w + a[t].w << '\n';
			else cout << "-1\n";
		} else {
			int L1 = min(a[s].l, a[t].l) - 1, L2 = max(a[s].l, a[t].l) - 1;
			int R1 = max(a[s].r, a[t].r) + 1, R2 = min(a[s].r, a[t].r) + 1;
			int ans = min({pre[L1], suf[R1], pre[L2] + suf[R2]});
			if (ans < inf) cout << ans + a[s].w + a[t].w << '\n';
			else cout << "-1\n";
		}
	}
}