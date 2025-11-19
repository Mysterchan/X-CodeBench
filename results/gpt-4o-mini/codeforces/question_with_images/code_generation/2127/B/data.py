def days_to_escape(test_cases):
    results = []
    for n, x, s in test_cases:
        x -= 1  # Convert to 0-based index

        # Find the nearest walls to the left and right of Hamid's position
        left_wall = right_wall = None
        
        # Search for the nearest wall to the left
        for i in range(x - 1, -1, -1):
            if s[i] == '#':
                left_wall = i
                break
        
        # Search for the nearest wall to the right
        for i in range(x + 1, n):
            if s[i] == '#':
                right_wall = i
                break
        
        # Calculate the distance to the nearest walls
        left_distance = x - left_wall if left_wall is not None else float('inf')
        right_distance = right_wall - x if right_wall is not None else float('inf')

        # The answer is the maximum of the two distances
        # If Hamid can escape in the first move (both sides open), return 1
        if left_distance == float('inf') or right_distance == float('inf'):
            results.append(1)
        else:
            results.append(max(left_distance, right_distance))

    return results


t = int(input())
test_cases = []
for _ in range(t):
    n, x = map(int, input().split())
    s = input().strip()
    test_cases.append((n, x, s))

results = days_to_escape(test_cases)
for result in results:
    print(result)