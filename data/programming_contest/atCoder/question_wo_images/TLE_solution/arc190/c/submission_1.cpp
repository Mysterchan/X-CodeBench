#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const int N = 2e5 + 5;
const ll mod = 998244353;

char op[N];

ll n, m, q, sx, sy, val[N];

vector<ll> a[N], b, f[N], g[N];

inline void calc1(int i) {
	for (int j = 1; j <= m; ++j) {
		f[i][j] = (f[i][j - 1] + f[i - 1][j]) * a[i][j] % mod;
	}
}

inline void calc2(int i) {
	if (i > n) {
		return;
	}
	for (int j = m; j; --j) {
		g[i][j] = (g[i][j + 1] + g[i + 1][j]) * a[i][j] % mod;
	}
}

inline ll query(int i) {
	ll res = 0;
	for (int j = 1; j <= m; ++j) {
		(res += f[i][j] * g[i + 1][j]) %= mod;
	}
	return res;
}

int main() {
#ifdef LOCAL
	assert(freopen("test.in", "r", stdin));
	assert(freopen("test.out", "w", stdout));
#endif
	ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
	cin >> n >> m;
	for (int i = 1; i <= n * m; ++i) {
		ll u;
		cin >> u;
		b.emplace_back(u);
	}
	cin >> q >> sx >> sy;
	for (int i = 1; i <= q; ++i) {
		cin >> op[i] >> val[i];
	}
	if (n > m) {
		swap(n, m);
		swap(sx, sy);
		for (int i = 0; i <= n + 1; ++i) {
			a[i].resize(m + 2);
		}
		for (int i = 1, cnt = 0; i <= m; ++i) {
			for (int j = 1; j <= n; ++j) {
				a[j][i] = b[cnt++];
			}
		}
		for (int i = 1; i <= q; ++i) {
			if (op[i] == 'L') {
				op[i] = 'U';
			} else if (op[i] == 'R') {
				op[i] = 'D';
			} else if (op[i] == 'U') {
				op[i] = 'L';
			} else {
				op[i] = 'R';
			}
		}
	} else {
		for (int i = 0; i <= n + 1; ++i) {
			a[i].resize(m + 2);
		}
		for (int i = 1, cnt = 0; i <= n; ++i) {
			for (int j = 1; j <= m; ++j) {
				a[i][j] = b[cnt++];
			}
		}
	}
	for (int i = 0; i <= n + 1; ++i) {
		f[i].resize(m + 2);
		g[i].resize(m + 2);
	}
	f[1][0] = 1;
	for (int i = 1; i <= sx; ++i) {
		calc1(i);
	}
	g[n + 1][m] = 1;
	for (int i = n; i > sx; --i) {
		calc2(i);
	}
	for (int i = 1; i <= q; ++i) {
		if (op[i] == 'L' || op[i] == 'R') {
			if (op[i] == 'L') {
				--sy;
			} else {
				++sy;
			}
			a[sx][sy] = val[i];
			calc1(sx);
		} else if (op[i] == 'U') {
			calc2(sx);
			--sx;
			a[sx][sy] = val[i];
			calc1(sx);
		} else {
			++sx;
			a[sx][sy] = val[i];
			calc1(sx);
		}
		cout << query(sx) << "\n";
	}
	return 0;
}