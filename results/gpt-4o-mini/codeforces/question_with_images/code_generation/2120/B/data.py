def potted_balls_in_pool(t, test_cases):
    results = []
    
    for case in test_cases:
        n, s, balls = case
        potted_count = 0
        
        for d_x, d_y, x_i, y_i in balls:
            # Determine the pocket hit based on the direction and the starting coordinates.
            if d_x == 1:  # Moving right
                if d_y == 1:  # Moving up
                    if (s - x_i) == (s - y_i):  # Hits top-right pocket (s, s)
                        potted_count += 1
                elif d_y == -1:  # Moving down
                    if (s - x_i) == y_i:  # Hits bottom-right pocket (s, 0)
                        potted_count += 1
            
            elif d_x == -1:  # Moving left
                if d_y == 1:  # Moving up
                    if x_i == y_i:  # Hits top-left pocket (0, s)
                        potted_count += 1
                elif d_y == -1:  # Moving down
                    if x_i == (s - y_i):  # Hits bottom-left pocket (0, 0)
                        potted_count += 1
        
        results.append(potted_count)
    
    return results

# Read input
t = int(input())
test_cases = []

for _ in range(t):
    n, s = map(int, input().split())
    balls = [tuple(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, s, balls))

# Calculate the results
results = potted_balls_in_pool(t, test_cases)

# Print results
for result in results:
    print(result)