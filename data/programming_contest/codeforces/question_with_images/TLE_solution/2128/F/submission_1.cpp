#include <bits/stdc++.h>
using namespace std;
#define int long long
#define For(i, a, b) for(int i = (a); i <= (b); i++)
#define Rof(i, a, b) for(int i = (a); i >= (b); i--)
#define Debug(...) fprintf(stderr, __VA_ARGS__)
template<typename T>void cmax(T &x, T y){x = max(x, y);}
template<typename T>void cmin(T &x, T y){x = min(x, y);}
using pr = pair<int, int>;
const int N = 5e5 + 5, inf = 1e18;
int n, m, k, dis[N], dp[N];
vector<array<int, 3>> e[N];
void Solve(){
	cin >> n >> m >> k;
	For(i, 1, n) dis[i] = dp[i] = inf, e[i].clear();
	For(i, 1, m){
		int u, v, l, r;
		cin >> u >> v >> l >> r;
		e[u].push_back({v, l, r});
		e[v].push_back({u, l, r});
	}
	priority_queue<pr, vector<pr>, greater<pr>> q;
	dis[k] = 0; q.push({0, k});
	while(!q.empty()){
		auto [d, u] = q.top(); q.pop();
		if(-d != dis[u]) continue;
		for(auto [v, _, w] : e[u]){
			if(dis[v] <= dis[u] + w) continue;
			dis[v] = dis[u] + w; q.push({-dis[v], v});
		}
	}
	dp[1] = -dis[1]; q.push({-dp[1], 1});
	while(!q.empty()){
		auto [d, u] = q.top(); q.pop();
		if(-d != dp[u] || dp[u] >= dis[u]) continue;
		for(auto [v, w, _] : e[u]){
			if(dp[v] <= max(-dis[v], dp[u] + w)) continue;
			dp[v] = max(-dis[v], dp[u] + w); q.push({-dp[v], v});
		}
	}
	cout << (dp[n] < dis[n] ? "YES" : "NO") << '\n';
}
signed main(){
	cin.tie(nullptr)->sync_with_stdio(false);
	int T = 1; cin >> T;
	while(T--) Solve();
	return 0;
}