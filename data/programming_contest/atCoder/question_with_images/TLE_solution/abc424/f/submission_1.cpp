#include <bits/stdc++.h>
#define LL long long
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define Let (u<<1)
#define Rit (u<<1|1)
#define lowbit(x) (x&(-x))
using namespace std;
void read(int &val) {
	int res = 0, f = 1;
	char c = ' ';
	while (c != '-' && (c < '0' || c > '9')) c = getchar();
	if (c == '-') f = -1, c = getchar();
	while ('0' <= c && c <= '9') res = res * 10 + (c - '0'), c = getchar();
	return val = res * f, void();
}
const int INF = 0x3f3f3f3f;
const int maxn = 1e4 + 5;
int n, m, x, y;
struct Seg_tree {
	unordered_map<int, unordered_map<int, int > > val;
	void add(int sx, int sy) {
		for (int i = sx; i <= n; i += lowbit(i))
			for (int j = sy; j <= n; j += lowbit(j))
				val[i][j]++;
		return ;
	}
	int query(int sx, int sy) {
		int res = 0;
		for (int i = sx; i; i -= lowbit(i))
			for (int j = sy; j; j -= lowbit(j))
				res += val[i][j];
		return res;
	}
	int solve(int sx, int sy, int tx, int ty) {
		return query(tx, ty) - query(sx - 1, ty) - query(tx, sy - 1) + query(sx - 1, sy - 1);
	}
} t;
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0), cout.tie(0);
	cin >> n >> m;
	while (m--) {
		cin >> x >> y;
		if (x > y) swap(x, y);
		if (t.solve(1, x + 1, x - 1, y - 1) || t.solve(x + 1, y + 1, y - 1, n)) {
			cout << "No\n";
			continue;
		}
		t.add(x, y);
		cout << "Yes\n";
	}
	return 0;
}