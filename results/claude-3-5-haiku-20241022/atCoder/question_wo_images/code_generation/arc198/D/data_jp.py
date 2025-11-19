from collections import defaultdict, deque

def solve():
    N = int(input())
    
    # Build adjacency list for the tree
    adj = defaultdict(list)
    for _ in range(N - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Read matrix A
    A = []
    for _ in range(N):
        row = input().strip()
        A.append([int(c) for c in row])
    
    # Find path between two nodes in tree
    def find_path(start, end):
        if start == end:
            return [start]
        
        visited = set()
        parent = {}
        queue = deque([start])
        visited.add(start)
        
        while queue:
            node = queue.popleft()
            if node == end:
                path = []
                current = end
                while current in parent:
                    path.append(current)
                    current = parent[current]
                path.append(start)
                return path[::-1]
            
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = node
                    queue.append(neighbor)
        
        return []
    
    # Check if (i, j) is a palindrome pair for given x
    def is_palindrome_pair(x, i, j):
        path = find_path(i, j)
        n = len(path)
        for k in range(n):
            if x[path[k] - 1] != x[path[n - 1 - k] - 1]:
                return False
        return True
    
    # Check if assignment x is valid (satisfies A constraints)
    def is_valid(x):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if A[i - 1][j - 1] == 1:
                    if not is_palindrome_pair(x, i, j):
                        return False
        return True
    
    # Count palindrome pairs for valid x
    def count_palindrome_pairs(x):
        count = 0
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if is_palindrome_pair(x, i, j):
                    count += 1
        return count
    
    # Generate all possible assignments (brute force for small N)
    # For larger N, we need smarter approach
    min_score = 10**100
    
    # Try all possible colorings with limited colors
    max_colors = N
    
    def generate_assignments(pos, current_x):
        nonlocal min_score
        
        if pos == N:
            if is_valid(current_x):
                score = count_palindrome_pairs(current_x)
                min_score = min(min_score, score)
            return
        
        # Prune: try colors up to max_colors
        for color in range(1, min(max_colors + 1, pos + 2)):
            current_x.append(color)
            generate_assignments(pos + 1, current_x)
            current_x.pop()
    
    generate_assignments(0, [])
    
    print(min_score)

solve()