#include <bits/stdc++.h>

using i64 = long long;
constexpr i64 mod = 998244353;
constexpr i64 inv2 = 499122177;
constexpr i64 inv24 = 332748118 * inv2 % mod * inv2 % mod * inv2 % mod;

inline i64 count1(int n, int m) {
    return (m - n) * (m - n + 1) % mod * inv2 % mod;
}

inline i64 count2(int n, int m) {
    
    return (m - n - 1) * (m - n) % mod * (m - n + 1) % mod * (m - n + 2) % mod * inv24 % mod;
}

inline void solve() {
    int n, h, w;
    scanf("%d%d%d", &n, &h, &w);

    if (std::min(h, w) < n * 2) {
        return puts("0"), void();
    }

    h -= n - 1, w -= n - 1;

    i64 ans1 = count1(n, h) * count1(n, w) % mod;
    ans1 = ans1 * ans1 % mod;

    i64 ans2 = count2(n, h) * count2(n, w) % mod;

    printf("%lld\n", (ans1 - ans2 * 2 + mod * 2) % mod);    
}

int main() {
    int t; scanf("%d", &t);
    while (t--) solve();
    return 0;
}