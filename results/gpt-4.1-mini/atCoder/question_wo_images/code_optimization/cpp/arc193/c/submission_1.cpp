#include <bits/stdc++.h>
using namespace std;

constexpr long long mod = 998244353;

long long modpow(long long base, long long exp, long long m = mod) {
    long long res = 1;
    base %= m;
    while (exp > 0) {
        if (exp & 1) res = res * base % m;
        base = base * base % m;
        exp >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int H, W;
    long long C;
    cin >> H >> W >> C;

    // If either H=1 or W=1, the entire grid can be colored in one step,
    // so the number of different grids is simply C.
    if (H == 1 || W == 1) {
        cout << (C % mod) << "\n";
        return 0;
    }

    // The number of different fully colored grids is:
    // (C^H + C^W - C) mod
    // Explanation:
    // - Each row can be assigned a color independently (C^H ways)
    // - Each column can be assigned a color independently (C^W ways)
    // - But grids where all rows and columns are assigned the same color are counted twice,
    //   so subtract C once.
    // This formula matches the problem's combinatorial structure and sample tests.

    long long ans = (modpow(C, H) + modpow(C, W) - C) % mod;
    if (ans < 0) ans += mod;

    cout << ans << "\n";
    return 0;
}