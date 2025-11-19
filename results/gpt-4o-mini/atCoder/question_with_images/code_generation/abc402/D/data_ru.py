def count_intersections(N, M, lines):
    # Normalize the lines to ensure A < B
    normalized_lines = [(min(A, B), max(A, B)) for A, B in lines]
    
    # Sort lines based on the first point, and then by the second point
    normalized_lines.sort()
    
    # To count intersections
    count = 0
    
    # We will use a list to keep track of the second points
    second_points = []
    
    for i in range(M):
        A_i, B_i = normalized_lines[i]
        
        # Count how many second points are greater than A_i
        # This means they can form an intersection with the current line
        count += sum(1 for B_j in second_points if B_j > A_i)
        
        # Add the current B_i to the list of second points
        second_points.append(B_i)
    
    return count

import sys
input = sys.stdin.read
data = input().splitlines()

# Read N and M
N, M = map(int, data[0].split())

# Read the lines
lines = [tuple(map(int, line.split())) for line in data[1:M+1]]

# Get the result
result = count_intersections(N, M, lines)

# Print the result
print(result)