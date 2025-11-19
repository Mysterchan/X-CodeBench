#include <bits/stdc++.h>
using namespace std;

#define LL long long
#define mod 998244353ll

string s;
map<tuple<int,int,int,int,int,int>, LL> memo;

LL go(int c, int last, int z, int t, int fst, int ftype, int n) {
  if(c >= n) {
    if(last == 0) return 1;
    if(last != ftype) return 1;
    if(last == 1 && t) return 1;
    if(last == 2 && z) return 1;
    if(fst) return 1;
    return 0;
  }
  
  auto key = make_tuple(c, last, z, t, fst, ftype);
  auto it = memo.find(key);
  if(it != memo.end()) return it->second;
  
  LL ret = 0;

  // Edge from i to i+1
  if(last == 0) {
    ret += go(c+1, 1, 0, 0, t, 1, n);
  } else if(last == 2 || t) {
    ret += go(c+1, 1, 0, 0, fst, ftype, n);
  }
  
  // Edge from i+1 to i
  if(last == 0) {
    ret += go(c+1, 2, 0, 0, z, 2, n);
  } else if(last == 1 || z) {
    ret += go(c+1, 2, 0, 0, fst, ftype, n);
  }
  
  // Edges with vertex N
  if(s[c] == '0') {
    ret += go(c+1, last, z, t, fst, ftype, n);
  } else {
    ret += go(c+1, last, 1, t, fst, ftype, n);
    ret += go(c+1, last, z, 1, fst, ftype, n);
  }

  ret %= mod;
  memo[key] = ret;
  return ret;
}

void solve() {
  int n; 
  cin >> n >> s;
  memo.clear();
  cout << go(0, 0, 0, 0, 0, 0, n) << endl;
}

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  solve();
}