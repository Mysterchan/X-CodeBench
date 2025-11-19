#include <bits/stdc++.h>
using namespace std;

int n, k;
set<int> adj[200005];
bool explored[200005];
int cnt[200005];

int dfs(int v, int p, int d) {
	int mx = 0;
	for (int e : adj[v]) {
		if (e == p) continue;
		mx = min(mx, dfs(e, v, d + 1));
	}
	return d;
}

void solve() {
	cin >> n >> k;
	for (int i = 1; i < n; i++) {
		int u;
		cin >> u;
		u--;
		adj[i].insert(u);
		adj[u].insert(i);
	}
	
	int asdf = 0;
	int mn = dfs(0, 0, 1);
	for (int _ = 0; _ < 2; _++) {
		queue<int> q;
		q.push(0);
		explored[0] = true;
		int run = 0;
		while (!q.empty()) {
			run++;
			int sz = q.size();
			for (int i = 0; i < sz; i++) {
				int v = q.front();
				cnt[run]++;
				q.pop();
				for (int e : adj[v]) {
					if (explored[e]) continue;
					q.push(e);
					explored[e] = true;
				}
			}
		}

		run = 0;
		int ans = 0;
		for (int i = 1; i <= n + 1; i++) {
			run += cnt[i];
			if (run > k || cnt[i] == 0) {
				ans += i - 1;
				break;
			}
		}

		for (int i = 0; i <= n; i++) {
			cnt[i] = 0;
			explored[i] = false;
		}

		while (!q.empty()) q.pop();
		for (int i = 0; i < n; i++) {
			if (adj[i].size() <= 1 && i != 0) {
				q.push(i);
				explored[i] = true;
			}
		}
		run = 0;
		while (!q.empty()) {
			run++;
			int sz = q.size();
			for (int i = 0; i < sz; i++) {
				int v = q.front();
				cnt[run]++;
				q.pop();
				for (int e : adj[v]) {
					if (explored[e]) continue;
					q.push(e);
					explored[e] = true;
				}
			}
		}
		run = 0;
		for (int i = 1; i <= n + 1; i++) {
			run += cnt[i];
			if (run > n - k || cnt[i] == 0) {
				ans += i - 1;
				break;
			}
		}
		asdf = max(ans, asdf);
		for (int i = 0; i <= n + 1; i++) {
			explored[i] = false;
			cnt[i] = 0;
		}
		k = n - k;
	}
	cout << min(mn, asdf) << endl;
	for (int i = 0; i <= n + 1; i++) {
		adj[i].clear();
		explored[i] = false;
		cnt[i] = 0;
	}

}

int main() {
	istream::sync_with_stdio(0);
	cin.tie(nullptr);
	int t;
	cin >> t;
	while (t--) {
		solve();
	}
	return 0;
}