import sys
import threading
from collections import deque

def main():
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.readline

    H, W = map(int, input().split())
    F = [list(map(int, input().split())) for _ in range(H)]

    Q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(Q)]

    # Idea:
    # The problem reduces to finding the minimal number of stairs used to go from (A,B,Y) to (C,D,Z).
    # Moves:
    # - Inside building: cost = abs(Y - Z)
    # - Between buildings: can move horizontally at the same floor X if both buildings have at least X floors.
    #
    # We want to minimize total stairs usage.
    #
    # Key observation:
    # Moving horizontally at floor X is possible only if both buildings have at least X floors.
    # So, the floors where we can move horizontally form a graph of buildings connected by edges,
    # but only for floors <= min(F[i,j], F[i',j']).
    #
    # We want to find a path from (A,B,Y) to (C,D,Z) minimizing:
    # abs(Y - X_start) + horizontal moves at floor X + abs(Z - X_end)
    #
    # But horizontal moves cost 0 stairs, only vertical moves cost stairs.
    #
    # So the minimal stairs usage is:
    # min over floor X:
    #   abs(Y - X) + dist_floorX((A,B),(C,D)) + abs(Z - X)
    #
    # where dist_floorX((A,B),(C,D)) is the minimal number of horizontal moves at floor X.
    #
    # Since horizontal moves cost 0 stairs, dist_floorX is just shortest path length in the graph of buildings
    # where edges exist if both buildings have floor >= X.
    #
    # So for each floor X, we have a graph G_X of buildings with floor >= X.
    #
    # We want to answer Q queries:
    # For each query, find min_X [abs(Y - X) + dist_floorX((A,B),(C,D)) + abs(Z - X)]
    #
    # Constraints:
    # H,W <= 500 => up to 250000 buildings
    # Q <= 2*10^5
    # F[i,j] up to 10^6
    #
    # We cannot build graphs for all floors (up to 10^6).
    #
    # Approach:
    # 1) Preprocessing:
    #    For each building, we know F[i,j].
    # 2) Build a graph of buildings connected by edges (adjacent blocks).
    #
    # 3) We want to answer queries efficiently.
    #
    # Observation:
    # The horizontal connectivity depends on floor X:
    # For floor X, the graph includes only buildings with F[i,j] >= X.
    #
    # So the graph shrinks as X increases.
    #
    # Another observation:
    # The distance between two buildings in the graph G_X is non-increasing as X decreases,
    # because G_X includes all buildings with floor >= X.
    #
    # So dist_floorX((A,B),(C,D)) is non-increasing as X decreases.
    #
    # We want to find X minimizing abs(Y - X) + dist_floorX + abs(Z - X).
    #
    # Since dist_floorX is non-increasing as X decreases,
    # and abs(Y - X) + abs(Z - X) is V-shaped with minimum at median(Y,Z),
    # the minimal total cost is achieved near median(Y,Z).
    #
    # So we can try to find dist_floorX for some candidate floors X near median(Y,Z).
    #
    # But computing dist_floorX for arbitrary X is expensive.
    #
    # Alternative approach:
    #
    # Let's consider the problem differently:
    #
    # Define a graph where nodes are buildings.
    # Edges exist between adjacent buildings.
    #
    # We want to find the minimal number of horizontal moves between (A,B) and (C,D) in the graph
    # restricted to buildings with floor >= X.
    #
    # So for each query, we want to find the minimal dist_floorX((A,B),(C,D)) for some X.
    #
    # Since dist_floorX is non-increasing as X decreases,
    # and the cost function is abs(Y - X) + dist_floorX + abs(Z - X),
    # we can try to find the minimal cost by binary searching on X.
    #
    # But Q is large, and each BFS per query is too expensive.
    #
    # So we need a data structure to answer queries efficiently.
    #
    # Key insight:
    # The graph is fixed, edges between adjacent buildings.
    # The only difference is the floor threshold X.
    #
    # For each edge between buildings u and v,
    # the edge exists only if min(F[u], F[v]) >= X.
    #
    # So edges disappear as X increases.
    #
    # So the graph is a decreasing sequence of graphs as X increases.
    #
    # We can process edges sorted by their min(F[u], F[v]) in decreasing order.
    #
    # Then, for each floor X, the graph G_X includes all edges with min(F[u], F[v]) >= X.
    #
    # So if we process edges in decreasing order of min(F[u], F[v]),
    # and maintain connectivity using Union-Find,
    # then for each X, the connected components correspond to G_X.
    #
    # So for each query, if we fix X, we can check if (A,B) and (C,D) are connected in G_X.
    #
    # But we want shortest path length, not just connectivity.
    #
    # However, the graph is a grid, edges have length 1.
    #
    # If the graph is connected, the shortest path length is the minimal number of edges.
    #
    # But we cannot get shortest path length from Union-Find.
    #
    # Alternative:
    #
    # Since edges are unweighted and the graph is a grid,
    # the shortest path length between two nodes is the Manhattan distance if the path exists.
    #
    # But the graph is not necessarily fully connected.
    #
    # So if (A,B) and (C,D) are connected in G_X,
    # the shortest path length is at least the Manhattan distance between (A,B) and (C,D).
    #
    # But it can be larger if some blocks are missing.
    #
    # So Manhattan distance is a lower bound.
    #
    # So we can approximate dist_floorX((A,B),(C,D)) by:
    # - If connected in G_X: shortest path length >= Manhattan distance
    # - If not connected: infinite
    #
    # So we can use connectivity as a proxy.
    #
    # Then the cost function becomes:
    # abs(Y - X) + abs(Z - X) + dist_floorX((A,B),(C,D))
    #
    # If not connected, cost = infinite.
    #
    # So for each query, we want to find minimal cost over X:
    # abs(Y - X) + abs(Z - X) + dist_floorX((A,B),(C,D))
    #
    # Since dist_floorX is infinite if not connected, and non-increasing as X decreases,
    # the minimal X where (A,B) and (C,D) become connected is the key.
    #
    # So for each query, we want to find the minimal X such that (A,B) and (C,D) are connected in G_X.
    #
    # Then cost = abs(Y - X) + abs(Z - X) + dist_floorX((A,B),(C,D))
    #
    # But we don't know dist_floorX exactly.
    #
    # Let's approximate dist_floorX by the shortest path length in the full graph (with all edges),
    # which is the Manhattan distance between (A,B) and (C,D).
    #
    # Because edges are only removed as X increases,
    # the shortest path length can only increase or become infinite.
    #
    # So the minimal path length is at least Manhattan distance.
    #
    # So we can use Manhattan distance as dist_floorX.
    #
    # So the minimal cost is:
    # abs(Y - X) + abs(Z - X) + Manhattan_distance((A,B),(C,D))
    #
    # where X >= minimal X such that (A,B) and (C,D) are connected in G_X.
    #
    # So the problem reduces to:
    # For each query, find minimal X such that (A,B) and (C,D) are connected in G_X.
    #
    # Then answer = abs(Y - X) + abs(Z - X) + Manhattan_distance((A,B),(C,D))
    #
    # Implementation plan:
    #
    # 1) For each edge between adjacent buildings u and v,
    #    compute w = min(F[u], F[v]).
    # 2) Sort edges by w descending.
    # 3) For each query, we want to find minimal X such that (A,B) and (C,D) connected in G_X.
    #    Since G_X includes all edges with w >= X,
    #    connectivity increases as X decreases.
    #
    # So we can process queries offline:
    #
    # - Sort queries by X in ascending order (we will binary search X).
    #
    # But we don't know X in advance.
    #
    # Instead, we can binary search X for each query:
    #
    # - For each query, binary search X in [1, max_floor].
    # - For each mid, check if (A,B) and (C,D) connected in G_mid.
    #
    # But Q=2e5 and binary search with Union-Find rebuild each time is too slow.
    #
    # Alternative:
    #
    # We can do a parallel binary search:
    #
    # - For each query, maintain low=1, high=max_floor+1 (max_floor = max F[i,j])
    # - While there are queries with low < high:
    #   - mid = (low+high)//2
    #   - For all queries with current mid, check connectivity in G_mid
    #   - To do this efficiently, we process edges in descending order of w,
    #     and add edges with w >= mid to Union-Find.
    #   - For each mid, we can process all queries with that mid.
    #
    # But we have multiple mid values.
    #
    # So we do a parallel binary search:
    #
    # - For each iteration:
    #   - For all queries, compute mid = (low+high)//2
    #   - Group queries by mid
    #   - For all mid in sorted order descending:
    #     - Add edges with w >= mid to Union-Find
    #     - For queries with mid, check connectivity
    #     - Update low or high accordingly
    #
    # To avoid rebuilding Union-Find from scratch each time,
    # we process mid in descending order, adding edges as mid decreases.
    #
    # Implementation details:
    #
    # - Sort edges by w descending
    # - For each iteration:
    #   - For all queries with low < high:
    #     - mid = (low+high)//2
    #   - Group queries by mid
    # - Process mids in descending order:
    #   - Add edges with w >= mid to Union-Find
    #   - For each query with mid:
    #     - Check if connected
    #     - Update low or high
    #
    # Repeat until all queries have low == high.
    #
    # Finally, for each query:
    # - minimal X = low
    # - cost = abs(Y - X) + abs(Z - X) + Manhattan_distance((A,B),(C,D))
    #
    # Note: If low == max_floor+1, means no connectivity at any floor, cost = infinite.
    # But problem guarantees start != end, so path exists at some floor.
    #
    # Let's implement this.

    max_floor = 0
    for i in range(H):
        for j in range(W):
            if F[i][j] > max_floor:
                max_floor = F[i][j]

    # Map 2D coordinates to 1D id
    def id(i, j):
        return i * W + j

    # Build edges with weight = min(F[u], F[v])
    edges = []
    for i in range(H):
        for j in range(W):
            u = id(i, j)
            for ni, nj in ((i+1,j),(i,j+1)):
                if 0 <= ni < H and 0 <= nj < W:
                    v = id(ni, nj)
                    w = min(F[i][j], F[ni][nj])
                    edges.append((w, u, v))
    edges.sort(reverse=True)  # descending by w

    # Queries: store (A,B,Y,C,D,Z)
    # Convert (A,B) and (C,D) to 0-based and id
    queries_data = []
    for idx, (A,B,Y,C,D,Z) in enumerate(queries):
        A -= 1
        B -= 1
        C -= 1
        D -= 1
        queries_data.append({
            'idx': idx,
            'start': id(A,B),
            'end': id(C,D),
            'Y': Y,
            'Z': Z,
            'low': 1,
            'high': max_floor + 1,
        })

    # Union-Find data structure
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [0]*n
        def find(self, x):
            while self.parent[x] != x:
                self.parent[x] = self.parent[self.parent[x]]
                x = self.parent[x]
            return x
        def unite(self, x, y):
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
        def same(self, x, y):
            return self.find(x) == self.find(y)

    # Parallel binary search
    uf = UnionFind(H*W)
    edge_ptr = 0  # pointer to edges

    # We will iterate until all queries have low == high
    # For each iteration:
    # - group queries by mid = (low+high)//2
    # - process mids in descending order
    # - add edges with w >= mid to uf
    # - check connectivity for queries with mid
    # - update low or high

    # To avoid rebuilding uf each iteration, we process mids in descending order,
    # adding edges as mid decreases.

    # We need to store queries indices for each mid
    from collections import defaultdict

    while True:
        mids_map = defaultdict(list)
        active = 0
        for q in queries_data:
            if q['low'] < q['high']:
                mid = (q['low'] + q['high']) // 2
                mids_map[mid].append(q)
                active += 1
        if active == 0:
            break

        # Process mids in descending order
        mids = sorted(mids_map.keys(), reverse=True)

        uf = UnionFind(H*W)
        edge_ptr = 0

        for mid in mids:
            # Add edges with w >= mid
            while edge_ptr < len(edges) and edges[edge_ptr][0] >= mid:
                _, u, v = edges[edge_ptr]
                uf.unite(u, v)
                edge_ptr += 1
            # Check queries with this mid
            for q in mids_map[mid]:
                if uf.same(q['start'], q['end']):
                    q['high'] = mid
                else:
                    q['low'] = mid + 1

    # Now for each query, minimal X = low
    # cost = abs(Y - X) + abs(Z - X) + Manhattan_distance((A,B),(C,D))

    # Precompute coordinates for each building id
    coords = [(i, j) for i in range(H) for j in range(W)]

    res = [0]*Q
    for q in queries_data:
        X = q['low']
        A_i, B_i = coords[q['start']]
        C_i, D_i = coords[q['end']]
        dist = abs(A_i - C_i) + abs(B_i - D_i)
        cost = abs(q['Y'] - X) + abs(q['Z'] - X) + dist
        res[q['idx']] = cost

    print('\n'.join(map(str, res)))

threading.Thread(target=main).start()