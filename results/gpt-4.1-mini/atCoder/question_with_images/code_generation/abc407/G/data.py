import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

# We model the problem as a maximum weight matching in a bipartite graph:
# - Each cell is a vertex.
# - Edges connect adjacent cells (right and down neighbors).
# - Edge weight = sum of the two cells' values.
# We want to find a matching that maximizes the sum of matched edges.
# The final answer = sum of all cells - sum of matched edges (because matched cells are covered by dominoes and excluded from score).

# The grid is bipartite if we color cells by (i+j) parity.
# We'll build a bipartite graph with edges only from black to white cells.

# Since HW <= 2000, we can implement a Hungarian algorithm for maximum weight matching in O(N^3) where N ~ 2000 is feasible.

# Step 1: Assign IDs to black and white cells
black_id = {}
white_id = {}
black_count = 0
white_count = 0

for i in range(H):
    for j in range(W):
        if (i + j) % 2 == 0:
            black_id[(i, j)] = black_count
            black_count += 1
        else:
            white_id[(i, j)] = white_count
            white_count += 1

# Step 2: Build graph edges from black to white with weights
# Edges only between adjacent cells (right and down)
# We'll store edges in adjacency list for black vertices:
# graph[u] = list of (v, weight)
graph = [[] for _ in range(black_count)]

for i in range(H):
    for j in range(W):
        if (i + j) % 2 == 0:
            u = black_id[(i, j)]
            # right neighbor
            if j + 1 < W:
                if (i + (j + 1)) % 2 == 1:
                    v = white_id[(i, j + 1)]
                    w = A[i][j] + A[i][j + 1]
                    graph[u].append((v, w))
            # down neighbor
            if i + 1 < H:
                if ((i + 1) + j) % 2 == 1:
                    v = white_id[(i + 1, j)]
                    w = A[i][j] + A[i + 1][j]
                    graph[u].append((v, w))

# Hungarian algorithm for maximum weight bipartite matching
# Reference implementation adapted for this problem

INF = 10**15

def hungarian():
    # n = number of black vertices
    # m = number of white vertices
    n = black_count
    m = white_count
    u = [0] * (n + 1)  # potential for left
    v = [0] * (m + 1)  # potential for right
    p = [0] * (m + 1)  # matched left vertex for right vertex j
    way = [0] * (m + 1)

    for i in range(1, n + 1):
        p[0] = i
        j0 = 0
        minv = [INF] * (m + 1)
        used = [False] * (m + 1)
        while True:
            used[j0] = True
            i0 = p[j0]
            delta = INF
            j1 = -1
            for j in range(1, m + 1):
                if not used[j]:
                    # find weight of edge i0-1 to j-1
                    # graph is 0-based, i0 and j are 1-based
                    # find weight w for edge (i0-1, j-1)
                    # If no edge, weight = -INF (or very negative)
                    w = -INF
                    for (to, weight) in graph[i0 - 1]:
                        if to == j - 1:
                            w = weight
                            break
                    cur = u[i0] + v[j] - w
                    if cur < minv[j]:
                        minv[j] = cur
                        way[j] = j0
                    if minv[j] < delta:
                        delta = minv[j]
                        j1 = j
            for j in range(m + 1):
                if used[j]:
                    u[p[j]] -= delta
                    v[j] += delta
                else:
                    minv[j] -= delta
            j0 = j1
            if p[j0] == 0:
                break
        # augmenting path
        while True:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1
            if j0 == 0:
                break

    # p[j] = matched left vertex for right vertex j
    # p[0] is dummy
    # Calculate max weight sum
    match = [-1] * n  # match[i] = matched white vertex for black i
    for j in range(1, m + 1):
        if p[j] != 0:
            match[p[j] - 1] = j - 1

    max_weight = 0
    for i in range(n):
        if match[i] != -1:
            # find weight of edge (i, match[i])
            w = 0
            for (to, weight) in graph[i]:
                if to == match[i]:
                    w = weight
                    break
            max_weight += w
    return max_weight

total_sum = 0
for row in A:
    total_sum += sum(row)

max_matched_sum = hungarian()
answer = total_sum - max_matched_sum
print(answer)