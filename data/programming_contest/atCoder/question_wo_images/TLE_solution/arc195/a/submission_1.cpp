#include <bits/stdc++.h>
using namespace std;

int main() {
  int n, m;
  cin >> n >> m;
  vector<int> a(n);
  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }
  vector<int> b(m);
  for (int i = 0; i < m; i++) {
    cin >> b[i];
  }
  
  int cnt = 0;
  auto dfs = [&](auto dfs, int i, int j) -> void {
    if (cnt >= 2) {
      return;
    }
    if (j == m) {
      cnt++;
      return;
    }
    for (int k = i + 1; k < n; k++) {
      if (a[k] == b[j]) {
        dfs(dfs, k, j + 1);
      }
      if (cnt == 2) {
        return;
      }
    }
    return;
  };
  
  dfs(dfs, -1, 0);
  cout << (cnt >= 2 ? "Yes" : "No") << endl;
}