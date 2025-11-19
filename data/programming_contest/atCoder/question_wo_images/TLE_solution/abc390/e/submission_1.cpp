#pragma GCC optimize("O3")
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

constexpr int INF = 1001001001;
constexpr ll LINF = 1001001001001001001ll;
constexpr int di[] = {0, -1, 0, 1};
constexpr int dj[] = {1, 0, -1, 0};

template <typename T> inline bool chmin(T& a, const T& b) {bool compare = a > b; if (a > b) a = b; return compare;}
template <typename T> inline bool chmax(T& a, const T& b) {bool compare = a < b; if (a < b) a = b; return compare;}
template <typename T> ostream& operator<<(ostream& os, const vector<T>& v) { for (const auto& e:v) os << e << " "; return os; }

int32_t main() {
  ios::sync_with_stdio(false);
	cin.tie(nullptr);

  int N, X; cin>>N>>X;
  vector<vector<tuple<ll, ll, ll>>> dp(X+1); dp[0].push_back({0, 0, 0});
  while(N--) {
    int V, C; ll A; cin>>V>>A>>C;
    ll ni=0, nj=0, nk=0;
    if(V==1) ni+=A;
    if(V==2) nj+=A;
    if(V==3) nk+=A;
    for(int i=X-C; i>=0; --i) {
      for(const auto& [vi, vj, vk]: dp[i]) dp[i+C].push_back({vi+ni, vj+nj, vk+nk});
    }
  }
  ll res=0;
  for(const auto& vec: dp) for(const auto& [vi, vj, vk]: vec) chmax(res, min({vi, vj, vk}));
  cout << res << endl;

  return 0;
}