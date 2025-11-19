import sys
input = sys.stdin.readline

H, W = map(int, input().split())
F = [list(map(int, input().split())) for _ in range(H)]

Q = int(input())

# The key insight:
# Takahashi can move horizontally (via walkways) only on the same floor number X,
# provided the adjacent building has at least X floors.
# He can move vertically (stairs) within the same building.
#
# To minimize stairs usage, it is optimal to:
# - Move vertically inside the start building from Y_i to some floor X,
# - Move horizontally on floor X from (A_i,B_i) to (C_i,D_i),
# - Move vertically inside the destination building from floor X to Z_i.
#
# The cost is |Y_i - X| + |Z_i - X| + horizontal cost on floor X.
#
# Horizontal cost on floor X is the shortest path length from (A_i,B_i) to (C_i,D_i)
# on the graph where edges exist between adjacent blocks if both have floors >= X.
#
# We want to find the minimal cost over all possible X.
#
# However, F_{i,j} can be up to 10^6, and Q up to 2*10^5, so checking all floors is impossible.
#
# Observation:
# The minimal cost is:
# min_X (|Y_i - X| + |Z_i - X| + dist_X((A_i,B_i),(C_i,D_i)))
#
# The term |Y_i - X| + |Z_i - X| is minimized at X between Y_i and Z_i (inclusive).
# The minimal value of |Y_i - X| + |Z_i - X| is |Y_i - Z_i| when X is between Y_i and Z_i.
#
# So the best X is in [min(Y_i,Z_i), max(Y_i,Z_i)].
#
# For each query, we want to find if there exists a path on floor X in [minY, maxY].
#
# If we can find the minimal horizontal distance on some floor X in [minY, maxY],
# then total cost = |Y_i - X| + |Z_i - X| + horizontal distance.
#
# Since |Y_i - X| + |Z_i - X| is minimized at X in [minY, maxY], and equals |Y_i - Z_i|,
# the minimal cost is at least |Y_i - Z_i| + minimal horizontal distance on some floor X in [minY, maxY].
#
# So the problem reduces to:
# For each query, find the minimal horizontal distance between (A_i,B_i) and (C_i,D_i)
# on any floor X in [minY, maxY].
#
# Because the horizontal graph changes with X (edges exist only if both buildings have floors >= X),
# the graph is monotone decreasing as X increases (edges disappear as X increases).
#
# We can use a technique:
# - For each floor level X, define a graph G_X with edges between adjacent blocks with floors >= X.
# - For each query, we want to find the minimal distance in G_X for some X in [minY, maxY].
#
# Since the graph changes monotonically with X, we can do a binary search on X for each query:
# - Check if (A_i,B_i) and (C_i,D_i) are connected in G_X.
# - If connected, try smaller X.
# - If not connected, try larger X.
#
# But Q=2*10^5 and H*W=250000, so doing a binary search with connectivity checks per query is expensive.
#
# Instead, we can:
# - For each floor X from max_floor down to 1:
#   - Build connectivity components of G_X using Union-Find.
#   - For each query, if minY <= X <= maxY and the start and end blocks are connected in G_X,
#     record the minimal horizontal distance (which is the shortest path length on G_X).
#
# But shortest path length is not just connectivity; we need the minimal number of edges.
#
# However, the graph is a grid, edges are unweighted, so shortest path length is the minimal number of edges.
#
# If we consider connectivity only, we know if a path exists, but not the distance.
#
# To get shortest path length, we can:
# - For each floor X, the graph G_X is a subgraph of the grid.
# - The shortest path length between two blocks is the Manhattan distance if the path exists.
#   But path may be blocked.
#
# So we need shortest path length on G_X.
#
# This is complicated to do for all queries and all floors.
#
# Alternative approach:
#
# Since the graph is a grid, and edges exist only if both blocks have floors >= X,
# the graph G_X is a subgraph of the grid.
#
# For each floor X, the connected components of G_X are sets of blocks with floors >= X connected.
#
# The shortest path length between two blocks in the same component is at least the Manhattan distance,
# but can be larger if some blocks are missing.
#
# But since edges are only between adjacent blocks with floors >= X,
# the shortest path length is the shortest path in the grid restricted to blocks with floors >= X.
#
# We can precompute for each block the "floor" at which it becomes connected to neighbors.
#
# Let's try a different approach:
#
# We want to find the minimal stairs usage:
# min_X (|Y_i - X| + |Z_i - X| + dist_X((A_i,B_i),(C_i,D_i)))
#
# Since |Y_i - X| + |Z_i - X| is minimized at X in [minY, maxY] and equals |Y_i - Z_i|,
# the minimal cost is |Y_i - Z_i| + minimal horizontal distance on floor X in [minY, maxY].
#
# So the problem reduces to:
# For each query, find the minimal horizontal distance between (A_i,B_i) and (C_i,D_i)
# on any floor X in [minY, maxY].
#
# If no path exists on any floor in [minY, maxY], then the minimal cost is larger.
#
# But the horizontal distance is at least the Manhattan distance.
#
# Let's consider the following:
#
# If we fix X, the graph G_X is the subgraph of blocks with floors >= X.
# The shortest path length between two blocks in G_X is the shortest path in the grid restricted to blocks with floors >= X.
#
# The shortest path length is at least the Manhattan distance.
#
# If the two blocks are in the same connected component of G_X, the shortest path length is at least Manhattan distance.
#
# So the minimal horizontal distance is at least Manhattan distance.
#
# So the minimal cost is at least |Y_i - Z_i| + Manhattan distance between (A_i,B_i) and (C_i,D_i).
#
# Can we achieve this minimal cost?
#
# If there exists a floor X in [minY, maxY] such that (A_i,B_i) and (C_i,D_i) are connected in G_X,
# then the minimal horizontal distance is at most Manhattan distance.
#
# Because the grid is connected, the shortest path length is exactly Manhattan distance if the path exists.
#
# So the minimal cost is:
# |Y_i - Z_i| + Manhattan distance if there exists X in [minY, maxY] with connectivity,
# else larger.
#
# So the problem reduces to:
# For each query, check if there exists X in [minY, maxY] such that (A_i,B_i) and (C_i,D_i) are connected in G_X.
#
# Since G_X connectivity is monotone decreasing with X,
# we can binary search on X for each query to find the minimal X where they are connected.
#
# But Q=2*10^5, binary searching for each query is expensive.
#
# Instead, we can process queries offline:
#
# - Sort queries by minY and maxY.
# - For each floor X from max_floor down to 1:
#   - Add edges between blocks with floors >= X.
#   - For all queries with minY <= X <= maxY, check if start and end are connected.
#
# But max_floor can be up to 10^6, too large.
#
# Optimization:
#
# The floors F_{i,j} are up to 10^6, but the number of distinct floor values is at most H*W = 250000.
#
# So we can compress floors:
# - Extract all distinct floor values from F.
# - Sort them descending.
# - For each distinct floor value, build G_X.
#
# For queries, we map minY and maxY to compressed indices.
#
# Then we process floors in descending order of distinct floor values.
#
# For each floor value f:
# - Union adjacent blocks with floors >= f.
# - For queries where minY <= f <= maxY, check connectivity.
#
# We can process queries offline:
# - For each query, we want to find if there exists f in [minY, maxY] such that start and end are connected.
#
# Since connectivity only changes when we add edges at floor f,
# we can process floors in descending order.
#
# For each floor f:
# - Union blocks with floors >= f.
# - For queries with minY <= f <= maxY, if start and end connected, record answer.
#
# To do this efficiently:
# - Sort queries by minY descending.
# - For each floor f descending:
#   - Union blocks with floors == f.
#   - For all queries with minY == f, check connectivity for all f in [minY, maxY].
#
# But maxY can be larger than minY.
#
# Instead, we can:
# - For each query, we want to find the minimal floor f in [minY, maxY] where start and end are connected.
#
# We can binary search on floor values for each query:
# - For each query, binary search on floor values to find minimal floor f in [minY, maxY] where connected.
#
# Since number of distinct floors is at most 250000, binary search is feasible.
#
# Implementation plan:
#
# 1. Extract distinct floors, sort descending.
# 2. Map each block's floor to its compressed index.
# 3. For each query, map minY and maxY to compressed indices.
# 4. For each query, binary search on compressed floor indices in [minY_idx, maxY_idx].
# 5. For each mid in binary search, build Union-Find up to floor mid (i.e., union blocks with floors >= floor[mid]).
# 6. Check connectivity.
# 7. After binary search, if connected at some floor, minimal cost = |Y_i - Z_i| + Manhattan distance.
#    Else, minimal cost = |Y_i - Z_i| + Manhattan distance + something large (no path).
#
# But building Union-Find from scratch for each binary search step is expensive.
#
# Optimization:
#
# We can do a parallel binary search:
# - For all queries, maintain low and high indices.
# - For each iteration:
#   - For each mid, collect queries with mid.
#   - Build Union-Find incrementally from highest floor down to current mid.
#   - For queries at mid, check connectivity.
#   - Update low/high accordingly.
#
# This is a standard parallel binary search approach.
#
# Let's implement this.

