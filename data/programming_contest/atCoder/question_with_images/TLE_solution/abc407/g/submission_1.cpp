#include <bits/stdc++.h>

#define all(a) a.begin(), a.end()
#define rall(a) a.rbegin(), a.rend()

using namespace std;

using ll = long long;
using ull = unsigned long long;
using vll = vector<ll>;
using a2 = array<ll, 2>;
using a3 = array<ll, 3>;
using pll = pair<ll, ll>;

const ll INF = 1e18;
const ll N = 1000;
const ll M = 998244353;
const ll offset = 2e12;

ll mincost_anyflow(vector<vector<pll>>& _G, ll s, ll t) {
	ll n = _G.size();
	vector<vll> G(n, vll(n, INF)), cap(n, vll(n));
	for(ll u = 0; u < n; u++) {
		for(auto [v, w]: _G[u]) {
			G[u][v] = w;
			cap[u][v] = 1;
			G[v][u] = -w;
		}
	}
	vll pot(n), par(n), d(n);
	pll cc;
	auto [aa, aaa] = cc;
	auto dijkstra = [&]() -> bool {
		vll used(n, 0);
		fill(all(d), INF);
		priority_queue<pll, vector<pll>, greater<pll>> q;
		d[s] = 0;
		q.push({0, s});
		while(q.size()) {
			auto [dist, u] = q.top(); q.pop();
			if(d[u] != dist) continue;
			for(ll v = 0; v < n; v++) {
				ll w = d[u] + G[u][v] + pot[u] - pot[v];
				if(cap[u][v] && d[v] > w) {
					d[v] = w;
					par[v] = u;
					q.push({w, v});
				}
			}
		}		
		return d[t] < INF;
	};
	ll ans = 0, res = 0, cnt = 0;
	while(dijkstra()) {
		for(ll i = 0; i < n; i++) {
			if(d[i] < INF) pot[i] += d[i];
		}
		ll delta = INF;	
		for(ll u = t; u != s; u = par[u]) {
			delta = min(delta, cap[par[u]][u]);
		}
		for(ll u = t; u != s; u = par[u]) {
			cap[par[u]][u] -= delta;
			cap[u][par[u]] += delta;
			res += delta * G[par[u]][u];
		}
		cnt++;
		ans = min(ans, res - offset * cnt);
	}
	return ans;
}

vll dr = {1, -1, 0, 0}, dc = {0, 0, 1, -1};

void atcoder() {
	ll h, w; cin >> h >> w;
	vector<vll> a(h, vll(w)); 
	for(auto& i: a) for(auto& j: i) cin >> j;
	vector<vector<pll>> G(h * w + 2);
	for(ll r = 0; r < h; r++) {
		for(ll c = 0; c < w; c++) {
			if((r + c) & 1) continue;
			for(ll i = 0; i < 4; i++) {
				ll nr = r + dr[i], nc = c + dc[i];
				if(nr < 0 || nr >= h || nc < 0 || nc >= w || a[r][c] + a[nr][nc] >= 0) continue;
				ll val = a[nr][nc] + a[r][c] + offset;
				G[r * w + c].push_back({nr * w + nc, val});
			}
		}
	}
	ll s = h * w, t = h * w + 1;
	for(ll r = 0; r < h; r++) {
		for(ll c = 0; c < w; c++) {
			if((r + c) & 1) {
				G[r * w + c].push_back({t, 0});
			} else {
				G[s].push_back({r * w + c, 0});
			}
		}
	}
	ll sum = 0;
	for(auto& i: a) sum += accumulate(all(i), 0ll);
	cout << sum - (mincost_anyflow(G, s, t)) << "\n";
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	#ifdef LOCAL
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	#endif
	ll t = 1; 
	while(t--) atcoder();
	return 0;
}