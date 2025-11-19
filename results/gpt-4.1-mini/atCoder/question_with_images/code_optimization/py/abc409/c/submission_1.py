import sys
input = sys.stdin.readline

N, L = map(int, input().split())
d = list(map(int, input().split()))

# Compute positions of points on the circle
pos = [0] * N
for i in range(1, N):
    pos[i] = (pos[i-1] + d[i-1]) % L

# Map position to index for O(1) lookup
pos_to_idx = {}
for i, p in enumerate(pos):
    pos_to_idx[p] = i

# If L is not divisible by 3, no equilateral triangle possible
if L % 3 != 0:
    print(0)
    exit()

step = L // 3
ans = 0

# For each point, check if points at pos+step and pos+2*step exist
for i in range(N):
    p1 = pos[i]
    p2 = (p1 + step) % L
    p3 = (p1 + 2 * step) % L
    if p2 in pos_to_idx and p3 in pos_to_idx:
        j = pos_to_idx[p2]
        k = pos_to_idx[p3]
        # Ensure indices are strictly increasing to avoid duplicates
        if i < j < k:
            ans += 1

print(ans)