import sys
from collections import defaultdict
from math import gcd
from itertools import combinations

input = sys.stdin.read
data = input().split()

N = int(data[0])
K = int(data[1])
A = list(map(int, data[2:N+2]))

max_gcd = [0] * N
gcd_count = defaultdict(list)

# Collect all indices by value for later retrieval
for idx, value in enumerate(A):
    gcd_count[value].append(idx)

# Process each element in A
for i in range(N):
    included_value = A[i]

    # Collect the gcd values considering A[i] with other values
    possible_values = []
    
    # Add A[i] itself
    possible_values.append(included_value)
    
    # Add other elements of A less than or equal to 10^6
    for val, indexes in gcd_count.items():
        if val != included_value:
            possible_values.extend([val] * min(K-1, len(indexes)))

    # Calculate maximum gcd among all K combinations including the A[i]
    max_gcd[i] = 1  # At least the gcd will be 1
    
    # Assess possible max gcd from those collected
    for comb in combinations(possible_values, K):
        current_gcd = gcd(comb[0], comb[1] if K > 1 else 0)
        for j in range(2, K):
            current_gcd = gcd(current_gcd, comb[j])
        max_gcd[i] = max(max_gcd[i], current_gcd)

for result in max_gcd:
    print(result)