#include<bits/stdc++.h>
using namespace std;
#define IOS ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr)
using LL = long long;
constexpr int MAXN = 405, mod = 998244353;
inline void inc(int &x, int y) { (x += y) >= mod && (x -= mod); }
inline void dec(int &x, int y) { (x -= y) < 0 && (x += mod); }
inline int qpow(int x, int y = mod - 2) {
	int ret = 1;
	while (y) {
		if (y & 1) ret = (LL)ret * x % mod;
		x = (LL)x * x % mod, y >>= 1;
	}
	return ret;
}
int n;
bool G[MAXN][MAXN];
inline bool contain(int x, int y) {
	bool ret = true;
	for (int i = 1; i <= n; ++i) ret &= (G[x][i] >= G[y][i]);
	return ret;
}
int main() {
	IOS;
	int T; cin >> T;
	while (T--) {
		cin >> n;
		int ans = 1;
		for (int i = 1; i <= n; ++i) {
			for (int j = 1; j <= n; ++j) cin >> G[i][j];
			int cnt = 0;
			for (int k = 2; k < i; ++k) {
				bool f = true;
				for (int j = 1; j <= n; ++j) f &= (G[i][j] == G[k][j]);
				cnt += f;
			}
			ans = (LL)ans * (cnt + 1) % mod;
		}
		for (int i = 1; i <= n; ++i) if (!G[1][i]) ans = 0;
		for (int i = 1; i <= n; ++i) for (int j = i + 1; j <= n; ++j) if (G[i][j] && !contain(i, j) && !contain(j, i)) ans = 0;
		cout << ans << '\n';
	}
	return 0;
}