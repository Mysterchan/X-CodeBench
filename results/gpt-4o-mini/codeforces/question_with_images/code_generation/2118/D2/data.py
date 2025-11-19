def will_leave_strip(t, test_cases):
    results = []
    for case in test_cases:
        n, k, positions, delays, q, queries = case
        lights = {positions[i]: delays[i] for i in range(n)}
        
        for start in queries:
            # Current position and direction
            current = start
            direction = 1
            
            # To avoid infinite loops, we will track visited positions
            visited = set()
            while True:
                # If current position is outside the strip
                if current < 1 or current > 10**15:
                    results.append("YES")
                    break
                
                # Check if we are at a traffic light
                if current in lights:
                    red_time = (current - 1) * k + lights[current]
                    if red_time % k == 0:
                        direction *= -1  # Turn around on encountering a red light
                
                # Move in the current direction
                if current in visited:
                    results.append("NO")  # We've looped back, we won't leave
                    break
                visited.add(current)
                
                current += direction
            
    return results

# Reading input
import sys
input = sys.stdin.read
data = input().splitlines()

index = 0
t = int(data[index])
index += 1

test_cases = []

for _ in range(t):
    n, k = map(int, data[index].split())
    index += 1
    positions = list(map(int, data[index].split()))
    index += 1
    delays = list(map(int, data[index].split()))
    index += 1
    q = int(data[index])
    index += 1
    queries = list(map(int, data[index].split()))
    index += 1
    
    test_cases.append((n, k, positions, delays, q, queries))

# Get results
results = will_leave_strip(t, test_cases)

# Print results
sys.stdout.write("\n".join(results) + "\n")