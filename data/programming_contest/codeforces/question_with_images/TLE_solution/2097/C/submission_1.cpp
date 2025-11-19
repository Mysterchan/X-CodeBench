#include <bits/stdc++.h>
#define rep(i, j, k) for(int i = (j); i <= (k); ++i)
#define per(i, j, k) for(int i = (j); i >= (k); --i)
#define pb emplace_back
#define mp make_pair
#define fir first
#define sec second
using ll = long long;
template<class T> bool ckmin(T &a, const T &b) { return b < a ? a = b, true : false; }
template<class T> bool ckmax(T &a, const T &b) { return a < b ? a = b, true : false; }
using namespace std;
ll exgcd(ll a, ll b, ll &x, ll &y) {
    if (!b) {
        x = 1;
        y = 0;
        return a;
    }
    ll d = exgcd(b, a % b, x, y);
    ll t = x;
    x = y;
    y = t - (a / b) * y;
    return d;
}
ll cal(ll x, ll y, ll n) {
    if (x % n == 0) x++;
    if (y % n == 0) y--;
    ll nx = x / n * n, ny = y / n * n;
    while (nx > x) nx -= n;
    while (ny > y) ny -= n;
    while (nx < x) nx += n;
    while (ny < y) ny += n;
    return (ny - nx) / n;
}
void solve() {
    ll n, a, b, vx, vy; cin >> n >> a >> b >> vx >> vy;
    ll x, y;
    ll g = exgcd(n * vy, n * vx, x, y);
    ll d = vy * a - vx * b;
    if (d % g) cout << -1 << '\n';
    else {
        y = -y;
        x *= d / g, y *= d / g;
        while (x > 0 || y > 0) x -= n * vx / g, y -= n * vy / g;
        while (x <= 0 || y <= 0) x += n * vx / g, y += n * vy / g;
        x *= n, y *= n;
        ll ans = 0;
        ans += cal(a, x, n) + cal(b, y, n);
        y -= n;
        b -= n;
        ans += cal(min(a + b, x + y), max(a + b, x + y), 2 * n);
        ans += cal(min(a - b, x - y), max(a - b, x - y), 2 * n);
        cout << ans << '\n';
    }
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int T; cin >> T;
    while (T--) solve();
    return 0;
}