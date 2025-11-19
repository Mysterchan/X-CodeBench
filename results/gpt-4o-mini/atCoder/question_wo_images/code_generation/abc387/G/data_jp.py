def count_graphs(n):
    MOD = 998244353
    
    # counting how many primes are less than or equal to n
    def sieve_of_eratosthenes(n):
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for p in range(2, int(n**0.5) + 1):
            if is_prime[p]:
                for multiple in range(p * p, n + 1, p):
                    is_prime[multiple] = False
        return sum(is_prime)

    prime_count = sieve_of_eratosthenes(n)

    # The number of graphs is 2^(n-1) * prime_count
    graph_count = (pow(2, n - 1, MOD) * prime_count) % MOD
    
    return graph_count

n = int(input().strip())
print(count_graphs(n))