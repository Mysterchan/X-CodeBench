def min_cost_to_align_teeth(N, X, teeth):
    U = [teeth[i][0] for i in range(N)]
    D = [teeth[i][1] for i in range(N)]
    
    # Calculate the minimum and maximum possible values of H
    min_H = float('inf')
    max_H = float('-inf')
    
    for i in range(N):
        min_H = min(min_H, U[i] + D[i])
        max_H = max(max_H, U[i] + D[i])
    
    # We need to check for all possible H values from min_H to max_H
    min_cost = float('inf')
    
    for H in range(min_H, max_H + 1):
        cost = 0
        valid = True
        
        for i in range(N):
            # Calculate the required U_i and D_i for this H
            required_U = H - D[i]
            required_D = H - U[i]
            
            # Check if we can achieve the required U_i and D_i
            if required_U < 0 or required_D < 0:
                valid = False
                break
            
            cost += max(0, U[i] - required_U) + max(0, D[i] - required_D)
        
        if valid:
            # Check the second condition
            for i in range(N - 1):
                if abs(U[i] - U[i + 1]) > X:
                    valid = False
                    break
            
            if valid:
                min_cost = min(min_cost, cost)
    
    return min_cost

# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

N, X = map(int, data[0].split())
teeth = [tuple(map(int, line.split())) for line in data[1:N + 1]]

# Calculate and print the result
result = min_cost_to_align_teeth(N, X, teeth)
print(result)