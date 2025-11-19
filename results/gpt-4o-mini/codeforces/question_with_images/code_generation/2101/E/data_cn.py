import sys
from collections import defaultdict, deque

input = sys.stdin.readline

def bfs(start, adj, dist):
    queue = deque([start])
    visited = {start}
    
    while queue:
        node = queue.popleft()
        for neighbor in adj[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)

def process_case(n, s, edges):
    if s.count('1') == 0:
        return [-1] * n
    
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    distance = {}
    for i in range(1, n + 1):
        if s[i - 1] == '1':
            distance[i] = {}
            bfs(i, adj, distance[i])
    
    results = [-1] * n

    for i in range(1, n + 1):
        if s[i - 1] == '1':
            current_length = 1
            last_weight = 0
            valid_nodes = [i]
            for j in range(1, n + 1):
                if s[j - 1] == '1' and j != i:
                    dist = distance[i][j] + 1
                    if last_weight == 0 or dist >= 2 * last_weight:
                        valid_nodes.append(j)
                        last_weight = dist
            
            results[i - 1] = len(valid_nodes)

    return results

def main():
    t = int(input())
    output = []
    
    for _ in range(t):
        n = int(input())
        s = input().strip()
        edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
        results = process_case(n, s, edges)
        output.append(' '.join(map(str, results)))

    print('\n'.join(output))

if __name__ == "__main__":
    main()