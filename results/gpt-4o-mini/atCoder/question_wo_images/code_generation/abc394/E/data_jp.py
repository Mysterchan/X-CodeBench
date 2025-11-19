def find_shortest_palindrome_paths(N, graph):
    # Initialize the distance array with infinity for each pair (i, j)
    dist = [[float('inf')] * N for _ in range(N)]
    
    # Fill the initial direct edges with their lengths
    for i in range(N):
        for j in range(N):
            if graph[i][j] != '-':
                dist[i][j] = 1  # Direct edge contributes a length of 1
    
    # Distance to itself is zero
    for i in range(N):
        dist[i][i] = 0
    
    # Floyd-Warshall algorithm to find all pairs shortest path with palindrome constraints
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][k] < float('inf') and dist[k][j] < float('inf'):
                    # We can reach j from i through k, we need to check if the path can form a palindrome
                    if (dist[i][k] + dist[k][j]) % 2 == 0:  # We can consider a palindrome-like connection
                        mid_length = (dist[i][k] + dist[k][j]) // 2
                        dist[i][j] = min(dist[i][j], mid_length * 2)
                    else:
                        mid_length = (dist[i][k] + dist[k][j]) // 2
                        dist[i][j] = min(dist[i][j], mid_length * 2 + 1)
    
    # Prepare output according to the format
    result = []
    for i in range(N):
        result.append(' '.join(str(dist[i][j]) if dist[i][j] != float('inf') else -1 for j in range(N)))
    
    return '\n'.join(result)

# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
graph = [list(data[i + 1]) for i in range(N)]

# Get the result and print it
output = find_shortest_palindrome_paths(N, graph)
print(output)