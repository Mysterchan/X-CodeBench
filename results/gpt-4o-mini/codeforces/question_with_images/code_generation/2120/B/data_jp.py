def count_potted_balls(t, cases):
    results = []
    for n, s, balls in cases:
        potted_count = 0
        
        for (dx, dy, x, y) in balls:
            if dx == 1:
                time_to_x_edge = (s - x) / dx
            else:  # dx == -1
                time_to_x_edge = x / -dx
            
            if dy == 1:
                time_to_y_edge = (s - y) / dy
            else:  # dy == -1
                time_to_y_edge = y / -dy
            
            t_min = min(time_to_x_edge, time_to_y_edge)
            
            if t_min == time_to_x_edge:
                # It hits x-edge, find whether it will hit pocket
                if dy == 1:  # moving upwards
                    if (y + dx * (s - x)) >= s: 
                        potted_count += 1
                else:  # moving downwards
                    if (y + dx * (s - x)) <= 0:
                        potted_count += 1
            else:
                # It hits y-edge, find whether it will hit pocket
                if dx == 1:  # moving to right
                    if (x + dy * (s - y)) >= s:
                        potted_count += 1
                else:  # moving to left
                    if (x + dy * (s - y)) <= 0:
                        potted_count += 1
        
        results.append(potted_count)
    
    return results


# Input processing
import sys
input = sys.stdin.read
data = input().splitlines()
index = 0
t = int(data[index])
index += 1
cases = []

for _ in range(t):
    n, s = map(int, data[index].split())
    index += 1
    balls = []
    for __ in range(n):
        d_x, d_y, x, y = map(int, data[index].split())
        balls.append((d_x, d_y, x, y))
        index += 1
    cases.append((n, s, balls))

# Run the function and print results
results = count_potted_balls(t, cases)
for result in results:
    print(result)