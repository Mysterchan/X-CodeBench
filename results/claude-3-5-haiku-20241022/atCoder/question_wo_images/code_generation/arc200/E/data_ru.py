MOD = 998244353

def solve(N, M):
    # Precompute factorials and inverse factorials
    max_val = M + 5
    fact = [1] * max_val
    for i in range(1, max_val):
        fact[i] = fact[i-1] * i % MOD
    
    inv_fact = [1] * max_val
    inv_fact[max_val-1] = pow(fact[max_val-1], MOD-2, MOD)
    for i in range(max_val-2, -1, -1):
        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
    
    def comb(n, k):
        if k < 0 or k > n:
            return 0
        return fact[n] * inv_fact[k] % MOD * inv_fact[n-k] % MOD
    
    # Dynamic programming approach
    # dp[k] = number of valid sequences where we've fixed k bits
    # For each bit position, we can choose:
    # - All values have 0 at this position
    # - All values have 1 at this position
    # - Some values have 0, some have 1 (but constrained by popcount condition)
    
    # Key insight: If we fix some bits, the XOR between any two numbers
    # can have at most 2 ones in popcount.
    
    # For each bit position independently:
    # - If all values have same bit: contributes 0 to XOR popcount
    # - If values differ: contributes 1 to XOR popcount
    
    # We can have at most 2 bit positions where values differ
    
    result = 0
    
    # Case 0: All values are the same (0 differing bits)
    # We have 2^M choices for the common value
    result = pow(2, M, MOD)
    
    # Case 1: Values differ in exactly 1 bit position (1 differing bit)
    # Choose which bit position: M ways
    # Choose the common value for other M-1 bits: 2^(M-1) ways
    # At the differing bit, we can partition N values into two groups (both non-empty)
    # Number of ways: 2^N - 2 (exclude all 0s and all 1s)
    if M >= 1:
        result += M * pow(2, M-1, MOD) % MOD * (pow(2, N, MOD) - 2) % MOD
        result %= MOD
    
    # Case 2: Values differ in exactly 2 bit positions (2 differing bits)
    # Choose which 2 bit positions: C(M, 2) ways
    # Choose the common value for other M-2 bits: 2^(M-2) ways
    # At the 2 differing bits, we need to ensure popcount(XOR) <= 2
    # This means for any two values, they differ in at most 2 positions
    # For 2 bit positions, each value has one of 4 patterns: 00, 01, 10, 11
    # We need all pairwise XORs to have popcount <= 2
    # Valid configurations: all same, or partition into groups differing in 1 bit
    
    if M >= 2:
        ways_2bits = 0
        # All values same in both bits: 4 ways (but already counted in case 0)
        # Values differ in exactly 1 of the 2 bits:
        # - Fix bit 1, vary bit 2: 2 * (2^N - 2) = 2 * (2^N - 2)
        # - Fix bit 2, vary bit 1: 2 * (2^N - 2) = 2 * (2^N - 2)
        # Total: 4 * (2^N - 2)
        ways_2bits = 4 * (pow(2, N, MOD) - 2) % MOD
        
        result += comb(M, 2) * pow(2, M-2, MOD) % MOD * ways_2bits % MOD
        result %= MOD
    
    return result

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(solve(N, M))