#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll exgcd(ll a, ll b, ll &x, ll &y) {
    if (b == 0) {
        x = 1; y = 0;
        return a;
    }
    ll d = exgcd(b, a % b, x, y);
    ll t = x;
    x = y;
    y = t - (a / b) * y;
    return d;
}

ll cal(ll x, ll y, ll n) {
    // Count how many multiples of n are strictly between x and y
    if (x % n == 0) x++;
    if (y % n == 0) y--;
    if (x > y) return 0;
    ll nx = (x + n - 1) / n * n;
    ll ny = y / n * n;
    if (nx > ny) return 0;
    return (ny - nx) / n + 1;
}

void solve() {
    ll n, a, b, vx, vy; 
    cin >> n >> a >> b >> vx >> vy;

    // Solve the Diophantine equation:
    // n*vy * X - n*vx * Y = vy*a - vx*b
    // to find integers X, Y > 0 such that:
    // x = n*vx*X, y = n*vy*Y are the coordinates of the vertex reached.

    ll x, y;
    ll g = exgcd(n * vy, n * vx, x, y);
    ll d = vy * a - vx * b;

    if (d % g != 0) {
        cout << -1 << '\n';
        return;
    }

    // Scale solution
    x *= d / g;
    y *= d / g;
    y = -y; // Because equation was rearranged

    // Adjust solution to positive X, Y
    ll vxg = n * vx / g;
    ll vyg = n * vy / g;

    // Shift solution to positive quadrant
    // We want x > 0 and y > 0
    // x = x + k * vxg
    // y = y + k * vyg
    // Find k such that both positive
    ll k1 = (x <= 0) ? ((-x + vxg - 1) / vxg) : 0;
    ll k2 = (y <= 0) ? ((-y + vyg - 1) / vyg) : 0;
    ll k = max(k1, k2);
    x += k * vxg;
    y += k * vyg;

    // Now count the number of boundary hits before reaching vertex (x,y)
    // Hits on vertical boundary x=0 or x=n*k:
    ll ans = 0;
    ans += cal(a, x, n);
    // Hits on horizontal boundary y=0 or y=n*k:
    ans += cal(b, y, n);

    // Hits on hypotenuse x + y = n*k:
    // We count hits on line x + y = m*2n (period 2n)
    // Because reflections cause periodicity of 2n on this line
    ans += cal(min(a + b, x + y), max(a + b, x + y), 2 * n);

    // Hits on line x - y = m*2n (period 2n)
    ans += cal(min(a - b, x - y), max(a - b, x - y), 2 * n);

    cout << ans << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;
    while (T--) solve();
    return 0;
}