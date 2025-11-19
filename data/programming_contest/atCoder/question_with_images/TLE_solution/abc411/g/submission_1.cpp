#include <bits/stdc++.h> 
using namespace std;
using ll =long long;
#define all(v) v.begin(),v.end()
 #define rep(i,a,b) for(int i=a;i<b;i++)
#define rrep(i,a,b) for(int i=a;i>=b;i--)

ll INF=2e18;

const int mod = 998244353;
class mint {
    long long x;
public:
    mint(long long x=0) : x((x%mod+mod)%mod) {}
    mint operator-() const { 
      return mint(-x);
    }
    mint& operator+=(const mint& a) {
        if ((x += a.x) >= mod) x -= mod;
        return *this;
    }
    mint& operator-=(const mint& a) {
        if ((x += mod-a.x) >= mod) x -= mod;
        return *this;
    }
    mint& operator*=(const  mint& a) {
        (x *= a.x) %= mod;
        return *this;
    }
    mint operator+(const mint& a) const {
        mint res(*this);
        return res+=a;
    }
    mint operator-(const mint& a) const {
        mint res(*this);
        return res-=a;
    }
    mint operator*(const mint& a) const {
        mint res(*this);
        return res*=a;
    }
    mint pow(ll t) const {
        if (!t) return 1;
        mint a = pow(t>>1);
        a *= a;
        if (t&1) a *= *this;
        return a;
    }
    mint inv() const {
        return pow(mod-2);
    }
    mint& operator/=(const mint& a) {
        return (*this) *= a.inv();
    }
    mint operator/(const mint& a) const {
        mint res(*this);
        return res/=a;
    }

    friend ostream& operator<<(ostream& os, const mint& m){
        os << m.x;
        return os;
    }
};


int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

ll N,M;cin>>N>>M;
vector<vector<ll>> vec(N,vector<ll> (N));
for(ll i=0;i<M;i++) {
  ll U,V;cin>>U>>V;U--;V--;
  vec[U][V]++,vec[V][U]++;
}

vector<vector<vector<mint>>> dp(N,vector<vector<mint>> (N,vector<mint> ((1LL<<N))));
for(ll i=0;i<N;i++) {
  for(ll j=0;j<N;j++) {
    if(i==j) continue;
    dp[i][j][(1LL<<i)+(1LL<<j)]=vec[i][j];
  }
}

for(ll i=0;i<(1LL<<N);i++) {
  vector<ll> a(0),b(0);
  for(ll j=0;j<N;j++) {
    if(i&(1LL<<j)) a.push_back(j);
    else b.push_back(j);
  }

  for(ll j=0;j<a.size();j++) {
    for(ll h=0;h<a.size();h++) {
      if(h==j) continue;
      for(ll k=0;k<b.size();k++) {
        dp[a[j]][b[k]][i+(1LL<<b[k])]+=dp[a[j]][a[h]][i]*vec[a[h]][b[k]];
      }
    }
  }
}

mint ans=0;
vector<mint> memo(N+1);
for(ll i=0;i<(1LL<<N);i++) {
  vector<ll> a(0);
  for(ll j=0;j<N;j++) {
    if(i&(1LL<<j)) a.push_back(j);
  }
  sort(all(a));
  ll cnt=__builtin_popcount(i);
  for(ll j=0;j<a.size();j++) {
    for(ll h=j+1;h<a.size();h++) {

     if(a.size()==2)  memo[cnt]+=dp[a[j]][a[h]][i]*(vec[a[h]][a[j]]-1);
     else  memo[cnt]+=dp[a[j]][a[h]][i]*(vec[a[h]][a[j]]);
    }
  }
}



for(ll i=2;i<=N;i++) {
  ans+=memo[i]/i;
}

cout<<ans<<endl;
}




 







  

