#include<bits/stdc++.h>
using namespace std;
#define rep(i, s, t) for(int i = (s); i <= (t); i ++)
#define per(i, s, t) for(int i = (s); i >= (t); i --)
template<typename T, typename T2>
inline void chmin(T &x, T2 &&y) { x = min(x, y); }
template<typename T, typename T2>
inline void chmax(T &x, T2 &&y) { x = max(x, y); }
typedef long long ll;

void solve()
{
    int a, b, c; cin >> a >> b >> c;
    if(!c && (b & 1)) return cout << "No\n", void();
    if(max((b + 1) / 2, c) > a)  return cout << "No\n", void();
    cout << "Yes\n";
}

signed main()
{
    ios::sync_with_stdio(0);cin.tie(0);
    int t;cin >> t;while(t --) solve();

    return 0;
}