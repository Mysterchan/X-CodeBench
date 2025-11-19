def min_cost_to_defeat_monsters(test_cases):
    results = []
    for monsters in test_cases:
        n = len(monsters)
        
        # Extract x and y coordinates
        x_coords = [monsters[i][0] for i in range(n)]
        y_coords = [monsters[i][1] for i in range(n)]
        
        # Find the min and max for both dimensions
        min_x = min(x_coords)
        max_x = max(x_coords)
        min_y = min(y_coords)
        max_y = max(y_coords)
        
        # Calculate the cost to clear all monsters
        width = max_x - min_x + 1
        height = max_y - min_y + 1
        cost = width * height
        
        results.append(cost)

    return results


t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    monsters = [tuple(map(int, input().split())) for _ in range(n)]
    test_cases.append(monsters)

results = min_cost_to_defeat_monsters(test_cases)
for result in results:
    print(result)