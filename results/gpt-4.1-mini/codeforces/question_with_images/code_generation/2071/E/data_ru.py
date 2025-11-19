import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 998244353

def modinv(a, m=MOD):
    # Fermat's little theorem for modular inverse since MOD is prime
    return pow(a, m-2, m)

t = int(input())
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
    adj = [[] for __ in range(n+1)]
    for __ in range(n-1):
        u,v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    # Precompute for each vertex:
    # P_fall[i] = p_i/q_i mod M
    # P_stay[i] = 1 - P_fall[i] mod M
    P_fall = [0]*(n+1)
    P_stay = [0]*(n+1)
    for i in range(1,n+1):
        P_fall[i] = p[i]*inv_q[i] % MOD
        P_stay[i] = (1 - P_fall[i]) % MOD

    # We want E = expected number of unordered pairs of distinct leaves in the resulting forest.
    # A vertex v is a leaf in the forest if:
    # 1) v did not fall
    # 2) Exactly one of its neighbors did not fall (degree in forest = 1)
    #
    # Let X_v = indicator that v is a leaf in the forest.
    # We want E = E[sum_{u<v} X_u * X_v] = sum_{u<v} E[X_u * X_v]
    #
    # Since X_v depends on v and its neighbors, and the falling events are independent,
    # we can compute E[X_v] and E[X_u * X_v] for edges (u,v).
    #
    # Note:
    # If u and v are not connected, X_u and X_v depend on disjoint sets of vertices,
    # so they are independent => E[X_u X_v] = E[X_u]*E[X_v].
    #
    # So:
    # E = sum_{u<v} E[X_u]*E[X_v] + sum_{(u,v) in edges} (E[X_u X_v] - E[X_u]*E[X_v])
    #
    # We can compute sum_{u<v} E[X_u]*E[X_v] = ( (sum E[X_v])^2 - sum E[X_v]^2 ) / 2
    #
    # Then add the correction for edges.

    # Compute E[X_v]:
    # X_v = 1 if v not fallen and exactly one neighbor not fallen
    # Probability:
    # P(X_v=1) = P_stay[v] * sum_{u in N(v)} P_stay[u] * product_{w in N(v), w!=u} P_fall[w]
    #
    # To compute efficiently:
    # prod_all = product_{w in N(v)} P_fall[w]
    # For each neighbor u:
    # term = P_stay[u] * (prod_all * inv(P_fall[u])) mod M
    # sum over neighbors u
    # multiply by P_stay[v]

    E_X = [0]*(n+1)
    for v in range(1,n+1):
        deg = len(adj[v])
        if deg == 0:
            # isolated vertex (only if n=1)
            # leaf requires degree 1, so E[X_v]=0
            E_X[v] = 0
            continue
        prod_all = 1
        for w in adj[v]:
            prod_all = (prod_all * P_fall[w]) % MOD
        s = 0
        for u in adj[v]:
            # inv P_fall[u]
            inv_pf = modinv(P_fall[u])
            val = P_stay[u] * (prod_all * inv_pf % MOD) % MOD
            s = (s + val) % MOD
        E_X[v] = P_stay[v] * s % MOD

    sum_E_X = 0
    sum_E_X2 = 0
    for v in range(1,n+1):
        sum_E_X = (sum_E_X + E_X[v]) % MOD
        sum_E_X2 = (sum_E_X2 + E_X[v]*E_X[v]) % MOD

    base = (sum_E_X * sum_E_X - sum_E_X2) % MOD
    base = base * modinv(2) % MOD

    # Now compute correction for edges:
    # For each edge (u,v), compute E[X_u X_v] - E[X_u]*E[X_v]
    #
    # Compute E[X_u X_v]:
    # X_u=1 means:
    # u not fallen
    # exactly one neighbor of u not fallen
    # X_v=1 means:
    # v not fallen
    # exactly one neighbor of v not fallen
    #
    # Since u and v are neighbors, their leaf conditions are coupled.
    #
    # Let's analyze:
    #
    # For X_u=1:
    # u not fallen
    # exactly one neighbor not fallen
    # neighbors of u: adj[u]
    #
    # For X_v=1:
    # v not fallen
    # exactly one neighbor not fallen
    # neighbors of v: adj[v]
    #
    # Since u and v are neighbors, they appear in each other's neighbor sets.
    #
    # Let:
    # A = set of neighbors of u except v
    # B = set of neighbors of v except u
    #
    # For X_u=1:
    # u not fallen
    # exactly one neighbor not fallen => either v is the only neighbor not fallen, or exactly one in A is not fallen and v fallen
    #
    # Similarly for X_v=1:
    # v not fallen
    # exactly one neighbor not fallen => either u is the only neighbor not fallen, or exactly one in B is not fallen and u fallen
    #
    # But since both u and v must be not fallen for X_u X_v=1, the cases where u or v fallen are impossible.
    #
    # So for X_u=1 and X_v=1 simultaneously:
    # u not fallen, v not fallen
    # For u: exactly one neighbor not fallen
    # For v: exactly one neighbor not fallen
    #
    # Neighbors of u: v + A
    # Neighbors of v: u + B
    #
    # Since u and v are not fallen, neighbors not fallen count includes each other.
    #
    # So for u:
    # neighbors not fallen count = 1 (v) + number of neighbors in A not fallen
    # For u to be leaf: neighbors not fallen count = 1 => number of neighbors in A not fallen = 0
    #
    # For v:
    # neighbors not fallen count = 1 (u) + number of neighbors in B not fallen
    # For v to be leaf: neighbors not fallen count = 1 => number of neighbors in B not fallen = 0
    #
    # So:
    # u and v not fallen
    # all neighbors in A fallen
    # all neighbors in B fallen
    #
    # Probability:
    # P_stay[u] * P_stay[v] *
    # product_{w in A} P_fall[w] *
    # product_{w in B} P_fall[w]
    #
    # This is E[X_u X_v].
    #
    # We already have E[X_u] and E[X_v].
    #
    # So correction = E[X_u X_v] - E[X_u]*E[X_v]

    # Precompute products for neighbors sets for each vertex to speed up:
    # For each vertex v, precompute:
    # prod_fall_neighbors[v] = product of P_fall[w] for w in adj[v]

    prod_fall_neighbors = [1]*(n+1)
    for v in range(1,n+1):
        pf = 1
        for w in adj[v]:
            pf = (pf * P_fall[w]) % MOD
        prod_fall_neighbors[v] = pf

    ans = base
    for u in range(1,n+1):
        for v in adj[u]:
            if u < v:
                # A = neighbors of u except v
                # B = neighbors of v except u
                # product over A
                prod_A = prod_fall_neighbors[u] * modinv(P_fall[v]) % MOD
                prod_B = prod_fall_neighbors[v] * modinv(P_fall[u]) % MOD
                val = P_stay[u] * P_stay[v] % MOD
                val = val * prod_A % MOD
                val = val * prod_B % MOD
                corr = (val - E_X[u]*E_X[v]) % MOD
                ans = (ans + corr) % MOD

    print(ans)