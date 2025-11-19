
#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int tt;
  cin >> tt;
  while (tt--) {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> g(n);
    for (int i = 0; i < m; i++) {
      int u, v;
      cin >> u >> v;
      --u; --v;
      g[u].push_back(v);
      g[v].push_back(u);
    }
    vector<int> path;
    vector<vector<vector<int>>> cycles(n);
    vector<bool> was(n);
    auto Dfs = [&](auto&& self, int v, int st) -> void {
      path.push_back(v);
      was[v] = true;
      for (int u : g[v]) {
        if (u == st) {
          if (int(path.size()) > 2) {
            cycles[*min_element(path.begin(), path.end())].push_back(path);
          }
        } else if (!was[u]) {
          was[u] = true;
          self(self, u, st);
          was[u] = false; 
        }
      }
      was[v] = false;
      path.pop_back();
    };
    for (int i = 0; i < n; i++) {
      Dfs(Dfs, i, i);
    }
    vector<int> cnt(n);
    vector<vector<int>> t(n);
    for (int i = 0; i < n; i++) {
      cnt[i] = int(cycles[i].size());
      t[i].resize(cnt[i]);
      for (int j = 0; j < cnt[i]; j++) {
        sort(cycles[i][j].begin(), cycles[i][j].end());
        for (int v : cycles[i][j]) {
          t[i][j] |= (1 << v);
        }
      }
    }
    vector<int> order(n);
    iota(order.begin(), order.end(), 0);
    sort(order.begin(), order.end(), [&](int i, int j) {
      return cnt[i] > cnt[j];
    });
    vector<int> L, R;
    for (int i = 0; i < n; i++) {
      if (i % 2 == 0) {
        L.push_back(order[i]);
      } else {
        R.push_back(order[i]);
      }
    }
    vector<int> f(1, 0);
    for (int i : L) {
      vector<int> new_f = f;
      for (int j = 0; j < cnt[i]; j++) {
        for (int msk : f) {
          if ((msk & t[i][j]) == 0) {
            new_f.push_back((msk | t[i][j]));
          }
        }
      }
      swap(f, new_f);
      sort(f.begin(), f.end());
      f.erase(unique(f.begin(), f.end()), f.end());
    }
    vector<int> e(1, 0);
    for (int i : R) {
      vector<int> new_e = e;
      for (int j = 0; j < cnt[i]; j++) {
        for (int msk : e) {
          if ((msk & t[i][j]) == 0) {
            new_e.push_back((msk | t[i][j]));
          }
        }
      }
      swap(e, new_e);
      sort(e.begin(), e.end());
      e.erase(unique(e.begin(), e.end()), e.end());
    }
    int res = n - 1;
    for (int mask : e) {
      int other = (mask ^ ((1 << n) - 1));
      int p = int(lower_bound(f.begin(), f.end(), other) - f.begin());
      if (p >= 0 && p < int(f.size()) && f[p] == other) {
        res = n;
        break;
      }
    }
    cout << res << '\n';
  }
  return 0;
}