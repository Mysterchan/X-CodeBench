import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(10**7)
    t = int(sys.stdin.readline())
    
    # We want to find a maximum subgraph with degree <= 2 for each vertex.
    # Such a subgraph is a collection of paths and cycles.
    # The problem reduces to finding a maximum subset of edges such that degree[v] <= 2.
    #
    # Constraints:
    # - n <= 30
    # - m up to n(n-1)/2
    # - Each vertex belongs to at most 5 simple cycles.
    #
    # This special property implies the graph is "almost" a cactus-like structure,
    # which limits the complexity of cycles.
    #
    # Approach:
    # We want to find a maximum edge subset with degree constraints.
    #
    # This is a maximum degree-2 subgraph problem.
    #
    # We can model this as a maximum matching-like problem with degree constraints.
    #
    # Since degree <= 2, the problem can be solved by a maximum matching in a line graph,
    # but that is complicated.
    #
    # Alternative approach:
    # Use backtracking with pruning and bitmasks.
    #
    # Since n <= 30 and sum n^2 <= 900, we can try a backtracking with pruning.
    #
    # Another approach:
    # Since degree <= 2, the subgraph is a union of vertex-disjoint paths and cycles.
    #
    # We can try to find a maximum matching in the line graph of G, but that is complicated.
    #
    # Let's try a backtracking with pruning:
    # - Keep track of degrees of vertices.
    # - Try to include or exclude edges in order.
    # - Prune if degree[v] > 2.
    #
    # To speed up:
    # - Sort edges by degree of endpoints (heuristic).
    # - Use memoization with bitmask of edges or degrees? Too large.
    #
    # Since each vertex belongs to at most 5 simple cycles, the graph is sparse in cycles.
    #
    # Another idea:
    # The problem is equivalent to finding a maximum 2-matching.
    #
    # Maximum 2-matching can be solved by reduction to maximum matching in an auxiliary graph.
    #
    # Let's implement a maximum 2-matching algorithm using Edmonds' blossom algorithm.
    #
    # But blossom algorithm is complicated to implement here.
    #
    # Alternative:
    # Since degree <= 2, the subgraph is a union of vertex-disjoint paths and cycles.
    #
    # Maximum 2-matching problem can be solved by a maximum matching in a certain auxiliary graph.
    #
    # Let's implement a maximum 2-matching using a reduction to maximum matching in a bipartite graph:
    #
    # But the graph is not bipartite.
    #
    # Since n is small, we can try a maximum weighted matching in general graph.
    #
    # Let's implement Edmonds' blossom algorithm for maximum matching.
    #
    # Then, maximum 2-matching can be found by solving a maximum matching in a certain auxiliary graph:
    #
    # Actually, maximum 2-matching is a classical problem:
    # It can be solved by a maximum matching in a graph where each vertex is split into two copies,
    # and edges connect these copies.
    #
    # But since the problem is complex, let's implement a maximum matching in general graph (Edmonds' blossom algorithm)
    # and then use it to find maximum 2-matching.
    #
    # However, maximum 2-matching is more general than maximum matching.
    #
    # Another approach:
    # Since degree <= 2, the subgraph is a union of vertex-disjoint paths and cycles.
    #
    # The maximum 2-matching problem can be solved by a maximum matching in a line graph of G.
    #
    # But line graph can be large.
    #
    # Since n=30, m up to 435, we can try a maximum matching in general graph with Edmonds' algorithm.
    #
    # Let's implement Edmonds' blossom algorithm for maximum matching.
    #
    # Then, maximum 2-matching can be found by solving a maximum matching in a certain auxiliary graph:
    #
    # Actually, maximum 2-matching is a maximum matching in the line graph of G.
    #
    # The line graph L(G) has a vertex for each edge of G.
    # Two vertices in L(G) are adjacent if the corresponding edges in G share a vertex.
    #
    # A matching in L(G) corresponds to a set of edges in G with no two edges sharing a vertex.
    #
    # But we want degree <= 2, so edges can share vertices up to degree 2.
    #
    # So maximum 2-matching is a generalization of matching allowing degree up to 2.
    #
    # There is a polynomial algorithm for maximum 2-matching using blossom algorithm.
    #
    # Let's implement a maximum 2-matching algorithm using Edmonds' blossom algorithm.
    #
    # The algorithm:
    # - Construct a graph H from G by replacing each vertex v by two copies v1 and v2.
    # - For each edge (u,v) in G, add edges (u1,v1), (u1,v2), (u2,v1), (u2,v2) in H.
    # - Find maximum matching in H.
    # - The size of maximum 2-matching in G is half the size of maximum matching in H.
    #
    # But this quadruples the number of vertices, which is 60 vertices in H.
    #
    # 60 vertices is still manageable for Edmonds' algorithm.
    #
    # Let's implement Edmonds' blossom algorithm for maximum matching in general graph.
    #
    # Then build H and find maximum matching.
    #
    # Output the size of maximum 2-matching = number of edges in the maximum 2-matching.
    #
    # Note: The maximum 2-matching is the maximum subgraph with degree <= 2.
    #
    # Reference: https://en.wikipedia.org/wiki/2-matching
    
    # Implement Edmonds' blossom algorithm for maximum matching in general graph.
    
    class Edmonds:
        def __init__(self, n):
            self.n = n
            self.adj = [[] for _ in range(n)]
        
        def add_edge(self, u, v):
            self.adj[u].append(v)
            self.adj[v].append(u)
        
        def max_matching(self):
            n = self.n
            adj = self.adj
            match = [-1]*n
            base = list(range(n))
            p = [-1]*n
            q = []
            inq = [False]*n
            inbloom = [False]*n
            edgelabel = [0]*n
            
            def lca(a,b):
                used = [False]*n
                while True:
                    a = base[a]
                    used[a] = True
                    if match[a] == -1:
                        break
                    a = p[match[a]]
                while True:
                    b = base[b]
                    if used[b]:
                        return b
                    b = p[match[b]]
            
            def mark_bloom(a,b,l):
                while base[a] != l:
                    inbloom[base[a]] = inbloom[base[match[a]]] = True
                    p[a] = b
                    b = match[a]
                    a = p[b]
            
            def blossom(v):
                inq[:] = [False]*n
                p[:] = [-1]*n
                base[:] = list(range(n))
                q.clear()
                q.append(v)
                inq[v] = True
                while q:
                    u = q.pop(0)
                    for w in adj[u]:
                        if base[u] == base[w] or match[u] == w:
                            continue
                        if w == v or (match[w] != -1 and p[match[w]] != -1):
                            l = lca(u,w)
                            inbloom[:] = [False]*n
                            mark_bloom(u,w,l)
                            mark_bloom(w,u,l)
                            for i in range(n):
                                if inbloom[base[i]]:
                                    base[i] = l
                                    if not inq[i]:
                                        inq[i] = True
                                        q.append(i)
                        elif p[w] == -1:
                            p[w] = u
                            if match[w] == -1:
                                return w
                            w_ = match[w]
                            inq[w_] = True
                            q.append(w_)
                return -1
            
            res = 0
            for i in range(n):
                if match[i] == -1:
                    v = blossom(i)
                    if v != -1:
                        res += 1
                        while v != -1:
                            pv = p[v]
                            ppv = match[pv]
                            match[v] = pv
                            match[pv] = v
                            v = ppv
            return res, match
    
    input = sys.stdin.readline
    
    for _ in range(t):
        n,m = map(int,input().split())
        edges = []
        for __ in range(m):
            u,v = map(int,input().split())
            u -= 1
            v -= 1
            edges.append((u,v))
        
        # Build graph H with 2*n vertices: for each vertex v in G, create v0 and v1 in H
        # For each edge (u,v) in G, add edges between all pairs of copies:
        # (u0,v0), (u0,v1), (u1,v0), (u1,v1)
        
        H = Edmonds(2*n)
        for (u,v) in edges:
            H.add_edge(u*2, v*2)
            H.add_edge(u*2, v*2+1)
            H.add_edge(u*2+1, v*2)
            H.add_edge(u*2+1, v*2+1)
        
        max_match_size, match = H.max_matching()
        # max_match_size is number of matched edges in H
        # maximum 2-matching size in G is max_match_size // 2
        # because each edge in G corresponds to 4 edges in H, and matching in H picks edges corresponding to edges in G
        # The maximum 2-matching size is max_match_size // 2
        
        print(max_match_size // 2)

threading.Thread(target=main).start()