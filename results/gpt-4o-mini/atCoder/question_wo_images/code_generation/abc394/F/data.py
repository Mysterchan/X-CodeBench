def alkane_max_vertices(N, edges):
    from collections import defaultdict

    # Create adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Count degrees of each vertex
    degree_count = {}
    for vertex in graph:
        degree_count[vertex] = len(graph[vertex])

    # Check for conditions of alkane subgraph
    count_1 = 0  # Count of vertices with degree 1
    count_4 = 0  # Count of vertices with degree 4

    for degree in degree_count.values():
        if degree == 1:
            count_1 += 1
        elif degree == 4:
            count_4 += 1
        elif degree != 0:  # Any degree other than 1 and 4 is invalid
            return -1

    # An alkane requires at least one vertex of degree 4
    if count_4 == 0:
        return -1

    # The maximum size of the alkane subgraph is the number of vertices with degree 1 and degree 4
    # Plus the degree 4 ones count as their neighborhoods can connect
    return count_1 + count_4

# Input reading
import sys
input = sys.stdin.read

data = input().strip().splitlines()
N = int(data[0])
edges = [tuple(map(int, line.split())) for line in data[1:]]

# Output the result
print(alkane_max_vertices(N, edges))