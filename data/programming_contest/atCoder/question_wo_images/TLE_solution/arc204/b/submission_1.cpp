#include <bits/stdc++.h>

#include <algorithm>

using namespace std;

const int INF = 1e9;

int main() {
  cin.tie(0)->sync_with_stdio(0);

  int N, K;
  cin >> N >> K;

  vector<int> P(N * K);
  for (auto &e : P) {
    cin >> e;
    e--;
  }

  vector<vector<int>> indices(N);
  auto solve = [&](vector<int> cycle) -> int {
    if (cycle.empty()) return 0;

    int M = cycle.size();

    for (auto e : cycle) {
      indices[e % N].clear();
    }
    for (int i = 0; i < M; i++) {
      indices[cycle[i] % N].push_back(i);
    }

    auto chmax = [&](int &a, int b) -> void { a = max(a, b); };

    vector dp(M + 1, vector<int>(M, -INF));
    for (int i = 0; i < M; i++) {
      dp[1][i] = 0;
    }
    for (int i = 2; i <= M; i++) {
      for (int j = 0; j < M; j++) {
        chmax(dp[i][j], dp[i - 1][(j + 1) % M]);
        for (auto k : indices[cycle[j] % N]) {
          int k_ = k < j ? k + M : k;
          if (k_ <= j or j + i <= k_) continue;
          chmax(dp[i][j], dp[k_ - j][j] + dp[i - (k_ - j)][k] + 1);
        }
      }
    }

    return *max_element(dp[M].begin(), dp[M].end());
  };

  vector<bool> seen(N * K, false);
  int ans = 0;
  for (int i = 0; i < N * K; i++) {
    vector<int> cycle;
    for (int j = i; !seen[j]; seen[j] = true, j = P[j]) {
      cycle.push_back(j);
    }
    ans += solve(cycle);
  }
  cout << ans << '\n';
}