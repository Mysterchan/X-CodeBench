#include <bits/stdc++.h>
using namespace std;
using i64 = long long;
typedef long long ll;
typedef unsigned long long ull;
typedef __int128 lll;
#define int long long
#define endl '\n'
const int N = 111;
int n,m,a,b;
unordered_map<int,int> mp;
int count(int n,int m) {
    if (n == 1 && m == 1) return 0;
    ull k = ( (int)n << 32 ) ^ (int)m;
    auto it = mp.find(k);
    if (it != mp.end()) return it->second;
    int h1 = (n + 1) / 2;
    int h2 = (m + 1) / 2;
    int r1 = LLONG_MAX, r2 = LLONG_MAX;
    if (n > 1) r1 = count(h1, m);
    if (m > 1) r2 = count(n, h2);
    int res = 1 + min(r1, r2);
    return mp[k] = res;
}
void solve() {
    cin>>n>>m>>a>>b;
     if (n == 1 && m == 1) {
        cout << 0 << endl;
        return;
    }
    int h = min(a, n - a + 1);
    int w = min(b, m - b + 1);
    int c1 = (n > 1 ? count(h, m) : LLONG_MAX);
    int c2 = (m > 1 ? count(n, w) : LLONG_MAX);
    int ans = 1 + min(c1, c2);
    cout << ans << endl;
}

signed main() {
    ios::sync_with_stdio(0), cin.tie(0);
    int _;
    cin >> _;
    while (_--) solve();
    return 0;
}