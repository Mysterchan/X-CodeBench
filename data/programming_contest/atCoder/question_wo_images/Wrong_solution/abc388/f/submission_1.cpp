#include <bits/stdc++.h>

using i64 = long long;
using pii = std::pair<int, int>;

const int mod = 1e9 + 7;
const int N = 1e5;

#define int i64

signed main() {
	std::ios::sync_with_stdio(false);
	std::cin.tie(0);

	i64 n, m, a, b;
	std::cin >> n >> m >> a >> b;
	std::vector<std::pair<i64, i64>> pv(m);
	for (int i = 0; i < m; i++) {
		std::cin >> pv[i].first >> pv[i].second;
	} 
	std::vector<std::pair<i64, i64>> v;
	for (int i = 0; i < m; ) {
		int j = i + 1;
		while (j < m && pv[j].first - pv[j - 1].second == 1) {
			j++;
		}
		v.push_back({pv[i].first, pv[j - 1].second});
		i = j;
	}
	i64 curr = 1;
	for (int i = 0; i < v.size(); i++) {
		i64 cnt = (v[i].first - curr) / a;
		curr += cnt * a;
		curr = std::min(v[i].first - 1, curr + cnt * (b - a));
		if (v[i].second - curr >= b) {
			std::cout << "No" << '\n';
			return 0;
		}
	}
	i64 final = (n - curr) / a;
	curr += final * a;
	curr = std::min(n, curr + final * (b - a));
	std::cout << (curr == n ? "Yes" : "No") << '\n';

	return 0;
}