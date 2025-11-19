import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

a = [list(map(int, list(input().rstrip()))) for _ in range(n)]

# Precompute parent for each node in BFS tree rooted at each node
# To optimize memory, we store only one BFS parent array at a time when needed.
# But since we need direction[i][j] for all pairs, we must store all.
# We'll optimize by using a single BFS from each node and store parents in a compact way.

# direction[i][j]: parent of j in BFS tree rooted at i
# We'll store direction as a list of arrays, each of size n
direction = [None] * n
from collections import deque

for i in range(n):
    par = [-1] * n
    par[i] = i
    q = deque([i])
    while q:
        v = q.popleft()
        for u in adj[v]:
            if par[u] == -1:
                par[u] = v
                q.append(u)
    direction[i] = par

# Union-Find for grouping nodes that must have same value
class UnionFind:
    __slots__ = ['parent', 'rank']
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
        return True

uf = UnionFind(n)

# We only need to process pairs (i,j) with A[i][j] = 1 and i<j
# For each such pair, union i and j, then union their parents in BFS trees rooted at i and j
# We use a stack to process pairs recursively until reaching the middle of the path

stack = []
for i in range(n):
    row = a[i]
    for j in range(i+1, n):
        if row[j] == 1:
            stack.append((i,j))

visited = [[False]*n for _ in range(n)]

while stack:
    i,j = stack.pop()
    if i == j:
        continue
    if visited[i][j]:
        continue
    visited[i][j] = True
    visited[j][i] = True
    uf.union(i,j)
    pi = direction[i][j]
    pj = direction[j][i]
    if pi == j:
        continue
    stack.append((pi,pj))

# Now, for counting palindromic pairs, we use DP with memoization
# flag[i][j] = True if path from i to j is palindromic under the union-find constraints
# We use iterative DP to avoid recursion overhead

flag = [[-1]*n for _ in range(n)]  # -1: unknown, 0: False, 1: True

# Base cases: i==j is always True
for i in range(n):
    flag[i][i] = 1

# We process pairs in order of increasing distance between i and j
# Distance can be approximated by BFS levels or just by difference in indices (not accurate)
# Instead, we process pairs by increasing path length using BFS approach

from collections import deque
q = deque()
for i in range(n):
    q.append((i,i))

while q:
    i,j = q.popleft()
    if flag[i][j] == 0:
        continue
    # For pairs where i != j, try to propagate to neighbors
    if i != j:
        pi = direction[i][j]
        pj = direction[j][i]
        if pi == j:
            # adjacent nodes, path length 2, already True if union-find same set
            continue
        if flag[pi][pj] == -1:
            # Check union-find condition
            if uf.find(pi) != uf.find(pj):
                flag[pi][pj] = 0
            else:
                flag[pi][pj] = 1
                q.append((pi,pj))

# Count palindromic pairs
ans = 0
for i in range(n):
    for j in range(n):
        if flag[i][j] == 1:
            ans += 1

print(ans)