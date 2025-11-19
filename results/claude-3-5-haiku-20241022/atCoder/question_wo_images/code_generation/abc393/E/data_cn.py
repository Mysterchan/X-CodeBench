from math import gcd
from collections import defaultdict

def get_divisors(n):
    divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
        i += 1
    return sorted(divisors, reverse=True)

N, K = map(int, input().split())
A = list(map(int, input().split()))

# Count elements divisible by each divisor
MAX_VAL = max(A)
count = [0] * (MAX_VAL + 1)

for a in A:
    i = 1
    while i * i <= a:
        if a % i == 0:
            count[i] += 1
            if i != a // i:
                count[a // i] += 1
        i += 1

results = []
for i in range(N):
    a_i = A[i]
    divisors = get_divisors(a_i)
    
    for d in divisors:
        # Count how many elements are divisible by d (excluding a_i itself)
        total = count[d]
        # We need at least K elements divisible by d including a_i
        if total >= K:
            results.append(d)
            break

for r in results:
    print(r)