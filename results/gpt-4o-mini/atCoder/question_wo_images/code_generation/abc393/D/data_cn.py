def min_operations_to_make_ones_continuous(N, S):
    # Find the positions of all '1's in the string
    positions = [i for i in range(N) if S[i] == '1']
    
    # The number of '1's
    count_ones = len(positions)
    
    # If there is only one '1', no operations are needed
    if count_ones <= 1:
        return 0
    
    # Calculate the minimum number of swaps needed
    # We want to move all '1's to be continuous
    # The ideal positions for the '1's would be from positions[0] to positions[0] + count_ones - 1
    # Calculate the total number of moves needed to achieve this
    moves = 0
    for i in range(count_ones):
        # The target position for the i-th '1' is positions[0] + i
        moves += abs(positions[i] - (positions[0] + i))
    
    return moves

# Read input
N = int(input().strip())
S = input().strip()

# Get the result and print it
result = min_operations_to_make_ones_continuous(N, S)
print(result)