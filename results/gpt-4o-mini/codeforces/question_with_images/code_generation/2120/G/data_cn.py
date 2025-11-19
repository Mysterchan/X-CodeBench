def has_eulerian_path(n, m, k, edges):
    if k == 0:
        return True
    
    degree = [0] * (n + 1)
    
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1
    
    odd_count = sum(1 for x in degree if x % 2 == 1)
    
    if odd_count == 0:
        return True  # All even degrees, Eulerian circuit, hence Eulerian path exists
    elif odd_count == 2:
        return k % 2 == 1  # Exactly two odd degrees means it has a path if k is odd
    else:
        return False  # More than two odd degrees, no Eulerian path

import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
results = []
index = 1

for _ in range(t):
    n, m, k = map(int, data[index].split())
    edges = [tuple(map(int, data[i].split())) for i in range(index + 1, index + m + 1)]
    index += m + 1
    
    if has_eulerian_path(n, m, k, edges):
        results.append("YES")
    else:
        results.append("NO")

print("\n".join(results))