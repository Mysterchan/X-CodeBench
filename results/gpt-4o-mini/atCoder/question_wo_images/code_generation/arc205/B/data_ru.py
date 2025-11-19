def max_black_edges(N, M, edges):
    # Total edges in a complete graph with N vertices
    total_edges = N * (N - 1) // 2
    
    # If there are no black edges, all edges can be made black
    if M == 0:
        return total_edges
    
    # Count the number of black edges
    black_edges = M
    
    # Each operation can convert 3 edges to black, and we can do this for any triplet (a, b, c)
    # The maximum number of edges that can be black is the total edges minus the number of white edges
    # The number of white edges is total_edges - black_edges
    # Each operation can convert 3 white edges to black, but we can only do this if we have enough white edges
    # The maximum number of edges that can be black is total_edges
    
    # The maximum number of edges that can be black is total_edges
    return total_edges

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:M + 1]]

# Get the result
result = max_black_edges(N, M, edges)

# Print the result
print(result)