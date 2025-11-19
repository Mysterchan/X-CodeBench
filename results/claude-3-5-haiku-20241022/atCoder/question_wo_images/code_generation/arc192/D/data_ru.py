from math import gcd
from functools import reduce
from collections import defaultdict

MOD = 998244353

def factorize(n):
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    # Factorize all A_i
    A_factors = [factorize(a) for a in A]
    
    # Collect all primes
    primes = set()
    for factors in A_factors:
        primes.update(factors.keys())
    primes = sorted(primes)
    
    # For each prime, determine the constraints
    # For prime p, let e_i = exponent of p in S_i
    # If A_i = P_i * Q_i where gcd(P_i, Q_i) = 1
    # and S_i / S_{i+1} = P_i / Q_i
    # Then S_i * Q_i = S_{i+1} * P_i
    
    # For each prime p:
    # e_i + v_p(Q_i) = e_{i+1} + v_p(P_i)
    # where v_p(P_i * Q_i) = v_p(A_i)
    
    # We need to find all valid exponent sequences for each prime
    def get_valid_sequences(prime, A_factors, N):
        # For each i, we need to decide how A_i's prime factors split between P_i and Q_i
        # e_i - e_{i+1} = v_p(P_i) - v_p(Q_i)
        
        sequences = []
        
        def backtrack(idx, exponents):
            if idx == N:
                # Check if gcd constraint allows at least one sequence where min is 0
                if min(exponents) == 0:
                    sequences.append(tuple(exponents))
                return
            
            if idx == 0:
                # Try all possible starting exponents
                for e0 in range(1001):
                    backtrack(1, [e0])
            else:
                i = idx - 1  # index in A
                v_p_A = A_factors[i].get(prime, 0)
                
                # e_{i-1} - e_i = v_p(P_i) - v_p(Q_i)
                # v_p(P_i) + v_p(Q_i) = v_p_A
                # So v_p(P_i) - v_p(Q_i) can range from -v_p_A to v_p_A (odd parity same as v_p_A)
                
                e_prev = exponents[-1]
                for delta in range(-v_p_A, v_p_A + 1):
                    if (v_p_A - delta) % 2 == 0:  # delta and v_p_A must have same parity
                        e_curr = e_prev - delta
                        if e_curr >= 0:
                            backtrack(idx + 1, exponents + [e_curr])
        
        backtrack(0, [])
        
        # Filter to only keep sequences with min = 0
        valid = [seq for seq in sequences if min(seq) == 0]
        return valid
    
    # For each prime independently, get valid sequences
    prime_sequences = {}
    for p in primes:
        prime_sequences[p] = get_valid_sequences(p, A_factors, N)
    
    # Count combinations and compute sum
    total = 0
    
    # Use DP or enumerate all combinations
    def compute_sum(prime_idx, current_exponents):
        if prime_idx == len(primes):
            # Compute product of all S_i
            prod = 1
            for i in range(N):
                s_i = 1
                for j, p in enumerate(primes):
                    s_i = (s_i * pow(p, current_exponents[j][i], MOD)) % MOD
                prod = (prod * s_i) % MOD
            return prod
        
        p = primes[prime_idx]
        result = 0
        for seq in prime_sequences[p]:
            result = (result + compute_sum(prime_idx + 1, current_exponents + [seq])) % MOD
        return result
    
    total = compute_sum(0, [])
    print(total)

main()