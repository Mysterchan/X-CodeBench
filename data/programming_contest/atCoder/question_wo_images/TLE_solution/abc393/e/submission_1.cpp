#include <bits/stdc++.h>
#pragma GCC optimize(3, "Ofast", "inline")
using namespace std;
const int N = 2e6 + 2, M = 1e6 + 2;
int n, k, a[N], at[M], cnt[M];
int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr), cout.tie(nullptr);
	cin >> n >> k;
	const int m = 1e6;
	for (int i = 1; i <= n; ++i) cin >> a[i], ++at[a[i]];
	for (int i = 1; i <= m; ++i)
		for (int j = i; j <= m; j += i)
			cnt[i] += at[j];
	for (int i = 1; i <= n; ++i) {
		int x = a[i], res = 1;
		for (int d = 1, li = sqrt(x); d <= li; ++d)
			if (!(x % d)) {
				if (cnt[d] >= k) res = max(res, d);
				int d2 = x / d;
				if (cnt[d2] >= k) {
					res = max(res, d2);
					break;
				}
			}
		cout << res << '\n';
	}
	return 0;
} 
