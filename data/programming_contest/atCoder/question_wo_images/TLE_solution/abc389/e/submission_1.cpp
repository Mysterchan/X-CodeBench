#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (ll i = 0; i < (ll)(n); i++)
#define rep2(i, s, n) for (ll i = (s); i < (ll)(n); i++)
#define rrep(i, n) rep2(i, 1, n + 1)
#define repd(i,n) for(ll i=n-1;i>=0;i--)
#define rrepd(i,n) for(ll i=n;i>=1;i--)
#define fore(a, b) for (auto a : b)
#define _GLIBCXX_DEBUG
#define all(v) v.begin(), v.end()
using ll = long long;
using Graph = vector<vector<int>>;
#define YESNO(bool) if(bool){cout<<"YES"<<endl;}else{cout<<"NO"<<endl;}
#define yesno(bool) if(bool){cout<<"yes"<<endl;}else{cout<<"no"<<endl;}
#define YesNo(bool) if(bool){cout<<"Yes"<<endl;}else{cout<<"No"<<endl;}
using pii = pair<int, int>;
using pll = pair<ll, ll>;
using tll = tuple<ll, ll, ll>;

ll bin(ll p, ll next){
    ll ok = 1e9, ng = 0;
    while(ok - ng > 1){
        ll mid = (ok + ng) / 2;
        if(mid * mid * p > next) ok = mid;
        else ng = mid;
    }
    return ok;
}

ll bin2(ll p, ll m, ll tot, ll v){
    ll ok = 1e9, ng = 0;
    while(ok - ng > 0){
        ll mid = (ok + ng) / 2;
        if(tot + mid * mid * p - v <= m) ok = mid;
        else ng = mid;
    }
    return ok;
}

int main(){
    ll n, m; cin >> n >> m;
    vector<ll> p(n);
    rep(i, n) cin >> p[i];
    priority_queue<tll, vector<tll>, greater<tll>> que;
    ll ans = 0;
    ll tot = 0;
    rep(i, n) que.push({p[i], 1, i});
    while(true){
        auto [gain, k, idx] = que.top();
        que.pop();
        if(tot + gain > m) break;
        tot += gain;
        ans++;
        que.push({p[idx] * (2 * k + 1), k + 1, idx});
    }   
    cout << ans << endl;
}