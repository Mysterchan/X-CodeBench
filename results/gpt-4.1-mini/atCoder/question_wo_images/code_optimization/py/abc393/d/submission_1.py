N = int(input())
S = input()

positions = [i for i, ch in enumerate(S) if ch == '1']
k = len(positions)

# If all 1s are already contiguous, no swaps needed
if k == 1:
    print(0)
    exit()

# Find median index
mid = k // 2
median_pos = positions[mid]

# Calculate minimal swaps
# The target positions for 1s are consecutive positions centered around median_pos
# The cost is sum of absolute differences between current positions and target positions
# target positions: median_pos - mid, median_pos - mid +1, ..., median_pos - mid + k -1
ans = 0
for i in range(k):
    ans += abs(positions[i] - (median_pos - mid + i))

print(ans)