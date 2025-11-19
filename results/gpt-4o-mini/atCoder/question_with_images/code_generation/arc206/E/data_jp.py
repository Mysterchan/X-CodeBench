def min_cost_to_blacken(T, test_cases):
    results = []
    
    for case in test_cases:
        N, U, D, L, R = case
        # Calculate the minimum cost to blacken all cells
        min_cost = float('inf')
        
        # Find the minimum values for each side
        min_U = min(U)
        min_D = min(D)
        min_L = min(L)
        min_R = min(R)
        
        # Calculate the minimum cost using the combinations of edges
        min_cost = min(
            min_U + min_D + min_L + min_R,  # U, D, L, R
            min_U + min_L + min_L + min_U,  # U, L, L, U
            min_D + min_R + min_R + min_D   # D, R, R, D
        )
        
        results.append(min_cost)
    
    return results

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

results = min_cost_to_blacken(T, test_cases)
for result in results:
    print(result)