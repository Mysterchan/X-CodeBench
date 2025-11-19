def min_cost_to_destroy_monsters(test_cases):
    results = []
    for n, positions in test_cases:
        x_coords = [p[0] for p in positions]
        y_coords = [p[1] for p in positions]
        
        # Coordinates of the bounding box for the monsters
        min_x = min(x_coords)
        max_x = max(x_coords)
        min_y = min(y_coords)
        max_y = max(y_coords)
        
        # Initial cost to destroy all monsters without moves
        initial_cost = (max_x - min_x + 1) * (max_y - min_y + 1)
        min_cost = initial_cost
        
        # Try moving each monster to the corners (min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)
        for i in range(n):
            x_i, y_i = positions[i]
            # Moving the monster to each corner
            for move_x, move_y in [(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)]:
                new_positions = positions[:i] + [(move_x, move_y)] + positions[i+1:]

                new_x_coords = [p[0] for p in new_positions]
                new_y_coords = [p[1] for p in new_positions]
                
                new_min_x = min(new_x_coords)
                new_max_x = max(new_x_coords)
                new_min_y = min(new_y_coords)
                new_max_y = max(new_y_coords)
                
                # Calculate the new cost
                new_cost = (new_max_x - new_min_x + 1) * (new_max_y - new_min_y + 1)
                
                # Check for minimum cost
                min_cost = min(min_cost, new_cost)

        results.append(min_cost)

    return results


# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []

index = 1
for _ in range(t):
    n = int(data[index])
    positions = []
    for j in range(n):
        x, y = map(int, data[index + 1 + j].split())
        positions.append((x, y))
    test_cases.append((n, positions))
    index += n + 1

# Get results
results = min_cost_to_destroy_monsters(test_cases)

# Print results
for result in results:
    print(result)