#include <iostream>
using namespace std;

const int MOD = 998244353;

long long mod_pow(long long base, long long exp, long long mod) {
    long long result = 1;
    while (exp) {
        if (exp & 1) result = result * base % mod;
        base = base * base % mod;
        exp >>= 1;
    }
    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int H, W;
    cin >> H >> W;

    // Total number of matrices obtained by operations
    long long total_matrices = mod_pow(2, H + W, MOD);

    // Total sum is total_matrices * (H + W) - the empty matrix case
    long long answer = (total_matrices * (H + W) % MOD - 1 + MOD) % MOD;

    cout << answer << '\n';
    return 0;
}
