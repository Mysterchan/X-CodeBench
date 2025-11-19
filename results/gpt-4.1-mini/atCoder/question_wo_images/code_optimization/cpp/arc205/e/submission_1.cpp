#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;
const int MAXB = 20;
const int MAX_MASK = 1 << MAXB;

int n;
int a[400005];
int freq[MAX_MASK];
int prod[MAX_MASK];

// Modular multiplication
inline int mul(int a, int b) {
    return (int)((1LL * a * b) % MOD);
}

// Modular exponentiation
int modpow(int base, int exp) {
    int res = 1;
    int cur = base;
    while (exp > 0) {
        if (exp & 1) res = mul(res, cur);
        cur = mul(cur, cur);
        exp >>= 1;
    }
    return res;
}

// Modular inverse using Fermat's little theorem (MOD is prime)
inline int modinv(int x) {
    return modpow(x, MOD - 2);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;
    for (int i = 1; i <= n; i++) cin >> a[i];

    // freq[x] = product of all A_j == x (mod MOD)
    // Initialize freq with 1
    fill(freq, freq + MAX_MASK, 1);

    // We'll maintain freq[x] as product of all A_j == x for j <= current i
    // For each i, we update freq[a[i]] *= a[i]

    // After updating freq, we compute prod = SOS product over subsets:
    // prod[mask] = product of freq[submask] for all submask subset of mask
    // This is done by SOS DP over subsets

    // We'll do incremental updates:
    // For each i:
    //   freq[a[i]] *= a[i]
    //   Recompute prod using SOS DP
    //   Output prod[a[i]]

    // To avoid recomputing prod from scratch each time (which is O(N*2^20)),
    // we use a block approach similar to original code but optimized.

    // Block size chosen to balance time and memory
    const int BLOCK = 1024;

    // freq and prod arrays
    // freq: product of all elements equal to mask in processed blocks
    // prod: SOS product over freq

    // We'll process in blocks:
    // For each block:
    //   Update freq with all elements in block
    //   Compute prod by SOS DP
    //   For each element in block:
    //     ans = prod[a[i]] * product of elements in current block before i that satisfy condition

    // To handle the "product of elements in current block before i that satisfy (a[j] | a[i]) == a[i]",
    // we keep the elements of the block and for each i in block, iterate over previous elements in block.

    // This approach is O(N * BLOCK + BLOCK * 2^20) which is feasible for BLOCK ~ 1024.

    int blocks = (n + BLOCK - 1) / BLOCK;

    // freq and prod initialized to 1
    fill(freq, freq + MAX_MASK, 1);
    fill(prod, prod + MAX_MASK, 1);

    for (int b = 0; b < blocks; b++) {
        int start = b * BLOCK + 1;
        int end = min(n, (b + 1) * BLOCK);

        // Update freq with elements in this block
        for (int i = start; i <= end; i++) {
            freq[a[i]] = mul(freq[a[i]], a[i]);
        }

        // Compute prod = SOS product over freq
        // Initialize prod = freq
        for (int i = 0; i < MAX_MASK; i++) prod[i] = freq[i];

        // SOS DP over subsets for product:
        // For each bit, for mask with bit set, prod[mask] *= prod[mask ^ (1 << bit)]
        for (int bit = 0; bit < MAXB; bit++) {
            for (int mask = 0; mask < MAX_MASK; mask++) {
                if (mask & (1 << bit)) {
                    prod[mask] = mul(prod[mask], prod[mask ^ (1 << bit)]);
                }
            }
        }

        // For each element in block, compute answer
        // ans = prod[a[i]] * product of elements in current block before i with (a[j] | a[i]) == a[i]
        // We can do this by iterating over previous elements in block

        // To speed up, we can precompute prefix products in block for each mask
        // But since BLOCK=1024, iterating over previous elements is acceptable

        for (int i = start; i <= end; i++) {
            int ans = prod[a[i]];
            for (int j = start; j < i; j++) {
                if ((a[j] | a[i]) == a[i]) {
                    ans = mul(ans, a[j]);
                }
            }
            cout << ans << "\n";
        }
    }

    return 0;
}