from collections import defaultdict, deque

def solve():
    N = int(input())
    
    if N == 1:
        print(-1)
        return
    
    graph = defaultdict(list)
    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    degrees = {i: len(graph[i]) for i in range(1, N + 1)}
    
    # Check if any vertex has degree 4 or more
    has_degree_4_or_more = any(deg >= 4 for deg in degrees.values())
    
    if not has_degree_4_or_more:
        print(-1)
        return
    
    max_vertices = 0
    
    # Try each vertex with degree >= 4 as the potential degree-4 vertex in alkane
    for root in range(1, N + 1):
        if degrees[root] < 4:
            continue
        
        # BFS to find largest alkane subgraph rooted at this vertex
        # We'll try all possible ways to select branches
        neighbors = graph[root]
        
        # For each neighbor, compute the size of subtree we can take
        branch_sizes = []
        for neighbor in neighbors:
            # BFS from neighbor, avoiding root
            size = compute_alkane_branch_size(graph, neighbor, root, degrees)
            branch_sizes.append(size)
        
        # We need to select branches such that total is exactly 4 branches
        # If we have >= 4 neighbors, select the 4 largest
        if len(branch_sizes) >= 4:
            branch_sizes.sort(reverse=True)
            total = 1 + sum(branch_sizes[:4])
            max_vertices = max(max_vertices, total)
    
    print(max_vertices if max_vertices > 0 else -1)

def compute_alkane_branch_size(graph, start, parent, degrees):
    """Compute size of alkane-valid subtree starting from 'start', not going back to 'parent'"""
    visited = {parent}
    queue = deque([start])
    visited.add(start)
    size = 1
    
    while queue:
        node = queue.popleft()
        degree_in_subtree = 1  # edge to parent
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                degree_in_subtree += 1
        
        # In alkane, degree must be 1 or 4
        # If node has only connection to parent, degree is 1 (leaf) - OK
        # If node is internal, we need to check
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                # Check if we can include this neighbor
                # Simple greedy: include all possible nodes
                visited.add(neighbor)
                queue.append(neighbor)
                size += 1
    
    return size

# More careful approach
def solve():
    N = int(input())
    
    if N == 1:
        print(-1)
        return
    
    graph = defaultdict(list)
    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    degrees = {i: len(graph[i]) for i in range(1, N + 1)}
    
    max_vertices = 0
    
    # Try each vertex as root (degree-4 vertex)
    for root in range(1, N + 1):
        if degrees[root] < 4:
            continue
        
        # Compute valid alkane size for each branch from root
        branch_info = []
        for neighbor in graph[root]:
            size = dfs_branch(graph, neighbor, root)
            branch_info.append(size)
        
        if len(branch_info) >= 4:
            branch_info.sort(reverse=True)
            total = 1 + sum(branch_info[:4])
            max_vertices = max(max_vertices, total)
    
    print(max_vertices if max_vertices > 0 else -1)

def dfs_branch(graph, node, parent):
    """DFS to find size of valid alkane branch"""
    children = [child for child in graph[node] if child != parent]
    
    if len(children) == 0:
        return 1
    elif len(children) == 1:
        return 1 + dfs_branch(graph, children[0], node)
    elif len(children) >= 4:
        sizes = [dfs_branch(graph, child, node) for child in children]
        sizes.sort(reverse=True)
        return 1 + sum(sizes[:4])
    else:
        return 0

solve()