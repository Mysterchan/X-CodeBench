#include <bits/stdc++.h>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int N, K;
  cin >> N >> K;

  vector<int> P(N * K);
  for (auto &e : P) {
    cin >> e;
    e--;
  }

  auto solve = [&](vector<int>& cycle) -> int {
    int M = cycle.size();
    if (M <= 1) return 0;

    vector<vector<int>> indices(N);
    for (int i = 0; i < M; i++) {
      indices[cycle[i] % N].push_back(i);
    }

    vector<int> dp(M, 0);
    vector<int> new_dp(M);
    
    for (int len = 2; len <= M; len++) {
      fill(new_dp.begin(), new_dp.end(), 0);
      
      for (int j = 0; j < M; j++) {
        new_dp[j] = dp[(j + 1) % M];
        
        int mod = cycle[j] % N;
        for (auto k : indices[mod]) {
          if (k == j) continue;
          
          int k_norm = k < j ? k + M : k;
          if (k_norm > j && k_norm < j + len) {
            int left_len = k_norm - j;
            int right_len = len - left_len;
            
            if (left_len <= M && right_len <= M) {
              int left_val = (left_len == 1) ? 0 : dp[j];
              int right_val = (right_len == 1) ? 0 : dp[k];
              new_dp[j] = max(new_dp[j], left_val + right_val + 1);
            }
          }
        }
      }
      
      swap(dp, new_dp);
    }

    return *max_element(dp.begin(), dp.end());
  };

  vector<bool> seen(N * K, false);
  int ans = 0;
  
  for (int i = 0; i < N * K; i++) {
    if (seen[i]) continue;
    
    vector<int> cycle;
    for (int j = i; !seen[j]; j = P[j]) {
      seen[j] = true;
      cycle.push_back(j);
    }
    
    if (cycle.size() > 1) {
      ans += solve(cycle);
    }
  }
  
  cout << ans << '\n';
  
  return 0;
}