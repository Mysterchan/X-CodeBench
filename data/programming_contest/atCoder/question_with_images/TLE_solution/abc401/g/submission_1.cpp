#pragma GCC optimize("Ofast")
#pragma GCC optimize("O3,unroll-loops")

#include <bits/stdc++.h>

using namespace std;

#define f0r(i, n) for (auto i = 0; i < (n); ++i)
#define fnr(i, n, k) for (auto i = (n); i < (k); ++i)
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define F first
#define S second
#define ctn(x) cout << x << '\n'
#define forl(a, l) for (auto a : l)
#define ctl(l) for (auto &a : (l)) cout << a << ' '; cout << endl;
#define lb(v, x) (lower_bound(all(v), x) - begin(v))
#define ub(v, x) (upper_bound(all(v), x) - begin(v))
#define pq priority_queue

template <class T>
using V = vector<T>;
using ll = long long;
using vi = V<int>;
using vl = V<ll>;
using pi = pair<int, int>;
using ti = tuple<int, int, int>;
using Adj = V<vi>;
using vvi = V<vi>;
using ld = long double;
using pd = pair<ld, ld>;

int N;
V<V<pair<int, ld>>> G;

V<bool> vis;
V<pair<int, ld>> mt;

bool try_kuhn(ld C, int v) {
	if (vis[v]) return false;
	vis[v] = 1;
	for (auto &[c, w]: G[v]) if (w <= C && (mt[c].F == -1 || try_kuhn(C, mt[c].F))) {
		mt[c] = {v, w};
		return true;
	}
	return false;
}

ld check(ld C) {
	mt.assign(N, {-1, 1e20});
	f0r(v, N) {
		vis.assign(N, 0);
		try_kuhn(C, v);
	}
	ld mx = 0;
	f0r(i, N) {
		if (mt[i].F == -1) return -1;
		mx = max(mt[i].S, mx);
	}
	return mx;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N;
	V<pd> people(N), butts(N);
	for (auto &[x, y]: people) cin >> x >> y;
	for (auto &[x, y]: butts) cin >> x >> y;
	G.resize(N);
	ld mx = 0;
	f0r(i, N) {
		auto &[x, y] = people[i];
		f0r(j, N) {
			auto &[bx, by] = butts[j];
			ld d = hypot(bx - x, by - y);
			mx = max(mx, d);
			G[i].pb({j, d});
		}
	}
	ld lo = 0, hi = mx, best = 1e20;
	int cnt = 0;
	while (lo <= hi && cnt < 60) {
		ld m = (lo + hi) / 2, k = check(m);
		if (k == -1) lo = m;
		else best = min(best, k), hi = m;
		++cnt;
	}
	ctn(setiosflags(ios_base::fixed) << setprecision(7) << best);
}
