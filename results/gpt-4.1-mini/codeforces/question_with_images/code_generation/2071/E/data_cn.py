import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 998244353

def modinv(a, m=MOD):
    # Fermat's little theorem for modular inverse since MOD is prime
    return pow(a, m-2, m)

t = int(input())
total_n = 0

for _ in range(t):
    n = int(input())
    total_n += n
    p = [0]*(n+1)
    q = [0]*(n+1)
    inv_q = [0]*(n+1)
    for i in range(1, n+1):
        pi, qi = map(int, input().split())
        p[i], q[i] = pi, qi
        inv_q[i] = modinv(qi)
    edges = [[] for __ in range(n+1)]
    for __ in range(n-1):
        u,v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)

    # Precompute P_alive[i] = p_i/q_i mod
    P_alive = [0]*(n+1)
    for i in range(1,n+1):
        P_alive[i] = p[i]*inv_q[i] % MOD

    # We want E = E[ sum_{u<v} I(u leaf) * I(v leaf) ]
    # = 1/2 * ( E[(sum I(u leaf))^2] - E[sum I(u leaf)] )
    # So we need E[sum I(u leaf)] and E[(sum I(u leaf))^2]

    # For each vertex i:
    # I(i leaf) = 1 if i alive and exactly one alive neighbor
    # Probability i alive = P_alive[i]
    # Probability neighbor j alive = P_alive[j]
    # Probability i leaf = P_alive[i] * product over neighbors j of P_alive[j]^(deg=1) or (1-P_alive[j])^(deg=0)
    # Actually, leaf means exactly one alive neighbor:
    # P(i leaf) = P_alive[i] * sum over neighbors j of (P_alive[j] * product over k!=j neighbors of (1 - P_alive[k]))

    # Compute P(i leaf)
    # For each node i:
    # Let neighbors = [v1,v2,...,vd]
    # P(i leaf) = P_alive[i] * sum_{j=1 to d} [ P_alive[v_j] * product_{k!=j} (1 - P_alive[v_k]) ]

    # To compute efficiently, precompute prefix and suffix products of (1 - P_alive[v_k])

    P_leaf = [0]*(n+1)
    for i in range(1,n+1):
        deg = len(edges[i])
        if deg == 0:
            # isolated node, no edges, can't be leaf
            P_leaf[i] = 0
            continue
        neighbors = edges[i]
        vals = [ (1 - P_alive[v]) % MOD for v in neighbors ]
        prefix = [1]*(deg+1)
        suffix = [1]*(deg+1)
        for idx in range(deg):
            prefix[idx+1] = prefix[idx]*vals[idx] % MOD
        for idx in range(deg-1,-1,-1):
            suffix[idx] = suffix[idx+1]*vals[idx] % MOD
        s = 0
        for j in range(deg):
            # P_alive[neighbors[j]] * product of (1 - P_alive[neighbors[k]]) for k!=j
            val = P_alive[neighbors[j]] * prefix[j] % MOD
            val = val * suffix[j+1] % MOD
            s = (s + val) % MOD
        P_leaf[i] = P_alive[i] * s % MOD

    # E[sum I(i leaf)] = sum P_leaf[i]
    S1 = 0
    for i in range(1,n+1):
        S1 = (S1 + P_leaf[i]) % MOD

    # Next, compute E[(sum I(i leaf))^2] = sum_i E[I(i leaf)] + 2*sum_{i<j} E[I(i leaf)*I(j leaf)]
    # We have sum_i E[I(i leaf)] = S1
    # Need sum_{i<j} E[I(i leaf)*I(j leaf)]

    # For i != j, E[I(i leaf)*I(j leaf)] = P(i leaf and j leaf)
    # I(i leaf) = i alive and exactly one alive neighbor
    # I(j leaf) = j alive and exactly one alive neighbor

    # The events depend on the alive states of i,j and their neighbors.
    # Since vertices fall independently, we can compute joint probability by considering the union of involved vertices.

    # To compute sum_{i<j} P(i leaf and j leaf) efficiently, we use the following:

    # For pairs (i,j) with no common neighbors and i!=j and not adjacent:
    # The sets of vertices involved in i leaf and j leaf are disjoint except possibly i and j themselves.
    # But since i != j and no adjacency, the sets are disjoint.
    # So P(i leaf and j leaf) = P(i leaf)*P(j leaf)

    # For pairs (i,j) that are adjacent or share neighbors, we need to compute exactly.

    # We will:
    # 1) sum all pairs i<j P(i leaf)*P(j leaf) = (S1^2 - sum_i P_leaf[i]^2)/2
    # 2) subtract pairs where i and j are adjacent or share neighbors, and add exact P(i leaf and j leaf)

    # But this is complicated.

    # Alternative approach:
    # Since n can be large, we try to compute sum_{i<j} P(i leaf and j leaf) by:
    # sum_{i<j} P(i leaf)*P(j leaf) - sum_{(i,j) in conflict} (P(i leaf)*P(j leaf) - P(i leaf and j leaf))

    # But the number of conflict pairs can be large.

    # Let's try a different approach:

    # Since leaf depends only on i and neighbors, and neighbors of neighbors,
    # the dependency is local.

    # Let's consider the following:

    # For each edge (u,v), the events I(u leaf) and I(v leaf) are dependent because u and v are neighbors.

    # For pairs (i,j) that are not neighbors and do not share neighbors, I(i leaf) and I(j leaf) are independent:
    # P(i leaf and j leaf) = P(i leaf)*P(j leaf)

    # For pairs (i,j) that are neighbors or share neighbors, we compute P(i leaf and j leaf) exactly.

    # So we can write:
    # sum_{i<j} P(i leaf and j leaf) = sum_{i<j} P(i leaf)*P(j leaf) - sum_{conflict pairs} (P(i leaf)*P(j leaf) - P(i leaf and j leaf))

    # The number of conflict pairs is manageable because each vertex has limited degree.

    # Let's find all conflict pairs:

    # Conflict pairs are pairs (i,j) where i and j are neighbors or share a neighbor.

    # For each vertex i:
    # - neighbors: edges[i]
    # - For each neighbor v in edges[i], pair (i,v) is conflict
    # - For each pair of neighbors (u,v) of i, pair (u,v) is conflict because they share neighbor i

    # So conflict pairs are:
    # - all edges (i,v)
    # - all pairs of neighbors of each vertex

    # We'll collect all conflict pairs in a set to avoid duplicates.

    conflict_pairs = set()
    for i in range(1,n+1):
        nbrs = edges[i]
        deg = len(nbrs)
        # pairs of neighbors
        for x in range(deg):
            for y in range(x+1, deg):
                a,b = nbrs[x], nbrs[y]
                if a > b:
                    a,b = b,a
                conflict_pairs.add((a,b))
        # edges
        for v in nbrs:
            a,b = i,v
            if a > b:
                a,b = b,a
            conflict_pairs.add((a,b))

    # Now compute sum_{i<j} P(i leaf)*P(j leaf)
    S1_sq = S1 * S1 % MOD
    sum_p2 = 0
    for i in range(1,n+1):
        sum_p2 = (sum_p2 + P_leaf[i]*P_leaf[i]) % MOD
    total_pairs = (S1_sq - sum_p2) * modinv(2) % MOD

    # For each conflict pair, compute P(i leaf and j leaf) exactly and adjust
    # We will subtract (P(i leaf)*P(j leaf) - P(i leaf and j leaf)) from total_pairs

    # To compute P(i leaf and j leaf):
    # I(i leaf) = i alive and exactly one alive neighbor
    # I(j leaf) = j alive and exactly one alive neighbor

    # The involved vertices are i, neighbors(i), j, neighbors(j)
    # The alive states are independent for each vertex.

    # We enumerate the possible alive neighbors for i and j to be exactly one alive neighbor each.

    # For i leaf:
    # sum over neighbor u of i: P_alive[u] * product over other neighbors (1 - P_alive[...])
    # Similarly for j leaf.

    # For joint probability:
    # sum over u in neighbors(i), v in neighbors(j):
    # P(i alive) * P(j alive) *
    # P_alive[u] * P_alive[v] *
    # product over other neighbors of i except u of (1 - P_alive) *
    # product over other neighbors of j except v of (1 - P_alive)

    # If neighbors(i) and neighbors(j) overlap, we must be careful to not multiply probabilities twice.

    # Also, if i == j or neighbors overlap, handle carefully.

    # Implement carefully:

    # Precompute for each node:
    # neighbors list and P_alive values

    # For each conflict pair (i,j):
    # Compute P(i leaf and j leaf)

    # To speed up, precompute for each node:
    # prefix and suffix products of (1 - P_alive) for neighbors

    # We'll store these for each node to avoid recomputing.

    prefix_products = [None]*(n+1)
    suffix_products = [None]*(n+1)
    for i in range(1,n+1):
        deg = len(edges[i])
        vals = [ (1 - P_alive[v]) % MOD for v in edges[i] ]
        prefix = [1]*(deg+1)
        suffix = [1]*(deg+1)
        for idx in range(deg):
            prefix[idx+1] = prefix[idx]*vals[idx] % MOD
        for idx in range(deg-1,-1,-1):
            suffix[idx] = suffix[idx+1]*vals[idx] % MOD
        prefix_products[i] = prefix
        suffix_products[i] = suffix

    # For quick index of neighbor in edges[i]
    neighbor_index = [{} for _ in range(n+1)]
    for i in range(1,n+1):
        for idx,v in enumerate(edges[i]):
            neighbor_index[i][v] = idx

    def P_i_leaf_given_neighbor(i,u):
        # P_alive[u] * product over neighbors except u of (1 - P_alive)
        idx = neighbor_index[i][u]
        pre = prefix_products[i][idx]
        suf = suffix_products[i][idx+1]
        return P_alive[u] * pre % MOD * suf % MOD

    # Now compute P(i leaf and j leaf)
    # i alive and j alive
    # sum over u in neighbors(i), v in neighbors(j):
    # P_alive[u] * P_alive[v] *
    # product over neighbors(i) except u of (1 - P_alive) *
    # product over neighbors(j) except v of (1 - P_alive)

    # If neighbors(i) and neighbors(j) overlap, the product over (1 - P_alive) for common neighbors is counted twice,
    # but since alive states are independent, the joint probability is product of probabilities for each vertex.

    # So for common neighbors c in neighbors(i) and neighbors(j):
    # The factor (1 - P_alive[c]) appears twice, but since it's the same vertex, we must only count once.

    # So we must correct for double counting.

    # Let's define:
    # S = set of neighbors(i) union neighbors(j)
    # For each u in neighbors(i), v in neighbors(j):
    # The product over neighbors(i) except u: product_{x in neighbors(i), x!=u} (1 - P_alive[x])
    # The product over neighbors(j) except v: product_{y in neighbors(j), y!=v} (1 - P_alive[y])

    # The combined product is product over S except u and v of (1 - P_alive[x])

    # If u == v (common neighbor), then we exclude u=v once.

    # So the combined product is product over S except u and v of (1 - P_alive[x])

    # So we can write:
    # P(i leaf and j leaf) = P_alive[i] * P_alive[j] *
    # sum_{u in neighbors(i)} sum_{v in neighbors(j)} P_alive[u] * P_alive[v] *
    # product_{x in S \ {u,v}} (1 - P_alive[x])

    # To compute product over S \ {u,v} (1 - P_alive[x]), we precompute product over S (1 - P_alive[x]) and divide by (1 - P_alive[u]) and (1 - P_alive[v]) if u != v,
    # if u == v, divide only once.

    # Implementation:

    # For each conflict pair (i,j):
    # 1) compute S = neighbors(i) union neighbors(j)
    # 2) compute product_all = product_{x in S} (1 - P_alive[x])
    # 3) for each u in neighbors(i):
    #    for each v in neighbors(j):
    #       if u == v:
    #          prod = product_all * inv(1 - P_alive[u]) mod
    #       else:
    #          prod = product_all * inv(1 - P_alive[u]) * inv(1 - P_alive[v]) mod
    #       sum += P_alive[u] * P_alive[v] * prod mod
    # 4) multiply sum by P_alive[i]*P_alive[j]

    # Precompute modular inverses of (1 - P_alive[x]) for all x to speed up

    inv_1_minus_P = [0]*(n+1)
    for i in range(1,n+1):
        val = (1 - P_alive[i]) % MOD
        if val == 0:
            inv_1_minus_P[i] = 0  # won't be used if zero
        else:
            inv_1_minus_P[i] = modinv(val)

    # To avoid recomputing product_all for each pair, we cache results.

    # We'll implement a function to compute product_all for a given set S.

    # Since sets are small (neighbors of i and j), we can do it directly.

    # Now implement the main loop:

    adjust = 0
    for (i,j) in conflict_pairs:
        if i == j:
            continue
        # neighbors sets
        set_i = set(edges[i])
        set_j = set(edges[j])
        S = set_i | set_j
        # product_all = product of (1 - P_alive[x]) for x in S
        product_all = 1
        for x in S:
            product_all = product_all * ((1 - P_alive[x]) % MOD) % MOD

        sum_uv = 0
        for u in edges[i]:
            Pu = P_alive[u]
            inv_u = inv_1_minus_P[u] if (1 - P_alive[u]) % MOD != 0 else 0
            for v in edges[j]:
                Pv = P_alive[v]
                if u == v:
                    # divide once
                    if inv_u == 0:
                        continue
                    prod = product_all * inv_u % MOD
                else:
                    inv_v = inv_1_minus_P[v] if (1 - P_alive[v]) % MOD != 0 else 0
                    if inv_u == 0 or inv_v == 0:
                        continue
                    prod = product_all * inv_u % MOD * inv_v % MOD
                sum_uv = (sum_uv + Pu * Pv % MOD * prod) % MOD

        P_i_j = P_alive[i] * P_alive[j] % MOD * sum_uv % MOD

        diff = (P_leaf[i] * P_leaf[j] - P_i_j) % MOD
        adjust = (adjust + diff) % MOD

    ans = (total_pairs - adjust) % MOD
    # E[(sum I(i leaf))^2] = S1 + 2 * ans
    E_square = (S1 + 2 * ans) % MOD

    # final answer = (E_square - S1) * inv(2) mod
    res = (E_square - S1) * modinv(2) % MOD
    print(res)