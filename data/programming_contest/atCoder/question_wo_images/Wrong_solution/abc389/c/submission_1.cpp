#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <ctime>
#include <cassert>
#include <complex>
#include <string>
#include <cstring>
#include <chrono>
#include <random>
#include <bitset>
#include <array>
#include <climits>
#include <iomanip>
#include <utility>
#include <stack>


using namespace std;

using ll = long long;
using ull = unsigned long long;
using pii = pair<int, int>;
using vi = vector<int>;
using vvi = vector<vi>;
using vll = vector<long long>;


void solve(){
  int q;
  cin >> q;
  vll pre;
  int bias = 0;
  ll sum = 0;
  while(q--){
    int cmd; cin >> cmd;
    if(cmd == 1){
      int l; cin >> l;
      sum += l;
      pre.push_back(sum);
    }else if(cmd == 2){
      bias++;
    }else{
      int k; cin >> k;
      --k;
      ll ans = pre[k-1 + bias];
      ll sbt = (bias -1 >= 0 ? pre[bias-1] : 0);
      
      cout << ans - sbt << '\n';
    }
  }
}


int main(){

  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int t = 1;

  while(t--){
    solve();
  }
  
  return 0;
}