sys.setrecursionlimit(10**7)

# Directions for adjacency
dirs = [(1,0),(-1,0),(0,1),(0,-1)]

# Flatten block index
def idx(i,j):
    return i*W + j

# Extract distinct floors
floors_set = set()
for i in range(H):
    for j in range(W):
        floors_set.add(F[i][j])
floors_list = sorted(floors_set, reverse=True)
floor_to_idx = {f:i for i,f in enumerate(floors_list)}
max_floor_idx = len(floors_list) - 1

# Map each block floor to compressed index
floor_idx_grid = [[floor_to_idx[F[i][j]] for j in range(W)] for i in range(H)]

# Queries
queries = []
for _ in range(Q):
    A,B,Y,C,D,Z = map(int, input().split())
    A -= 1
    B -= 1
    C -= 1
    D -= 1
    minY = min(Y,Z)
    maxY = max(Y,Z)
    # Map minY and maxY to compressed indices
    # We want the smallest floor >= minY and largest floor <= maxY
    # Use binary search on floors_list
    import bisect
    # floors_list is descending
    # Find left index for maxY (floors >= maxY)
    # Since floors_list descending, find leftmost floor <= maxY
    # So we find rightmost floor >= maxY
    # Actually, floors_list descending, so to find floor >= x:
    # bisect_left on reversed floors_list
    # Let's invert floors_list to ascending for bisect
    floors_asc = floors_list[::-1]
    # minY_idx: smallest floor >= minY
    # Find leftmost floor >= minY in descending floors_list
    # So in ascending floors_asc, find rightmost floor <= minY
    # So minY_idx = len(floors_list) - bisect_right(floors_asc, minY)
    minY_pos = len(floors_list) - bisect.bisect_right(floors_asc, minY)
    # maxY_idx: largest floor <= maxY
    maxY_pos = len(floors_list) - bisect.bisect_left(floors_asc, maxY) - 1
    # Clamp indices
    if minY_pos > max_floor_idx:
        minY_pos = max_floor_idx + 1  # no floor >= minY
    if maxY_pos < 0:
        maxY_pos = -1  # no floor <= maxY
    queries.append([A,B,Y,C,D,Z,minY_pos,maxY_pos])

