#include <bits/stdc++.h>
using namespace std;

#define int long long

int t, n, k;

void solve() {
  cin >> n >> k;
  
  int msb = 63 - __builtin_clzll(n);
  int limit = (1LL << (msb + 1));
  
  int count = 0;
  for (int bit = msb; bit >= 0; bit--) {
    if (n >> bit & 1) {
      int base = 1LL << bit;
      int candidates = min(base, limit - base);
      
      if (count + candidates >= k) {
        int offset = k - count - 1;
        int x = base + offset;
        return cout << x << '\n', void();
      }
      count += candidates;
    }
  }
  
  cout << "-1\n";
} 

signed main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cin >> t;
  while (t--) solve();
  return 0;
}