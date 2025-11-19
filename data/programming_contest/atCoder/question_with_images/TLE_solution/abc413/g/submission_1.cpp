#include <bits/stdc++.h>
using namespace std;
#define int long long


const int N = 1e6 + 12, INF = 1e18;

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
	int h, w, k;
	cin >>h >>w >>k;
	vector <vector <bool>> g(h + 1, vector <bool>(w + 1, false));
	for (int i = 0; i < k; i++) {
		int x, y;
		cin >>x >>y;
		g[x][y] = true;
	}
	queue <pair <int, int>> q;
	q.push({1, 1});
	g[1][1] = true;
	while (!q.empty()) {
		int x = q.front().first, y = q.front().second;
		q.pop();
		if (x - 1 > 0 && !g[x - 1][y]) {
			g[x - 1][y] = true;
			q.push({x - 1, y});
		}
		if (x + 1 <= h && !g[x + 1][y]) {
			g[x + 1][y] = true;
			q.push({x + 1, y});
		}
		if (y - 1 > 0 && !g[x][y - 1]) {
			g[x][y - 1] = true;
			q.push({x, y - 1});
		}
		if (y + 1 <= w && !g[x][y + 1]) {
			g[x][y + 1] = true;
			q.push({x, y + 1});
		}
	}
	if (g[h][w]) cout <<"Yes\n";
	else cout <<"No\n";
}