# If minY_pos > maxY_pos, no floor in [minY,maxY]
# So no path possible

# Union-Find implementation
class UnionFind:
    def __init__(self,n):
        self.par = list(range(n))
        self.sz = [1]*n
    def find(self,x):
        while self.par[x] != x:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.sz[x] < self.sz[y]:
            x,y = y,x
        self.par[y] = x
        self.sz[x] += self.sz[y]
        return True
    def same(self,x,y):
        return self.find(x) == self.find(y)

# Prepare edges by floor
# For each floor f in floors_list, we will union blocks with floors >= f
# So we process floors in descending order
# For each floor f, union edges between blocks with floors >= f
# We prepare edges for each floor f: edges between adjacent blocks where min floor >= f

# For each edge, the minimal floor of the two blocks is the minimal floor that allows the edge
# So we can group edges by minimal floor of the two blocks

edges_by_floor = [[] for _ in range(len(floors_list))]

for i in range(H):
    for j in range(W):
        for dx,dy in dirs:
            ni = i + dx
            nj = j + dy
            if 0 <= ni < H and 0 <= nj < W:
                f1 = floor_idx_grid[i][j]
                f2 = floor_idx_grid[ni][nj]
                min_floor = min(f1,f2)
                # This edge is available for all floors <= min_floor (since floors_list descending)
                # So we add edge to edges_by_floor[min_floor]
                edges_by_floor[min_floor].append((idx(i,j), idx(ni,nj)))

