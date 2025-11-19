MOD = 998244353

def solve(N, M):
    result = 0
    
    # Case 1: All bits fixed (all elements same)
    # 2^M choices for the common value, 1 way to arrange
    result = pow(2, M, MOD)
    
    # Case 2: Exactly 1 bit varies
    # Choose which bit varies: M ways
    # Choose values for fixed bits: 2^(M-1) ways
    # Each element can independently be 0 or 1 in varying bit: 2^N ways
    result = (result + M * pow(2, M - 1, MOD) % MOD * pow(2, N, MOD) % MOD) % MOD
    
    # Case 3: Exactly 2 bits vary
    # Choose which 2 bits vary: C(M,2) ways
    # Choose values for fixed bits: 2^(M-2) ways
    # Each element picks from 4 combinations: 4^N ways
    if M >= 2:
        combinations = M * (M - 1) // 2 % MOD
        result = (result + combinations * pow(2, M - 2, MOD) % MOD * pow(4, N, MOD) % MOD) % MOD
    
    return result

T = int(input())
for _ in range(T):
    N, M = map(input().split())
    N, M = int(N), int(M)
    print(solve(N, M))