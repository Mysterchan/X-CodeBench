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
    # For each b, check all possible differences d such that b-d and b+d are in S
    # To avoid O(N^2), we only check d where b-d and b+d are in range and present.
    # But checking all d up to max_val is too large.
    # Instead, we can iterate over possible d where b-d and b+d are in S.
    # Since S is large, we need a more efficient approach.

# The above naive approach is O(N * max_val), which is too large.

# Optimized approach:
# Sort S.
# For each pair (A, B) with A < B, check if C = 2*B - A is in S.
# If yes, (A, B, C) is a fine triplet.
# This approach is O(N^2) worst case, but we can optimize by using a set for O(1) lookup.

S.sort()
present_set = set(S)
count = 0

for i in range(N):
    A = S[i]
    for j in range(i+1, N):
        B = S[j]
        C = 2*B - A
        if C > max_val:
            # Since S is sorted, no need to check further for this i
            break
        if C in present_set:
            count += 1

print(count)