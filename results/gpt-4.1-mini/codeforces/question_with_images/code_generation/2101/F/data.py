import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 998244353

def modpow(base, exp, mod):
    result = 1
    cur = base
    while exp > 0:
        if exp & 1:
            result = (result * cur) % mod
        cur = (cur * cur) % mod
        exp >>= 1
    return result

def main():
    t = int(input())
    # Precompute powers of 3 up to 3000 for efficiency
    max_n = 3000
    pow3 = [1]*(max_n+1)
    for i in range(1, max_n+1):
        pow3[i] = (pow3[i-1]*3) % MOD

    for _ in range(t):
        n = int(input())
        edges = [[] for __ in range(n)]
        for __ in range(n-1):
            u,v = map(int,input().split())
            u -= 1
            v -= 1
            edges[u].append(v)
            edges[v].append(u)

        # We want to compute sum of coolness over all 3^n colorings.
        # coolness = max distance between a red and a blue vertex.
        # If no red or no blue vertex, coolness = 0.

        # Key insight:
        # For each pair of vertices (u,v), distance d(u,v) = dist
        # How many colorings have coolness >= dist?
        # coolness >= dist means there exists red vertex r and blue vertex b with distance >= dist.
        # So for each dist, count how many colorings have at least one red-blue pair at distance >= dist.

        # We can use binary search on dist or just iterate dist from max distance down to 1.
        # But max distance can be up to n-1.

        # Instead, we use a DP approach on pairs of vertices:
        # Define dp[u][v] = number of colorings of the tree such that:
        # - The red vertex is in subtree rooted at u (or u itself)
        # - The blue vertex is in subtree rooted at v (or v itself)
        # - The distance between u and v is exactly d(u,v)
        # Actually, this is complicated.

        # Alternative approach (from editorial ideas):
        # For each pair (u,v), consider the path between u and v.
        # The number of colorings where u is red, v is blue, and no other red or blue vertex is on the path between u and v.
        # Then, for each pair (u,v), the number of colorings where the max distance between red and blue is exactly d(u,v) is:
        # count of colorings where u is red, v is blue, no red or blue on path between u and v except u,v,
        # and no pair with distance > d(u,v) exists.

        # This is complicated, but we can use a DP on pairs of vertices:
        # dp[u][v] = number of colorings of the subtree rooted at u and v (disjoint subtrees separated by the path between u and v)
        # with no red or blue on the path between u and v except u and v,
        # and u is red, v is blue.

        # The sum over all pairs (u,v) of dp[u][v] * d(u,v) * 3^(n - (size of path between u and v)) gives the answer.

        # We will implement the DP on pairs of vertices as follows:

        # 1. Compute all distances between pairs using BFS from each node (O(n^2))
        # 2. For each pair (u,v), we want to compute dp[u][v]:
        #    dp[u][v] = number of ways to color the rest of the tree (excluding the path between u and v)
        #    such that u is red, v is blue, and no red or blue on the path except u,v.
        #    The path length is dist(u,v)+1 vertices.
        #    The rest of the tree has n - (dist(u,v)+1) vertices.
        #    Each of these vertices can be colored in 3 ways (red, blue, white),
        #    but we must exclude colorings that create red-blue pairs with distance > dist(u,v).
        #    However, by DP construction, dp[u][v] counts exactly the number of colorings with max distance between red and blue = dist(u,v).

        # The DP recurrence:
        # For dp[u][v], if u == v, dp[u][v] = 0 (can't have red and blue same vertex)
        # Otherwise, dp[u][v] = sum over neighbors u' of u closer to v and neighbors v' of v closer to u:
        # dp[u'][v'] * 2 (because for each step, we can choose to move u or v)
        # But this is complicated.

        # Instead, we use the approach from editorial:
        # Define dp[u][v] = number of ways to color the subtree rooted at u and v (disjoint subtrees separated by the path between u and v)
        # with u red, v blue, and no red or blue on the path between u and v except u,v.

        # We can build dp bottom-up by increasing distance between u and v.

        # Implementation details:
        # - Precompute dist[u][v] for all pairs.
        # - For pairs with dist=1 (adjacent), dp[u][v] = 1 (only u red, v blue, no other red/blue on path)
        # - For pairs with dist>1:
        #   dp[u][v] = sum over neighbors u' of u with dist[u'][v] = dist[u][v]-1 of dp[u'][v]
        #              + sum over neighbors v' of v with dist[u][v'] = dist[u][v]-1 of dp[u][v']

        # But this counts colorings multiple times, so we must be careful.

        # The editorial solution is:
        # - For each pair (u,v), dp[u][v] = 1 if u == v (base case)
        # - For u != v:
        #   dp[u][v] = sum over neighbors u' of u with dist[u'][v] = dist[u][v]-1 of dp[u'][v]
        #              + sum over neighbors v' of v with dist[u][v'] = dist[u][v]-1 of dp[u][v']

        # Then the answer is sum over all pairs (u,v) of dp[u][v] * dist[u][v] * 3^(n - dist[u][v] - 1)

        # Let's implement this.

        # Step 1: Compute dist[u][v]
        dist = [[-1]*n for __ in range(n)]
        for i in range(n):
            dist[i][i] = 0
            queue = [i]
            for u in queue:
                for w in edges[u]:
                    if dist[i][w] == -1:
                        dist[i][w] = dist[i][u] + 1
                        queue.append(w)

        # Step 2: Initialize dp
        dp = [[0]*n for __ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        # Step 3: Process pairs by increasing distance
        # We need to process pairs in order of increasing dist[u][v]
        pairs_by_dist = [[] for __ in range(n)]
        for u in range(n):
            for v in range(n):
                if u != v:
                    pairs_by_dist[dist[u][v]].append((u,v))

        for d in range(1, n):
            for u,v in pairs_by_dist[d]:
                res = 0
                # neighbors u' of u with dist[u'][v] = d-1
                for u2 in edges[u]:
                    if dist[u2][v] == d-1:
                        res += dp[u2][v]
                # neighbors v' of v with dist[u][v'] = d-1
                for v2 in edges[v]:
                    if dist[u][v2] == d-1:
                        res += dp[u][v2]
                dp[u][v] = res % MOD

        # Step 4: Calculate answer
        # For each pair (u,v), number of colorings with max distance between red and blue = dist[u][v] is:
        # dp[u][v] * 3^(n - dist[u][v] - 1)
        # Multiply by dist[u][v] and sum over all pairs

        ans = 0
        for u in range(n):
            for v in range(n):
                if u != v:
                    d = dist[u][v]
                    ways = dp[u][v] * pow3[n - d - 1] % MOD
                    ans += ways * d
        ans %= MOD

        print(ans)

if __name__ == "__main__":
    main()