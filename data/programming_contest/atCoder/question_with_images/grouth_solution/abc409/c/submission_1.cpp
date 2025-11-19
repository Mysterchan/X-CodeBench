#include <bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < n; i++)
using namespace std;
using ll = long long;
int main(){
  int N, L;
  cin >> N >> L;
  vector<ll> d(N - 1), p(N, 0), q(L, 0);
  int count = 0;
  q[0] = 1;
  rep(i, N - 1){
    cin >> d[i];
    count += d[i];
    count %= L;
    p[i] = count;
    q[count]++;
  }
  if(L % 3 != 0)cout << 0 << endl;
  else{
    int l = L / 3;
    ll ans = 0;
    rep(i, l){
      ans += q[i] * q[i + l] * q[i + 2 * l];
    }
    cout << ans << endl;
  }
}