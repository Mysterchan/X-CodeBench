from collections import deque

def solve():
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(input().strip())
    
    # For each (i, j) pair, find shortest palindrome path
    result = [[0] * N for _ in range(N)]
    
    for start in range(N):
        for end in range(N):
            if start == end:
                result[start][end] = 0
            else:
                result[start][end] = bfs_palindrome(graph, N, start, end)
    
    # Output
    for row in result:
        print(' '.join(map(str, row)))

def bfs_palindrome(graph, N, start, end):
    # BFS to find shortest palindrome path from start to end
    # State: (current_node, path_string)
    # We need to track the path string to check if it's a palindrome
    
    queue = deque([(start, "")])
    visited = {}  # (node, path_string) -> min_length
    visited[(start, "")] = 0
    
    max_length = N * N  # Reasonable upper bound
    
    while queue:
        curr, path = queue.popleft()
        
        if len(path) > max_length:
            continue
        
        # Check if we reached the end with a palindrome
        if curr == end and path == path[::-1]:
            return len(path)
        
        # Try all outgoing edges
        for next_node in range(N):
            if graph[curr][next_node] != '-':
                edge_label = graph[curr][next_node]
                new_path = path + edge_label
                
                # Pruning: if new_path can't possibly be a palindrome, skip
                # Check if new_path is a prefix of some palindrome
                if not can_be_palindrome_prefix(new_path):
                    continue
                
                state = (next_node, new_path)
                if state not in visited or visited[state] > len(new_path):
                    visited[state] = len(new_path)
                    queue.append((next_node, new_path))
    
    return -1

def can_be_palindrome_prefix(s):
    # Check if s can be a prefix of a palindrome
    # This is always true, so we need a better pruning strategy
    # For efficiency, we limit path length
    return len(s) <= 100

solve()