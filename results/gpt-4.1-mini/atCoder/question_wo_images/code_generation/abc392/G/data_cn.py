import sys
input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))

max_val = 10**6
present = [False] * (max_val + 1)
for x in S:
    present[x] = True

count = 0
for b in S:
    # For each b, check all possible differences d such that b - d and b + d are in S
    # To optimize, we only check d where b - d >= 1 and b + d <= max_val
    # But checking all d up to max_val is too slow (O(N*max_val))
    # Instead, we iterate over possible a in S less than b, and check if c = 2*b - a in S
    # This reduces complexity to O(N^2) worst case, still too large for N=10^6
    # So we use a different approach:
    # Since S is large, we iterate over all pairs (a,b) with a < b and check if c = 2*b - a in S
    # But O(N^2) is too large.
    # Alternative approach:
    # Sort S, then for each pair (a,b), check c = 2*b - a in S using presence array.
    # This is O(N^2) worst case, still too large.
    # We need a more efficient approach.

# Efficient approach:
# Sort S
S.sort()
present = set(S)

count = 0
# For each pair (a,b) with a < b, check if c = 2*b - a in present
# To reduce complexity, we fix b and iterate a < b
# But still O(N^2)
# We can fix c and b, then check a = 2*b - c
# Or fix a and c, then check b = (a + c)/2 if integer and in present
# This last approach is O(N^2) but we can optimize by using two pointers

# Use two pointers approach:
# For each pair (a,c), if (a+c) is even, b = (a+c)//2
# If b in present, count++

count = 0
S_list = S
present = set(S_list)
n = len(S_list)

for i in range(n):
    a = S_list[i]
    for j in range(i+1, n):
        c = S_list[j]
        s = a + c
        if s % 2 == 0:
            b = s // 2
            if b in present:
                count += 1

print(count)