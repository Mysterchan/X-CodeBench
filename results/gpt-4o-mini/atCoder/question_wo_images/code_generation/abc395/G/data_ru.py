import sys
import itertools

def read_input():
    input = sys.stdin.read
    data = input().splitlines()
    N, K = map(int, data[0].split())
    C = [list(map(int, line.split())) for line in data[1:N+1]]
    Q = int(data[N+1])
    queries = [tuple(map(int, line.split())) for line in data[N+2:N+2+Q]]
    return N, K, C, Q, queries

def min_cost_good_graph(N, K, C, queries):
    results = []
    
    # Precompute the minimum spanning tree (MST) costs for all combinations of K + 2 nodes
    # We will use a bitmask to represent the set of nodes
    for s, t in queries:
        # Convert to 0-based index
        s -= 1
        t -= 1
        
        # Nodes to consider: 1 to K (0 to K-1) and s, t
        nodes = list(range(K)) + [s, t]
        num_nodes = len(nodes)
        
        # Create a complete graph for the selected nodes
        subgraph = [[0] * num_nodes for _ in range(num_nodes)]
        for i in range(num_nodes):
            for j in range(num_nodes):
                if i != j:
                    subgraph[i][j] = C[nodes[i]][nodes[j]]
        
        # Use Prim's algorithm to find the cost of the minimum spanning tree
        min_cost = [float('inf')] * num_nodes
        min_cost[0] = 0  # Start from the first node
        visited = [False] * num_nodes
        total_cost = 0
        
        for _ in range(num_nodes):
            # Find the minimum cost edge to an unvisited node
            u = -1
            for v in range(num_nodes):
                if not visited[v] and (u == -1 or min_cost[v] < min_cost[u]):
                    u = v
            
            # Add the cost of the selected edge
            total_cost += min_cost[u]
            visited[u] = True
            
            # Update the costs for the remaining nodes
            for v in range(num_nodes):
                if not visited[v]:
                    min_cost[v] = min(min_cost[v], subgraph[u][v])
        
        results.append(total_cost)
    
    return results

def main():
    N, K, C, Q, queries = read_input()
    results = min_cost_good_graph(N, K, C, queries)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()