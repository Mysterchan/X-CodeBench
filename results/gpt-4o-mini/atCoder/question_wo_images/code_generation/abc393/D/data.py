def min_swaps_to_contiguous_ones(N, S):
    # Find the positions of all '1's in the string
    ones_positions = [i for i in range(N) if S[i] == '1']
    
    # The number of '1's
    count_ones = len(ones_positions)
    
    # If there is only one '1', no swaps are needed
    if count_ones <= 1:
        return 0
    
    # The target positions for the '1's to be contiguous
    # We want them to be in the middle of the current positions
    target_positions = range(ones_positions[0], ones_positions[0] + count_ones)
    
    # Calculate the number of swaps needed
    swaps = 0
    for i in range(count_ones):
        swaps += abs(ones_positions[i] - target_positions[i])
    
    return swaps

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
S = data[1]

# Get the result and print it
result = min_swaps_to_contiguous_ones(N, S)
print(result)