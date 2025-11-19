def can_reach(n, m, a, b, bad_intervals):
    if m == 0:
        return True  # No bad squares, we can reach N directly

    # Prepare to track the starting position
    current_pos = 1
    bad_start = [0] * (m + 2)
    bad_end = [0] * (m + 2)
    
    # Fill bad interval lists
    for i in range(m):
        bad_start[i + 1] = bad_intervals[i][0]
        bad_end[i + 1] = bad_intervals[i][1]
    
    bad_start[m + 1] = n + 1  # Sentinel at end of bad intervals
    bad_end[m + 1] = n + 1

    # Start navigating from position 1 to N
    while current_pos < n:
        # We need to find next valid move
        next_pos = current_pos + b
        
        # Check within the moving range possibilities
        valid_move_found = False
        
        while next_pos >= current_pos + a:
            # Check if next_pos is bad
            for i in range(1, m + 2):
                if bad_start[i] > next_pos:  # No more bad intervals
                    break
                if bad_start[i] <= next_pos <= bad_end[i]:
                    next_pos -= 1
                    break
            else:
                # We found a valid move
                current_pos = next_pos  # Move to the new position
                valid_move_found = True
                break
        
        if not valid_move_found:  # No valid moves found, we are stuck
            return False
    
    return True

import sys
input = sys.stdin.read
data = input().splitlines()

# Read input values
n, m, a, b = map(int, data[0].split())
bad_intervals = [tuple(map(int, line.split())) for line in data[1:m + 1]]

# Solve the problem
if can_reach(n, m, a, b, bad_intervals):
    print("Yes")
else:
    print("No")