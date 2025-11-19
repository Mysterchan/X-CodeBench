def max_operations(N, Q, A, queries):
    results = []
    for L, R in queries:
        B = A[L-1:R]
        total = sum(B)
        max_count = total // 2
        results.append(max_count)
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