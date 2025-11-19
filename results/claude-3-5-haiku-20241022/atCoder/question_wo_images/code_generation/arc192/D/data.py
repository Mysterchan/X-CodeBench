from math import gcd
from functools import reduce

def factorize(n):
    """Returns list of (P, Q) pairs where P*Q = n and gcd(P,Q) = 1"""
    factors = []
    for p in range(1, int(n**0.5) + 1):
        if n % p == 0:
            q = n // p
            if gcd(p, q) == 1:
                factors.append((p, q))
                if p != q:
                    factors.append((q, p))
    return factors

def solve():
    MOD = 998244353
    n = int(input())
    a = list(map(int, input().split()))
    
    # For each position, store possible coprime factorizations
    factorizations = [factorize(ai) for ai in a]
    
    # DP: dp[i][v] = sum of products of sequences ending at position i with value v
    # We also track the gcd separately
    dp = {}
    dp[0] = {1: 1}  # Start with S_1 = 1
    
    for i in range(n - 1):
        new_dp = {}
        for (p, q) in factorizations[i]:
            # If S_i = v*p, then S_{i+1} = v*q
            for v, count in dp[i].items():
                s_i = v * p
                s_next = v * q
                
                if s_next not in new_dp:
                    new_dp[s_next] = 0
                new_dp[s_next] = (new_dp[s_next] + count * s_i) % MOD
        
        dp[i + 1] = new_dp
    
    # Sum all final values, but need to handle gcd constraint
    # We need to enumerate actual sequences and check gcd
    
    # Better approach: use different DP tracking the actual sequence values
    # dp[i] = list of (sequence_so_far, product_so_far)
    
    sequences = [[1]]  # Start with S_1 = 1
    
    for i in range(n - 1):
        new_sequences = []
        for seq in sequences:
            v = seq[-1]
            for (p, q) in factorizations[i]:
                # Try s_i = v*p*k, s_{i+1} = v*q*k for any k
                # But this creates infinite possibilities
                # The key: we can factor out gcd at the end
                # So just use k=1
                new_seq = seq + [v * q]
                new_seq[i] = v * p
                new_sequences.append(new_seq)
        sequences = new_sequences
    
    # This approach explodes in size. Need smarter DP.
    
    # Track (current_value, gcd_so_far, product_so_far)
    dp = {(1, 0): 1}  # (value, gcd): count*product
    
    for i in range(n - 1):
        new_dp = {}
        for (v, g), prod in dp.items():
            for (p, q) in factorizations[i]:
                s_i = v * p
                s_next = v * q
                new_g = gcd(g, s_i) if g > 0 else s_i
                
                key = (s_next, new_g)
                if key not in new_dp:
                    new_dp[key] = 0
                new_dp[key] = (new_dp[key] + prod * s_i) % MOD
        dp = new_dp
    
    result = 0
    for (v, g), prod in dp.items():
        if gcd(g, v) == 1:
            result = (result + prod * v) % MOD
    
    print(result)

solve()