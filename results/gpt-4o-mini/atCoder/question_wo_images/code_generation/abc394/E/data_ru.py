def shortest_palindrome_paths(N, graph):
    inf = float('inf')
    dist = [[inf] * N for _ in range(N)]

    # Initialize distances with direct edges
    for i in range(N):
        for j in range(N):
            if graph[i][j] != '-':
                dist[i][j] = 1

    # Include the empty path case
    for i in range(N):
        dist[i][i] = 0

    # Use Floyd-Warshall algorithm to find shortest paths
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # Check for palindromes using dynamic programming
    for k in range(26):  # For each character 'a' to 'z'
        char = chr(k + ord('a'))
        for i in range(N):
            for j in range(N):
                if graph[i][j] == char:
                    # Storying the length of the shortest palindrome
                    for p in range(N):
                        for q in range(N):
                            if dist[p][i] != inf and dist[j][q] != inf:
                                dist[p][q] = min(dist[p][q], dist[p][i] + 1 + dist[j][q])

                # Check through middle point
                if graph[i][j] == char:
                    for p in range(N):
                        if dist[p][i] != inf:  # Path to i
                            for q in range(N):
                                if dist[j][q] != inf:  # Path from j
                                    dist[p][q] = min(dist[p][q], dist[p][i] + 1 + dist[j][q])

    # Prepare result
    result = []
    for i in range(N):
        result.append(['-1' if dist[i][j] == inf else str(dist[i][j]) for j in range(N)])

    return result

import sys

input = sys.stdin.read
data = input().splitlines()
N = int(data[0].strip())
graph = [line.strip() for line in data[1:N + 1]]

result = shortest_palindrome_paths(N, graph)

for row in result:
    print(" ".join(row))