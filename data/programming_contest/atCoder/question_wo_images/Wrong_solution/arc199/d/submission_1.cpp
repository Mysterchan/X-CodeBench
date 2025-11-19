#include <iostream>
using namespace std;

const int MOD = 998244353;

int combination(int n, int k) {
    if (k == 0 || k == n) return 1;
    long long res = 1;
    for (int i = 1; i <= k; ++i) {
        res *= (n - (k - i));
        res /= i;
        res %= MOD;
    }
    return res;
}

int main() {
    int H, W;
    cin >> H >> W;

    int ans = 0;
    for (int i = 1; i <= H; ++i) {
        for (int j = 1; j <= W; ++j) {
            int numSet = combination(H, i) * 1LL * combination(W, j) % MOD;
            numSet *= (1LL << (H + W - i - j)) % MOD;
            ans = (ans + numSet) % MOD;
        }
    }
    cout << ans << endl;
    return 0;
}