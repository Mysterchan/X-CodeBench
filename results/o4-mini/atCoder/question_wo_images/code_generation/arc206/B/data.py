import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
C = list(map(int, input().split()))

# We want to reorder slimes by ascending size (P sorted ascending).
# The operation allowed: swapping adjacent slimes of different colors.
# A sequence is "good" if by swapping adjacent slimes of different colors,
# we can sort the slimes by size.

# Key insight:
# Swapping adjacent slimes of different colors means slimes of the same color
# cannot be reordered internally by these swaps.
# So, the relative order of slimes of the same color in the original sequence
# must be the same as their order in the sorted-by-size sequence.
# Otherwise, we cannot sort the sequence by only swapping adjacent slimes of different colors.

# We want to find the minimal cost to recolor some slimes so that the sequence is good.
# Cost of recoloring a slime is the slime's current color value.
# We can recolor a slime to any color 1..N.

# After recoloring, the sequence must be "good":
# For each color, the slimes of that color appear in ascending order of size in the original sequence.

# Approach:
# 1. Sort slimes by size to get the target order.
# 2. For each slime in the target order, note its original position and color.
# 3. We want to assign colors to slimes so that the sequence of colors in the original order
#    forms non-decreasing sequences for each color (i.e., slimes of the same color appear in ascending order of their original positions).
# 4. We want to minimize the total cost of recoloring.

# Reformulate:
# We want to find a partition of the slimes into color groups so that
# the original positions of slimes in each group are strictly increasing.
# The cost is sum of original colors of slimes that we recolor.

# Since sizes are distinct and P is a permutation, sorting by size gives a permutation of indices.
# We want to find a largest subset of slimes that can keep their original color and form a "good" sequence.
# The rest must be recolored.

# So, the problem reduces to:
# Find the largest subset of slimes that can keep their color and form a sequence where,
# for each color, the original positions are strictly increasing in the order of sizes.

# This is equivalent to:
# For each color, find the longest increasing subsequence (LIS) of original positions in the order of sizes.
# The union of these LISs over all colors gives the maximum number of slimes that can keep their color.
# The cost is sum of colors of slimes not in this union.

# Implementation:
# - Sort slimes by size.
# - For each color, collect the original positions of slimes of that color in the order of sizes.
# - Find LIS length for each color's positions.
# - Sum lengths of all these LISs to get max number of slimes that can keep their color.
# - Total cost = sum of all colors - sum of colors of slimes in LIS sets.
#   But we need to know which slimes are in LIS sets to exclude their cost.

# To find LIS for each color efficiently:
# - For each color, we have a sequence of positions.
# - Find LIS length and also mark which slimes are in LIS.
# - We want to find the maximum total length of LIS over all colors combined.

# But we want to maximize the number of slimes that keep their color.
# So, we find LIS for each color separately and sum their lengths.

# Then, total cost = sum of all colors - sum of colors of slimes in LIS sets.

# To find which slimes are in LIS sets, we can:
# - For each color, find LIS and mark slimes in LIS.
# - Sum colors of these slimes.

# Since N can be up to 2*10^5, we need O(N log N) solution.

# Steps:
# 1. Create an array of tuples: (size, original_index, color)
# 2. Sort by size.
# 3. For each color, collect the original indices in order of size.
# 4. For each color, find LIS of original indices.
# 5. Mark slimes in LIS.
# 6. Sum colors of slimes in LIS.
# 7. Answer = sum(C) - sum(colors of slimes in LIS)

# LIS algorithm:
# - Use patience sorting method with binary search.
# - To reconstruct LIS, keep track of predecessors.

# Let's implement.

from bisect import bisect_left

slimes = [(P[i], i, C[i]) for i in range(N)]
slimes.sort(key=lambda x: x[0])  # sort by size

color_positions = dict()
for size, idx, color in slimes:
    if color not in color_positions:
        color_positions[color] = []
    color_positions[color].append(idx)

# For each color, find LIS of positions
# We'll store for each slime whether it is in LIS or not
in_lis = [False]*N

def find_lis_indices(seq):
    # seq: list of original indices
    # returns indices of elements in LIS (relative to seq)
    piles = []
    pile_tops = []
    predecessors = [-1]*len(seq)
    positions = []

    for i, x in enumerate(seq):
        pos = bisect_left(pile_tops, x)
        if pos == len(pile_tops):
            pile_tops.append(x)
            piles.append([])
        else:
            pile_tops[pos] = x
        piles[pos].append(i)
        if pos > 0:
            # predecessor is last element in previous pile
            predecessors[i] = piles[pos-1][-1]

    # Reconstruct LIS
    lis_indices = []
    # start from last pile last element
    cur = piles[-1][-1]
    while cur != -1:
        lis_indices.append(cur)
        cur = predecessors[cur]
    lis_indices.reverse()
    return lis_indices

for color, positions_list in color_positions.items():
    lis_idx = find_lis_indices(positions_list)
    # mark these slimes as in LIS
    for i in lis_idx:
        slime_idx = positions_list[i]
        in_lis[slime_idx] = True

total_cost = 0
for i in range(N):
    if not in_lis[i]:
        total_cost += C[i]

print(total_cost)