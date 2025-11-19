import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    C = [list(map(int, input().split())) for _ in range(N)]

    # Floyd-Warshall to get shortest paths between all pairs
    for k in range(N):
        Ck = C[k]
        for i in range(N):
            Ci = C[i]
            ik = Ci[k]
            for j in range(N):
                val = ik + Ck[j]
                if val < Ci[j]:
                    Ci[j] = val

    Q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(Q)]

    # We want to find the minimum cost of a connected subgraph containing:
    # vertices {1,...,K, s_i, t_i}
    # The graph is complete with edge weights = shortest paths after Floyd-Warshall.

    # Key observations:
    # - K ≤ 8 (small)
    # - s_i, t_i ∈ [K+1, N]
    # - We want to find a minimum Steiner tree on the terminals {1..K, s_i, t_i}
    #   in a complete graph with weights = shortest paths.
    #
    # Since K ≤ 8, total terminals per query = K + 2 ≤ 10.
    #
    # We can precompute a DP for Steiner tree on the fixed terminals {1..K} plus any two terminals from [K+1..N].
    #
    # But s_i and t_i vary per query, so we must handle queries efficiently.
    #
    # Approach:
    # 1) Precompute shortest paths between all nodes (done).
    # 2) We have a fixed set of K terminals: 0..K-1 (0-based indexing for terminals 1..K)
    # 3) For each query, terminals = {1..K} + {s_i, t_i}
    #
    # We can do the following:
    # - Precompute DP for Steiner tree on terminals {1..K} only.
    # - For each query, add s_i and t_i as terminals and compute Steiner tree including them.
    #
    # But that would be expensive per query.
    #
    # Instead, we do a DP over subsets of terminals including s_i and t_i as additional terminals.
    #
    # Since Q can be up to 5000, we need a fast query.
    #
    # Idea:
    # - Fix the K terminals as indices 0..K-1.
    # - For each node v in [K..N-1], precompute the cost to connect v to any subset of terminals.
    # - Then for each query, terminals = {0..K-1} + s_i-1 + t_i-1
    #
    # We can do a DP over subsets of terminals (up to size K+2 ≤ 10).
    #
    # But we have many queries, so we want to precompute a structure to answer queries quickly.
    #
    # Let's do the following:
    #
    # We consider the terminals as:
    # - fixed terminals: 0..K-1
    # - variable terminals: s_i-1 and t_i-1
    #
    # We will build a graph G' with nodes = terminals + all other nodes.
    # The cost between any two nodes is shortest path cost.
    #
    # We want the minimum Steiner tree connecting terminals {0..K-1, s_i-1, t_i-1}.
    #
    # Since N=80, K ≤ 8, and Q=5000, we can do the following:
    #
    # Precompute a DP for Steiner tree on terminals {0..K-1} only:
    # dp[mask][v] = minimum cost to connect terminals in mask ending at node v
    #
    # Then for each query, we add s_i and t_i as terminals.
    #
    # We can do a modified DP for each query:
    # - The terminals are {0..K-1, s_i-1, t_i-1}
    # - We can run a Steiner tree DP on these terminals only.
    #
    # But that would be O(3^T * N) per query, too large.
    #
    # Alternative approach:
    #
    # Since the graph is complete with shortest path weights, the minimum Steiner tree is the minimum spanning tree (MST)
    # on the terminals with edge weights = shortest path distances.
    #
    # Because the graph is complete and metric (triangle inequality holds after Floyd-Warshall),
    # the minimum Steiner tree on terminals in a metric graph is the MST on the terminals.
    #
    # So the problem reduces to:
    # For each query, find MST on terminals {1..K, s_i, t_i} with edge weights = shortest path distances.
    #
    # This is much simpler and efficient.
    #
    # Steps:
    # - For each query:
    #   - terminals = [0..K-1] + [s_i-1, t_i-1]
    #   - Build a complete graph on these terminals with edge weights = C[u][v]
    #   - Compute MST cost on this small graph (size K+2 ≤ 10)
    #
    # This is O(Q * (K+2)^2) which is feasible.

    # Precompute terminal indices for fixed terminals
    fixed_terminals = list(range(K))

    # Process queries
    for s, t in queries:
        s -= 1
        t -= 1
        terminals = fixed_terminals + [s, t]
        m = len(terminals)
        # Build complete graph on terminals
        edges = []
        for i in range(m):
            for j in range(i+1, m):
                u = terminals[i]
                v = terminals[j]
                w = C[u][v]
                edges.append((w, i, j))
        # Kruskal MST
        edges.sort()
        parent = list(range(m))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(a,b):
            a=find(a)
            b=find(b)
            if a!=b:
                parent[b]=a
                return True
            return False
        mst_cost = 0
        count = 0
        for w,u,v in edges:
            if union(u,v):
                mst_cost += w
                count += 1
                if count == m-1:
                    break
        print(mst_cost)

if __name__ == "__main__":
    main()