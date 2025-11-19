import sys
input = sys.stdin.readline

N = int(input())
C = [input().strip() for _ in range(N)]

from collections import deque

inf = 10**10
A = [[inf]*N for _ in range(N)]
q = deque()

# Initialize distances for pairs (i,i) = 0 (empty path)
for i in range(N):
    A[i][i] = 0
    q.append((i, i))

# Initialize distances for edges of length 1 (single edge palindrome)
for i in range(N):
    for j in range(N):
        if C[i][j] != '-':
            A[i][j] = 1
            q.append((i, j))

while q:
    i, j = q.popleft()
    dist = A[i][j]
    # Try to extend palindrome by adding matching edges on both sides
    # For all s with edge s->i labeled cs
    # and all t with edge j->t labeled ct, if cs == ct, update A[s][t]
    for s in range(N):
        cs = C[s][i]
        if cs == '-':
            continue
        for t in range(N):
            ct = C[j][t]
            if ct == '-' or cs != ct:
                continue
            nd = dist + 2
            if nd < A[s][t]:
                A[s][t] = nd
                q.append((s, t))

for i in range(N):
    for j in range(N):
        if A[i][j] == inf:
            A[i][j] = -1
    print(*A[i])