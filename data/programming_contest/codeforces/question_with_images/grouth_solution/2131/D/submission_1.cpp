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
    vector<vector<int>> g(n);
    for (int i = 0; i < n - 1; i++) {
      int x, y;
      cin >> x >> y;
      --x; --y;
      g[x].push_back(y);
      g[y].push_back(x);
    }
    if (n == 2) {
      cout << 0 << '\n';
      continue;
    }
    int ans = 0;
    for (int i = 0; i < n; i++) {
      if (g[i].size() == 1) {
        ans += 1;
      }
    }
    int mx = 0;
    for (int i = 0; i < n; i++) {
      int cnt = 0;
      for (int j : g[i]) {
        cnt += int(g[j].size() == 1);
      }
      mx = max(mx, cnt);
    }
    cout << ans - mx << '\n';
  }
  return 0;
}