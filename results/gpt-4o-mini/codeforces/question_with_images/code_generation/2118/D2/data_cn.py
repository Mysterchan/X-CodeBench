def will_exit_belt(test_cases):
    results = []
    for n, k, positions, delays, queries in test_cases:
        red_lights = {}
        
        # Create a dictionary to track the red light timings
        for p, d in zip(positions, delays):
            if p not in red_lights:
                red_lights[p] = []
            red_lights[p].append(d)
        
        for query in queries:
            pos = query
            direction = 1  # 1 means moving right, -1 means moving left
            visited = set()
            time = 0
            
            while True:
                if pos in visited:  # cyclic movement detected
                    results.append("NO")
                    break
                visited.add(pos)
                
                # Check if there is a red light at the current position
                if pos in red_lights:
                    # Calculate the next red light change time
                    red_time = (time + red_lights[pos][0]) % k
                    if red_time == 0:
                        direction *= -1  # turn around

                # Try to move in the current direction
                next_pos = pos + direction
                time += 1
                
                # Check if still on the belt
                if next_pos < 1 or next_pos > 10**15:
                    results.append("YES")
                    break

                pos = next_pos

    return results

# Input reading
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
    test_cases.append((n, k, positions, delays, queries))

# Get results for all test cases
results = will_exit_belt(test_cases)

# Output the results
sys.stdout.write("\n".join(results) + "\n")