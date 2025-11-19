def can_split_polynomino(test_cases):
    results = []
    for case in test_cases:
        n, ranges = case
        total_area = 0
        odd_count = 0
        
        for l, r in ranges:
            width = r - l + 1
            total_area += width
            if width % 2 == 1:
                odd_count += 1
        
        # Check if the total area is even and there are at least two odd widths
        if total_area % 2 == 0 and odd_count >= 2:
            results.append("YES")
        else:
            results.append("NO")
    
    return results

# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
index = 1
test_cases = []

for _ in range(t):
    n = int(data[index])
    index += 1
    ranges = []
    for _ in range(n):
        l, r = map(int, data[index].split())
        ranges.append((l, r))
        index += 1
    test_cases.append((n, ranges))

# Get results
results = can_split_polynomino(test_cases)

# Output results
print("\n".join(results))