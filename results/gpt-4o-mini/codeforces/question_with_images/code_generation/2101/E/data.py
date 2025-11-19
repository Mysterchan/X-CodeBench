def dfs(tree, node, parent, distance, distances):
    distances[node] = distance
    for neighbor in tree[node]:
        if neighbor != parent:
            dfs(tree, neighbor, node, distance + 1, distances)

def calculate_nice_paths(tree, valid_vertices, distances):
    n = len(distances)
    k = len(valid_vertices)
    max_nice_path = [-1] * n

    for start in valid_vertices:
        current_path = []
        for v in valid_vertices:
            if v != start:
                current_distance = distances[v] - distances[start]
                current_path.append((current_distance, v))
        
        current_path.sort()
        allowed_length = 0
        last_distance = -1
        
        for distance, vertex in current_path:
            if last_distance == -1 or distance >= 2 * last_distance:
                allowed_length += 1
                last_distance = distance
        
        max_nice_path[start] = allowed_length

    return max_nice_path

def process_test_case(n, binary_string, edges):
    tree = [[] for _ in range(n)]
    valid_vertices = []
    
    for i in range(n):
        if binary_string[i] == '1':
            valid_vertices.append(i)

    for u, v in edges:
        tree[u - 1].append(v - 1)
        tree[v - 1].append(u - 1)

    distances = [-1] * n
    dfs(tree, 0, -1, 0, distances)
    
    result = calculate_nice_paths(tree, valid_vertices, distances)

    # Prepare output where invalid nodes give -1
    final_output = []
    for i in range(n):
        if binary_string[i] == '1':
            final_output.append(result[i])
        else:
            final_output.append(-1)
    
    return final_output

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
        binary_string = data[index]
        index += 1
        edges = []
        
        for _ in range(n - 1):
            u, v = map(int, data[index].split())
            edges.append((u, v))
            index += 1
        
        result = process_test_case(n, binary_string, edges)
        results.append(" ".join(map(str, result)))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()