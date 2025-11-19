from math import gcd
from functools import reduce

N = int(input())
A = list(map(int, input().split()))
mod = 998244353

def prime_factors(n):
    factors = []
    is_prime = [True] * (n + 1)
    for i in range(2, n + 1):
        if is_prime[i]:
            factors.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return factors

primes = prime_factors(1000)

def count_good_sequences(primes, A):
    m = len(A)
    total_score = 1
    for prime in primes:
        dp = [[0] * (10 * N + 1) for _ in range(m + 1)]
        dp[0][0] = 1
        
        h = [pow(prime, i, mod) for i in range(10 * N + 1)]
        
        for i in range(m):
            y = A[i]
            c = 0
            
            while y % prime == 0:
                c += 1
                y //= prime
            
            for j in range(10 * N + 1):
                if dp[i][j] == 0:
                    continue
                
                dp[i + 1][j + c] = (dp[i + 1][j + c] + dp[i][j] * h[j + c]) % mod
                
                if c > 0:
                    if j >= c:
                        dp[i + 1][j - c] = (dp[i + 1][j - c] + dp[i][j] * h[j - c]) % mod
                    else:
                        z = c - j
                        dp[i + 1][0] = (dp[i + 1][0] + dp[i][j] * h[z * (i + 1)]) % mod

        total_score = (total_score * sum(dp[m]) % mod) % mod

    return total_score

result = count_good_sequences(primes, A)
print(result)