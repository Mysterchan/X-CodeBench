def min_crossings(t, test_cases):
    results = []
    
    for case in test_cases:
        n, m, x, y, a, b = case
        crossings = 0

        if n > 0:
            crossings += 1  # First crossing to get over the first horizontal laser
            crossings += 1  # Last crossing to exit over the last horizontal laser
            # If there's more than 1 horizontal laser, we cross one for each additional laser
            crossings += n - 1
        
        if m > 0:
            crossings += 1  # First crossing to get to the first vertical laser
            crossings += 1  # Last crossing to exit through the last vertical laser
            # If there's more than 1 vertical laser, we cross one for each additional laser
            crossings += m - 1
        
        results.append(crossings)
    
    return results

# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []
index = 1

for _ in range(t):
    n, m, x, y = map(int, data[index].split())
    a = list(map(int, data[index + 1].split())) if n > 0 else []
    b = list(map(int, data[index + 2].split())) if m > 0 else []
    test_cases.append((n, m, x, y, a, b))
    index += 3 if n > 0 and m > 0 else (2 if n > 0 or m > 0 else 1)

results = min_crossings(t, test_cases)

# Output results
for result in results:
    print(result)