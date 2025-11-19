import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
chords = []

for _ in range(n):
    l, r = map(int, input().split())
    chords.append((min(l, r), max(l, r)))

# Sort chords based on the right end
chords.sort(key=lambda x: x[1])

# Calculate the maximum number of non-intersecting chords when selected by their right endpoints
right_max = [0] * (2 * n + 1)
co_linear = []

for l, r in chords:
    pos = 0
    while pos < len(co_linear) and co_linear[pos] < l:
        pos += 1

    if pos == len(co_linear):
        co_linear.append(l)
    else:
        co_linear[pos] = l
        
    right_max[r] = len(co_linear)

# Prepare to calculate the maximum number of non-intersecting chords selected by their left endpoints
left_max = [0] * (2 * n + 1)
co_linear.clear()

# Sort chords based on the left end in decreasing order
chords.sort(reverse=True)

for l, r in chords:
    pos = 0
    while pos < len(co_linear) and co_linear[pos] > r:
        pos += 1

    if pos == len(co_linear):
        co_linear.append(r)
    else:
        co_linear[pos] = r
            
    left_max[l] = len(co_linear)

# Calculate the final answer by combining the two maximum counts
max_intersections = 0

for border in range(1, 2 * n + 1):
    max_intersections = max(max_intersections, right_max[border] + left_max[border + 1])

print(max_intersections)