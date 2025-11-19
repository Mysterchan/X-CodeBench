def solve():
    n = int(input())
    if n == 1:
        print(-1)
        return
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    
    max_size = -1
    
    # Try each vertex as a potential degree-4 node
    for root in range(1, n + 1):
        # DFS to compute maximum alkane size in each subtree
        def dfs(u, parent):
            # Returns maximum alkane size rooted at u (u can be degree 1 or 4)
            # Returns -1 if no valid alkane exists
            
            children = [v for v in adj[u] if v != parent]
            
            if len(children) == 0:
                # Leaf node - valid alkane of size 1 (degree 1)
                return 1
            
            # Compute max alkane size for each child subtree
            child_sizes = []
            for child in children:
                size = dfs(child, u)
                if size > 0:
                    child_sizes.append(size)
            
            # Option 1: u is degree 1 (only if u is leaf)
            if len(children) == 0:
                return 1
            
            # Option 2: u is degree 4 (needs exactly 4 children)
            if len(child_sizes) >= 4:
                # Take the 4 largest valid child subtrees
                child_sizes.sort(reverse=True)
                total = 1 + sum(child_sizes[:4])
                return total
            
            return -1
        
        # Compute alkane rooted at 'root'
        size = dfs(root, -1)
        if size > 1:  # Must have at least one degree-4 vertex
            max_size = max(max_size, size)
    
    print(max_size)

solve()