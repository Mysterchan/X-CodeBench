def mod_prime_graph_count(n):
    MOD = 998244353

    # Helper function to calculate prime numbers up to n using sieve of Eratosthenes
    def sieve(n):
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if (is_prime[p] == True):
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    # Count the number of prime numbers up to 2N
    primes = sieve(2 * n)
    prime_count = len(primes)

    # Calculate the total number of connected graphs with prime cycle lengths
    answer = 0
    for k in range(1, n + 1):
        answer += pow(prime_count, k, MOD) * pow(2, n - k, MOD)
        answer %= MOD

    return answer

# Input reading
n = int(input().strip())
print(mod_prime_graph_count(n))