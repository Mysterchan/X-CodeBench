def max_black_edges(N, M, edges):
    # Total edges in a complete graph with N vertices
    total_edges = N * (N - 1) // 2
    
    # If there are no black edges, all edges are white
    if M == 0:
        return total_edges
    
    # Count the number of edges that can be turned black
    # Each operation can turn 3 edges black if we choose (a, b, c) correctly
    # The maximum number of edges that can be black is total_edges - (total_edges - M)
    # which is total_edges + M (since we can turn M edges black)
    
    # The maximum number of black edges we can achieve
    max_black = total_edges + M
    
    # However, we cannot exceed the total number of edges
    return min(max_black, total_edges)

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