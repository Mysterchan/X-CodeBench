#include <bits/stdc++.h>

using namespace std;

int main() {
  int n, k;
  cin >> n >> k;
  vector<int> p(n * k);
  for (int i = 0; i < n * k; ++i) {
    cin >> p[i];
    p[i]--;
  }

  vector<bool> vis(n * k);
  int ans = 0;
  for (int i = 0; i < n * k; ++i) {
    if (vis[i]) {
      continue;
    }

    vector<int> cycle;
    int cur = i;
    while (!vis[cur]) {
      cycle.push_back(cur);
      vis[cur] = true;
      cur = p[cur];
    }

    if (cycle.size() == 1) {
      continue;
    }

    int cyc = cycle.size();    
    vector<vector<int>> g(n);
    for (int i = 0; i < cyc; ++i) {
      g[cycle[i] % n].push_back(cycle[i]);
    }

    vector<vector<int>> dp(cyc + 1, vector<int> (cyc + 1));
    for (int l = 2; l <= cyc; ++l) {
      for (int i = 0; i + l - 1 < cyc; ++i) {
        int j = i + l - 1;
        dp[i][j] = max(dp[i][j], dp[i + 1][j]);
        for (int p : g[cycle[i] % n]) {
          if (i < p && p <= j) {
            dp[i][j] = max(dp[i][j], dp[i + 1][p] + dp[p + 1][j] + 1);
          }
        }
      }
    }

    ans += dp[0][cyc - 1]; 
  }

  cout << ans << endl;
}