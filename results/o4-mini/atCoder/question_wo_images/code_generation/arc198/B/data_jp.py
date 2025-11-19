def can_form_sequence(X, Y, Z):
    total = X + Y + Z
    max_count = max(X, Y, Z)
    if max_count > (total - max_count + 1):
        return "No"
    return "Yes"

import sys
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
results = []
for i in range(1, T + 1):
    X, Y, Z = map(int, data[i].split())
    results.append(can_form_sequence(X, Y, Z))

print("\n".join(results))