N = int(input())
C = [input() for _ in range(N)]

from collections import deque
q = deque()
inf = 10**10
A = [[inf]*N for _ in range(N)]
for i in range(N):
    q.append([0, i, i])
    A[i][i] = 0
for i in range(N):
    for j in range(N):
        if i == j or C[i][j] == '-':
            continue
        q.append([1, i, j])
        A[i][j] = 1

kakutei = set()
while q:
    n, i, j = q.popleft()
    if (i, j) in kakutei:
        continue
    kakutei.add((i, j))
    for s in range(N):
        cs = C[s][i]
        if cs == '-':
            continue
        for t in range(N):
            ct = C[j][t]
            if ct == '-' or cs != ct or (s, t) in kakutei or n+2 >= A[s][t]:
                continue
            A[s][t] = n+2
            q.append([n+2, s, t])
for i in range(N):
    for j in range(N):
        if A[i][j] == inf:
            A[i][j] = -1
    print(*A[i])