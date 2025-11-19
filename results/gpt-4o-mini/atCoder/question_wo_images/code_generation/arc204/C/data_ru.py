def mex(x, y):
    return 0 if x != 0 and y != 0 else 1 if x != 1 and y != 1 else 2

def max_score(N, P, queries):
    results = []
    for A0, A1, A2 in queries:
        score = 0
        # Count the number of 0s, 1s, and 2s in the good sequence
        if A0 > 0:
            score += sum(mex(0, P[i]) for i in range(A0))
        if A1 > 0:
            score += sum(mex(1, P[i]) for i in range(A0, A0 + A1))
        if A2 > 0:
            score += sum(mex(2, P[i]) for i in range(A0 + A1, N))
        results.append(score)
    return results

import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
P = list(map(int, data[1:N+1]))
Q = int(data[N+1])
queries = [tuple(map(int, data[N+2+i*3:N+2+i*3+3])) for i in range(Q)]

results = max_score(N, P, queries)
print('\n'.join(map(str, results)))