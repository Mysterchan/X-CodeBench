#include <bits/stdc++.h>
#define int long long
using namespace std;

const int N = 460;
const int M = 200010;
const int mod = 998244353;

int n, m;
int fac[M], inv[M];
vector<int> f[M], g[M];

int qpow(int a, int b)
{
	int res = 1;
	while (b)
	{
		if (b & 1) res = res * a % mod;
		a = a * a % mod;
		b >>= 1;
	}
	return res;
}

void init()
{
	fac[0] = fac[1] = inv[0] = inv[1] = 1;
	for (int i = 1; i < M; i++) fac[i] = fac[i - 1] * i % mod;
	inv[M - 1] = qpow(fac[M - 1], mod - 2);
	for (int i = M - 2; i >= 2; i--) inv[i] = inv[i + 1] * (i + 1) % mod;
}

int C(int n, int m) { if (n < m || m < 0) return 0; return fac[n] * inv[m] % mod * inv[n - m] % mod; }

signed main()
{
	init();
	
	cin >> n >> m;
	if (m > n) swap(n, m);
	for (int i = 0; i <= n; i++) f[i].resize(m + 1, 0), g[i].resize(m + 1, 0);
	for (int i = 0; i <= m; i++) f[0][i] = 1;
	for (int i = 0; i <= n; i++) f[i][0] = 1;
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= m; j++)
		{
			f[i][j] = f[i - 1][j], g[i][j] = (g[i - 1][j] + f[i - 1][j] * j % mod) % mod;
			for (int k = 0; k <= j - 1; k++)
			{
				f[i][j] = (f[i][j] + C(j, k + 1) * f[i - 1][j - k] % mod) % mod;
				g[i][j] = (g[i][j] + C(j, k + 1) * (f[i - 1][j - k] * k % mod * i % mod + g[i - 1][j - k]) + C(j, k + 2) * f[i - 1][j - k] % mod % mod) % mod;
			}
		}
	cout << g[n][m];
	return 0;
}