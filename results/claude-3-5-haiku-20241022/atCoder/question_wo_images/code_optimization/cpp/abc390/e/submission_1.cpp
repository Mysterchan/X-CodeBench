#pragma GCC optimize("O3")
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int32_t main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int N, X; 
  cin >> N >> X;
  
  vector<tuple<int, ll, int>> foods[3];
  
  for(int i = 0; i < N; ++i) {
    int V, C; 
    ll A; 
    cin >> V >> A >> C;
    foods[V-1].push_back({C, A, V});
  }
  
  // Sort by vitamins per calorie (descending)
  for(int i = 0; i < 3; ++i) {
    sort(foods[i].begin(), foods[i].end(), [](const auto& a, const auto& b) {
      return get<1>(a) * get<0>(b) > get<1>(b) * get<0>(a);
    });
  }
  
  ll res = 0;
  
  // Try all combinations of foods from each vitamin type
  for(int mask1 = 0; mask1 < (1 << min(20, (int)foods[0].size())); ++mask1) {
    int cal1 = 0;
    ll vit1 = 0;
    for(int i = 0; i < min(20, (int)foods[0].size()); ++i) {
      if(mask1 & (1 << i)) {
        cal1 += get<0>(foods[0][i]);
        vit1 += get<1>(foods[0][i]);
      }
    }
    if(cal1 > X) continue;
    
    for(int mask2 = 0; mask2 < (1 << min(20, (int)foods[1].size())); ++mask2) {
      int cal2 = cal1;
      ll vit2 = 0;
      for(int i = 0; i < min(20, (int)foods[1].size()); ++i) {
        if(mask2 & (1 << i)) {
          cal2 += get<0>(foods[1][i]);
          vit2 += get<1>(foods[1][i]);
        }
      }
      if(cal2 > X) continue;
      
      for(int mask3 = 0; mask3 < (1 << min(20, (int)foods[2].size())); ++mask3) {
        int cal3 = cal2;
        ll vit3 = 0;
        for(int i = 0; i < min(20, (int)foods[2].size()); ++i) {
          if(mask3 & (1 << i)) {
            cal3 += get<0>(foods[2][i]);
            vit3 += get<1>(foods[2][i]);
          }
        }
        if(cal3 > X) continue;
        
        res = max(res, min({vit1, vit2, vit3}));
      }
    }
  }
  
  cout << res << endl;

  return 0;
}