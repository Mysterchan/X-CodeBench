def dfs(node, parent, graph, weights, time, current_life):
    if current_life == 0 or time > len(graph) - 1:
        return 0
    result = 0
    for neighbor in graph[node]:
        if neighbor != parent:  # avoid going back to the parent
            # Calculate life at the start of the next second
            new_life = current_life + weights[neighbor - 1]
            if time + 1 <= len(graph) - 1 and new_life > 0:  # if still alive
                result = max(result, 1 + dfs(neighbor, node, graph, weights, time + 1, new_life))
    return result

def solve_case(n, st, weights, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    # Start DFS from starting point st with initial time 0 and life 1
    return dfs(st, -1, graph, weights, 0, 1)

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    index = 0
    T = int(data[index])
    index += 1
    results = []
    for _ in range(T):
        n, st = map(int, data[index].split())
        index += 1
        weights = list(map(int, data[index].split()))
        index += 1
        edges = []
        for __ in range(n - 1):
            u, v = map(int, data[index].split())
            edges.append((u, v))
            index += 1
        result = solve_case(n, st, weights, edges)
        results.append(result)
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()