#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>
#include <chrono>
#include <random>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <iomanip>
#include <array>
#define dibs reserve
#define OVER9000 1234567890123456789LL
#define tisic 47
#define soclose 1e-8
#define patkan 9
#define ff first
#define ss second
using uint = unsigned int;
using cat = long long;
using dbl = long double;
constexpr dbl pi = 3.14159265358979323846;
using namespace std;

#ifdef DONLINE_JUDGE
	#define lld I64d
#endif

template <typename T>
T abs(T x) { return (x < 0) ? (-x) : x; }

cat gcd(cat a, cat b) {
	if(a > b) swap(a, b);
	while(a) {
		cat c = b%a;
		b = a;
		a = c;
	}
	return b;
}

cat pw(cat a, cat e, cat mod) {
	if(e <= 0) return 1;
	cat x = pw(a, e/2, mod);
	x = x * x % mod;
	return (e&1) ? x * a % mod : x;
}

constexpr cat MOD = 998244353;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	cout << fixed << setprecision(12);
	int H, W;
	cin >> H >> W;
	vector< vector<cat> > A(H);
	for(int i = 0; i < H; i++) {
		A[i].resize(W);
		for(int j = 0; j < W; j++) cin >> A[i][j];
	}
	bool sw = false;
	if(H > W) {
		vector< vector<cat> > A_tr(W, vector<cat>(H));
		for(int i = 0; i < H; i++) for(int j = 0; j < W; j++) A_tr[j][i] = A[i][j];
		A = A_tr;
		swap(H, W);
		sw = true;
	}
	vector< vector<cat> > dp_top(H, vector<cat>(W, 0));
	dp_top[0][0] = 1;
	for(int i = 0; i < H; i++) for(int j = 0; j < W; j++) {
		if(i > 0) dp_top[i][j] += dp_top[i-1][j];
		if(j > 0) dp_top[i][j] += dp_top[i][j-1];
		dp_top[i][j] = dp_top[i][j] * A[i][j] % MOD;
	}
	cat ans = dp_top[H-1][W-1];
	vector< vector<cat> > dp_bot(H+1, vector<cat>(W+1, 0));
	dp_bot[H-1][W-1] = 1;
	for(int i = H-1; i >= 0; i--) for(int j = W-1; j >= 0; j--) {
		dp_bot[i][j] += dp_bot[i+1][j];
		dp_bot[i][j] += dp_bot[i][j+1];
		dp_bot[i][j] = dp_bot[i][j] * A[i][j] % MOD;
	}
	int Q, pos_r, pos_c;
	cin >> Q >> pos_r >> pos_c;
	pos_r--, pos_c--;
	if(sw) swap(pos_r, pos_c);
	for(int q = 0; q < Q; q++) {
		string dir;
		cat val;
		cin >> dir >> val;
		if(sw) {
			if(dir == "U") dir = "L";
			else if(dir == "L") dir = "U";
			if(dir == "D") dir = "R";
			else if(dir == "R") dir = "D";
		}
		if(dir == "U") {
			for(int c = W-1; c >= 0; c--) {
				int r = (c <= pos_c) ? pos_r : (pos_r-1);
				dp_bot[r][c] = (c == W-1 && r == H-1) ? 1 : 0;
				dp_bot[r][c] += dp_bot[r+1][c] + dp_bot[r][c+1];
				dp_bot[r][c] = dp_bot[r][c] * A[r][c] % MOD;
			}
			pos_r--;
		}
		if(dir == "D") {
			for(int c = 0; c < W; c++) {
				int r = (c >= pos_c) ? pos_r : (pos_r+1);
				dp_top[r][c] = (r == 0 && c == 0) ? 1 : 0;
				if(r > 0) dp_top[r][c] += dp_top[r-1][c];
				if(c > 0) dp_top[r][c] += dp_top[r][c-1];
				dp_top[r][c] = dp_top[r][c] * A[r][c] % MOD;
			}
			pos_r++;
		}
		if(dir == "L") {
			dp_bot[pos_r][pos_c] = (pos_r == H-1 && pos_c == W-1) ? 1 : 0;
			dp_bot[pos_r][pos_c] += dp_bot[pos_r+1][pos_c] + dp_bot[pos_r][pos_c+1];
			dp_bot[pos_r][pos_c] = dp_bot[pos_r][pos_c] * A[pos_r][pos_c] % MOD;
			pos_c--;
		}
		if(dir == "R") {
			dp_top[pos_r][pos_c] = (pos_r == 0 && pos_c == 0) ? 1 : 0;
			if(pos_r > 0) dp_top[pos_r][pos_c] += dp_top[pos_r-1][pos_c];
			if(pos_c > 0) dp_top[pos_r][pos_c] += dp_top[pos_r][pos_c-1];
			dp_top[pos_r][pos_c] = dp_top[pos_r][pos_c] * A[pos_r][pos_c] % MOD;
			pos_c++;
		}
		cat sum_top = (pos_r == 0 && pos_c == 0) ? 1 : 0;
		if(pos_r > 0) sum_top += dp_top[pos_r-1][pos_c];
		if(pos_c > 0) sum_top += dp_top[pos_r][pos_c-1];
		cat sum_bot = (pos_r == H-1 && pos_c == W-1) ? 1 : (dp_bot[pos_r][pos_c+1] + dp_bot[pos_r+1][pos_c]);
		ans = (ans + sum_top * sum_bot % MOD * (val - A[pos_r][pos_c] + MOD)) % MOD;
		A[pos_r][pos_c] = val;
		cout << ans << "\n";
	}
}