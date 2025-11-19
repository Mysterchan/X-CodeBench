from collections import defaultdict, deque
import sys

input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
index = 1
results = []

for _ in range(T):
    N, M, X, Y = map(int, data[index].split())
    index += 1
    
    graph = defaultdict(list)
    
    for _ in range(M):
        U, V = map(int, data[index].split())
        graph[U].append(V)
        graph[V].append(U)
        index += 1
    
    # Sort the adjacency list to ensure lexicographical order
    for key in graph:
        graph[key].sort()
    
    # BFS to find the lexicographically smallest path
    queue = deque([(X, [X])])
    visited = set()
    visited.add(X)
    answer = []

    while queue:
        current, path = queue.popleft()
        
        if current == Y:
            answer = path
            break
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    results.append(" ".join(map(str, answer)))

print("\n".join(results))