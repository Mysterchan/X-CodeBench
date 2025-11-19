#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
#define pb emplace_back
const int N = 3005, mod = 998244353;

int n;
vector<int> e[N];

int bel[N], d[N], id[N], cur;

ll f[N][4][2], g[N][4][2];
void add(ll &x, ll y) {
	x += y;
	if (x >= mod)
		x -= mod;
}
ll DP(ll X, ll Y) {
	queue<int> q;
	for (int i = 1; i <= n; i++)
		bel[i] = d[i] = id[i] = 0;
	cur = 0;
	if (Y) {
		d[X] = d[Y] = 0;
		bel[X] = X, bel[Y] = Y;
		id[++cur] = X, id[++cur] = Y;
		for (auto i: e[X])
			if (!bel[i]) {
				bel[i] = X, d[i] = 1;
				q.push(i);
			}
		for (auto i: e[Y])
			if (!bel[i]) {
				bel[i] = Y, d[i] = 1;
				q.push(i);
			}
	}
	else {
		d[X] = 0;
		bel[X] = X;
		id[++cur] = X;
		for (auto i: e[X]) {
			bel[i] = i, d[i] = 1;
			q.push(i);
		}
	}
	while (!q.empty()) {
		int u = q.front();
		q.pop();
		id[++cur] = u;
		for (auto i: e[u])
			if (!bel[i]) {
				bel[i] = bel[u], d[i] = d[u] + 1;
				q.push(i);
			}
	}
	
	reverse(id + 1, id + cur + 1);
	
	for (int i = 0; i <= cur; i++)
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 2; k++)
				f[i][j][k] = g[i][j][k] = 0;
	f[0][0][0] = 1, g[0][0][0] = 0;
	
	for (int i = 1; i <= cur; i++) {
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 2; k++) {
				add(f[i][j][k], f[i - 1][j][k]);
				add(g[i][j][k], g[i - 1][j][k]); 
				
				if (j) {
					add(f[i][j | 1][k], f[i - 1][j][k]);
					add(g[i][j | 1][k], g[i - 1][j][k]);
				}
				else {
					add(f[i][j | 1][k], f[i - 1][j][k]);
					add(g[i][j | 1][k], g[i - 1][j][k] + f[i - 1][j][k] * d[id[i]] % mod);
				}
				
				if (k) {
					add(f[i][j][k | 1], f[i - 1][j][k]);
					add(g[i][j][k | 1], g[i - 1][j][k]);
				}
				else {
					add(f[i][j][k | 1], f[i - 1][j][k]);
					add(g[i][j][k | 1], g[i - 1][j][k] + f[i - 1][j][k] * d[id[i]] % mod);
				}
			}
		if (i == cur)
			break;
		if (bel[id[i]] != bel[id[i + 1]]) {
			for (int k = 0; k < 2; k++) {
				add(f[i][2][k], f[i][1][k]);
				add(g[i][2][k], g[i][1][k]);
				f[i][1][k] = g[i][1][k] = 0;
			}
		}
		if (d[id[i]] != d[id[i + 1]])  {
			for (int k = 0; k < 2; k++)
				f[i][1][k] = f[i][2][k] = g[i][1][k] = g[i][2][k] = 0;
		}
	}
	
	if (Y)
		return (g[cur][3][1] + f[cur][3][1]) % mod;
	return (g[cur][3][1] + g[cur][1][1]) % mod;
}

void slv() {
	cin >> n;
	for (int i = 1; i <= n; i++)
		vector<int>().swap(e[i]);
	for (int i = 1, u, v; i < n; i++) {
		cin>> u >> v;
		e[u].pb(v);
		e[v].pb(u);
	}
	ll ans = 0;
	for (int i = 1; i <= n; i++) {
		(ans += DP(i, 0)) %= mod;
		for (auto j: e[i])
			if (i < j)
				(ans += DP(i, j)) %= mod;
	} 
	cout << ans << '\n';
}

int main() {
	ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
	int T;
	cin >> T;
	while (T--)
		slv();
	return 0;
}