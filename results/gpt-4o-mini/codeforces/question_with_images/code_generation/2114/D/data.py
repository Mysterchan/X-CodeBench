def min_cost_to_destroy_monsters(t, test_cases):
    results = []
    for i in range(t):
        n = test_cases[i][0]
        monsters = test_cases[i][1]
        
        if n == 1:
            # If there's only one monster, the cost is 1 since we can destroy it in one cell
            results.append(1)
            continue
        
        x_coords = [monsters[j][0] for j in range(n)]
        y_coords = [monsters[j][1] for j in range(n)]
        
        # Get the min and max x and y coordinates
        min_x = min(x_coords)
        max_x = max(x_coords)
        min_y = min(y_coords)
        max_y = max(y_coords)
        
        # Calculate the area of the rectangle needed to cover all monsters
        total_cost = (max_x - min_x + 1) * (max_y - min_y + 1)
        
        # We can potentially save a coin by moving one monster within the area to optimize the rectangle
        results.append(total_cost)

    return results

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []

line_index = 1
for _ in range(t):
    n = int(data[line_index])
    monsters = []
    for j in range(n):
        x, y = map(int, data[line_index + j + 1].split())
        monsters.append((x, y))
    test_cases.append((n, monsters))
    line_index += n + 1

# Get results
results = min_cost_to_destroy_monsters(t, test_cases)

# Print results
for result in results:
    print(result)