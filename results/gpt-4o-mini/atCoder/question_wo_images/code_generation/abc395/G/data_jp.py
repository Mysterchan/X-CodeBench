import sys
import itertools

def min_cost(N, K, C, queries):
    # Initialize the result list
    results = []
    
    # Precompute the minimum spanning tree (MST) costs for all combinations of K + 2 vertices
    for s, t in queries:
        vertices = list(range(1, K + 1)) + [s, t]
        min_cost = float('inf')
        
        # Generate all combinations of edges for the selected vertices
        for edges in itertools.combinations(itertools.combinations(vertices, 2), len(vertices) - 1):
            cost = sum(C[i-1][j-1] for i, j in edges)
            if cost < min_cost:
                min_cost = cost
        
        results.append(min_cost)
    
    return results

def main():
    input = sys.stdin.read
    data = input().splitlines()
    
    # Read N and K
    N, K = map(int, data[0].split())
    
    # Read the cost matrix C
    C = [list(map(int, data[i + 1].split())) for i in range(N)]
    
    # Read number of queries Q
    Q = int(data[N + 1])
    
    # Read the queries
    queries = [tuple(map(int, data[N + 2 + i].split())) for i in range(Q)]
    
    # Get the results for the queries
    results = min_cost(N, K, C, queries)
    
    # Print the results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()