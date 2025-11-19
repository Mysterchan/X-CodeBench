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
        heights = [0] * (n + 1)
        for i in range(n):
            heights[p[i]] += 1
        
        # Count the number of blocks of each color at each height
        color_count = {}
        for i in range(1, n + 1):
            if heights[i] > 0:
                color = c[i - 1]
                if color not in color_count:
                    color_count[color] = 0
                color_count[color] += heights[i]
        
        # Calculate the number of valid (p', c') pairs
        total_blocks = sum(heights)
        result = factorial_mod(total_blocks, mod)
        
        for count in color_count.values():
            result = (result * pow(factorial_mod(count, mod), mod - 2, mod)) % mod
        
        results.append(result)
    
    return results

# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []
index = 1

for _ in range(t):
    n = int(data[index])
    p = list(map(int, data[index + 1].split()))
    c = list(map(int, data[index + 2].split()))
    test_cases.append((n, p, c))
    index += 3

# Get results
results = count_pairs(t, test_cases)

# Output results
for res in results:
    print(res)