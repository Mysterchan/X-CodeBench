import sys
from itertools import combinations

def main():
    input = sys.stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        m = int(data[index + 1])
        index += 2
        
        edges = []
        adj = [[] for _ in range(n)]
        
        for _ in range(m):
            u = int(data[index]) - 1
            v = int(data[index + 1]) - 1
            edges.append((u, v))
            adj[u].append(v)
            adj[v].append(u)
            index += 2

        # Try to find maximum independent set of edges
        max_edges = 0
        
        # All possible combinations of edges
        for k in range(0, m + 1):
            for comb in combinations(edges, k):
                degree_count = [0] * n
                valid = True
                for u, v in comb:
                    degree_count[u] += 1
                    degree_count[v] += 1
                    if degree_count[u] > 2 or degree_count[v] > 2:
                        valid = False
                        break
                if valid:
                    max_edges = max(max_edges, k)

        results.append(str(max_edges))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()