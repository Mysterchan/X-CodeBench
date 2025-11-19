def min_cost_to_fit_teeth(N, X, teeth):
    U = [teeth[i][0] for i in range(N)]
    D = [teeth[i][1] for i in range(N)]
    
    # Calculate the minimum and maximum possible values of H
    min_H = float('inf')
    max_H = float('-inf')
    
    for i in range(N):
        min_H = min(min_H, U[i] + D[i])
        max_H = max(max_H, U[i] + D[i])
    
    # The cost to adjust the teeth
    min_cost = float('inf')
    
    for H in range(min_H, max_H + 1):
        cost = 0
        valid = True
        
        for i in range(N):
            if U[i] + D[i] > H:
                cost += U[i] + D[i] - H
            
        for i in range(N - 1):
            if abs(U[i] - U[i + 1]) > X:
                valid = False
                break
        
        if valid:
            min_cost = min(min_cost, cost)
    
    return min_cost

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