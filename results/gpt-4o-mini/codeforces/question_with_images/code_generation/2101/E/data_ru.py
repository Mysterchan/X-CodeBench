def dfs(node, parent, depth, graph, depth_map):
    depth_map[node] = depth
    for neighbor in graph[node]:
        if neighbor != parent:
            dfs(neighbor, node, depth + 1, graph, depth_map)

def find_beautiful_paths(start, graph, depths, ones, n):
    max_count = 1
    current_length = 0
    last_depth = 0
    
    def dfs_recursive(node, parent):
        nonlocal max_count, current_length, last_depth
        for neighbor in graph[node]:
            if neighbor != parent and ones[neighbor] == 1:
                distance = depths[neighbor] - depths[node]
                if current_length == 0 or distance >= 2 * last_depth:
                    last_depth = distance
                    current_length += 1
                    max_count = max(max_count, current_length + 1)
                    dfs_recursive(neighbor, node)
                    current_length -= 1

    last_depth = 0
    dfs_recursive(start, -1)
    return max_count

def process_test_case(n, s, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    depths = [0] * (n + 1)
    dfs(1, -1, 0, graph, depths)
    
    ones = [0] * (n + 1)
    for i in range(n):
        ones[i + 1] = 1 if s[i] == '1' else 0

    results = []
    for i in range(1, n + 1):
        if ones[i] == 0:
            results.append(-1)
        else:
            max_count = find_beautiful_paths(i, graph, depths, ones, n) 
            results.append(max_count)

    return results

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        s = data[index]
        index += 1
        
        edges = []
        for _ in range(n - 1):
            u, v = map(int, data[index].split())
            edges.append((u, v))
            index += 1
        
        result = process_test_case(n, s, edges)
        results.append(' '.join(map(str, result)))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()