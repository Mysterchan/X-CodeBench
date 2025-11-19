def can_exit_strip(test_cases):
    results = []
    
    for n, k, p, d, q, a in test_cases:
        # Create a timeline for signals.
        signal_triggers = []
        
        for pos, delay in zip(p, d):
            # Calculate when the signal turns red for this position
            signal_triggers.append((pos, delay))
        
        for start in a:
            position = start
            direction = 1  # 1 for right, -1 for left
            time = 0
            
            # Create a set to track visited positions
            visited = set()
            while 1 <= position <= 10**15:
                if (position, direction) in visited:
                    results.append("NO")
                    break
                visited.add((position, direction))
                
                time += 1
                
                # Check the current position's signal
                current_signal = None
                for sig_pos, delay in signal_triggers:
                    if sig_pos == position:
                        current_signal = (time + delay) % k == 0
                        break
                
                if current_signal:  # There's a red signal
                    direction *= -1  # Change direction
                
                # Move to the next position
                position += direction
            
            else:
                results.append("YES")
    
    return results

# Reading input
import sys

input = sys.stdin.read
data = input().splitlines()
idx = 0

t = int(data[idx])
idx += 1

test_cases = []

for _ in range(t):
    n, k = map(int, data[idx].split())
    idx += 1
    p = list(map(int, data[idx].split()))
    idx += 1
    d = list(map(int, data[idx].split()))
    idx += 1
    q = int(data[idx])
    idx += 1
    a = list(map(int, data[idx].split()))
    idx += 1
    test_cases.append((n, k, p, d, q, a))

# Getting results and printing them
results = can_exit_strip(test_cases)

# Printing the results
print('\n'.join(results))