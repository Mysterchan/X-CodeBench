#include <bits/stdc++.h>
#define int long long int
using namespace std;

signed main() {
	ios::sync_with_stdio(false); cin.tie(0);
	int n;
	string s;
	cin >> n >> s;
	
	vector<int> ones;
	for (int i = 0; i < n; i++) {
		if (s[i] == '1') {
			ones.push_back(i);
		}
	}
	
	int cnt = ones.size();
	int ans = LLONG_MAX;
	
	for (int i = 0; i < cnt; i++) {
		int cost = 0;
		for (int j = 0; j < cnt; j++) {
			cost += abs(ones[j] - (ones[i] + j));
		}
		ans = min(ans, cost);
	}
	
	cout << ans;
	return 0;
}