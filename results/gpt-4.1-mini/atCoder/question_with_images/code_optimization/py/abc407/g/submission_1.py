import sys
input=sys.stdin.readline

H,W=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(H)]

# Sum of all cells
total = sum(sum(row) for row in A)

# We want to place dominoes to cover cells with negative sum pairs to maximize uncovered sum.
# Each domino covers two adjacent cells (horizontal or vertical).
# Placing a domino removes the sum of those two cells from the uncovered sum.
# So placing dominoes on pairs with negative sum increases the uncovered sum.

# We model the grid as a bipartite graph:
# Color cells by parity of (i+j).
# Edges between black and white cells if adjacent.
# Edge weight = sum of the two cells.
# We want to find maximum weight matching with edges having negative weight (sum < 0),
# because placing dominoes on negative sum pairs increases the uncovered sum.

# Since HW <= 2000, we can implement a maximum matching on a bipartite graph with weights.
# But maximum weighted matching is O(N^3), too slow.
# However, since edge weights are sum of two cells, and we only want to pick edges with negative sum,
# we can greedily pick edges with negative sum and no conflicts.

# Approach:
# 1. Build list of edges with negative sum.
# 2. Sort edges by sum ascending (most negative first).
# 3. Greedily pick edges if both endpoints are unmatched.

# This greedy approach works because:
# - Each cell can be matched at most once.
# - We pick edges with most negative sum first to maximize gain.
# - No cycles or complex structures needed.

# Implementation:

matched = [False]*(H*W)

edges = []
for i in range(H):
    for j in range(W):
        c = i*W + j
        if (i+j)%2==0:
            # black cell, check right and down neighbors
            if j+1 < W:
                s = A[i][j] + A[i][j+1]
                if s < 0:
                    edges.append((s, c, i*W + (j+1)))
            if i+1 < H:
                s = A[i][j] + A[i+1][j]
                if s < 0:
                    edges.append((s, c, (i+1)*W + j))

edges.sort()  # ascending by sum (most negative first)

res = total
for s, u, v in edges:
    if not matched[u] and not matched[v]:
        matched[u] = True
        matched[v] = True
        res -= s  # subtract negative sum => add abs(sum)

print(res)