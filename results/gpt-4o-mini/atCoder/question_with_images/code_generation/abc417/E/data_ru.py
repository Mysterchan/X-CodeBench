from collections import deque, defaultdict
import sys
input = sys.stdin.read

def bfs_lexicographic_path(graph, start, end):
    queue = deque([(start, [start])])
    visited = set()
    visited.add(start)

    while queue:
        current, path = queue.popleft()
        
        if current == end:
            return path
        
        for neighbor in sorted(graph[current]):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

def main():
    data = input().splitlines()
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
        
        path = bfs_lexicographic_path(graph, X, Y)
        results.append(" ".join(map(str, path)))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()