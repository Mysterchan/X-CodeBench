import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 998244353

def modinv(a, m=MOD):
    # Fermat's little theorem for modular inverse since MOD is prime
    return pow(a, m-2, m)

t = int(input())
# sum of n over all test cases <= 10^5, so we can process all efficiently

for _ in range(t):
    n = int(input())
    p = [0]*(n+1)
    q = [0]*(n+1)
    inv_q = [0]*(n+1)
    for i in range(1, n+1):
        pi, qi = map(int, input().split())
        p[i] = pi % MOD
        q[i] = qi % MOD
        inv_q[i] = modinv(q[i])
    # probabilities of falling: p[i]/q[i]
    # probabilities of not falling: (q[i]-p[i])/q[i]

    # Read edges
    adj = [[] for _ in range(n+1)]
    deg = [0]*(n+1)
    for _ in range(n-1):
        u,v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
        deg[u] += 1
        deg[v] += 1

    # Precompute probabilities of not falling and falling modulo MOD
    # p_fall[i] = p[i]*inv_q[i] mod
    # p_not_fall[i] = (q[i]-p[i])*inv_q[i] mod
    p_fall = [0]*(n+1)
    p_not_fall = [0]*(n+1)
    for i in range(1, n+1):
        p_fall[i] = p[i]*inv_q[i] % MOD
        p_not_fall[i] = (q[i]-p[i])*inv_q[i] % MOD

    # We want expected number of unordered pairs of distinct vertices that become leaves.
    # A vertex i is a leaf in the resulting forest if:
    # - i has not fallen
    # - exactly one of its neighbors has not fallen (degree in forest = 1)
    #
    # Let X_i = indicator that vertex i is a leaf in the forest.
    # We want E[ sum_{i<j} X_i * X_j ] = sum_{i<j} E[X_i * X_j]
    #
    # Since vertices fall independently, we can compute E[X_i * X_j].
    #
    # X_i = 1 if:
    #   i not fallen AND exactly one neighbor not fallen
    #
    # For each vertex i:
    #   Let N(i) = neighbors of i
    #   deg[i] = degree of i in original tree
    #
    # Probability that i is leaf:
    #   P(i leaf) = P(i not fallen) * sum over neighbors u of:
    #       P(u not fallen) * product over w in N(i), w != u of P(w fallen)
    #
    # Similarly, for E[X_i * X_j], we consider cases:
    # - i and j are distinct vertices
    # - both are leaves simultaneously
    #
    # We can split pairs into two types:
    # 1) i and j are not adjacent
    # 2) i and j are adjacent
    #
    # For non-adjacent pairs (i,j):
    #   X_i and X_j depend on disjoint sets of vertices except possibly neighbors.
    #   But since the tree is connected, neighbors sets may overlap only if i and j are adjacent.
    #
    # For adjacent pairs (i,j):
    #   We must consider joint probability carefully.
    #
    # Approach:
    # - Compute E[X_i] for all i
    # - Compute E[X_i * X_j] for all edges (i,j)
    # - For non-adjacent pairs, since X_i and X_j depend on disjoint sets of vertices (except possibly neighbors),
    #   but neighbors sets do not overlap for non-adjacent vertices, so X_i and X_j are independent.
    #   So E[X_i * X_j] = E[X_i] * E[X_j]
    #
    # So:
    # sum_{i<j} E[X_i * X_j] = (sum_i E[X_i])^2 - sum_i E[X_i]^2
    #                         + sum_{(i,j) in edges} (E[X_i * X_j] - E[X_i]*E[X_j])
    #
    # Because for edges, X_i and X_j are not independent, so we add correction term.
    #
    # So the plan:
    # 1) Compute E[X_i] for all i
    # 2) Compute sum E[X_i], sum E[X_i]^2
    # 3) For each edge (u,v), compute E[X_u * X_v]
    # 4) Compute answer = ((sum E[X_i])^2 - sum E[X_i]^2 + sum over edges (E[X_u*X_v] - E[X_u]*E[X_v])) / 2
    #
    # Divide by 2 because pairs are unordered and counted twice in sum_i sum_j.
    #
    # Implementation details:
    # For each vertex i:
    #   E[X_i] = p_not_fall[i] * sum_{u in N(i)} (p_not_fall[u] * product_{w in N(i), w!=u} p_fall[w])
    #
    # For each edge (u,v):
    #   E[X_u * X_v] = P(u leaf and v leaf)
    #
    # Conditions for u leaf:
    #   u not fallen
    #   exactly one neighbor of u not fallen
    #
    # Conditions for v leaf:
    #   v not fallen
    #   exactly one neighbor of v not fallen
    #
    # Since u and v are neighbors, they can be the "one neighbor not fallen" for each other.
    #
    # So for u leaf:
    #   u not fallen
    #   neighbors of u except v all fallen
    #   v not fallen
    #
    # For v leaf:
    #   v not fallen
    #   neighbors of v except u all fallen
    #   u not fallen
    #
    # So for both u and v leaf simultaneously:
    #   u not fallen
    #   v not fallen
    #   neighbors of u except v all fallen
    #   neighbors of v except u all fallen
    #
    # Probability:
    #   p_not_fall[u] * p_not_fall[v] *
    #   product_{w in N(u), w!=v} p_fall[w] *
    #   product_{x in N(v), x!=u} p_fall[x]
    #
    # This is E[X_u * X_v].
    #
    # We already have E[X_u] and E[X_v], so we can compute correction term.
    #
    # Finally output answer modulo MOD.

    # Precompute for each vertex:
    # prod_fall_neighbors[i] = product of p_fall[w] for w in N(i)
    prod_fall_neighbors = [1]*(n+1)
    for i in range(1, n+1):
        res = 1
        for w in adj[i]:
            res = (res * p_fall[w]) % MOD
        prod_fall_neighbors[i] = res

    # Compute E[X_i]
    E = [0]*(n+1)
    for i in range(1, n+1):
        if deg[i] == 0:
            # isolated vertex (n=1 case)
            # leaf means degree 1, so no leaf possible
            E[i] = 0
            continue
        val = 0
        for u in adj[i]:
            # product of p_fall[w] for w in N(i), w!=u
            # = prod_fall_neighbors[i] * inv(p_fall[u])
            inv_p_fall_u = modinv(p_fall[u])
            val += p_not_fall[u] * (prod_fall_neighbors[i] * inv_p_fall_u % MOD)
            val %= MOD
        E[i] = p_not_fall[i] * val % MOD

    sumE = 0
    sumE2 = 0
    for i in range(1, n+1):
        sumE += E[i]
        if sumE >= MOD:
            sumE -= MOD
        sumE2 += E[i]*E[i]
        sumE2 %= MOD

    # Compute sum over edges of E[X_u * X_v]
    sum_edge = 0
    for u in range(1, n+1):
        for v in adj[u]:
            if u < v:
                # compute E[X_u * X_v]
                # = p_not_fall[u] * p_not_fall[v] *
                #   product_{w in N(u), w!=v} p_fall[w] *
                #   product_{x in N(v), x!=u} p_fall[x]
                # Use prod_fall_neighbors and remove p_fall[v] and p_fall[u] respectively
                inv_p_fall_v = modinv(p_fall[v])
                inv_p_fall_u = modinv(p_fall[u])
                pu = (prod_fall_neighbors[u] * inv_p_fall_v) % MOD
                pv = (prod_fall_neighbors[v] * inv_p_fall_u) % MOD
                val = p_not_fall[u] * p_not_fall[v] % MOD
                val = val * pu % MOD
                val = val * pv % MOD
                sum_edge += val
                if sum_edge >= MOD:
                    sum_edge -= MOD

    # Calculate final answer:
    # (sumE^2 - sumE2 + sum_edge) / 2 mod MOD
    ans = (sumE*sumE - sumE2 + sum_edge) % MOD
    inv2 = (MOD+1)//2
    ans = ans * inv2 % MOD

    print(ans)