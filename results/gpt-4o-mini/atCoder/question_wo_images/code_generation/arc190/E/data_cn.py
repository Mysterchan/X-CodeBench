def max_operations(N, Q, A, queries):
    results = []
    for L, R in queries:
        B = A[L-1:R]
        total_operations = 0
        for i in range(len(B)):
            if B[i] > 0:
                if i > 0 and B[i-1] > 0:
                    pairs = min(B[i], B[i-1])
                    total_operations += pairs
                    B[i] -= pairs
                    B[i-1] -= pairs
                if i < len(B) - 1 and B[i+1] > 0:
                    pairs = min(B[i], B[i+1])
                    total_operations += pairs
                    B[i] -= pairs
                    B[i+1] -= pairs
        results.append(total_operations)
    return results

import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
Q = int(data[1])
A = list(map(int, data[2:N+2]))
queries = []
for i in range(Q):
    L = int(data[N+2 + 2*i])
    R = int(data[N+3 + 2*i])
    queries.append((L, R))

results = max_operations(N, Q, A, queries)
for result in results:
    print(result)