import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        edges = [tuple(map(int, input().split())) for __ in range(m)]

        # We want to find a maximum subgraph with degree <= 2 for every vertex.
        # This means the subgraph is a collection of paths and cycles.
        # The problem constraints:
        # - n <= 30
        # - each vertex belongs to at most 5 simple cycles
        # - graph is connected and simple

        # Approach:
        # Since degree <= 2, each vertex can have at most 2 edges.
        # We want to select a subset of edges maximizing the count,
        # with the constraint deg[v] <= 2 for all v.

        # This is a maximum subgraph with degree constraints problem.
        # We can solve it by backtracking with pruning or by a maximum matching style DP.
        # But since n=30 and m can be up to ~n^2/2, brute force over edges is impossible.

        # Key insight:
        # The problem is equivalent to finding a maximum subset of edges such that
        # no vertex has degree > 2.
        # This is a maximum degree-2 subgraph problem.

        # We can model this as a maximum matching-like problem with degree constraints.
        # Since degree <= 2, we can try a backtracking with pruning and memoization.

        # Another approach:
        # Since each vertex belongs to at most 5 simple cycles,
        # the graph is "almost" a cactus-like structure.
        # This means the number of cycles is limited and the graph is sparse in cycles.

        # We can try a DP over edges with bitmask of degrees.
        # But degree can be 0,1,2 per vertex, so 3 states per vertex.
        # 3^n states is too large.

        # Alternative:
        # Use a maximum weighted matching in a line graph or maximum matching with degree constraints.
        # But no weights, just maximize edges.

        # Since degree <= 2, the subgraph is a union of paths and cycles.
        # The maximum number of edges is at most n (if a cycle) or n-1 (if a path).

        # Let's try a backtracking with pruning:
        # - Keep track of degrees of vertices.
        # - Try to include or exclude edges.
        # - Prune if degree > 2.
        # - Use memoization by storing (index, degrees tuple) to avoid recomputation.

        # Since n=30, degrees tuple is 30 integers in [0..2].
        # We can encode degrees in base 3 integer for memoization.

        # Let's implement this with memoization.

        from functools import lru_cache

        # Encode degrees array to an integer key for memoization
        def encode(deg):
            res = 0
            for d in deg:
                res = res * 3 + d
            return res

        @lru_cache(None)
        def dfs(i, deg_key):
            if i == m:
                return 0
            deg = []
            key = deg_key
            for _ in range(n):
                deg.append(key % 3)
                key //= 3
            u, v = edges[i]
            u -= 1
            v -= 1

            # Option 1: skip edge i
            res = dfs(i+1, deg_key)

            # Option 2: take edge i if possible
            if deg[u] < 2 and deg[v] < 2:
                deg[u] += 1
                deg[v] += 1
                new_key = 0
                for d in reversed(deg):
                    new_key = new_key * 3 + d
                res = max(res, 1 + dfs(i+1, new_key))
            return res

        # Initial degrees all zero
        print(dfs(0, 0))

if __name__ == "__main__":
    main()