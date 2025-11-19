def count_subsequences(N, M, A, B):
    from collections import defaultdict

    # Create a mapping of positions for each value in A
    positions = defaultdict(list)
    for index, value in enumerate(A):
        positions[value].append(index)

    # To store the starting positions of the subsequences matching B
    start_positions = []

    # Find all starting positions of subsequences matching B
    current_position = -1
    for value in B:
        if value not in positions:
            return "No"
        # Find the next position in A that is greater than current_position
        found = False
        for pos in positions[value]:
            if pos > current_position:
                start_positions.append(pos)
                current_position = pos
                found = True
                break
        if not found:
            return "No"

    # Now we need to check if there are at least two valid starting positions
    if len(start_positions) < 2:
        return "No"

    # Check for duplicates in start_positions
    if len(set(start_positions)) < len(start_positions):
        return "Yes"

    return "No"

# Read input
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
A = list(map(int, data[2:N+2]))
B = list(map(int, data[N+2:N+2+M]))

# Get the result and print it
result = count_subsequences(N, M, A, B)
print(result)