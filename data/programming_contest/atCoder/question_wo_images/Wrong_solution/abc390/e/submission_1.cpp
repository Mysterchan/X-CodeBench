#include <bits/stdc++.h>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  int n, x;
  cin >> n >> x;
  vector<int> cal[3], unit[3];
  for (int i = 0; i < n; i++) {
    int v, a, c;
    cin >> v >> a >> c;
    v--;
    cal[v].push_back(c);
    unit[v].push_back(a);
  }
  auto f = [&](auto &cal, auto &unit) -> vector<int> {
    auto C = accumulate(cal.begin(), cal.end(), 0);
    vector<int> res(C + 1);
    for (int i = 0; i < (int)cal.size(); i++) {
      for (int j = C - cal[i]; j >= 0; j--) {
        res[j + cal[i]] = max(res[j + cal[i]], res[j] + unit[i]);
      }
    }
    return res;
  };
  vector<int> dp[3];
  for (int i = 0; i < 3; i++)
    dp[i] = f(cal[i], unit[i]);
  int ans = 0;
  for (int i = 0; i < (int)dp[0].size(); i++) {
    for (int j = 0; j < (int)dp[1].size() && i + j <= x; j++) {
      int k = x - i - j;
      if (k < (int)dp[2].size())
        ans = max(ans, min({dp[0][i], dp[1][j], dp[2][k]}));
    }
  }
  cout << ans << '\n';
}
