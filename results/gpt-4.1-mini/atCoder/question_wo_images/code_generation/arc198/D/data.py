import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
edges = [[] for _ in range(N)]
for _ in range(N-1):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    edges[u].append(v)
    edges[v].append(u)

A = [list(map(int,list(input().strip()))) for _ in range(N)]

# The problem:
# We want to assign integers x_i to vertices i to minimize the score.
# Score:
# - If there exists (i,j) with A[i][j] = 1 and path(i,j) is NOT palindrome in x, score = 10^100 (huge)
# - Otherwise, score = number of palindromic pairs (i,j)
#
# Goal: minimize score over all x.
#
# Observations:
# 1) If any (i,j) with A[i][j]=1 is not palindrome, huge penalty.
# 2) So for all (i,j) with A[i][j]=1, path(i,j) must be palindrome.
#
# The path palindrome condition means:
# For the path v_1,...,v_n from i to j,
# x[v_k] = x[v_{n+1-k}] for all k.
#
# This implies a set of equality constraints on x:
# For each (i,j) with A[i][j]=1, and path p = v_1,...,v_n,
# x[v_k] = x[v_{n+1-k}] for k=1..n
#
# So for each such pair, we get equalities between pairs of vertices.
#
# We want to find an assignment x that satisfies all these equalities.
# If impossible, score = 10^100.
#
# If possible, then score = number of palindromic pairs (i,j).
#
# Note that (i,i) is always palindrome (path length 1).
#
# Also, if (i,j) is palindrome, then (j,i) is palindrome.
#
# The problem reduces to:
# - Build an undirected graph of equality constraints between vertices induced by all pairs (i,j) with A[i][j]=1.
# - Each equality constraint is between two vertices that must have the same x value.
#
# So the vertices are partitioned into connected components by these equality constraints.
# Each component must have the same x value assigned.
#
# Now, the score counts the number of palindromic pairs (i,j).
# A pair (i,j) is palindrome if for the path from i to j, the sequence x on the path is palindrome.
#
# But since x is constant on each connected component of the equality graph,
# the path palindrome condition means:
# For the path v_1,...,v_n,
# x[v_k] = x[v_{n+1-k}] for all k.
#
# Since x is constant on connected components, this means:
# For each k, v_k and v_{n+1-k} must be in the same connected component.
#
# So the path palindrome condition for (i,j) is:
# For all k, v_k and v_{n+1-k} are in the same equality component.
#
# So the palindromic pairs are those (i,j) where the path from i to j is "component-palindromic":
# The path's vertices are symmetric w.r.t. connected components.
#
# We want to minimize the score = number of palindromic pairs.
#
# But the problem states: if any (i,j) with A[i][j]=1 is not palindrome, score=10^100.
# So the equality graph must include all constraints from A[i][j]=1 pairs.
#
# So the equality graph is fixed by the input.
#
# Now, the score is the number of pairs (i,j) such that the path from i to j is component-palindromic.
#
# We want to find the minimal score over all x.
#
# But the equality graph fixes the partition of vertices into components.
# The assignment x must be constant on each component.
#
# So the minimal score is the number of pairs (i,j) whose path is component-palindromic.
#
# So the problem reduces to:
# 1) Build equality graph from all pairs (i,j) with A[i][j]=1:
#    For each such pair, for the path from i to j, add edges between v_k and v_{n+1-k}.
# 2) Find connected components of equality graph.
# 3) For each pair (i,j), check if path(i,j) is component-palindromic:
#    For all k, v_k and v_{n+1-k} in same component.
# 4) Count how many pairs (i,j) satisfy this.
#
# If any (i,j) with A[i][j]=1 is not component-palindromic, output 10^100.
# Else output the count.
#
# Implementation details:
# - N up to 3000, O(N^2) is borderline but possible with efficient code.
# - We need to find path between i and j quickly.
# - Since T is a tree, we can preprocess LCA and parent arrays.
# - Then path from i to j can be decomposed into i->LCA and j->LCA.
#
# To get the path vertices in order:
# path(i,j) = i->LCA path + reversed(j->LCA path without LCA)
#
# We can store parent and depth arrays.
#
# For each pair (i,j) with A[i][j]=1:
# - get path vertices
# - for k in 1..len(path), add equality edges between v_k and v_{n+1-k}
#
# Then find connected components of equality graph.
#
# Then for all pairs (i,j), check if path(i,j) is component-palindromic:
# - For k in 1..len(path), check if v_k and v_{n+1-k} in same component.
#
# Count how many pairs satisfy this.
#
# Output 10^100 if any (i,j) with A[i][j]=1 fails.
#
# Optimization:
# - We only need to check pairs (i,j) with A[i][j]=1 for the huge penalty.
# - For counting palindromic pairs, we check all pairs.
#
# To speed up:
# - Precompute connected component id for each vertex.
# - For path palindrome check, just check component ids.
#
# Let's implement.

