from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
C = [input().strip() for _ in range(N)]

# dist[i][j] = minimal length of palindrome path from i to j
# i, j are 0-based indices
dist = [[-1]*N for _ in range(N)]

# BFS queue for pairs (i,j)
q = deque()

# Initialize:
# 1) dist[i][i] = 0 (empty path, empty string is palindrome)
for i in range(N):
    dist[i][i] = 0
    q.append((i,i))

# 2) For edges i->j with label c, if there is also edge j->i with same label c,
# then path i->j (length 1) and j->i (length 1) can form palindrome of length 2 (c + c)
# Actually, for pairs (i,j) where i!=j, if C[i][j] == C[j][i] != '-', then dist[i][j] = 2
# But we will handle this in BFS expansion.

# We will do BFS on pairs (i,j) representing the "front" and "back" pointers of the palindrome path.
# The idea:
# - dist[i][j] = minimal length of palindrome path from i to j
# - We start from dist[i][i] = 0 (empty path)
# - For each edge i->k with label c and edge j->l with label c, if dist[k][l] is not set,
#   then dist[k][l] = dist[i][j] + 2, and enqueue (k,l)
# - Also, if there is an edge i->j with label c, then dist[i][j] = 1 (single edge palindrome)
#   if not set yet.

# First, set dist[i][j] = 1 for edges i->j with label c (single edge palindrome)
for i in range(N):
    for j in range(N):
        if C[i][j] != '-':
            if dist[i][j] == -1 or dist[i][j] > 1:
                dist[i][j] = 1
                q.append((i,j))

# BFS
while q:
    i,j = q.popleft()
    d = dist[i][j]
    # If d is even, then we can try to expand from both ends by edges with same label
    # If d is odd, same logic applies (no difference)
    # For all edges i->k with label c
    # and edges j->l with label c
    # if dist[k][l] not set, set dist[k][l] = d + 2
    for c in range(26):
        ch = chr(ord('a') + c)
        # find all k with edge i->k labeled ch
        # find all l with edge j->l labeled ch
        # For efficiency, precompute adjacency by label
        # But N=100, so nested loops are acceptable here
        for k in range(N):
            if C[i][k] == ch:
                for l in range(N):
                    if C[j][l] == ch:
                        if dist[k][l] == -1:
                            dist[k][l] = d + 2
                            q.append((k,l))

# Output
for i in range(N):
    print(' '.join(str(dist[i][j]) for j in range(N)))