#include <bits/stdc++.h>
using namespace std;
using lint = long long;
using pi = array<lint, 2>;
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(), (v).end()
#define cr(v, n) (v).clear(), (v).resize(n);
const int MAXN = 70005;

vector<vector<int>> gph;
vector<int> dfn;
int sz[MAXN], msz[MAXN], vis[MAXN];

void dfs(int x, int p = -1) {
	dfn.push_back(x);
	sz[x] = 1, msz[x] = 0;
	for (auto &y : gph[x]) {
		if (y != p && !vis[y]) {
			dfs(y, x);
			sz[x] += sz[y];
			msz[x] = max(msz[x], sz[y]);
		}
	}
}

int get_center(int x) {
	dfn.clear();
	dfs(x);
	pi ret{int(1e9), -1};
	for (auto &x : dfn) {
		int w = max(sz(dfn) - sz[x], msz[x]);
		ret = min(ret, pi{w, x});
	}
	return ret[1];
}

vector<array<int, 4>> vect;
vector<int> dist;

void gather(int x, int p, int d, int cnum) {
	vect.push_back({cnum, dist[x] / 2, d, x});
	for (auto &y : gph[x]) {
		if (!vis[y] && y != p) {
			gather(y, x, d + 1, cnum);
		}
	}
};

const int MAXT = 270000;

struct seg {
	int tree[MAXT], lim;
	void init(int n) {
		for (lim = 1; lim <= n; lim <<= 1)
			;
		fill(tree, tree + 2 * lim, -int(1e9));
	}
	void upd(int x, int v) {
		x += lim;
		tree[x] = v;
		while (x > 1) {
			x >>= 1;
			tree[x] = max(tree[2 * x], tree[2 * x + 1]);
		}
	}
	int query(int s, int e) {
		s += lim;
		e += lim;
		int ret = -1e9;
		while (s < e) {
			if (s % 2 == 1)
				ret = max(ret, tree[s++]);
			if (e % 2 == 0)
				ret = max(ret, tree[e--]);
			s >>= 1;
			e >>= 1;
		}
		if (s == e)
			ret = max(ret, tree[s]);
		return ret;
	}
} seg;

vector<int> go(vector<int> dd) {
	dist = dd;
	int n = sz(dist);
	fill(vis, vis + n, 0);
	vector<int> ret(n, -1);
	queue<int> que;
	que.push(0);
	vector<int> mapping(n);
	while (sz(que)) {
		int x = que.front();
		que.pop();
		x = get_center(x);
		vect.clear();
		int cnum = 0;
		for (auto &y : gph[x]) {
			if (!vis[y]) {
				gather(y, x, 1, cnum++);
			}
		}
		auto cmp = [&](const array<int, 4> &a, const array<int, 4> &b) { return a[1] - a[2] < b[1] - b[2]; };
		sort(all(vect), cmp);
		bool unfucked = false;
		for (int i = 0; i < sz(vect); i++) {
			if (vect[i][1] > 0)
				unfucked = true;
			mapping[vect[i][3]] = i;
		}
		if (unfucked == false)
			continue;
		vector<vector<array<int, 3>>> byComp(cnum);
		for (auto &[c1, l1, d1, i1] : vect) {
			byComp[c1].push_back({i1, l1, d1});
		}
		for (auto &v : byComp) {
			for (auto &w : v)
				seg.upd(mapping[w[0]], w[2]);
		}
		for (auto &v : byComp) {
			for (auto &w : v)
				seg.upd(mapping[w[0]], -1e9);
			for (auto &[i2, l2, d2] : v) {
				int it = lower_bound(all(vect), array<int, 4>{0, d2, 0, 0}, cmp) - vect.begin();
				int d1 = seg.query(it, sz(vect) - 1); // prefix atleast, take max
				ret[i2] = max(ret[i2], d1 + d2);
			}
			for (auto &w : v)
				seg.upd(mapping[w[0]], w[2]);
		}
		for (auto &v : byComp) {
			for (auto &w : v)
				seg.upd(mapping[w[0]], -1e9);
		}
		for (auto &[c2, l2, d2, i2] : vect) {
			if (d2 <= dist[x] / 2)
				ret[i2] = max(ret[i2], d2);
			if (d2 <= l2)
				ret[x] = max(ret[x], d2);
		}
		vis[x] = 1;
		for (auto &y : gph[x]) {
			if (!vis[y]) {
				que.push(y);
			}
		}
	}
	return ret;
}

void solve() {
	int n;
	cin >> n;
	string s;
	cin >> s;
	cr(gph, n);
	seg.init(n);

	for (int i = 0; i < n - 1; i++) {
		int u, v;
		cin >> u >> v;
		u--;
		v--;
		gph[u].push_back(v);
		gph[v].push_back(u);
	}
	vector<int> dist(n, -1);
	for (int i = 0; i < n; i++) {
		if (s[i] == '1')
			dist[i] = 5 * n;
	}
	vector<int> ans(n, -1);
	for (int it = 1; *max_element(all(dist)) >= 0; it++) {
		for (int j = 0; j < n; j++) {
			if (dist[j] >= 1)
				ans[j] = max(ans[j], it);
		}
		auto eist = go(dist);
		for (int j = 0; j < n; j++) {
			if (s[j] == '0')
				eist[j] = -1;
		}
		dist = eist;
	}
	for (auto &x : ans)
		cout << x << " ";
	cout << "\n";
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int t;
	cin >> t;
	while (t--)
		solve();
}