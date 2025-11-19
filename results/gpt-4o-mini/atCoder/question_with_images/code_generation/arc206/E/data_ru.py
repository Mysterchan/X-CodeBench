def min_cost_to_paint(T, test_cases):
    results = []
    
    for case in test_cases:
        N, U, D, L, R = case
        # Collect all good cells' costs
        costs = []
        for i in range(N - 2):
            costs.append((U[i], (1, i + 1)))  # Upper row
            costs.append((D[i], (N, i + 1)))  # Lower row
            costs.append((L[i], (i + 1, 1)))  # Left column
            costs.append((R[i], (i + 1, N)))  # Right column
        
        # Sort costs based on the values
        costs.sort()
        
        total_cost = 0
        used = set()
        
        # We will use a greedy approach to select pairs of cells
        for i in range(0, len(costs), 2):
            if i + 1 < len(costs):
                total_cost += costs[i][0] + costs[i + 1][0]
        
        results.append(total_cost)
    
    return results

# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
test_cases = []

index = 1
for _ in range(T):
    N = int(data[index])
    U = list(map(int, data[index + 1].split()))
    D = list(map(int, data[index + 2].split()))
    L = list(map(int, data[index + 3].split()))
    R = list(map(int, data[index + 4].split()))
    test_cases.append((N, U, D, L, R))
    index += 5

# Get results
results = min_cost_to_paint(T, test_cases)

# Output results
for result in results:
    print(result)