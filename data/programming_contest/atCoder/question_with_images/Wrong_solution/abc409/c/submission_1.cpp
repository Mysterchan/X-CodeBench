#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using P = pair<int,int>;

#define rep(i,n) for(int i=0; i<(n); ++i)
#define rep1(i,n) for(int i=1; i<=(n); ++i)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define pb push_back
#define eb emplace_back
#define fi first
#define se second
#define fast_io ios::sync_with_stdio(false); cin.tie(nullptr)

const ll INF = (1LL<<60);
const int MOD = 1000000007;

template<class T> bool chmin(T &a, const T &b){ if(a>b){ a=b; return true; } return false; }
template<class T> bool chmax(T &a, const T &b){ if(a<b){ a=b; return true; } return false; }

int main(){
    ll N, L;
    cin>>N>>L;
    vector<ll> x(N);
    x[0] = 0;

    for(int i=1; i<N; i++) {
        ll d;
        cin>>d;
        x[i] = x[i-1] + d;
        x[i] %= L;
    }
    
    vector<ll> M(L);
    
    rep(i, N){
        M[x[i]] += 1;
    }
    int ans =0;
    int r = L/3;
    rep(i, L){
        ans += M[i] * M[(i + r)%L] * M[(i + 2*r)%L];
    }
    cout<<ans/3<<endl;

}