# Step 1: Preprocessing for LCA
LOG = 15  # since N <= 3000, 2^15=32768 > 3000
parent = [[-1]*N for _ in range(LOG)]
depth = [0]*N

def dfs(v,p,d):
    depth[v] = d
    parent[0][v] = p
    for nv in edges[v]:
        if nv == p:
            continue
        dfs(nv,v,d+1)

dfs(0,-1,0)

for k in range(LOG-1):
    for v in range(N):
        if parent[k][v] < 0:
            parent[k+1][v] = -1
        else:
            parent[k+1][v] = parent[k][parent[k][v]]

def lca(u,v):
    if depth[u] > depth[v]:
        u,v = v,u
    # depth[u] <= depth[v]
    diff = depth[v] - depth[u]
    for k in range(LOG):
        if diff & (1 << k):
            v = parent[k][v]
    if u == v:
        return u
    for k in reversed(range(LOG)):
        if parent[k][u] != parent[k][v]:
            u = parent[k][u]
            v = parent[k][v]
    return parent[0][u]

def get_path(u,v):
    # return list of vertices on path u->v
    w = lca(u,v)
    path_u = []
    cur = u
    while cur != w:
        path_u.append(cur)
        cur = parent[0][cur]
    path_v = []
    cur = v
    while cur != w:
        path_v.append(cur)
        cur = parent[0][cur]
    path = path_u + [w] + path_v[::-1]
    return path

# Step 2: Build equality graph
eq_graph = [[] for _ in range(N)]

def add_eq_edge(a,b):
    eq_graph[a].append(b)
    eq_graph[b].append(a)

