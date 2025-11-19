def balls_in_pockets(test_cases):
    results = []
    for case in test_cases:
        n, s, balls = case
        count = 0
        for dx, dy, xi, yi in balls:
            if dx == 1:  # Moving right
                time_to_x = (s - xi) / 1  # Time to reach the right edge
            else:  # Moving left
                time_to_x = xi / -1  # Time to reach the left edge

            if dy == 1:  # Moving upward
                time_to_y = (s - yi) / 1  # Time to reach the top edge
            else:  # Moving downward
                time_to_y = yi / -1  # Time to reach the bottom edge

            time_to_pocket = min(time_to_x, time_to_y)
            
            if time_to_pocket == time_to_x:
                # Find which pocket at top or bottom
                if dy == 1:  # Goes to the top edge
                    if (s - xi) % s == 0:
                        count += 1
                else:  # Goes to the bottom edge
                    if xi % s == 0:
                        count += 1
            else:
                # Find which pocket at left or right
                if dx == 1:  # Goes to the right edge
                    if (s - yi) % s == 0:
                        count += 1
                else:  # Goes to the left edge
                    if yi % s == 0:
                        count += 1

        results.append(count)
    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n, s = map(int, input().split())
    balls = [tuple(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, s, balls))

# Compute results
results = balls_in_pockets(test_cases)

# Output results
for result in results:
    print(result)