# Parallel binary search
# For each query, we binary search on floor index in [minY_pos, maxY_pos]
# If minY_pos > maxY_pos, answer is no path

low = [q[6] for q in queries]  # minY_pos
high = [q[7] for q in queries]  # maxY_pos
res = [-1]*Q

# Queries that have no valid floor range get answer immediately
for i,(A,B,Y,C,D,Z,minY_pos,maxY_pos) in enumerate(queries):
    if minY_pos > maxY_pos:
        # No floor in range, no path
        res[i] = -1

# We do parallel binary search on queries with res[i] == -1 (not answered yet)
# max iterations ~ log2(len(floors_list)) <= 18

active = [i for i in range(Q) if res[i] == -1]

while active:
    mid_map = dict()
    for i in active:
        if low[i] <= high[i]:
            m = (low[i] + high[i]) // 2
            mid_map.setdefault(m, []).append(i)
    if not mid_map:
        break

    uf = UnionFind(H*W)
    # Process floors from highest (0) to lowest (max_floor_idx)
    # We will add edges for floors >= current floor index
    # So we process floors in ascending order of floor index (descending floors)
    # But we need to process floors from 0 to max_floor_idx
    # For each floor index f, add edges in edges_by_floor[f]

    # We process floors in ascending order, and for each floor index f,
    # we check queries with mid == f

    # To do this efficiently, we process floors from 0 to max_floor_idx,
    # and at each floor f, add edges_by_floor[f], then check queries with mid == f

    # Prepare queries by mid
    # mid_map already prepared

    # We process floors from 0 to max_floor_idx
    # For each floor f:
    #   add edges_by_floor[f]
    #   if f in mid_map:
    #       for each query i in mid_map[f]:
    #           check connectivity

    # Because floors_list is descending, floor index 0 is highest floor

    # So we process floors from 0 to max_floor_idx

    # To speed up, we can precompute the order of floors to process

    # Process floors in ascending order
    for f in range(len(floors_list)):
        for u,v in edges_by_floor[f]:
            uf.union(u,v)
        if f in mid_map:
            for i in mid_map[f]:
                A,B,Y,C,D,Z,minY_pos,maxY_pos = queries[i]
                s = idx(A,B)
                t = idx(C,D)
                if uf.same(s,t):
                    # Connected at floor f
                    res[i] = f
                    high[i] = f - 1
                else:
                    low[i] = f + 1
    active = [i for i in active if res[i] == -1]

# Now compute answers
# For queries with res[i] == -1, no path exists in any floor in [minY,maxY]
# So answer is |Y_i - Z_i| + Manhattan distance + large number (no path)
# But problem states we must print minimal stairs usage
# If no path, minimal stairs usage is infinite, but problem constraints guarantee path?
# No guarantee, so print minimal stairs usage as |Y_i - Z_i| + Manhattan distance + large number

# For queries with res[i] != -1:
# minimal stairs usage = |Y_i - Z_i| + Manhattan distance between (A_i,B_i) and (C_i,D_i)

for i,(A,B,Y,C,D,Z,minY_pos,maxY_pos) in enumerate(queries):
    if res[i] == -1:
        # No path
        # Output |Y-Z| + Manhattan distance + large number (e.g. 10^9)
        ans = abs(Y - Z) + abs(A - C) + abs(B - D) + 10**9
    else:
        ans = abs(Y - Z) + abs(A - C) + abs(B - D)
    print(ans)