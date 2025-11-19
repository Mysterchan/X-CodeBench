#include <bits/stdc++.h>
using namespace std;

#define int long long
#define x first
#define y second
#define pb push_back
#define eb emplace_back
#define v vector
#define printv(a, x) for (int i = x; i < a.size(); i ++ ) \
                      cout << a[i] << " \n"[i == a.size() - 1]
#define all(x) x.begin(), x.end()
#define print2(a, b) cout << (a) << ' ' << (b) << '\n'
#define print3(a, b, c) cout << (a) << ' ' << (b) << ' ' << (c) << '\n'
#define readv(a, n, x) for (int i = x; i < n + x; i ++ ) \
                      cin >> a[i]
#define readvv(a, n, m, x) for (int i = x; i < n + x; i ++ ) \
                            for (int j = x; j < m + x; j ++ ) \
                              cin >> a[i][j]
#define gt greater
#define pq priority_queue
#define umap unordered_map
#define uset unordered_set
#define lbound(a, x) lower_bound(a.begin(), a.end(), x) - a.begin()
#define ubound(a, x) upper_bound(a.begin(), a.end(), x) - a.begin()

typedef long long i64;
typedef unsigned long long u64;
typedef __int128 i128;
typedef pair<int, int> pII;
typedef tuple<int, int, int> pIII;

std::mt19937 rnd(std::chrono::steady_clock().now().time_since_epoch().count());

struct PII {
  int x, y;
  bool operator< (const PII &tmp) const {
    return x < tmp.x;
  }
};

const int N = 2e5 + 10, M = 1e6 + 10, mod = 1e9 + 7, 
inf = 0x3f3f3f3f3f3f3f3f, base = 131;
int t, n, m, q, k;
int dx[] = {0, 0, 1, -1}, dy[] = {1, -1, 0, 0};

void solve() {
  cin >> n >> k;
  for (int i = 0; i < 31; i ++ )
    if (n >> i & 1) { 
      int tmp = 1 << i;
      for (int j = 0; j < tmp; j ++ ) {
        if (((j | tmp) ^ n) >= n) break;
        if (((j | tmp) ^ n) == ((j | tmp) % n))
          if ( -- k == 0) 
            return cout << (j | tmp) << '\n', void();
      }
    }
  cout << "-1\n";
} 

signed main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr); cout.tie(nullptr);
  cin >> t;
  while (t -- ) solve();
  return 0;
}