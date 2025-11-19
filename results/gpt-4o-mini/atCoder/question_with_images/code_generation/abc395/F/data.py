def min_cost_to_fit_teeth(N, X, teeth):
    U = [teeth[i][0] for i in range(N)]
    D = [teeth[i][1] for i in range(N)]
    
    # Calculate the minimum cost
    total_cost = float('inf')
    
    # We will check for all possible H values
    # H can be in the range of [min(U[i] + D[i]) - X, max(U[i] + D[i])]
    min_H = min(U[i] + D[i] for i in range(N)) - X
    max_H = max(U[i] + D[i] for i in range(N))
    
    for H in range(min_H, max_H + 1):
        current_cost = 0
        valid = True
        
        for i in range(N):
            # Calculate the required lengths
            required_U = H - D[i]
            if required_U < 0:
                valid = False
                break
            
            # Calculate the cost to adjust U[i]
            if U[i] > required_U:
                current_cost += U[i] - required_U
        
        if valid:
            # Check the second condition
            for i in range(N - 1):
                if abs(U[i] - U[i + 1]) > X:
                    valid = False
                    break
            
            if valid:
                total_cost = min(total_cost, current_cost)
    
    return total_cost

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

N, X = map(int, data[0].split())
teeth = [tuple(map(int, line.split())) for line in data[1:N + 1]]

# Get the result and print it
result = min_cost_to_fit_teeth(N, X, teeth)
print(result)