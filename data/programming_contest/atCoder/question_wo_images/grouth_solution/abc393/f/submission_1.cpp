#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#define eb emplace_back
#define pb push_back
#define int long long
using namespace std;
using namespace __gnu_pbds;
using ldb = long double;
using ll = long long;
using pii = pair<int, int>;
using ull = unsigned long long;
const int N = 2e5 + 2;
int n, q, a[N], num[N], rt[N];
struct node {
	int ls, rs, mx;
} t[N * 120];
int idx;
void update(int &x, int y, int l, int r, int pos, int val) {
	t[x = ++idx] = t[y];
	if (l == r) {
		t[x].mx = max(t[x].mx, val);
		return;
	}
	int mid = l + r >> 1;
	if (pos <= mid) update(t[x].ls, t[y].ls, l, mid, pos, val);
	else update(t[x].rs, t[y].rs, mid + 1, r, pos, val);
	t[x].mx = max(t[t[x].ls].mx, t[t[x].rs].mx);
}
int query(int u, int l, int r, int ql, int qr) {
	if (!u) return 0;
	if (ql <= l && r <= qr) return t[u].mx;
	int mid = l + r >> 1;
	if (ql <= mid && mid < qr)
		return max(query(t[u].ls, l, mid, ql, qr), query(t[u].rs, mid + 1, r, ql, qr));
	if (ql <= mid) return query(t[u].ls, l, mid, ql, qr);
	return query(t[u].rs, mid + 1, r, ql, qr);
}
signed main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr), cout.tie(nullptr);
	cin >> n >> q;
	for (int i = 1; i <= n; ++i) cin >> a[i], num[i] = a[i];
	sort(num + 1, num + n + 1);
	int tot = unique(num + 1, num + n + 1) - num - 1;
	for (int i = 1; i <= n; ++i)
		a[i] = lower_bound(num + 1, num + tot + 1, a[i]) - num;
	for (int i = 1; i <= n; ++i) {
		int x = a[i] > 1 ? query(rt[i - 1], 1, tot, 1, a[i] - 1) : 0;
		update(rt[i], rt[i - 1], 1, tot, a[i], x + 1);
	}
	num[tot + 1] = 2e9;
	for (int r, x; q; --q) {
		cin >> r >> x;
		x = upper_bound(num + 1, num + tot + 2, x) - num - 1;
		cout << query(rt[r], 1, tot, 1, x) << '\n';
	}
	return 0;
} 