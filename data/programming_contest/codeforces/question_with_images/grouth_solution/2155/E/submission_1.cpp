
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
    int n, m, k;
    cin >> n >> m >> k;
    set<int> s;
    for (int i = 0; i < k; i++) {
      int x, y;
      cin >> x >> y;
      if (n == 1) {
        y = (y == 2 ? 2 : 1);
      }
      if (y > 1) {
        auto it = s.find(y);
        if (it != s.end()) {
          s.erase(it);
        } else {
          s.insert(y);
        }
      }
    }
    cout << (s.empty() ? "Yuyu" : "Mimo") << '\n';
  }
  return 0;
}
