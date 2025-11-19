def can_split_polimino(test_cases):
    results = []
    for l_r in test_cases:
        n = l_r[0]
        segments = l_r[1:]
        
        total_area = 0
        min_left = float('inf')
        max_right = float('-inf')
        
        for l, r in segments:
            total_area += (r - l + 1)
            min_left = min(min_left, l)
            max_right = max(max_right, r)
        
        if total_area % 2 != 0:
            results.append("NO")
            continue
        
        # Check if we can split the polimino
        half_area = total_area // 2
        current_area = 0
        found_split = False
        
        for i in range(n):
            l, r = segments[i]
            current_area += (r - l + 1)
            if current_area == half_area:
                found_split = True
                break
            elif current_area > half_area:
                break
        
        if found_split:
            results.append("YES")
        else:
            results.append("NO")
    
    return results

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []
index = 1

for _ in range(t):
    n = int(data[index])
    segments = []
    for j in range(n):
        l, r = map(int, data[index + j + 1].split())
        segments.append((l, r))
    test_cases.append((n, *segments))
    index += n + 1

# Get results
results = can_split_polimino(test_cases)

# Print results
for result in results:
    print(result)