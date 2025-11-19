
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
    int n, m;
    cin >> n >> m;
    vector<int> f(n);
    f[0] = 1;
    f[1] = 2;
    for (int i = 2; i < n; i++) {
      f[i] = f[i - 1] + f[i - 2];
    }
    for (int i = 0; i < m; i++) {
      int a, b, c;
      cin >> a >> b >> c;
      if (a > b) swap(a, b);
      if (a > c) swap(a, c);
      if (b > c) swap(b, c);
      cout << (a >= f[n - 1] && b >= f[n - 1] && c >= f[n - 1] + f[n - 2] ? 1 : 0);
    }
    cout << '\n';
  }
  return 0;
}
