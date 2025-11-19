#include <bits/stdc++.h>
 
using namespace std;
 
#ifdef LOCAL
#include "algo/debug.h"
#else
#define debug(...) 42
#endif
 
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int tt;
  cin >> tt;
  while (tt--) {
    int n;
    cin >> n;
    int64_t ans = 0;
    for (int i = 0; i < n; i++) {
      int a, b, c, d;
      cin >> a >> b >> c >> d;
      if (b <= d) {
        ans += max(0, a - c);
      } else {
        ans += a;
        ans += max(0, b - d);
      }
    }
    cout << ans << '\n';
  }
  return 0;
}