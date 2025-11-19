import sys
from collections import defaultdict
from math import gcd
from functools import reduce

input = sys.stdin.read
data = input().split()
N, K = int(data[0]), int(data[1])
A = list(map(int, data[2:]))

MAX_A = 10**6
count = [0] * (MAX_A + 1)

# Count frequencies of each number in A
for num in A:
    count[num] += 1

# To store the results for each index
results = [0] * N

# Iterate through all possible GCDs from MAX_A down to 1
for g in range(MAX_A, 0, -1):
    total = 0
    
    # Calculate how many multiples of g are in A
    for multiple in range(g, MAX_A + 1, g):
        total += count[multiple]

    if total >= K:
        # If we can select K elements that are multiples of g
        # We need to check for each index
        for i in range(N):
            if A[i] % g == 0:
                results[i] = g

# Print results
print('\n'.join(map(str, results)))