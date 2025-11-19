def process_graphs(t, data_sets):
    results = []
    
    for data in data_sets:
        n, m, q, edges, queries = data
        from collections import defaultdict, deque
        
        graph = defaultdict(list)
        incoming_edges = [0] * (n + 1)
        red = [False] * (n + 1)
        
        for u, v in edges:
            graph[u].append(v)
            incoming_edges[v] += 1
        
        def check_win(start):
            if red[start]: 
                return False
            if not graph[start]: 
                return True
            
            visited = [False] * (n + 1)
            queue = deque([start])
            can_win = True

            while queue:
                node = queue.popleft()
                if red[node]:
                    can_win = False
                    continue
                
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            
            return can_win
        
        for query in queries:
            x, u = query
            if x == 1:
                red[u] = True
            else:
                results.append("YES" if check_win(u) else "NO")
    
    return results

# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()
t = int(data[0])
index = 1
data_sets = []

for _ in range(t):
    n, m, q = map(int, data[index].split())
    edges = [tuple(map(int, data[index + i + 1].split())) for i in range(m)]
    queries = [tuple(map(int, data[index + m + i + 1].split())) for i in range(q)]
    data_sets.append((n, m, q, edges, queries))
    index += m + q + 1
    
results = process_graphs(t, data_sets)
sys.stdout.write('\n'.join(results) + '\n')