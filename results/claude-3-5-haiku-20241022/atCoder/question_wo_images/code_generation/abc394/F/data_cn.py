import sys
from collections import defaultdict, deque

def solve():
    N = int(input())
    
    if N == 1:
        print(-1)
        return
    
    adj = defaultdict(list)
    for _ in range(N - 1):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    
    degrees = [len(adj[i]) for i in range(N + 1)]
    
    # Check if any vertex has degree 4
    has_degree_4 = any(degrees[i] == 4 for i in range(1, N + 1))
    if not has_degree_4:
        print(-1)
        return
    
    max_size = 0
    
    # Try each vertex with degree >= 4 as a potential center
    for root in range(1, N + 1):
        if degrees[root] < 4:
            continue
        
        # BFS to find largest alkane subgraph rooted at this vertex
        # We'll try to include vertices greedily
        result = find_alkane(root, adj, N)
        max_size = max(max_size, result)
    
    print(max_size if max_size > 0 else -1)

def find_alkane(root, adj, N):
    # Try to build an alkane with vertices having degree 1 or 4
    # Use BFS from root
    visited = set([root])
    queue = deque([root])
    included = {root}
    edges_in_subgraph = []
    
    # For each vertex, track how many edges we've included
    degree_in_subgraph = defaultdict(int)
    
    # Greedy approach: include all neighbors, then expand
    for neighbor in adj[root]:
        visited.add(neighbor)
        queue.append(neighbor)
    
    # Build subgraph using DFS/BFS strategy
    # We want to maximize vertices while keeping degrees as 1 or 4
    best = try_build_alkane(root, adj, N)
    return best

def try_build_alkane(start, adj, N):
    # Try all possible subsets using pruning
    max_vertices = 0
    
    # Use DFS to explore subgraphs
    def dfs(vertices, edges_set):
        nonlocal max_vertices
        
        # Check if current subgraph is valid alkane
        if is_valid_alkane(vertices, edges_set, adj):
            max_vertices = max(max_vertices, len(vertices))
        
        # Try adding more vertices
        candidates = set()
        for v in vertices:
            for u in adj[v]:
                if u not in vertices:
                    candidates.add(u)
        
        for candidate in candidates:
            new_edges = set()
            for v in vertices:
                if candidate in adj[v]:
                    new_edges.add((min(v, candidate), max(v, candidate)))
            
            new_vertices = vertices | {candidate}
            new_edges_set = edges_set | new_edges
            
            dfs(new_vertices, new_edges_set)
    
    # Start with just the root
    dfs({start}, set())
    return max_vertices

def is_valid_alkane(vertices, edges_set, adj):
    if len(vertices) == 0:
        return False
    
    # Check connectivity
    if len(edges_set) != len(vertices) - 1:
        return False
    
    # Check degrees
    degree = defaultdict(int)
    for u, v in edges_set:
        degree[u] += 1
        degree[v] += 1
    
    has_degree_4 = False
    for v in vertices:
        d = degree[v]
        if d != 1 and d != 4:
            return False
        if d == 4:
            has_degree_4 = True
    
    return has_degree_4

# Optimized solution
def solve_optimized():
    N = int(input())
    
    if N == 1:
        print(-1)
        return
    
    adj = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    
    degrees = [len(adj[i]) for i in range(N + 1)]
    
    # Check if any vertex has degree 4
    has_degree_4 = any(degrees[i] == 4 for i in range(1, N + 1))
    if not has_degree_4:
        print(-1)
        return
    
    max_size = 0
    
    # For each vertex with degree 4, compute max alkane
    for root in range(1, N + 1):
        if degrees[root] != 4:
            continue
        
        # Compute size recursively
        size = 1  # root itself
        for neighbor in adj[root]:
            size += dfs_subtree(neighbor, root, adj)
        
        max_size = max(max_size, size)
    
    print(max_size)

def dfs_subtree(node, parent, adj):
    # Count nodes in subtree that can be part of alkane
    total = 1
    for child in adj[node]:
        if child != parent:
            total += dfs_subtree(child, node, adj)
    return total

solve_optimized()