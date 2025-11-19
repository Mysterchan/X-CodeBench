import sys
from collections import defaultdict

input = sys.stdin.read
data = input().split()
N = int(data[0])
K = int(data[1])
A = list(map(int, data[2:N+2]))

max_value = 10**6
count = [0] * (max_value + 1)

# Count occurrences of each number in A
for num in A:
    count[num] += 1

# Prepare to find maximum GCD for each number
gcd_count = [0] * (max_value + 1)

# Calculate how many numbers are multiples of each number
for i in range(1, max_value + 1):
    for j in range(i, max_value + 1, i):
        gcd_count[i] += count[j]

# Prepare the result for each A[i]
result = []
for num in A:
    if num == 1:
        result.append(1)
        continue
    max_gcd = 1
    for divisor in range(num, max_value + 1, num):
        if gcd_count[divisor] >= K:
            max_gcd = divisor
    result.append(max_gcd)

# Print the results
sys.stdout.write('\n'.join(map(str, result)) + '\n')