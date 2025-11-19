def simulate_bermuda_triangle(test_cases):
    results = []
    for n, x, y, v_x, v_y in test_cases:
        collisions = 0
        while True:
            if x == 0 and y == 0:
                results.append(collisions)
                break
            if x == 0 and y == n:
                results.append(collisions)
                break
            if x == n and y == 0:
                results.append(collisions)
                break
            
            # Calculate the time to hit each side
            time_to_left = (0 - x) / v_x if v_x < 0 else float('inf')
            time_to_bottom = (0 - y) / v_y if v_y < 0 else float('inf')
            time_to_hypotenuse = (n - y) / (v_y + (v_x * (n - x)) / (n - y)) if v_y + (v_x * (n - x)) / (n - y) > 0 else float('inf')

            min_time = min(time_to_left, time_to_bottom, time_to_hypotenuse)

            if min_time == float('inf'):
                results.append(-1)
                break

            x += v_x * min_time
            y += v_y * min_time
            
            if x < 0 or y < 0 or x + y >= n:
                results.append(-1)
                break
            
            # Count collision
            if min_time == time_to_left:
                v_x = -v_x  # Reflect on the left wall
                collisions += 1
                x = 0  # Snap to the wall
            elif min_time == time_to_bottom:
                v_y = -v_y  # Reflect on the bottom wall
                collisions += 1
                y = 0  # Snap to the wall
            elif min_time == time_to_hypotenuse:
                # Reflect on the hypotenuse
                v_x, v_y = -v_y * (n - y) / (n - x), -v_x * (n - x) / (n - y)
                collisions += 1
                # Calculate where to snap
                x = n - y if y < n else n
                y = n - x if x < n else n

    return results

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()
t = int(data[0])
test_cases = [tuple(map(int, line.split())) for line in data[1:t + 1]]

# Get results
outputs = simulate_bermuda_triangle(test_cases)

# Print results
for output in outputs:
    print(output)