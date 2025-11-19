def min_steps_to_reach(t, cases):
    results = []
    for x, y in cases:
        # Ensure x is the larger or equal value for easier handling
        if x < y:
            x, y = y, x
        
        # Initialize variables
        step = 0
        s_x, s_y = 0, 0
        length = 0
        
        # While we haven't reached the target yet
        while s_x < x or s_y < y:
            step += 1
            
            # Determine whether the step is x direction or y direction
            if step % 2 == 1:  # x direction
                length += 1
                s_x += length
            else:  # y direction
                length += 1
                s_y += length
            
            # Check if we overshoot or can't reach the exact point
            if s_x > x or s_y > y:
                if s_x > x and s_y > y:
                    break
                elif s_x > x:
                    s_x -= length  # undo last move
                    length -= 1  # adjust length
                    s_x += length  # try with new length
                elif s_y > y:
                    s_y -= length  # undo last move
                    length -= 1  # adjust length
                    s_y += length  # try with new length
        
        if s_x == x and s_y == y:
            results.append(step)
        else:
            results.append(-1)
    
    return results

# Read input
import sys
input = sys.stdin.read
data = input().strip().split()
t = int(data[0])
cases = [(int(data[i*2+1]), int(data[i*2+2])) for i in range(t)]

# Get results for all cases
results = min_steps_to_reach(t, cases)

# Print results
for result in results:
    print(result)