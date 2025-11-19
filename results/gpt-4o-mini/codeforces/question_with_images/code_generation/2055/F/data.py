def can_partition_polyomino(test_cases):
    results = []
    
    for case in test_cases:
        n, rows = case
        total_area = 0
        leftmost = float('inf')
        rightmost = float('-inf')
        
        for l, r in rows:
            total_area += (r - l + 1)
            leftmost = min(leftmost, l)
            rightmost = max(rightmost, r)
        
        # Check if the total area is even (guaranteed by the problem)
        if total_area % 2 != 0:
            results.append("NO")
            continue
        
        # Check if we can partition
        half_area = total_area // 2
        current_area = 0
        can_partition = False
        
        for l, r in rows:
            current_area += (r - l + 1)
            if current_area == half_area:
                can_partition = True
                break
            elif current_area > half_area:
                break
        
        if can_partition:
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
    rows = []
    for i in range(n):
        l, r = map(int, data[index + 1 + i].split())
        rows.append((l, r))
    test_cases.append((n, rows))
    index += n + 1

# Get results
results = can_partition_polyomino(test_cases)

# Print results
for result in results:
    print(result)