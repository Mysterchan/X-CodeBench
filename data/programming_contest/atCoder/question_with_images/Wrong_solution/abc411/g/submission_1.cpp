#include <bits/stdc++.h>
using namespace std;

#define int long long
#define double long double
#define endl "\n"

const int maxn = 22, mod = 998244353;

int n, m;
int edge[maxn][maxn];
int f[1 << maxn][maxn];

int cnt[1 << maxn];

int ksm(int a, int b)
{
	int c = 1;
	while (b)
	{
		if (b % 2)
			c = c * a % mod;
		a = a * a % mod;
		b /= 2;
	}
	return c;
}

void solve()
{
	int ny2 = ksm(2, mod - 2);

	cin >> n >> m;
	for (int i = 1; i <= m; i++)
	{
		int x, y;
		cin >> x >> y, x--, y--;
		edge[x][y]++, edge[y][x]++;
	}

	int ans = 0;
	for (int i = 2; i < n; i++)
	{
		for (int j = 0; j < 1 << (i + 1); j++)
			for (int k = 0; k <= i; k++)
				f[j][k] = 0;
		f[1 << i][i] = 1;

		for (int j = 0; j < 1 << (i + 1); j++)
			for (int k1 = 0; k1 <= i; k1++)
				if ((j >> k1) % 2)
					for (int k2 = 0; k2 <= i; k2++)
						f[j][k1] = (f[j][k1] + f[j - (1 << k1)][k2] * edge[k2][k1]) % mod;

		for (int j = 0; j < 1 << (i + 1); j++)
			for (int k = 0; k <= i; k++)
				if (cnt[j] >= 3)
					ans = (ans + (f[j][k] * edge[k][i] % mod) * ny2) % mod;
				else if (cnt[j] >= 2)
					ans = (ans + (f[j][k] * (edge[k][i] - 1) % mod) * ny2) % mod;
	}
	cout << ans << endl;
}

int get(int x)
{
	int c = 0;
	for (int i = maxn - 1; i >= 0; i--)
		if ((x >> i) % 2)
			c++;
	return c;
}

signed main()
{
	for (int j = 0; j < 1 << maxn; j++)
		cnt[j] = get(j);

	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	cout << fixed << setprecision(10);

	int t = 1;
	while (t--)
		solve();

	return 0;
}