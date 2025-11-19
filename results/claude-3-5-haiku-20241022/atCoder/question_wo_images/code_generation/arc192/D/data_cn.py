from math import gcd
from functools import reduce

def prime_factorize(n):
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

def solve():
    MOD = 998244353
    N = int(input())
    A = list(map(int, input().split()))
    
    # Factorize all A[i]
    A_factors = []
    for a in A:
        A_factors.append(prime_factorize(a))
    
    # For each prime, track the exponent changes
    all_primes = set()
    for factors in A_factors:
        all_primes.update(factors.keys())
    all_primes = sorted(all_primes)
    
    # Build the constraint matrix
    # For each prime p, we have constraints on the exponents
    prime_to_idx = {p: i for i, p in enumerate(all_primes)}
    
    # Generate all valid exponent sequences
    def generate_sequences(idx, current_exp):
        if idx == N:
            # Check if gcd = 1 (at least one exponent is 0)
            if any(current_exp[p] == 0 for p in all_primes):
                yield current_exp.copy()
            return
        
        if idx == 0:
            # First position can be anything non-negative
            for exp_set in generate_first(current_exp):
                yield from generate_sequences(1, exp_set)
        else:
            # Based on A[idx-1], determine valid next exponents
            for exp_set in generate_next(idx - 1, current_exp):
                yield from generate_sequences(idx, exp_set)
    
    def generate_first(exp_dict):
        # Start with all zeros
        yield {p: 0 for p in all_primes}
    
    def generate_next(pos, prev_exp):
        # Given S[pos] exponents, find S[pos+1] exponents
        # f(S[pos]/S[pos+1]) = A[pos]
        # Need to enumerate all valid combinations
        
        # This is too complex, let's use a different approach
        pass
    
    # Different approach: enumerate all possible S sequences directly
    # Use dynamic programming with memoization
    
    from collections import defaultdict
    
    # State: (position, exponent_tuple for each prime)
    # Too large state space
    
    # Better approach: for small constraints, enumerate divisors
    
    # Generate all valid sequences by backtracking
    def backtrack(pos, current_seq):
        if pos == N:
            # Check gcd = 1
            g = reduce(gcd, current_seq)
            if g == 1:
                # Calculate score
                prod = 1
                for s in current_seq:
                    prod = (prod * s) % MOD
                return prod
            return 0
        
        total = 0
        if pos == 0:
            # Try different values for S[0]
            # Limit search space based on A values
            max_val = 10000  # Adjust based on constraints
            for s0 in range(1, min(max_val + 1, 100)):
                total = (total + backtrack(1, [s0])) % MOD
        else:
            # S[pos] must satisfy f(S[pos-1]/S[pos]) = A[pos-1]
            s_prev = current_seq[-1]
            a = A[pos - 1]
            
            # Find all s such that f(s_prev/s) = a
            # s_prev/s in lowest terms is p/q with p*q = a
            # So s_prev = p * k, s = q * k for some k, gcd(p,q)=1, p*q=a
            
            for p in range(1, a + 1):
                if a % p == 0:
                    q = a // p
                    if gcd(p, q) == 1:
                        if s_prev % p == 0:
                            k = s_prev // p
                            s = q * k
                            total = (total + backtrack(pos + 1, current_seq + [s])) % MOD
        
        return total
    
    result = backtrack(0, [])
    print(result)

solve()