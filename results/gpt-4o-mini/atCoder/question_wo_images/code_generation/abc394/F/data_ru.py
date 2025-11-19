def main():
    import sys
    from collections import defaultdict, deque

    input = sys.stdin.read
    data = input().splitlines()
    
    N = int(data[0])
    if N < 4:
        print(-1)
        return
    
    edges = [tuple(map(int, line.split())) for line in data[1:N]]
    
    # Build the graph as an adjacency list
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    # Count degrees of each vertex
    degree = [0] * (N + 1)
    for node in graph:
        degree[node] = len(graph[node])
    
    # To find an "alkan" subgraph, we need to check vertices with degree 1 and 4
    count1 = sum(1 for d in degree if d == 1)
    count4 = sum(1 for d in degree if d == 4)

    # If there are no vertices of degree 4, return -1
    if count4 == 0:
        print(-1)
        return

    # The maximum size of the alkan subgraph
    # Each vertex of degree 4 contributes 5 to the size (4 + 1 leaf attached to it)
    # Each degree 1 vertex contributes 1 to the size
    # The max vertices in the "alkan" subgraph is: count4 * 5 + count1
    max_vertices = count4 * 5 + count1
    print(max_vertices)

if __name__ == "__main__":
    main()