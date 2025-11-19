def minimum_cost_to_sort(N, P):
    # Create a list of positions for each number in the permutation
    position = [0] * (N + 1)
    for i in range(N):
        position[P[i]] = i

    total_cost = 0
    # Iterate through each number from 1 to N
    for i in range(1, N + 1):
        # While the current number is not in the correct position
        while position[i] != i - 1:
            # Get the current position of the number i
            current_pos = position[i]
            # The position it should be in
            target_pos = i - 1
            
            # Swap the current number with the next one
            # The cost of this swap is the index of the current position (1-based)
            total_cost += current_pos
            
            # Perform the swap in the position array
            # Swap the numbers in the position array
            position[P[current_pos]], position[P[current_pos + 1]] = position[P[current_pos + 1]], position[P[current_pos]]
            # Swap the actual numbers in the permutation
            P[current_pos], P[current_pos + 1] = P[current_pos + 1], P[current_pos]

    return total_cost

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
P = list(map(int, data[1:]))

# Get the result and print it
result = minimum_cost_to_sort(N, P)
print(result)