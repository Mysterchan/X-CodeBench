def can_transform(t, cases):
    results = []
    
    for n, s, t in cases:
        if s == t:
            results.append("Yes")
            continue

        if (s.count('1') > 0) and (t.count('1') > 0):
            results.append("Yes")
        else:
            results.append("No")
    
    return results

import sys
input = sys.stdin.read

data = input().splitlines()
t = int(data[0])
cases = []

index = 1
for _ in range(t):
    n = int(data[index])
    s = data[index + 1]
    t = data[index + 2]
    cases.append((n, s, t))
    index += 3

results = can_transform(t, cases)
print("\n".join(results))