def process_queries(n, m, edges, queries):
    from sys import stdout
    from collections import defaultdict

    # Create adjacency list for the graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    results = []
    
    for l, r, k in queries:
        # Calculate the values of f(u) for u in range(l, r+1)
        f_values = []
        for u in range(l, r + 1):
            xor_value = 0
            for v in graph[u]:
                if l <= v <= r:  # Only consider neighbors in the induced subgraph
                    xor_value ^= v
            f_values.append(xor_value)

        f_values.sort()  # Sort the f_values list
        results.append(f_values[k - 1])  # k is 1-indexed

    return results

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    index = 0
    t = int(data[index])
    index += 1
    output = []
    
    for _ in range(t):
        n, m = map(int, data[index].split())
        index += 1
        edges = []
        
        for _ in range(m):
            u, v = map(int, data[index].split())
            edges.append((u, v))
            index += 1
        
        q = int(data[index])
        index += 1
        queries = []
        
        for _ in range(q):
            l, r, k = map(int, data[index].split())
            queries.append((l, r, k))
            index += 1
        
        answers = process_queries(n, m, edges, queries)
        output.extend(answers)
    
    sys.stdout.write('\n'.join(map(str, output)) + '\n')

if __name__ == "__main__":
    main()