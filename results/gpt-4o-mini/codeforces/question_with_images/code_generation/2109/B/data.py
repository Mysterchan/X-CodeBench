def duel_turns(t, test_cases):
    results = []
    for n, m, a, b in test_cases:
        # Calculate the distances to the edges
        top = a - 1
        bottom = n - a
        left = b - 1
        right = m - b
        
        # The number of turns is determined by the maximum distance to any edge
        max_distance = max(top, bottom, left, right)
        
        # The number of turns is the maximum distance plus one
        results.append(max_distance + 1)
    
    return results

# Read input
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

# Get results
results = duel_turns(t, test_cases)

# Print results
for result in results:
    print(result)