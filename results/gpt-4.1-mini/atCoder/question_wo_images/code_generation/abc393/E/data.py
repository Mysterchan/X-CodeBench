import sys
import math
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

MAX_A = 10**6

# freq[d] = number of elements divisible by d
freq = [0] * (MAX_A + 1)
for x in A:
    freq[x] += 1

# Count multiples for each d using a sieve-like approach
for d in range(MAX_A, 0, -1):
    s = 0
    for multiple in range(d * 2, MAX_A + 1, d):
        freq[d] += freq[multiple]

# For each element A[i], find the maximum gcd g such that freq[g] >= K and g divides A[i]
# We do this by checking divisors of A[i] in descending order and pick the first with freq[d] >= K

# Precompute divisors for each A[i] efficiently:
# Since max A[i] = 10^6, we can find divisors by checking up to sqrt(A[i])

res = [0] * N
for i in range(N):
    x = A[i]
    best = 1
    divisors = []
    limit = int(math.isqrt(x))
    for d in range(1, limit + 1):
        if x % d == 0:
            divisors.append(d)
            if d * d != x:
                divisors.append(x // d)
    # Check divisors in descending order
    divisors.sort(reverse=True)
    for d in divisors:
        if freq[d] >= K:
            best = d
            break
    res[i] = best

print('\n'.join(map(str, res)))