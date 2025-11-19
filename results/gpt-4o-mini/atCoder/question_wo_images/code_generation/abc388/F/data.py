def can_reach_end(N, M, A, B, bad_ranges):
    # Initialize a set to keep track of bad squares
    bad_squares = set()
    
    # Fill the set with bad squares from given ranges
    for L, R in bad_ranges:
        for j in range(L, R + 1):
            bad_squares.add(j)

    # Starting from square 1
    current_square = 1
    
    while current_square < N:
        next_move_found = False
        for step in range(B, A - 1, -1): # Try moves from B to A
            next_square = current_square + step
            if next_square > N: # Ensure we don't go beyond N
                continue
            if next_square not in bad_squares: # Check if the next square is not bad
                current_square = next_square
                next_move_found = True
                break
        if not next_move_found: # If no valid move was found, break out
            break

    return "Yes" if current_square == N else "No"


# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

first_line = list(map(int, data[0].split()))
N, M, A, B = first_line[0], first_line[1], first_line[2], first_line[3]

bad_ranges = []
for i in range(1, M + 1):
    L, R = map(int, data[i].split())
    bad_ranges.append((L, R))

# Determine if we can reach the end
result = can_reach_end(N, M, A, B, bad_ranges)
print(result)