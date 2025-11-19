def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.read
    data = input().splitlines()
    
    N = int(data[0])
    edges = [tuple(map(int, line.split())) for line in data[1:N]] 

    # Create a graph representation
    graph = defaultdict(list)
    degree = [0] * (N + 1)
    
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
        degree[a] += 1
        degree[b] += 1

    # Check the conditions for being an "アルカン"
    # 1. There should be at least one vertex with degree 4
    # 2. All vertices must have degree 1 or 4

    has_four_degree = any(d == 4 for d in degree)
    if not has_four_degree:
        print(-1)
        return

    # Count the valid vertices that can be part of the "アルカン"
    valid_count = 0
    for d in degree[1:]:  # since we are using 1-indexed
        if d == 1 or d == 4:
            valid_count += 1

    if valid_count == 0:
        print(-1)
    else:
        print(valid_count)

if __name__ == "__main__":
    main()