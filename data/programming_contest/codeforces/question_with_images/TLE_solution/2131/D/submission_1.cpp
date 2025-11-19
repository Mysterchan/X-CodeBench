#include <bits/stdc++.h>
#define ll long long
#define endl '\n'
#define int long long
using namespace std;

int deg[200005];
vector<int> vec[200005];

int dfs(int cur, int pre) {
    int ret = 0;
    if (deg[cur] == 1) {
        ret = 1;
    }
    for (auto v : vec[cur]) {
        if (v == pre) continue;
        ret += dfs(v, cur);
    }
    return ret;
}

void solve() {
	int n;
    cin >> n;
    for (int i=1;i<=n;i++) {
        vec[i].clear();
        deg[i] = 0;
    }
    int maxn = 0;
    for (int i=1;i<n;i++) {
        int u, v;
        cin >> u >> v;
        vec[u].push_back(v);
        vec[v].push_back(u);
        deg[u]++;
        deg[v]++;
        maxn = max(maxn, max(deg[u], deg[v]));
    }
    if (n == 2) {
        cout << 0 << endl;
        return;
    }
    int ans = 1e18;
    for (int i=1;i<=n;i++) {
        int mid = 0;
        for (auto v : vec[i]) {
            if (deg[v] == 1) continue;
            mid += dfs(v, i);
        }
        ans = min(ans, mid);
    }
    cout << ans << endl;
}

void init() {
    
}

signed main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int t = 1;
    init();
	cin >> t;
	while (t--) {
		solve();
	}
	return 0;
}