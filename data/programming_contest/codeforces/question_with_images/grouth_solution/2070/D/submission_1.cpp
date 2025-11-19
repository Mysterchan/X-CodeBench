#pragma GCC optimize("O3")
#pragma GCC optimize("unroll-loops")
#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef vector<ll> vi;
typedef vector<vi> vvi;
#define FOR(i,l,r) for(ll i=l;i<r;i++)
#define REP(i,n) FOR(i,0,n)
#define RREP(i,n) for(ll i=n-1;i>=0;i--)
#define sz(c) (ll)(c.size())

template<const long long int mod=998244353>
struct modint {
    using mint = modint<mod>;
    long long int x;
    modint(long long int _x=0):x(_x%mod){if(x<0)x+=mod;}
    long long int val(){return x;}
    mint& operator+=(const mint&a){x+=a.x;if(x>=mod)x-=mod;return *this;}
    mint& operator-=(const mint&a){x-=a.x;if(x<0)x+=mod;return *this;}
    mint& operator*=(const mint&a){x*=a.x;x%=mod;return *this;}
    friend mint operator+(const mint&a,const mint&b){return mint(a)+=b;}
    friend mint operator-(const mint&a,const mint&b){return mint(a)-=b;}
    friend mint operator*(const mint&a,const mint&b){return mint(a)*=b;}
};
using mint = modint<998244353>;
typedef vector<mint> vm;

int main() {
    std::cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);
    int _ = 1; cin >> _;
    while (_--) {
        ll N; cin >> N;
        vi P(N);
        FOR(i, 1, N) { cin >> P[i]; P[i]--; }
        vi D(N);
        FOR(i, 1, N) {
            D[i] = D[P[i]] + 1;
        }
        vvi C(N);
        FOR(i, 1, N) C[P[i]].emplace_back(i);
        vvi E(N);
        REP(i, N) E[D[i]].emplace_back(i);
        vm DP(N);
        RREP(d, N) if (sz(E[d])) {
            mint s = 0;
            for (auto v : E[d]) {
                for (auto u : C[v]) {
                    s = s + DP[u];
                }
            }
            for (auto v : E[d]) {
                DP[v] = s + 1;
                if (d) for (auto u : C[v]) DP[v] = DP[v] - DP[u];
            }
        }
        cout << DP[0].val() << endl;
    }
    return 0;
}