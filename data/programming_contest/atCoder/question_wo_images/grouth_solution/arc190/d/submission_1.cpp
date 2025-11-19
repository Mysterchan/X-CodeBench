#include <bits/stdc++.h>
#define INF 0x3f3f3f3f
#define INF_LL 0x3f3f3f3f3f3f3f3f
#define scanf(...) assert(scanf(__VA_ARGS__))
using namespace std;
using ll = long long;
using ull = unsigned long long;

const int N = 100 + 5;

int n, P;

int qpow(int b) {
	return (b & 1 ? P - 1 : 1);
}

int tmp[N][N];
void mul(int (*a)[N], int (*b)[N]) {
	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j <= n; ++j) {
			tmp[i][j] = 0;
		}
	}
	for (int i = 1; i <= n; ++i) {
		for (int k = 1; k <= n; ++k) {
			int val = a[i][k];
			if (!val) {
				continue;
			}
			for (int j = 1; j <= n; ++j) {
				tmp[i][j] = (tmp[i][j] + 1ll * val * b[k][j]) % P;
			}
		}
	}
	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j <= n; ++j) {
			a[i][j] = tmp[i][j];
		}
	}
}

int a[N][N], b[N][N], c[N][N];

int main() {
#ifdef LOCAL
	assert(freopen("test.in", "r", stdin));
	assert(freopen("test.out", "w", stdout));
#elif defined(FILE)
	assert(freopen(FILE".in", "r", stdin));
	assert(freopen(FILE".out", "w", stdout));
#endif

	cin.tie(0), cout.tie(0);
	cin >> n >> P;

	int num = 0;
	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j <= n; ++j) {
			cin >> a[i][j];
			b[i][j] = a[i][j];
			num += (!a[i][j]);
		}
	}
	for (int i = 1; i <= n; ++i) {
		c[i][i] = 1;
	}

	if (P == 2) {
		for (int i = 1; i <= n; ++i) {
			for (int j = 1; j <= n; ++j) {
				if (!b[i][j]) {
					b[i][j] = 1;
				}
			}
		}
	}

	int k = P;
	while (k) {
		if (k & 1) {
			mul(c, b);
		}
		mul(b, b);
		k >>= 1;
	}

	if (P == 2) {
		for (int i = 1; i <= n; ++i) {
			for (int j = 1; j <= n; ++j) {
				cout << c[i][j] << ' ';
			}
			cout << '\n';
		}
		return 0;
	}

	if (P == 3) {
		for (int i = 1; i <= n; ++i) {
			for (int j = 1; j <= n; ++j) {
				if (i == j || !a[j][i] || a[i][j]) {
					continue;
				}
				c[i][j] = (c[i][j] + a[j][i]) % P;
			}
		}
	}

	for (int i = 1; i <= n; ++i) {
		if (!a[i][i]) {
			for (int j = 1; j <= n; ++j) {
				if (a[i][j]) {
					c[i][j] = (c[i][j] + a[i][j]) % P;
				}
				if (a[j][i]) {
					c[j][i] = (c[j][i] + a[j][i]) % P;
				}
			}
		}
	}

	int tmp = qpow(num);
	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j <= n; ++j) {
			cout << 1ll * c[i][j] * tmp % P << ' ';
		}
		cout << '\n';
	}

	return 0;
}