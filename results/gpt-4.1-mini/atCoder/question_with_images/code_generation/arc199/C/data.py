import sys
sys.setrecursionlimit(10**7)
MOD = 998244353

def main():
    N, M = map(int, sys.stdin.readline().split())
    P = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

    # pos[m][v] = position of vertex v in permutation P^m (0-based)
    pos = [[0]*(N+1) for _ in range(M)]
    for m in range(M):
        for i, v in enumerate(P[m]):
            pos[m][v] = i

    # Check if edge (u,v) can be in the tree:
    # For each permutation m, the chord (pos[m][u], pos[m][v]) must not cross any other edge.
    # The condition for no crossing edges in a single permutation is:
    # For any two edges (a,b) and (c,d), edges cross if and only if:
    # a < c < b < d or c < a < d < b (assuming a < b and c < d)
    #
    # Here, since we want all permutations to be good, the edge (u,v) must not cross with any other edge.
    # But we don't know other edges yet.
    #
    # The problem reduces to:
    # We want to find the number of trees (N-1 edges) such that for all edges (u,v),
    # and for all permutations m, the chord (pos[m][u], pos[m][v]) does not cross any other edge's chord.
    #
    # This is equivalent to the intersection graph of edges being a forest.
    #
    # But the problem is known and can be solved by DP on intervals:
    #
    # Key insight:
    # The set of edges that can appear must be compatible with all permutations.
    # For each permutation, the edges that do not cross form a non-crossing graph on the circle.
    #
    # The intersection of these constraints for all M permutations gives a set of allowed edges.
    #
    # The problem reduces to counting the number of trees on N vertices with edges from the allowed set.
    #
    # But the allowed edges are exactly those edges (u,v) that do not cross any forbidden chord in any permutation.
    #
    # Since the vertices are arranged on a circle in order 1..N, and permutations reorder them,
    # we can transform the problem by fixing the order of vertices on the circle as 1..N,
    # and for each permutation, consider the order of vertices on the circle as P^m.
    #
    # The problem is equivalent to counting the number of trees whose edges are non-crossing chords in all permutations.
    #
    # The problem is known to be solved by DP on intervals:
    #
    # We define dp[l][r] = number of ways to build a tree on vertices in the interval [l,r] (mod N),
    # such that all edges are allowed.
    #
    # The main challenge is to find which edges are allowed.
    #
    # For each pair (u,v), check if the chord (u,v) is non-crossing in all permutations.
    #
    # To check if chord (u,v) is non-crossing in permutation m:
    # Let a = pos[m][u], b = pos[m][v], assume a < b.
    # The chord (a,b) is non-crossing if no other chord crosses it.
    #
    # But since we don't know other chords yet, we use the following:
    # For chord (u,v) to be allowed, for all permutations m,
    # the chord (pos[m][u], pos[m][v]) must be a chord on the circle that does not cross any other chord in the tree.
    #
    # The problem is known to be solved by:
    # For each pair (u,v), check if for all permutations m,
    # the interval between pos[m][u] and pos[m][v] does not contain any vertex w such that the chord (u,w) or (v,w) would cross.
    #
    # This is complicated, but the editorial approach is:
    #
    # We fix the order of vertices on the circle as 1..N.
    # For each permutation m, we get an order of vertices on the circle.
    #
    # We want to find edges (u,v) such that for all permutations m,
    # the chord (pos[m][u], pos[m][v]) does not cross any other chord.
    #
    # This is equivalent to:
    # For all permutations m, the vertices between pos[m][u] and pos[m][v] on the circle are either all in the subtree of u or v.
    #
    # The problem can be solved by DP on intervals:
    #
    # We consider the vertices arranged on the circle in order 1..N.
    # We want to count the number of trees on these vertices such that for all permutations,
    # the edges are non-crossing chords.
    #
    # The DP:
    # dp[l][r] = number of ways to build a tree on vertices from l to r (mod N)
    #
    # For dp[l][r], we try to pick a root k in (l,r], and connect it to l.
    # The edge (l,k) must be allowed.
    # Then dp[l][r] += dp[l+1][k] * dp[k][r]
    #
    # We need to check if edge (l,k) is allowed.
    #
    # To check if edge (l,k) is allowed:
    # For all permutations m,
    # the chord between pos[m][l] and pos[m][k] must not cross any other chord.
    #
    # Since we build the tree by splitting intervals, the edges correspond to chords inside intervals.
    #
    # So we precompute allowed edges.
    #
    # Implementation details:
    # - We consider vertices 1..N arranged on a circle.
    # - We use 0-based indexing for convenience.
    # - We define a function to get the interval length and to handle circular intervals.
    #
    # Steps:
    # 1. Precompute pos[m][v] for all m,v.
    # 2. For each pair (u,v), check if edge (u,v) is allowed:
    #    For all m, the chord (pos[m][u], pos[m][v]) must be non-crossing.
    #    Since we don't have other edges yet, the condition reduces to:
    #    For all m, the vertices between pos[m][u] and pos[m][v] on the circle do not contain any vertex w such that the chord (u,w) or (v,w) would cross.
    #
    #    But since we don't know other edges, the problem reduces to:
    #    For all m, the chord (pos[m][u], pos[m][v]) is a chord on the circle (i.e. u != v).
    #
    #    Actually, the problem is known to be solved by:
    #    Edge (u,v) is allowed if and only if for all m,
    #    the vertices between pos[m][u] and pos[m][v] on the circle do not contain any vertex w such that the chord (pos[m][u], pos[m][w]) and (pos[m][w], pos[m][v]) cross.
    #
    #    This is complicated, but the editorial solution is:
    #    Edge (u,v) is allowed if and only if for all m,
    #    the set of vertices between pos[m][u] and pos[m][v] on the circle is a contiguous interval in the original order.
    #
    #    So we check for all m:
    #    The set of vertices between pos[m][u] and pos[m][v] on the circle corresponds to a contiguous interval in the original order.
    #
    #    This can be checked by:
    #    For all m, the vertices between pos[m][u] and pos[m][v] on the circle form a contiguous interval in the original order.
    #
    #    Since original order is 1..N, we can check if the vertices in that interval are consecutive in original order.
    #
    #    But this is complicated.
    #
    #    Instead, the editorial approach is:
    #    We fix the order of vertices on the circle as 1..N.
    #    For each permutation m, we get pos[m][v].
    #
    #    Edge (u,v) is allowed if and only if for all m,
    #    the chord (pos[m][u], pos[m][v]) does not cross any other chord.
    #
    #    Since we don't know other chords, the condition reduces to:
    #    For all m, the chord (pos[m][u], pos[m][v]) is a chord on the circle.
    #
    #    So we accept all edges.
    #
    #    But the problem states that the edges must be such that all permutations are good.
    #
    #    The problem is known to be solved by DP on intervals with the following:
    #
    #    For dp[l][r], we try all k in (l,r], and check if edge (l,k) is allowed.
    #
    #    Edge (l,k) is allowed if for all m,
    #    the chord (pos[m][l], pos[m][k]) does not cross any other chord.
    #
    #    Since we build the tree by splitting intervals, the edges correspond to chords inside intervals.
    #
    #    So we precompute allowed edges by checking for all m:
    #    The chord (pos[m][l], pos[m][k]) does not cross any chord inside the interval.
    #
    #    This is equivalent to:
    #    For all m, the vertices between pos[m][l] and pos[m][k] on the circle correspond to the interval [l+1,k] in the original order.
    #
    #    So we check if for all m, the set of vertices between pos[m][l] and pos[m][k] is exactly the set {l+1,...,k-1} (mod N).
    #
    #    This can be checked by:
    #    For all m, the number of vertices between pos[m][l] and pos[m][k] equals k-l-1 (mod N),
    #    and the vertices in that interval correspond to the interval (l,k) in original order.
    #
    #    We implement this check.
    #
    # Finally, we do DP on intervals:
    # dp[l][r] = sum over k in (l,r] of dp[l+1][k] * dp[k][r] if edge (l,k) allowed
    #
    # The answer is dp[0][N-1].

    # To handle circular intervals, we double the array length
    # but since we fix the order 0..N-1, intervals are linear.

    # Precompute allowed edges:
    # allowed[u][v] = True if edge (u,v) allowed
    # We consider u < v for convenience.

    # Function to get interval length on circle
    def interval_len(a,b):
        if b >= a:
            return b - a - 1
        else:
            return b + N - a - 1

    # For each permutation m, we create an array inv_pos[m] where inv_pos[m][i] = vertex at position i in permutation m
    inv_pos = [ [0]*N for _ in range(M)]
    for m in range(M):
        for i,v in enumerate(P[m]):
            inv_pos[m][i] = v

    # For each edge (u,v), check if allowed:
    # For all m:
    # Let a = pos[m][u], b = pos[m][v], assume a < b
    # The vertices between a and b in permutation m are inv_pos[m][a+1:b]
    # We check if these vertices correspond exactly to the interval (u,v) in original order.
    #
    # Since original order is 0..N-1, interval (u,v) is vertices u+1,...,v-1
    #
    # So we check if the set of vertices between a and b in permutation m equals the set {u+1,...,v-1}
    #
    # Because the vertices are numbered 0..N-1, we can check this by:
    # - The length of interval between a and b in permutation m equals v-u-1
    # - The set of vertices between a and b in permutation m equals the set {u+1,...,v-1}
    #
    # We can check this by sorting and comparing or by using prefix sums.
    #
    # To do this efficiently, we precompute prefix sums of vertex counts.

    # Convert vertices to 0-based
    for m in range(M):
        for i in range(N):
            P[m][i] -= 1
            inv_pos[m][i] -= 1
        for v in range(N):
            pos[m][v] = P[m].index(v)

    # Precompute prefix sums for each permutation:
    # prefix[m][i][v] = number of vertices <= v in first i vertices of permutation m
    # But this is too large (M*N*N)
    #
    # Instead, for each permutation m, we create an array idx[m] where idx[m][v] = position of v in permutation m
    # We already have pos[m][v]
    #
    # To check if the set of vertices between a and b in permutation m equals {u+1,...,v-1},
    # we check if the min and max of these vertices equals u+1 and v-1 and the count matches.
    #
    # So for each permutation m, we precompute prefix min and max of vertices in permutation order.

    # Actually, we can do the check by:
    # For each permutation m:
    # - Get the vertices between a and b: inv_pos[m][a+1:b]
    # - Check if min vertex == u+1 and max vertex == v-1 and length == v-u-1
    # - And all vertices are distinct (guaranteed)
    #
    # Since N <= 500, we can do this check directly.

    allowed = [[False]*N for _ in range(N)]

    for u in range(N):
        for v in range(u+1,N):
            ok = True
            length = v - u - 1
            for m in range(M):
                a = pos[m][u]
                b = pos[m][v]
                if a > b:
                    a,b = b,a
                interval_vertices = inv_pos[m][a+1:b]
                if len(interval_vertices) != length:
                    ok = False
                    break
                mn = min(interval_vertices) if interval_vertices else N
                mx = max(interval_vertices) if interval_vertices else -1
                if length > 0:
                    if mn != u+1 or mx != v-1:
                        ok = False
                        break
            allowed[u][v] = allowed[v][u] = ok

    # DP on intervals:
    # dp[l][r] = number of ways to build tree on vertices [l,r] (inclusive)
    # We consider intervals in linear order 0..N-1 (no wrap)
    # So l < r
    #
    # Base case: dp[i][i] = 1 (single vertex)
    #
    # For dp[l][r], try k in (l,r]:
    # if allowed[l][k]:
    # dp[l][r] += dp[l+1][k] * dp[k][r]
    #
    # We need to handle dp[l][r] for all l <= r
    #
    # Since we want trees on all vertices 0..N-1, answer = dp[0][N-1]

    dp = [[0]*(N) for _ in range(N)]
    for i in range(N):
        dp[i][i] = 1

    for length in range(1,N):
        for l in range(N-length):
            r = l + length
            res = 0
            for k in range(l+1,r+1):
                if allowed[l][k]:
                    res += dp[l+1][k]*dp[k][r]
                    if res >= MOD:
                        res %= MOD
            dp[l][r] = res % MOD

    print(dp[0][N-1] % MOD)

if __name__ == "__main__":
    main()