# For all pairs (i,j) with A[i][j]=1, add equality edges for path palindrome constraints
for i in range(N):
    for j in range(i,N):
        if A[i][j] == 1:
            path = get_path(i,j)
            n = len(path)
            for k in range(n//2):
                a = path[k]
                b = path[n-1-k]
                if a != b:
                    add_eq_edge(a,b)

# Step 3: Find connected components of equality graph
comp_id = [-1]*N
cid = 0
from collections import deque
for v in range(N):
    if comp_id[v] == -1:
        q = deque([v])
        comp_id[v] = cid
        while q:
            x = q.popleft()
            for nx in eq_graph[x]:
                if comp_id[nx] == -1:
                    comp_id[nx] = cid
                    q.append(nx)
        cid += 1

# Step 4: Check if all (i,j) with A[i][j]=1 are component-palindromic
# i.e. for path(i,j), for all k, comp_id[v_k] == comp_id[v_{n+1-k}]
for i in range(N):
    for j in range(i,N):
        if A[i][j] == 1:
            path = get_path(i,j)
            n = len(path)
            for k in range(n//2):
                if comp_id[path[k]] != comp_id[path[n-1-k]]:
                    print(10**100)
                    sys.exit()

# Step 5: Count number of palindromic pairs (i,j)
# For all pairs (i,j), check if path(i,j) is component-palindromic
# To speed up, we can precompute for all pairs:
# But O(N^2) * O(path length) ~ O(N^3) is too large.
#
# Optimization:
# Since path length can be up to O(N), O(N^3) is too big.
#
# Alternative approach:
# We can precompute for each pair (u,v) whether path(u,v) is component-palindromic.
#
# But that is O(N^3).
#
# We need a faster method.
#
# Observation:
# The condition "path(u,v) is component-palindromic" means:
# For all k, comp_id[v_k] == comp_id[v_{n+1-k}]
#
# Since the path is symmetric, this means the sequence of comp_id on the path is a palindrome.
#
# Let's define a function f(u,v) = True if path(u,v) is component-palindromic.
#
# We want to count number of pairs (i,j) with f(i,j)=True.
#
# Let's try to use DP on tree:
#
# Define dp[u][v] = True if path(u,v) is component-palindromic.
#
# Since path(u,v) = u->LCA + reversed v->LCA, we can try to use a two-pointer approach.
#
# But that is complicated.
#
# Alternative approach:
#
# Since the path palindrome condition depends on pairs of vertices symmetric on the path,
# and the equality graph components are fixed,
# we can try to use a BFS approach on pairs of vertices:
#
# Define a graph on pairs (u,v):
# - (u,v) is palindromic if:
#   - comp_id[u] == comp_id[v]
#   - and if u == v, then True
#   - else if u != v, then for neighbors of u and v on the path, the inner path is palindromic
#
# But path(u,v) is unique, so the neighbors on the path are:
# - If u == v: path length 1, palindrome
# - Else:
#   - Let u' = parent of u towards v
#   - Let v' = parent of v towards u
#
# But this is complicated.
#
# Another approach:
#
# Since the tree is undirected, and path(u,v) is unique,
# we can define a DP on pairs (u,v):
#
# dp[u][v] = True if path(u,v) is component-palindromic
#
# Base case:
# dp[u][u] = True
#
# For u != v:
# Let neighbors of u and v on the path be u1 and v1 respectively.
#
# Then dp[u][v] = (comp_id[u] == comp_id[v]) and dp[u1][v1]
#
# How to find u1 and v1?
#
# The path from u to v:
# - If u == v: done
# - Else:
#   - If depth[u] > depth[v], u1 = parent[u], v1 = v
#   - Else if depth[v] > depth[u], u1 = u, v1 = parent[v]
#   - Else if depth[u] == depth[v]:
#       - If u and v are neighbors, then path length 2, dp[u][v] = comp_id[u]==comp_id[v]
#       - Else:
#         u1 = parent[u], v1 = parent[v]
#
# Let's implement this DP.
#
# Since N=3000, dp is 3000x3000 = 9 million booleans, which is large but might be possible with bitsets.
#
# We'll use a bottom-up approach:
#
# We'll process pairs in order of increasing distance between u and v.
#
# Distance can be computed as depth[u] + depth[v] - 2*depth[lca(u,v)]
#
# We'll group pairs by distance.
#
# For distance=0: dp[u][u] = True
#
# For distance=1: dp[u][v] = (comp_id[u] == comp_id[v])
#
# For distance>1:
# dp[u][v] = (comp_id[u] == comp_id[v]) and dp[u1][v1]
#
# where u1 and v1 are the next vertices on the path from u to v.
#
# To find u1 and v1:
# - If u == v: no next
# - Else:
#   - If depth[u] > depth[v]: u1 = parent[u], v1 = v
#   - Else if depth[v] > depth[u]: u1 = u, v1 = parent[v]
#   - Else:
#       - If u and v are neighbors: no inner path, dp[u][v] = comp_id[u]==comp_id[v]
#       - Else: u1 = parent[u], v1 = parent[v]
#
# We'll precompute distance and sort pairs by distance.
#
# Then compute dp.
#
# Finally, count number of pairs (i,j) with dp[i][j] = True.
#
# Let's implement.

# Precompute distance and lca for all pairs
# O(N^2) is acceptable here.

dist = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(i,N):
        w = lca(i,j)
        d = depth[i] + depth[j] - 2*depth[w]
        dist[i][j] = d
        dist[j][i] = d

# Group pairs by distance
max_dist = max(max(row) for row in dist)
pairs_by_dist = [[] for _ in range(max_dist+1)]
for i in range(N):
    for j in range(i,N):
        pairs_by_dist[dist[i][j]].append((i,j))

dp = [[False]*N for _ in range(N)]

# distance=0
for i in range(N):
    dp[i][i] = True

# distance=1
for (u,v) in pairs_by_dist[1]:
    dp[u][v] = (comp_id[u] == comp_id[v])
    dp[v][u] = dp[u][v]

# For distance >= 2
for d in range(2, max_dist+1):
    for (u,v) in pairs_by_dist[d]:
        if comp_id[u] != comp_id[v]:
            dp[u][v] = False
            dp[v][u] = False
            continue
        if u == v:
            dp[u][v] = True
            continue
        if depth[u] > depth[v]:
            u1 = parent[0][u]
            v1 = v
        elif depth[v] > depth[u]:
            u1 = u
            v1 = parent[0][v]
        else:
            # depth[u] == depth[v]
            # check if u and v are neighbors
            if v in edges[u]:
                # path length 2, no inner path
                dp[u][v] = True
                dp[v][u] = True
                continue
            else:
                u1 = parent[0][u]
                v1 = parent[0][v]
        dp[u][v] = dp[u1][v1]
        dp[v][u] = dp[u][v]

# Step 6: Count palindromic pairs
ans = 0
for i in range(N):
    for j in range(N):
        if dp[i][j]:
            ans += 1

print(ans)