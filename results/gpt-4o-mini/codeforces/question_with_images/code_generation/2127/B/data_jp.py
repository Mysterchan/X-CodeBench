def min_days_to_escape(t, test_cases):
    results = []
    for i in range(t):
        n, x = test_cases[i][0]
        s = test_cases[i][1]
        x -= 1  # Convert to 0-indexed

        left_wall = None
        right_wall = None

        # Check for the nearest wall to the left
        for j in range(x, -1, -1):
            if s[j] == '#':
                left_wall = j
                break

        # Check for the nearest wall to the right
        for j in range(x, n):
            if s[j] == '#':
                right_wall = j
                break

        distance_left = float('inf') if left_wall is None else x - left_wall
        distance_right = float('inf') if right_wall is None else right_wall - x

        # Minimum days to escape in either direction, plus one for wall building
        days_to_escape = min(distance_left, distance_right)

        # Add 1 day for building the wall in the direction Hammid would go
        days_to_escape += 1

        results.append(days_to_escape)

    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n, x = map(int, input().split())
    s = input().strip()
    test_cases.append(((n, x), s))

# Calculate and print results
results = min_days_to_escape(t, test_cases)
print('\n'.join(map(str, results)))