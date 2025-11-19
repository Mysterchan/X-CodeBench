#include <map>
#include <set>
#include <list>
#include <array>
#include <cmath>
#include <deque>
#include <queue>
#include <stack>
#include <tuple>
#include <bitset>
#include <cfloat>
#include <memory>
#include <vector>
#include <random>
#include <string>
#include <cassert>
#include <climits>
#include <cstring>
#include <iomanip>
#include <numeric>
#include <iostream>
#include <algorithm>
#include <functional>
#include <unordered_map>
#include <unordered_set>

using namespace std;

#define rep(i, s, e) for (int i = s; i <= e; ++i)
#define per(i, s, e) for (int i = s; i >= e; --i)
#define file(a) freopen(#a".in", "r", stdin), freopen(#a".out", "w", stdout)
#define pv(a) cout << #a << " = " << a << endl
#define pa(a, l, r) cout << #a " : "; rep(_, l, r) cout << a[_] << " \n"[_ == r]

const int P = 998244353;

int read() {
  int x = 0, f = 1; char c = getchar();
  for (; c < '0' || c > '9'; c = getchar()) if (c == '-') f = -1;
  for (; c >= '0' && c <= '9'; c = getchar()) x = x * 10 + (c - 48);
  return x * f;
}

int inc(int a, int b) { return (a += b) >= P ? a - P : a; }
int dec(int a, int b) { return (a -= b) < 0 ? a + P : a; }
int mul(int a, int b) { return 1ll * a * b % P; }
void add(int &a, int b) { (a += b) >= P ? a -= P : 1; }
void sub(int &a, int b) { (a -= b) < 0 ? a += P : 1; }
int sgn(int x) { return x & 1 ? P - 1 : 1; }
int qpow(int a, int b) { int res = 1; for (; b; b >>= 1, a = mul(a, a)) if (b & 1) res = mul(res, a); return res; }

int n, m, ans;
void solve() {
  n = read(), m = read(), ans = 0;
  add(ans, mul(inc(dec(qpow(4, n - 1), mul(3, qpow(3, n - 1))), dec(mul(3, qpow(2, n - 1)), 1)), mul(mul(m, m - 1), mul(m - 2, (P + 1) / 6))));
  add(ans, mul(dec(qpow(m + 1, n - 1), inc(qpow(2, n - 1), mul(m - 1, dec(qpow(3, n - 1), qpow(2, n - 1))))), m));
  add(ans, mul(dec(qpow(4, n - 1), qpow(3, n - 1)), mul(mul(m, m - 1), (P + 1) / 2)));
  add(ans, qpow(m + 1, n - 1));
  ans = mul(ans, qpow(2, m));
  printf("%d\n", ans);
}

int main() {
  int tc = read();
  while (tc--) solve();
  return 0;
}