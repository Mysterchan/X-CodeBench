
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
    auto Solve = [&](vector<string> s) {
      int n = int(s.size());
      int m = int(s[0].size());
      int b = (m + 63) / 64;
      const uint64_t one = 1;
      vector<vector<uint64_t>> v(n, vector<uint64_t>(b));
      for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
          if (s[i][j] == '1') {
            v[i][j >> 6] |= (one << (j & 63));
          }
        }
      }
      int at = 0;
      for (int c = 0; c < m; c++) {
        bool found = false;
        for (int i = at; i < n; i++) {
          if (v[i][c >> 6] & (one << (c & 63))) {
            swap(v[i], v[at]);
            found = true;
            break;
          }
        }
        if (!found) {
          continue;
        }
        for (int i = 0; i < n; i++) {
          if (i != at && v[i][c >> 6] & (one << (c & 63))) {
            for (int j = 0; j < b; j++) {
              v[i][j] ^= v[at][j];
            }
          }
        }
        at += 1;
      }
      return v;
    };
    int n;
    cin >> n;
    string a, b;
    cin >> a >> b;
    while (n % 2 == 0) {
      n /= 2;
    }
    vector<string> sa, sb;
    for (int i = 0; i < int(a.size()); i += n) {
      sa.push_back(a.substr(i, n));
      sb.push_back(b.substr(i, n));
    }
    cout << (Solve(sa) == Solve(sb) ? "Yes" : "No") << '\n';
  }
  return 0;
}
