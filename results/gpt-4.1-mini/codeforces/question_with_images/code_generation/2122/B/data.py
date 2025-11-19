import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    total_diff_0 = 0
    total_diff_1 = 0
    for __ in range(n):
        a, b, c, d = map(int, input().split())
        # Calculate difference in zeros and ones for each pile
        total_diff_0 += c - a
        total_diff_1 += d - b
    # The problem guarantees a solution exists, so total_diff_0 and total_diff_1 should be zero
    # The minimum number of operations is the sum of positive differences in zeros and ones
    # But since total_diff_0 and total_diff_1 are zero, we need to count how many zeros and ones need to be moved
    # Actually, the minimal number of operations is the sum of absolute differences in zeros and ones divided by 2
    # Because each operation moves one element, and each element moved fixes one zero or one difference.
    # But we need to count the total number of elements that need to be moved.
    # Let's do it by summing the positive differences in zeros and ones separately.

    # We need to re-iterate to get the positive differences per pile:
    # But since sum of differences is zero, sum of positive differences = sum of negative differences (absolute)
    # So minimal operations = sum of positive differences in zeros + sum of positive differences in ones

    # Let's do it in one pass:
    # We'll store the differences in arrays and then sum positive parts.

    # Since we didn't store differences, let's do it again:
    # To avoid double reading, let's store input first.

# Revised approach: read all test cases first, then process.

import sys
input = sys.stdin.readline

t = int(input())
results = []
for _ in range(t):
    n = int(input())
    diff_0 = 0
    diff_1 = 0
    moves_0 = 0
    moves_1 = 0
    for __ in range(n):
        a, b, c, d = map(int, input().split())
        diff0 = c - a
        diff1 = d - b
        if diff0 > 0:
            moves_0 += diff0
        if diff1 > 0:
            moves_1 += diff1
    # minimal moves is max of moves_0 and moves_1 or sum? 
    # Actually, each operation moves one element (either zero or one).
    # So total moves = moves_0 + moves_1
    results.append(str(moves_0 + moves_1))

print("\n".join(results))