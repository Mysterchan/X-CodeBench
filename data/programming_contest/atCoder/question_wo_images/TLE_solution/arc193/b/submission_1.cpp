#include "bits/stdc++.h"
#include <chrono>
using namespace std;

#define LL long long
#define mod 998244353ll
#define PI acos(-1.0)
#define set0(ar) memset(ar, 0, sizeof ar)
#define setinf(ar) memset(ar, 126, sizeof ar)

inline LL bigmod(LL p, LL e, LL M) {
  LL r = 1;
  for (; e > 0; e >>= 1, p = (p * p) % M)
    if (e & 1) r = (r * p) % M;
  return r;
}
inline LL modinverse(LL a, LL M) { return bigmod(a, M - 2, M); }


LL dp[1000001][3][2][2][2][3];
string s;
LL go(int c, int last, int z, int t, int fst, int ftype, int n) {
  if(c >= n) {
    if(last == 0) return 1;
    if(last != ftype) return 1;
    if(last == 1 && t) return 1;
    if(last == 2 && z) return 1;
    if(fst) return 1;
    return 0;
  }
  LL &ret = dp[c][last][z][t][fst][ftype];
  if(ret != -1) return ret;
  ret = 0;

  {
    if(last == 0) ret += go(c+1, 1, 0, 0, t, 1, n);
    else if(last == 2 || t) ret += go(c+1, 1, 0, 0, fst, ftype, n);
  }
  {
    if(last == 0) ret += go(c+1, 2, 0, 0, z, 2, n);
    else if(last == 1 || z) ret += go(c+1, 2, 0, 0, fst, ftype, n);
  }
  if(s[c] == '0') {
    ret += go(c+1, last, z, t, fst, ftype, n);
  } else {
    ret += go(c+1, last, 1, t, fst, ftype, n) + go(c+1, last, z, 1, fst, ftype, n);
  }

  ret %= mod;
  return ret;
}


void solve() {
  int n; cin >> n;
  cin >> s;
  memset(dp, -1, sizeof dp);
  cout << go(0, 0, 0, 0, 0, 0, n) << endl;
}


int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int T = 1;
  for (int ts = 1; ts <= T; ts++) {
    solve();
  }
}
