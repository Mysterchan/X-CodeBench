def min_cost_to_fit_teeth(N, X, teeth):
    U = [teeth[i][0] for i in range(N)]
    D = [teeth[i][1] for i in range(N)]
    
    # Calculate the minimum and maximum possible values for H
    min_H = float('inf')
    max_H = float('-inf')
    
    for i in range(N):
        min_H = min(min_H, U[i] + D[i])
        max_H = max(max_H, U[i] + D[i])
    
    # We will check for each possible H in the range [min_H, max_H]
    total_cost = float('inf')
    
    for H in range(min_H, max_H + 1):
        cost = 0
        valid = True
        
        for i in range(N):
            # Calculate the required lengths
            required_U = H - D[i]
            if required_U < 0:
                valid = False
                break
            
            # Calculate the cost to adjust U[i]
            cost += max(0, U[i] - required_U)
        
        if valid:
            # Check the second condition |U[i] - U[i+1]| <= X
            for i in range(N - 1):
                if abs(U[i] - U[i + 1]) > X:
                    valid = False
                    break
            
            if valid:
                total_cost = min(total_cost, cost)
    
    return total_cost

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

N, X = map(int, data[0].split())
teeth = [tuple(map(int, line.split())) for line in data[1:N + 1]]

# Get the result
result = min_cost_to_fit_teeth(N, X, teeth)

# Print the result
print(result)