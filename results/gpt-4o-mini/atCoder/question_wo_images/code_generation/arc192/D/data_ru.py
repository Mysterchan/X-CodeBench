def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * (b // gcd(a, b))

def f(x):
    from math import gcd
    p, q = x
    return p * q

def find_good_sequences(N, A):
    MOD = 998244353
    from collections import defaultdict
    from math import gcd
    from functools import reduce

    # Step 1: Calculate the required pairs (P, Q) for each A_i
    pairs = []
    for a in A:
        for p in range(1, a + 1):
            if a % p == 0:
                q = a // p
                if gcd(p, q) == 1:
                    pairs.append((p, q))

    # Step 2: Build the graph of possible transitions
    graph = defaultdict(list)
    for i in range(len(A)):
        for p1, q1 in pairs:
            for p2, q2 in pairs:
                if f((p1, q1)) == A[i] and f((p2, q2)) == A[i]:
                    graph[(p1, q1)].append((p2, q2))

    # Step 3: Count valid sequences
    total_sum = 0
    for start in pairs:
        stack = [(start, [start])]
        while stack:
            current, sequence = stack.pop()
            if len(sequence) == N:
                if reduce(gcd, (s[0] for s in sequence)) == 1:
                    product = reduce(lambda x, y: x * y % MOD, (s[0] for s in sequence), 1)
                    total_sum = (total_sum + product) % MOD
                continue
            for next_pair in graph[current]:
                stack.append((next_pair, sequence + [next_pair]))

    return total_sum

# Input reading
N = int(input().strip())
A = list(map(int, input().strip().split()))

# Output the result
print(find_good_sequences(N, A))