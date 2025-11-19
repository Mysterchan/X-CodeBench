from itertools import combinations

def max_candy_edges(n, edges):
    max_edges = 0
    all_edges = list(combinations(range(n), 2))
    
    # Check all subsets of edges
    for r in range(len(edges) + 1):
        for edge_set in combinations(edges, r):
            degree = [0] * n
            for u, v in edge_set:
                degree[u - 1] += 1
                degree[v - 1] += 1
            
            if all(d <= 2 for d in degree):
                max_edges = max(max_edges, len(edge_set))
    
    return max_edges

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n, m = map(int, data[idx].split())
        idx += 1
        edges = []
        
        for __ in range(m):
            u, v = map(int, data[idx].split())
            edges.append((u, v))
            idx += 1
        
        result = max_candy_edges(n, edges)
        results.append(result)
    
    print('\n'.join(map(str, results)))

main()