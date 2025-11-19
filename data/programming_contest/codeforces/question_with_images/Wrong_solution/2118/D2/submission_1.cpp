#include<bits/stdc++.h>
using namespace std;
#define i64 long long
#define ll long long
#define ls p << 1
#define rs p << 1 | 1
using PII=pair<int,int>;
#define lowbit(x) (x&(-x))
const int N = 5e5;
const int M = 51;
const int mod = 998244353;
vector<vector<int>> nex(N, vector<int>(2));
bool in[N], ans[N];
i64 p[N], d[N];	
vector<int> e[N];
map<i64, int> mp;
vector<pair<int, int> > q(N);
void solve() {
	i64 n, k; cin >> n >> k;
	for (int i = 0; i <= 2 * n; i++) e[i].clear(), in[i] = 0;
	for (int i = 1; i <= n; i++) cin >> p[i];
	for (int i = 1; i <= n; i++) cin >> d[i];
	mp.clear();
	auto plus = [&] (i64 a, i64 b) {
		return (a + b) % k;
	};
	auto minus = [&] (i64 a, i64 b) {
		return ((a - b) % k + k) % k;
	};
	for (int i = 1; i <= n; i++) {
		nex[i][0] = mp[plus(d[i], p[i])];
		mp[plus(p[i], d[i])] = i;
		e[nex[i][0] ? nex[i][0] + n : 0].emplace_back(i);
	}
	mp.clear();
	for (int i = n; i; i--) {
		nex[i][1] = mp[minus(p[i], d[i])];
		mp[minus(p[i], d[i])] = i;
		e[nex[i][1]].emplace_back(i + n);
	}
	function<void(int)> dfs = [&] (int u) {
		in[u] = 1;
		for (auto &v : e[u]) {
			if (!in[v]) dfs(v);
		}
	};
	dfs(0);
	int m; cin >> m;
	
	for (int i = 0; i < m; i++) {
		cin >> q[i].first;
		q[i].second = i;
	}
	sort(q.begin(), q.begin() + m);
	int it = n;
	mp.clear();
	for (int i = m - 1; i >= 0; i--) {
		while (it && p[it] >= q[i].first) mp[minus(p[it], d[it])] = it, it--;
		ans[q[i].second] = in[mp[q[i].first % k]];
	}
	for (int i = 0; i < m; i++) {
		puts(ans[i] ? "YES" : "NO");
	}
}
int main () {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int T = 1;
    cin >> T;
    while (T--) {
        solve();
    }
    return 0;
}