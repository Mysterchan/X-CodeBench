
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
    int64_t k;
    cin >> n >> k;
    vector<int64_t> p(n);
    for (int i = 0; i < n; i++) {
      cin >> p[i];
      --p[i];
    }
    vector<int64_t> d(n);
    for (int i = 0; i < n; i++) {
      cin >> d[i];
    }
    map<int64_t, vector<pair<int64_t, int>>> plus, minus;
    for (int i = 0; i < n; i++) {
      plus[(p[i] + d[i]) % k].emplace_back(p[i], i);
      minus[(p[i] + k - d[i]) % k].emplace_back(p[i], i);
    }
    auto Right = [&](int64_t x, int64_t m) {
      auto val = (x + k - m) % k;
      auto it = minus.find(val);
      if (it == minus.end()) {
        return -1;
      }
      auto bin = lower_bound(it->second.begin(), it->second.end(), make_pair(x, -1));
      if (bin == it->second.end()) {
        return -1;
      }
      return bin->second;
    };
    auto Left = [&](int64_t x, int64_t m) {
      auto val = (x + m) % k;
      auto it = plus.find(val);
      if (it == plus.end()) {
        return -1;
      }
      auto bin = lower_bound(it->second.begin(), it->second.end(), make_pair(x + 1, -1));
      if (bin == it->second.begin()) {
        return -1;
      }
      return prev(bin)->second;
    };
    vector<vector<int>> g(2 * n + 1);
    for (int at = 0; at < n; at++) {
      for (int dir = 0; dir < 2; dir++) {
        int from = at * 2 + dir;
        int to = (dir == 0 ? Left(p[at] - 1, d[at] + 1) : Right(p[at] + 1, d[at] + 1));
        to = (to == -1 ? 2 * n : to * 2 + (1 - dir));
        g[to].push_back(from);
      }
    }
    vector<bool> was(2 * n + 1, false);
    was[2 * n] = true;
    vector<int> que(1, 2 * n);
    for (int it = 0; it < int(que.size()); it++) {
      for (int u : g[que[it]]) {
        if (!was[u]) {
          que.push_back(u);
          was[u] = true;
        }
      }
    }
    int q;
    cin >> q;
    while (q--) {
      int64_t x;
      cin >> x;
      --x;
      int to = Right(x, 0);
      to = (to == -1 ? 2 * n : to * 2 + 0);
      cout << (was[to] ? "YES" : "NO") << '\n';
    }
  }
  return 0;
}
