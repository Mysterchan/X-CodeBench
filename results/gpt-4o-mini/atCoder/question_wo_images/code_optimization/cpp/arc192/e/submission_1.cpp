#include <iostream>
#define MOD 998244353
using namespace std;

long long factorial[2000005], inverse[2000005];

// Function to compute modular inverse using Fermat's Little Theorem
long long modInverse(long long a, long long m) {
    long long m0 = m, y = 0, x = 1;
    if (m == 1) return 0;
    while (a > 1) {
        long long q = a / m;
        long long t = m;
        m = a % m, a = t;
        t = y;
        y = x - q * y;
        x = t;
    }
    if (x < 0) x += m0;
    return x;
}

// Precompute factorials and their modular inverses
void precompute(int maxN) {
    factorial[0] = 1;
    for (int i = 1; i <= maxN; i++)
        factorial[i] = factorial[i - 1] * i % MOD;
    
    for (int i = 0; i <= maxN; i++)
        inverse[i] = modInverse(factorial[i], MOD);
}

// Function to compute nCk
long long nCr(int n, int k) {
    if (k > n || n < 0 || k < 0) return 0;
    return factorial[n] * inverse[k] % MOD * inverse[n - k] % MOD;
}

int main() {
    int W, H, L, R, D, U;
    cin >> W >> H >> L >> R >> D >> U;
    
    // Precompute factorials up to 2 * (W + H)
    precompute(2000004);
    
    long long totalPaths = 0;

    // Iterate over all x positions in the range [0, W]
    for (int x = 0; (x <= W); x++) {
        if (x < L || x > R) {
            // Iterate over all y positions in the range [0, H]
            for (int y = 0; (y <= H); y++) {
                if (y < D || y > U) {
                    long long pathsToReach = nCr(W - x + H - y, W - x);
                    totalPaths = (totalPaths + pathsToReach) % MOD;
                }
            }
        }
    }
    
    // Output the total number of paths
    cout << totalPaths << endl;
    return 0;
}
