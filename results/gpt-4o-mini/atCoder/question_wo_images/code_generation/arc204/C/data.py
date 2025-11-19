def mex(x, y):
    return 3 - (x == 0) - (y == 0) - (x == 1) - (y == 1)

def max_score(N, P, queries):
    results = []
    for A0, A1, A2 in queries:
        score = 0
        for i in range(N):
            if A0 > 0 and A1 > 0:
                score += mex(0, 1)
                A0 -= 1
                A1 -= 1
            elif A1 > 0 and A2 > 0:
                score += mex(1, 2)
                A1 -= 1
                A2 -= 1
            elif A2 > 0 and A0 > 0:
                score += mex(2, 0)
                A2 -= 1
                A0 -= 1
            elif A0 > 0:
                score += mex(0, 0)
                A0 -= 1
            elif A1 > 0:
                score += mex(1, 1)
                A1 -= 1
            elif A2 > 0:
                score += mex(2, 2)
                A2 -= 1
        results.append(score)
    return results

import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
P = list(map(int, data[1:N+1]))
Q = int(data[N+1])
queries = []

for i in range(Q):
    A0, A1, A2 = map(int, data[N+2 + 3*i:N+5 + 3*i])
    queries.append((A0, A1, A2))

results = max_score(N, P, queries)
for result in results:
    print(result)