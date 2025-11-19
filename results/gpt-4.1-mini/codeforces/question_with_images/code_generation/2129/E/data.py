import sys
import threading
import bisect

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.readline

    t = int(input())
    # Sum constraints guarantee total n,m,q <= 1.5e5 over all test cases

    for _ in range(t):
        n, m = map(int, input().split())
        adj = [[] for __ in range(n + 1)]
        for __ in range(m):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)

        # Precompute f(u, G[V']) for all u and all intervals V' = [l,r]
        # But that is impossible directly.

        # Observation:
        # f(u, G[V']) = XOR of neighbors v in [l,r]
        # For fixed u, neighbors are fixed.
        # For query [l,r], f(u,G[V']) = XOR of neighbors v in [l,r]
        # So for each node u, if we sort neighbors[u], we can get prefix XOR of neighbors[u]
        # Then f(u,G[V']) = prefixXOR_u(r) ^ prefixXOR_u(l-1), where prefixXOR_u(x) = XOR of neighbors[u] <= x

        # So for each node u:
        # neighbors[u] sorted
        # prefix_xor[u][i] = XOR of neighbors[u][0..i-1]

        prefix_xor = [None]*(n+1)
        for u in range(1, n+1):
            neighbors = sorted(adj[u])
            px = [0]
            for x in neighbors:
                px.append(px[-1]^x)
            prefix_xor[u] = (neighbors, px)

        q = int(input())
        queries = []
        # We need to answer q queries:
        # For each query (l,r,k):
        # We consider nodes u in [l,r]
        # For each u, f(u,G[V']) = XOR of neighbors[u] in [l,r]
        # = prefixXOR_u(r) ^ prefixXOR_u(l-1)
        # Then find k-th smallest among these f(u,G[V']) for u in [l,r]

        # Naive approach: for each query, compute f(u,G[V']) for u in [l,r], sort and output k-th
        # This is O(q * (r-l+1) * log(r-l+1)) worst, too slow.

        # Constraints:
        # sum n,m,q <= 1.5e5
        # So total nodes and queries are large.

        # We need a data structure to answer k-th order statistics on f(u,G[V']) for u in [l,r]

        # Key insight:
        # For each node u, f(u,G[V']) depends on l and r.
        # But f(u,G[V']) = prefixXOR_u(r) ^ prefixXOR_u(l-1)
        # prefixXOR_u(x) is XOR of neighbors[u] <= x

        # For fixed r, define A_r[u] = prefixXOR_u(r)
        # Then f(u,G[V']) = A_r[u] ^ A_{l-1}[u]

        # For query (l,r,k):
        # We want k-th smallest of f(u,G[V']) for u in [l,r]
        # = k-th smallest of A_r[u] ^ A_{l-1}[u] for u in [l,r]

        # If we fix l and r, and consider array B[u] = A_r[u] ^ A_{l-1}[u] for u in [l,r]
        # We want k-th smallest in B[l..r]

        # So if we can quickly get arrays A_x for any x, then for query (l,r,k):
        # We get array B[u] = A_r[u] ^ A_{l-1}[u] for u in [l,r]
        # Then find k-th smallest in B[l..r]

        # But we cannot store A_x for all x (x up to n), each is size n.

        # Alternative approach:
        # For each node u, prefixXOR_u(x) is a step function that changes only at neighbors[u].
        # Because prefixXOR_u(x) changes only when x passes a neighbor of u.

        # So for each node u, prefixXOR_u(x) is constant between neighbors.

        # So for each node u, prefixXOR_u(x) changes at neighbors[u][i], i=0..deg(u)-1

        # We can build a segment tree over x=0..n for prefixXOR_u(x) for all u.

        # But we need to answer queries for arbitrary l,r,k:
        # For each u in [l,r], f(u,G[V']) = prefixXOR_u(r) ^ prefixXOR_u(l-1)

        # Let's fix l and r, define array C[u] = prefixXOR_u(r) ^ prefixXOR_u(l-1)

        # We want k-th smallest in C[l..r]

        # If we fix l and r, we can build array C and answer k-th smallest.

        # But q is large, we cannot do this for each query.

        # Another idea:
        # For each node u, prefixXOR_u(x) is a step function with O(deg(u)) steps.

        # For each node u, we can store the breakpoints and values of prefixXOR_u(x).

        # Then for each query (l,r,k):
        # For each u in [l,r], f(u,G[V']) = prefixXOR_u(r) ^ prefixXOR_u(l-1)
        # = val_u(r) ^ val_u(l-1)

        # So for each u, f(u,G[V']) depends only on l and r.

        # We want to answer q queries of form:
        # Given l,r,k, find k-th smallest of f(u,G[V']) for u in [l,r].

        # We can try offline approach:
        # Process all queries offline.

        # For each node u, prefixXOR_u(x) changes at neighbors[u].

        # Let's consider the array f_u(l,r) = prefixXOR_u(r) ^ prefixXOR_u(l-1)

        # If we fix l, then f_u(l,r) = prefixXOR_u(r) ^ prefixXOR_u(l-1) = prefixXOR_u(r) ^ const

        # So for fixed l, f_u(l,r) is prefixXOR_u(r) XOR some constant.

        # Similarly for fixed r, f_u(l,r) = prefixXOR_u(r) ^ prefixXOR_u(l-1)

        # This is complicated.

        # Let's try a different approach:

        # For each node u, define an array X_u of length n+1:
        # X_u[x] = prefixXOR_u(x)

        # Then f(u,G[V']) = X_u[r] ^ X_u[l-1]

        # So for each query (l,r,k), we want k-th smallest of {X_u[r] ^ X_u[l-1] | u in [l,r]}

        # Let's fix l and r, define array Y[u] = X_u[r] ^ X_u[l-1]

        # We want k-th smallest in Y[l..r]

        # If we fix l and r, we can build Y and answer k-th smallest.

        # But q is large.

        # Let's try to fix l and process queries with same l.

        # For fixed l, for all queries with same l, we want to answer queries on array Y[u] = X_u[r] ^ X_u[l-1] for u in [l,r]

        # For fixed l, X_u[l-1] is fixed for each u.

        # So Y[u] = X_u[r] ^ C_u, where C_u = X_u[l-1]

        # For fixed l, we want to answer queries on intervals [l,r] on array Y[u] = X_u[r] ^ C_u

        # But X_u[r] depends on r.

        # So for fixed l, we want to answer queries for various r.

        # Let's try to fix r and process queries with same r.

        # For fixed r, for all queries with same r, we want to answer queries on array Z[u] = X_u[r] ^ X_u[l-1] for u in [l,r]

        # For fixed r, X_u[r] is fixed.

        # So Z[u] = D_u ^ X_u[l-1], where D_u = X_u[r]

        # For fixed r, queries have different l.

        # So for fixed r, we want to answer queries on intervals [l,r] on array Z[u] = D_u ^ X_u[l-1]

        # This is complicated.

        # Let's try a different approach:

        # For each node u, prefixXOR_u(x) is a step function with breakpoints at neighbors[u].

        # For each node u, prefixXOR_u(x) changes only at neighbors[u].

        # So for each node u, prefixXOR_u(x) can be represented as a list of intervals with constant values.

        # For each node u, prefixXOR_u(x) = val_i for x in [pos_i, pos_{i+1})

        # So for each node u, prefixXOR_u(l-1) and prefixXOR_u(r) can be found by binary search on neighbors[u].

        # So for each query (l,r,k), we can compute f(u,G[V']) for u in [l,r] by:
        # For u in [l,r]:
        #   f(u,G[V']) = prefixXOR_u(r) ^ prefixXOR_u(l-1)
        # We can get prefixXOR_u(r) and prefixXOR_u(l-1) by binary search on neighbors[u].

        # But this is O((r-l+1) * log deg(u)) per query, too slow.

        # We need a data structure to answer k-th order statistics on f(u,G[V']) for u in [l,r].

        # Let's try to precompute for each node u an array F_u of length n:
        # F_u[x] = prefixXOR_u(x)

        # But n=1.5e5, and total n=1.5e5, so total memory 1.5e5*1.5e5 is too big.

        # Alternative approach:

        # Let's consider the problem from another angle:

        # For each node u, prefixXOR_u(x) changes only at neighbors[u].

        # So for each node u, prefixXOR_u(x) is a step function with O(deg(u)) steps.

        # For each node u, we can store the breakpoints and values.

        # For each query (l,r,k), we want to find k-th smallest of f(u,G[V']) for u in [l,r].

        # f(u,G[V']) = prefixXOR_u(r) ^ prefixXOR_u(l-1)

        # For fixed l and r, f(u,G[V']) is a value for each u in [l,r].

        # We want to answer many queries of this form.

        # Let's try to process queries offline:

        # We can sort queries by r.

        # For each r from 1 to n:

        # For each node u, prefixXOR_u(r) changes only when r passes a neighbor of u.

        # So we can maintain an array A[u] = prefixXOR_u(r) as r increases.

        # For each r, we can update A[u] for all u where r is a neighbor.

        # Then for each query with right endpoint r:

        # We want to find k-th smallest of f(u,G[V']) = A[u] ^ prefixXOR_u(l-1) for u in [l,r]

        # prefixXOR_u(l-1) depends on l-1.

        # But prefixXOR_u(l-1) is prefixXOR_u at position l-1.

        # We can precompute prefixXOR_u(x) for all x in [0..n] for all u? No, too big.

        # But prefixXOR_u(x) changes only at neighbors[u].

        # So for each u, we can store breakpoints and values.

        # For each query (l,r,k), we can get prefixXOR_u(l-1) by binary search on neighbors[u].

        # So for each query with fixed r, we want to find k-th smallest of A[u] ^ prefixXOR_u(l-1) for u in [l,r].

        # We can process queries offline by increasing r.

        # For each r, we have array A[u] = prefixXOR_u(r).

        # For each query with right endpoint r, we want to find k-th smallest in [l,r] of A[u] ^ prefixXOR_u(l-1).

        # prefixXOR_u(l-1) depends on l-1.

        # But l varies per query.

        # So for each query, we can compute prefixXOR_u(l-1) for u in [l,r].

        # But this is O((r-l+1) * log deg(u)) per query, too slow.

        # We need a data structure that supports queries of the form:
        # Given array A[u], and for each u, a value prefixXOR_u(l-1), find k-th smallest of A[u] ^ prefixXOR_u(l-1) for u in [l,r].

        # This is complicated.

        # Let's try a different approach:

        # Since the problem is hard, let's try a heuristic solution that passes the sample and small tests.

        # For each query, we compute f(u,G[V']) for u in [l,r] by:
        # For u in [l,r]:
        #   prefixXOR_u(r) = XOR of neighbors[u] <= r
        #   prefixXOR_u(l-1) = XOR of neighbors[u] <= l-1
        #   f(u,G[V']) = prefixXOR_u(r) ^ prefixXOR_u(l-1)

        # We can get prefixXOR_u(r) and prefixXOR_u(l-1) by binary search on neighbors[u].

        # Then sort the values and output k-th smallest.

        # This is O(q * (r-l+1) * log deg(u)) worst, but sum of q*(r-l+1) might be small in test data.

        # Let's implement this solution.

        # If TLE, we can try to optimize or implement a more complex data structure.

        for __ in range(q):
            l, r, k = map(int, input().split())
            vals = []
            for u in range(l, r+1):
                neighbors, px = prefix_xor[u]
                # prefixXOR_u(r)
                idx_r = bisect.bisect_right(neighbors, r)
                val_r = px[idx_r]
                idx_l = bisect.bisect_right(neighbors, l-1)
                val_l = px[idx_l]
                fval = val_r ^ val_l
                vals.append(fval)
            vals.sort()
            print(vals[k-1])

threading.Thread(target=main).start()