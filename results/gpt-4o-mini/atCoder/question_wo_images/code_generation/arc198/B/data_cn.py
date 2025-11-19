def can_form_sequence(x, y, z):
    total = x + y + z
    if total < 3:
        return "No"
    
    # Check the conditions for forming the sequence
    if (x > 0 and y > 0 and z > 0) or (x == 0 and y == 0) or (y == 0 and z == 0) or (z == 0 and x == 0):
        return "Yes"
    
    # If one of the counts is zero, check the other two
    if x == 0:
        return "Yes" if abs(y - z) <= 1 else "No"
    if y == 0:
        return "Yes" if abs(z - x) <= 1 else "No"
    if z == 0:
        return "Yes" if abs(x - y) <= 1 else "No"
    
    return "No"

import sys
input = sys.stdin.read

data = input().splitlines()
T = int(data[0])
results = []

for i in range(1, T + 1):
    x, y, z = map(int, data[i].split())
    results.append(can_form_sequence(x, y, z))

print("\n".join(results))