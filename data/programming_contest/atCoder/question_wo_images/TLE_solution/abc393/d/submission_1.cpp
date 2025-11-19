#include <bits/stdc++.h>
#define int long long int
using namespace std;

int n;
string s;

signed main() {
	ios::sync_with_stdio(false); cin.tie(0);
	cin >> n >> s; s = ' ' + s;
	int sum = 0, cnt = 0;
	for (int i = 1; i <= n; i++) {
		if (s[i] == '1') {
			sum += i;
			cnt ++;
		}
	}
	int mid = sum / cnt;
	int pos = 0, dis = 0x3f3f3f3f;
	int ans = 0x3f3f3f3f;
	for (pos = 1; pos <= n; pos ++) {
		if (s[pos] != '1') continue;
		int p = mid, t = 0;
		for (int i = pos; i <= n; i++) {
			if (s[i] == '1') {
				t += abs(i - p); p ++;
			}
		}
		p = mid - 1;
		for (int i = pos - 1; i >= 1; i--) {
			if (s[i] == '1') {
				t += abs(p - i); p --;
			}
		}
		ans = min(ans, t);
	}
	cout << ans;
	return 0;
}