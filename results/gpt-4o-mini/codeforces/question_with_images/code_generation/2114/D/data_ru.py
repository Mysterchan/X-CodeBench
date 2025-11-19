def min_cost_to_destroy_monsters(test_cases):
    results = []
    for monsters in test_cases:
        n = len(monsters)
        if n == 1:
            # If there's only one monster, we can destroy it with just 1 coin.
            results.append(1)
            continue
            
        # Extract coordinates
        x_coords = sorted(x for x, y in monsters)
        y_coords = sorted(y for x, y in monsters)
        
        # Calculate the minimum rectangle that can cover all monsters
        min_x = x_coords[0]
        max_x = x_coords[-1]
        min_y = y_coords[0]
        max_y = y_coords[-1]
        
        # The area (cost) of this rectangle is the total cells in it
        area_cost = (max_x - min_x + 1) * (max_y - min_y + 1)
        
        # Store the result for this test case
        results.append(area_cost)

    return results


# Input processing
import sys

input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []

index = 1
for _ in range(t):
    n = int(data[index])
    monsters = []
    for j in range(n):
        x, y = map(int, data[index + 1 + j].split())
        monsters.append((x, y))
    test_cases.append(monsters)
    index += n + 1

# Get results
results = min_cost_to_destroy_monsters(test_cases)

# Output results
for result in results:
    print(result)