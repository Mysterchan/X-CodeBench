#include <iostream>
using namespace std;
using LL = long long;
const int mod = 998244353;

inline int mod_add(int a, int b) {
    a += b;
    if (a >= mod) a -= mod;
    return a;
}

inline int mod_sub(int a, int b) {
    a -= b;
    if (a < 0) a += mod;
    return a;
}

inline int mod_mul(int a, int b) {
    return (int)((LL)a * b % mod);
}

int mod_pow(int base, LL exp) {
    int res = 1;
    int cur = base;
    while (exp > 0) {
        if (exp & 1) res = mod_mul(res, cur);
        cur = mod_mul(cur, cur);
        exp >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int H, W;
    cin >> H >> W;

    // The problem reduces to:
    // Number of matrices = 2^(H+W)
    // Sum of all elements over all matrices = H * W * 3^(H+W-2) mod 998244353

    if (H == 1 && W == 1) {
        // Only two matrices: all zero and all one
        // Sum of elements over all matrices = 0 + 1 = 1
        cout << 1 << "\n";
        return 0;
    }

    int pw = mod_pow(3, (LL)H + W - 2);
    int ans = mod_mul(mod_mul(H, W), pw);
    cout << ans << "\n";

    return 0;
}