from math import gcd
from functools import reduce
from collections import defaultdict

def prime_factorize(n):
    factors = defaultdict(int)
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] += 1
            n //= d
        d += 1
    if n > 1:
        factors[n] += 1
    return factors

def factorize_A(A):
    N = len(A) + 1
    factor_lists = []
    all_primes = set()
    
    for a in A:
        factors = prime_factorize(a)
        factor_lists.append(factors)
        all_primes.update(factors.keys())
    
    return factor_lists, sorted(all_primes)

def solve():
    MOD = 998244353
    
    N = int(input())
    A = list(map(int, input().split()))
    
    factor_lists, primes = factorize_A(A)
    
    # For each prime p, we need to find valid exponent sequences
    # e[0], e[1], ..., e[N-1] such that:
    # |e[i] - e[i+1]| = factor_lists[i][p] for all i
    # gcd constraint: at least one e[i] must be 0
    
    def count_sequences_for_prime(p):
        exponents = [factors.get(p, 0) for factors in factor_lists]
        
        # DP to count sequences
        # State: (position, current_exponent, has_zero)
        # We'll use a different approach: enumerate all possible sequences
        
        # Constraints: e[i+1] = e[i] ± exponents[i]
        # Start from position 0, try all possible starting values
        
        # Find range of possible exponents
        max_exp = sum(exponents) + 10
        
        dp = defaultdict(lambda: defaultdict(int))
        dp[0][0] = 1  # Start at position 0 with exponent 0
        
        # Also try starting with non-zero
        for start in range(1, max_exp):
            dp[0][start] = 1
        
        for i in range(N - 1):
            new_dp = defaultdict(lambda: defaultdict(int))
            exp_diff = exponents[i]
            
            for e in dp[i]:
                for has_zero in dp[i][e]:
                    count = dp[i][e][has_zero]
                    if count == 0:
                        continue
                    
                    # Two choices for next exponent
                    for next_e in [e + exp_diff, e - exp_diff]:
                        if next_e >= 0:
                            new_has_zero = has_zero or (next_e == 0)
                            new_dp[next_e][new_has_zero] = (new_dp[next_e][new_has_zero] + count) % MOD
            
            dp = new_dp
        
        # Count sequences with at least one zero
        total = 0
        for e in dp[N - 1]:
            if 1 in dp[N - 1][e]:  # has_zero = True
                total = (total + dp[N - 1][e][1]) % MOD
        
        return total
    
    # For each prime, count valid sequences
    counts = {}
    for p in primes:
        counts[p] = count_sequences_for_prime(p)
    
    # Product of all counts
    result = 1
    for p in primes:
        result = (result * counts[p]) % MOD
    
    # Multiply by product of A_i values (contribution from the constraint)
    prod_A = 1
    for a in A:
        prod_A = (prod_A * a) % MOD
    
    result = (result * prod_A) % MOD
    
    print(result)

solve()