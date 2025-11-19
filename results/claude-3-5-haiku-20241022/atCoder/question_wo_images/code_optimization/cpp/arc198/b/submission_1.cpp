#include <bits/stdc++.h>
using namespace std;

int main() {
  int t;
  scanf("%d", &t);
  
  while (t--) {
    long long x, y, z;
    scanf("%lld%lld%lld", &x, &y, &z);
    
    if (x < z) {
      puts("No");
      continue;
    }
    
    long long needed = 0;
    
    // Each 2 (except possibly last) needs up to 2 ones around it
    if (z > 0) {
      needed += min(2LL * z - 1, 2LL * z);
      needed = min(needed, 2LL * z - 1);
    }
    
    // Remaining 0's after pairing with 2's
    long long remaining_zeros = x - z;
    needed += 2LL * remaining_zeros;
    
    // If we have 2's, we might need one more 1
    if (z > 0) {
      needed += 1;
    }
    
    puts(y == needed ? "Yes" : "No");
  }
  
  return 0;
}