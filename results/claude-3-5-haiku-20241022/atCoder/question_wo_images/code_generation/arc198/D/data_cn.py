from collections import deque, defaultdict

def solve():
    N = int(input())
    
    # Build adjacency list
    adj = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Read matrix A
    A = []
    for _ in range(N):
        row = input().strip()
        A.append([int(c) for c in row])
    
    # Find path between two nodes
    def find_path(start, end):
        if start == end:
            return [start]
        parent = [-1] * (N + 1)
        visited = [False] * (N + 1)
        q = deque([start])
        visited[start] = True
        
        while q:
            u = q.popleft()
            if u == end:
                break
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    q.append(v)
        
        path = []
        curr = end
        while curr != -1:
            path.append(curr)
            curr = parent[curr]
        return path[::-1]
    
    # Check if assignment satisfies all A[i][j]=1 constraints
    def is_valid(x):
        for i in range(N):
            for j in range(N):
                if A[i][j] == 1:
                    path = find_path(i + 1, j + 1)
                    n = len(path)
                    for k in range(n):
                        if x[path[k] - 1] != x[path[n - 1 - k] - 1]:
                            return False
        return True
    
    # Count palindromic pairs
    def count_palindromic(x):
        count = 0
        for i in range(N):
            for j in range(N):
                path = find_path(i + 1, j + 1)
                n = len(path)
                is_palindrome = True
                for k in range(n):
                    if x[path[k] - 1] != x[path[n - 1 - k] - 1]:
                        is_palindrome = False
                        break
                if is_palindrome:
                    count += 1
        return count
    
    # Try different assignments
    min_score = float('inf')
    
    # Use DFS with constraint propagation
    def search(x, idx):
        nonlocal min_score
        
        if idx == N:
            if is_valid(x):
                score = count_palindromic(x)
                min_score = min(min_score, score)
            return
        
        # Try values 1 to N
        for val in range(1, N + 1):
            x[idx] = val
            search(x, idx + 1)
    
    x = [0] * N
    search(x, 0)
    
    print(min_score)

solve()