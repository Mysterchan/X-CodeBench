#ifdef NACHIA
#define _GLIBCXX_DEBUG
#else
#define NDEBUG
#endif
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
using ll = long long;
const ll INF = 1ll << 60;
#define REP(i,n) for(ll i=0; i<ll(n); i++)
template <class T> using V = vector<T>;
template <class A, class B> void chmax(A& l, const B& r){ if(l < r) l = r; }
template <class A, class B> void chmin(A& l, const B& r){ if(r < l) l = r; }

void testcase(){
  ll N, rk, ck, rd, cd; cin >> N >> rk >> ck >> rd >> cd;
  if(rk > rd){
    rk = N-rk;
    rd = N-rd;
  }
  if(ck > cd){
    ck = N-ck;
    cd = N-cd;
  }
  ll ans = 0;
  if(rk != rd){
    chmax(ans, rd);
  }
  if(ck != cd){
    chmax(ans, cd);
  }
  cout << ans << "\n";
}

int main(){
  cin.tie(0)->sync_with_stdio(0);
  ll T; cin >> T;
  REP(t,T)
  testcase();
  return 0;
}
