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
  
  // dp[j] = number of ways to match first j elements of B
  // We cap at 2 to avoid overflow and for efficiency
  vector<long long> dp(m + 1, 0);
  dp[0] = 1; // one way to match empty sequence
  
  for (int i = 0; i < n; i++) {
    // Traverse backwards to avoid using same element twice
    for (int j = m - 1; j >= 0; j--) {
      if (a[i] == b[j]) {
        dp[j + 1] += dp[j];
        // Cap at 2 to avoid overflow
        if (dp[j + 1] > 2) {
          dp[j + 1] = 2;
        }
      }
    }
    // Early exit if we found 2 ways
    if (dp[m] >= 2) {
      cout << "Yes" << endl;
      return 0;
    }
  }
  
  cout << (dp[m] >= 2 ? "Yes" : "No") << endl;
  return 0;
}