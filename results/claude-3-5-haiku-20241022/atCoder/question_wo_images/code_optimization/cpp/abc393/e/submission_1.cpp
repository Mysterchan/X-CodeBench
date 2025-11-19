#include <bits/stdc++.h>
using namespace std;

const int M = 1e6 + 2;
int n, k, cnt[M], ans[M];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
	cin >> n >> k;
	const int m = 1e6;
	
	vector<int> a(n);
	for (int i = 0; i < n; ++i) {
		cin >> a[i];
		++cnt[a[i]];
	}
	
	// Compute cnt[i] = count of elements divisible by i
	for (int i = 1; i <= m; ++i)
		for (int j = i; j <= m; j += i)
			cnt[i] += cnt[j / i];
	
	// For each divisor d, find the maximum d such that cnt[d] >= k
	for (int d = m; d >= 1; --d) {
		if (cnt[d] >= k) {
			for (int j = d; j <= m; j += d) {
				if (!ans[j]) ans[j] = d;
			}
		}
	}
	
	// Output answer for each element
	for (int i = 0; i < n; ++i) {
		cout << ans[a[i]] << '\n';
	}
	
	return 0;
}