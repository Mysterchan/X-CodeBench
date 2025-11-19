#include <bits/stdc++.h>
#define INF 0x3f3f3f3f
#define INF_LL 0x3f3f3f3f3f3f3f3f
#define scanf(...) assert(scanf(__VA_ARGS__))
using namespace std;
using ll = long long;
using ull = unsigned long long;

const int N = 5e5 + 5;

int mp[4][4] = {{1, 0, 1, 0},
				{0, 1, 0, 1},
				{1, 0, 1, 1},
				{0, 1, 1, 1}};

int n, x, y;

int a[N], b[N];

int tmp[N];

int work(int *f) {
	int cnt = 0, len = 0;
	for (int i = 1; i <= n; ++i) {
		if (i > 1 && f[i] != f[i - 1]) {
			while (cnt--) {
				tmp[++len] = f[i - 1];
			}
			cnt = 0;
		}
		++cnt;
		if (f[i] == 0 && cnt == x) {
			cnt = 0;
			tmp[++len] = 2;
		}
		if (f[i] == 1 && cnt == y) {
			cnt = 0;
			tmp[++len] = 3;
		}
	}
	while (cnt--) {
		tmp[++len] = f[n];
	}
	for (int i = 1; i <= len; ++i) {
		f[i] = tmp[i];
	}
	return len;
}

string s, t;

int main() {
#ifdef LOCAL
	assert(freopen("test.in", "r", stdin));
	assert(freopen("test.out", "w", stdout));
#elif defined(FILE)
	assert(freopen(FILE".in", "r", stdin));
	assert(freopen(FILE".out", "w", stdout));
#endif

	cin.tie(0), cout.tie(0);
	ios::sync_with_stdio(0);
	cin >> n >> x >> y;
	cin >> s >> t;
	for (int i = 0; i < n; ++i) {
		a[i + 1] = s[i] - '0';
	}
	for (int i = 0; i < n; ++i) {
		b[i + 1] = t[i] - '0';
	}
	int l1 = work(a), l2 = work(b);


	if (l1 ^ l2) {
		cout << "No\n";
		return 0;
	}

	for (int i = 1; i <= l1; ++i) {
		int pos = -1;
		for (int j = i; j <= n; ++j) {
			if (a[j] == b[i]) {
				pos = j;
				break;
			}
		}
		if (pos == -1) {
			cout << "No\n";
			return 0;
		}
		for (int j = pos; j > i; --j) {
			if (!mp[a[j]][a[j - 1]]) {
				cout << "No\n";
				return 0;
			}
			swap(a[j], a[j - 1]);
		}
	}
	cout << "Yes\n";

	return 0;
}