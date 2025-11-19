#include <bits/stdc++.h>
using namespace std;
template<class T>bool chmax(T &a, const T &b) { if (a<b) { a=b; return true; } return false; }
template<class T>bool chmin(T &a, const T &b) { if (b<a) { a=b; return true; } return false; }
#define all(x) (x).begin(), (x).end()
#define All(x) (x).begin() + 1, (x).end()
using ull = unsigned long long;
using ll = long long;

constexpr int mod = 998244353;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> a(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
    }

    vector<int> f(n + 1);
    int x = 0, px = 0;
    for (int i = 1; i <= n; i++) {
        if (a[i] == -1) {
            continue;
        }
        if (i < n && a[i] == i + 1) {
            f[i] = 1;
        } else if (i > 1 && a[i] == i - 1) {
            f[i] = -1;
        } else {
            x++;
            px = i;
        }
    }

    int R = 0, L = n + 1;
    for (int i = 1; i <= n; i++) {
        if (f[i] == 1) {
            chmax(R, i);
        } else if (f[i] == -1) {
            chmin(L, i);
        }
    }

    if (R >= L || x > 1) {
        cout << 0 << '\n';
        return 0;
    }

    if (x == 0) {
        if (R + 1 == L) {
            cout << 1 << '\n';
            return 0;
        }
        ll ans = L - R - (R == 0) - (L == n + 1);
        for (int i = R + 1; i < L; i++) {
            ans += n - (i > 1) - (i < n);
            ans %= mod;
        }
        cout << ans << '\n';
    } else {
        cout << (px > R && px < L) << '\n';
    }

    return 0;
}