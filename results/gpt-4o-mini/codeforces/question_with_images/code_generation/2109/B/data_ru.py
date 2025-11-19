def duel_duration(t, test_cases):
    results = []
    for n, m, a, b in test_cases:
        # Calculate the distances to the edges
        top = a - 1
        bottom = n - a
        left = b - 1
        right = m - b
        
        # The maximum distance to any edge
        max_distance = max(top, bottom, left, right)
        
        # The number of moves is the maximum distance to the edge plus one
        results.append(max_distance + 1)
    
    return results

# Read input
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

# Get results
results = duel_duration(t, test_cases)

# Print results
for result in results:
    print(result)