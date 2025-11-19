def count_arrangements(t, test_cases):
    MOD = 998244353
    results = []
    
    for n, p, c in test_cases:
        # Create a list of (height, color) pairs
        heights = [(p[i], c[i]) for i in range(n)]
        # Sort by height
        heights.sort()
        
        # Count the number of blocks of the same color at each height
        color_count = {}
        for height, color in heights:
            if color not in color_count:
                color_count[color] = 0
            color_count[color] += 1
        
        # Calculate the number of arrangements
        arrangements = 1
        for count in color_count.values():
            # Multiply by factorial of the count of each color
            for i in range(1, count + 1):
                arrangements = (arrangements * i) % MOD
        
        results.append(arrangements)
    
    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    test_cases.append((n, p, c))

# Get results
results = count_arrangements(t, test_cases)

# Print results
for result in results:
    print(result)