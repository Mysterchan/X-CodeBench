def max_black_edges(N, M, edges):
    # Total edges in a complete graph with N vertices
    total_edges = N * (N - 1) // 2
    
    # Count the number of black edges
    black_edges = M
    
    # The maximum number of edges that can be black is total edges minus the number of edges that cannot be made black
    # Each black edge can be part of a triangle with two other vertices
    # Each triangle can contribute 3 edges, and we can flip the colors of these edges
    # The maximum number of edges that can be black is total_edges - (M * 3)
    
    # However, we cannot have more than total_edges, so we need to ensure we do not exceed that
    max_possible_black_edges = total_edges - black_edges + (N - 1) * (N - 2) // 2
    
    return min(total_edges, max_possible_black_edges)

import sys
input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:M + 1]]

result = max_black_edges(N, M, edges)
print(result)