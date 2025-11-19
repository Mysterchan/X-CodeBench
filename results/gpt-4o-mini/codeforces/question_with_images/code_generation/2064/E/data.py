def factorial_mod(n, mod):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % mod
    return result

def count_pairs(t, test_cases):
    mod = 998244353
    results = []
    
    for n, p, c in test_cases:
        # Create a list of (height, color) pairs
        height_color_pairs = [(p[i], c[i]) for i in range(n)]
        
        # Sort by height
        height_color_pairs.sort()
        
        # Count occurrences of each color at each height
        from collections import defaultdict
        color_count = defaultdict(int)
        for height, color in height_color_pairs:
            color_count[color] += 1
        
        # Calculate the number of valid permutations
        result = 1
        for count in color_count.values():
            result = (result * factorial_mod(count, mod)) % mod
        
        results.append(result)
    
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
results = count_pairs(t, test_cases)

# Print results
for res in results:
    print(res)