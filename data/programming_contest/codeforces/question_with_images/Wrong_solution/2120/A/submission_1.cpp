#include <stdio.h>
#include <stdint.h>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <map>
#include <stack>

using namespace std;

void solve(int32_t x[]) {
  if(x[0] == x[2] && x[2] == x[4]) {
    if(x[1] + x[3] + x[5] == x[0]) {
      printf("YES\n");
      return ;
    }
  }
  if(x[1] == x[3] && x[3] == x[5]) {
    if(x[0] + x[2] + x[4] == x[1]) {
      printf("YES\n");
      return ;
    }
  }
  if(x[0] == x[2] + x[4] || x[1] == x[3] + x[5]) {
    printf("YES\n");
    return ;
  }
  printf("NO\n");
}

int main() {
  int32_t t;
  cin >> t;
  while(t--) {
    int32_t x[6];
    for(int32_t i = 0; i < 6; i++) {
      cin >> x[i];
    }
    solve(x);
  }
}