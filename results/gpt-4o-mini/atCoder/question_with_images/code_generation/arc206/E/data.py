def min_cost_to_color(T, test_cases):
    results = []
    
    for case in test_cases:
        N, U, D, L, R = case
        total_cost = 0
        
        # Calculate the minimum cost to color all cells
        for i in range(N - 2):
            total_cost += min(U[i] + D[i], L[i] + R[i])
        
        results.append(total_cost)
    
    return results

# Read input
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
results = min_cost_to_color(T, test_cases)

# Print results
for result in results:
    print(result)