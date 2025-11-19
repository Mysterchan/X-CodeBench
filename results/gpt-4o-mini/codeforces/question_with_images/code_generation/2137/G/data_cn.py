def process_game(t, test_cases):
    results = []
    
    for case in test_cases:
        n, m, q, edges, queries = case
        graph = [[] for _ in range(n + 1)]
        out_degree = [0] * (n + 1)
        red = [0] * (n + 1)  # 0 = blue, 1 = red
        
        for u, v in edges:
            graph[u].append(v)
            out_degree[u] += 1
        
        for query in queries:
            x, u = query
            if x == 1:
                red[u] = 1  # Make node u red
            else:  # x == 2
                # Check if Cry wins starting from node u
                if red[u] == 1 or out_degree[u] == 0:
                    results.append("NO")
                else:
                    can_cry_win = True
                    stack = [u]
                    visited = set()
                    
                    while stack:
                        node = stack.pop()
                        if node in visited:
                            continue
                        visited.add(node)
                        if red[node] == 1 or out_degree[node] == 0:
                            can_cry_win = False
                            break
                        for next_node in graph[node]:
                            stack.append(next_node)
                    
                    results.append("YES" if can_cry_win else "NO")
    
    return results

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

index = 0
t = int(data[index])
index += 1
test_cases = []

for _ in range(t):
    n, m, q = map(int, data[index].split())
    index += 1
    edges = [tuple(map(int, data[index + i].split())) for i in range(m)]
    index += m
    queries = [tuple(map(int, data[index + i].split())) for i in range(q)]
    index += q
    test_cases.append((n, m, q, edges, queries))

# Process the game and print results
results = process_game(t, test_cases)
print("\n".join(results))