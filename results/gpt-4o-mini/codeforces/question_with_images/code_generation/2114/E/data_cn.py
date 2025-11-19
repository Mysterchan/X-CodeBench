def compute_threat_values(t, test_cases):
    results = []
    
    for case in test_cases:
        n, a, edges = case
        graph = [[] for _ in range(n + 1)]
        
        for v, u in edges:
            graph[v].append(u)
            graph[u].append(v)
            
        threat_values = [0] * (n + 1)
        
        def dfs(node, parent, is_positive):
            current_sum = a[node - 1] if is_positive else -a[node - 1]
            threat_values[node] = current_sum
            
            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs(neighbor, node, not is_positive)
                    current_sum += -a[neighbor - 1] if is_positive else a[neighbor - 1]

        dfs(1, -1, True)
        
        results.append(threat_values[1:])
    
    return results

# Input format handling
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    index = 0
    t = int(data[index])
    index += 1
    test_cases = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index].split()))
        index += 1
        edges = []
        
        for __ in range(n - 1):
            v, u = map(int, data[index].split())
            edges.append((v, u))
            index += 1
        
        test_cases.append((n, a, edges))
    
    results = compute_threat_values(t, test_cases)
    
    for result in results:
        print(" ".join(map(str, result)))