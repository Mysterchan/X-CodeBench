from collections import defaultdict, deque
import sys

input = sys.stdin.read
data = input().splitlines()

def bfs_min_path(graph, start, end):
    queue = deque([(start, [start])])
    visited = set()
    visited.add(start)

    while queue:
        node, path = queue.popleft()
        
        if node == end:
            return path
        
        for neighbor in sorted(graph[node]):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

def main():
    index = 0
    T = int(data[index])
    index += 1
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
        
        path = bfs_min_path(graph, X, Y)
        results.append(" ".join(map(str, path)))
    
    print("\n".join(results))

main()