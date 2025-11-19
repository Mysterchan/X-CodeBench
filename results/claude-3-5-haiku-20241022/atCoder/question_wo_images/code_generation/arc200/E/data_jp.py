MOD = 998244353

def modinv(a, m=MOD):
    return pow(a, m - 2, m)

def solve(N, M):
    # popcount(A_i XOR A_j) <= 2 means A_i and A_j differ in at most 2 bit positions
    
    # Key insight: We need to count sequences where any two elements differ in at most 2 bits
    # This means we need to find the size of maximum independent set in a graph where
    # vertices are M-bit numbers and edges connect numbers differing in more than 2 bits
    
    # Better approach: Use inclusion-exclusion or dynamic programming
    # For small differences, we can think of it as selecting numbers from equivalence classes
    
    # Let's think differently: Fix the first element, then count valid extensions
    # Actually, we can use the fact that the constraint is very restrictive
    
    # For N=2: count pairs (a,b) where popcount(a XOR b) <= 2
    # This is 2^M choices for a, and for each a, count b's with hamming distance <= 2
    # Distance 0: 1 (same as a)
    # Distance 1: M choices
    # Distance 2: M*(M-1)/2 choices
    # Total per a: 1 + M + M*(M-1)/2
    
    if N == 2:
        per_element = 1 + M + M * (M - 1) // 2
        result = pow(2, M, MOD) * per_element % MOD
        return result
    
    # For general N, use matrix exponentiation or DP
    # State: which "pattern" of bits are fixed
    
    # Alternative: Enumerate all possible "types" where elements can differ
    # If all elements must be within hamming distance 2 from each other,
    # we need to find cliques in the graph
    
    # Key observation: If popcount(a XOR b) <= 2 and popcount(b XOR c) <= 2,
    # then popcount(a XOR c) <= 4 (triangle inequality doesn't directly apply)
    
    # Use DP: dp[mask] = number of ways to assign values to elements seen so far
    # But this is too complex for large N
    
    # Better: For each possible "center" configuration and radius:
    # Count sequences where all elements are within distance 2 from some reference
    
    # Ultimate approach: 
    # Fix a reference value r. Count sequences where all A_i satisfy popcount(A_i XOR r) <= 2
    # But elements also need to satisfy constraints pairwise
    
    # Key: If all A_i are within distance 2 from reference r, are they pairwise distance <= 2?
    # No! Example: r=000, a=110, b=011, then popcount(a XOR b) = popcount(101) = 2 (OK)
    # But r=000, a=100, b=010, popcount(a XOR b) = popcount(110) = 2 (OK)
    
    # Strategy: For each subset S of at most 2 bit positions that can vary,
    # all elements must come from the 2^|S| possibilities by varying those bits
    # Count: C(M, 0) * 2^0 + C(M, 1) * 2^1 + C(M, 2) * 2^2 choices per "class"
    # Then (choice)^N for N elements, times 2^M for the base value
    
    total = 0
    
    # For each choice of which bits can vary (0, 1, or 2 bits)
    for k in range(min(3, M + 1)):
        if k == 0:
            num_patterns = 1
        elif k == 1:
            num_patterns = M
        else:  # k == 2
            num_patterns = M * (M - 1) // 2
        
        choices_per_pattern = pow(2, k)
        contribution = num_patterns * pow(choices_per_pattern, N, MOD) % MOD
        total = (total + contribution) % MOD
    
    return total

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(solve(N, M))