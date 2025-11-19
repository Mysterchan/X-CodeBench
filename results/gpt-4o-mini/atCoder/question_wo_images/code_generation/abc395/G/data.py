import sys
import itertools

def min_cost_good_graph(N, K, C, queries):
    # Precompute the minimum spanning tree costs for all combinations of K + 2 vertices
    # We will use Prim's algorithm to find the minimum spanning tree cost
    from itertools import combinations
    
    # Store the results for each query
    results = []
    
    # Generate all combinations of K + 2 vertices from the set {1, 2, ..., N}
    vertices = list(range(1, N + 1))
    
    for s, t in queries:
        # Create a set of vertices to consider
        selected_vertices = {1, 2} | {s, t}
        
        # We need to find the minimum spanning tree cost for the selected vertices
        selected_vertices = list(selected_vertices)
        m = len(selected_vertices)
        
        # Prim's algorithm initialization
        min_cost = 0
        in_mst = [False] * m
        min_edge = [float('inf')] * m
        min_edge[0] = 0  # Start from the first vertex in the selected set
        
        for _ in range(m):
            # Find the vertex with the minimum edge cost that is not in the MST
            u = -1
            for v in range(m):
                if not in_mst[v] and (u == -1 or min_edge[v] < min_edge[u]):
                    u = v
            
            # Add the cost of the selected edge to the total cost
            min_cost += min_edge[u]
            in_mst[u] = True
            
            # Update the minimum edge costs for the remaining vertices
            for v in range(m):
                if not in_mst[v]:
                    edge_cost = C[selected_vertices[u] - 1][selected_vertices[v] - 1]
                    if edge_cost < min_edge[v]:
                        min_edge[v] = edge_cost
        
        results.append(min_cost)
    
    return results

def main():
    input = sys.stdin.read
    data = input().splitlines()
    
    # Read N and K
    N, K = map(int, data[0].split())
    
    # Read the cost matrix C
    C = []
    for i in range(1, N + 1):
        C.append(list(map(int, data[i].split())))
    
    # Read number of queries Q
    Q = int(data[N + 1])
    
    # Read the queries
    queries = []
    for i in range(N + 2, N + 2 + Q):
        s, t = map(int, data[i].split())
        queries.append((s, t))
    
    # Get the results for the queries
    results = min_cost_good_graph(N, K, C, queries)
    
    # Print the results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()