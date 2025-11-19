#include <bits/stdc++.h>
#define Code using
#define by namespace
#define zzx std
Code by zzx;

const int N = 20;
const long long mod = 998244353ll;

int n, m; long long ans = 0ll;
int mp[N + 10][N + 10], id[(1 << N)];
long long dp[(1 << N)][N];

long long q_pow(long long u, long long v) {
	long long res = 1ll;
	while(v) {
		if(v & 1ll) res = res * u % mod;
		u = u * u % mod; v >>= 1;
	}
	return res;
}

int main() {
	cin >> n >> m;
	for(int i = 1; i <= m; ++i) {
		int u, v; cin >> u >> v; --u; --v;
		++mp[u][v]; ++mp[v][u];
	}
	for(int i = 0; i < n; ++i) id[1 << i] = i;
	for(int i = 0; i < n; ++i) dp[1 << i][i] = 1ll;
	for(int s = 1; s < (1 << n); ++s) {
		for(int i = id[(s & -s)]; i < n; ++i) {
			if(!dp[s][i]) continue;
			for(int j = id[(s & -s)] + 1; j < n; ++j) {
				if(s & (1 << j)) continue;
				dp[s + (1 << j)][j] = (dp[s + (1 << j)][j] + dp[s][i] * (long long)mp[i][j]) % mod;
			}
		}
	}
	for(int s = 1; s < (1 << n); ++s) {
		for(int i = id[(s & -s)] + 1; i < n; ++i) {
			ans = (ans + dp[s][i] * mp[id[(s & -s)]][i]) % mod;
		}
	}
	cout << (ans - m + mod) % mod * q_pow(2ll, mod - 2ll) % mod;
	return 0;
}