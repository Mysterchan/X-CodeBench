def count_cycles(N, M, edges):
    from collections import defaultdict
    from itertools import combinations

    MOD = 998244353

    # Create an adjacency list for the graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Function to find all cycles using backtracking
    def find_cycles(start, path, visited):
        if len(path) > 1 and path[0] == path[-1]:
            # Found a cycle
            return 1
        if len(path) > N:  # No cycle can be longer than N
            return 0
        
        count = 0
        for neighbor in graph[start]:
            if neighbor not in visited or (len(path) > 1 and neighbor == path[0]):
                count += find_cycles(neighbor, path + [neighbor], visited | {neighbor})
                count %= MOD
        return count

    total_cycles = 0
    for i in range(1, N + 1):
        total_cycles += find_cycles(i, [i], {i})
        total_cycles %= MOD

    # Each cycle is counted k times (where k is the number of vertices in the cycle)
    # We need to divide by the number of vertices in the cycle to get unique cycles
    # Since we counted each cycle starting from each vertex, we need to divide by the length of the cycle
    # We can use a set to store unique cycles
    unique_cycles = set()

    def find_unique_cycles(start, path, visited):
        if len(path) > 1 and path[0] == path[-1]:
            # Found a unique cycle
            cycle = tuple(sorted(path[:-1]))  # Sort to avoid duplicates
            unique_cycles.add(cycle)
            return
        if len(path) > N:  # No cycle can be longer than N
            return
        
        for neighbor in graph[start]:
            if neighbor not in visited or (len(path) > 1 and neighbor == path[0]):
                find_unique_cycles(neighbor, path + [neighbor], visited | {neighbor})

    for i in range(1, N + 1):
        find_unique_cycles(i, [i], {i})

    total_cycles = len(unique_cycles)
    return total_cycles

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:M + 1]]

# Get the result
result = count_cycles(N, M, edges)

# Print the result
print(result)