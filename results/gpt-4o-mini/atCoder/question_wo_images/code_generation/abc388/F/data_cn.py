def can_reach_end(N, M, A, B, bad_ranges):
    bad_set = set()
    
    for L, R in bad_ranges:
        for block in range(L, R + 1):
            bad_set.add(block)
    
    current_positions = {1}
    
    while current_positions:
        next_positions = set()
        
        for pos in current_positions:
            for step in range(A, B + 1):
                next_pos = pos + step
                if next_pos == N:
                    return "Yes"
                if next_pos > N or next_pos in bad_set:
                    continue
                next_positions.add(next_pos)
        
        current_positions = next_positions
    
    return "No"

# Read input
import sys
input = sys.stdin.read
data = input().strip().splitlines()

N, M, A, B = map(int, data[0].split())
bad_ranges = [tuple(map(int, line.split())) for line in data[1:M + 1]]

# Output result
print(can_reach_end(N, M, A, B, bad_ranges))