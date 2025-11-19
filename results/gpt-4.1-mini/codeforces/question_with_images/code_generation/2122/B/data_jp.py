import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    zero_diff = 0
    one_diff = 0
    for __ in range(n):
        a, b, c, d = map(int, input().split())
        zero_diff += c - a
        one_diff += d - b
    # zero_diff and one_diff must be zero-sum overall (guaranteed by problem)
    # minimal moves = sum of positive differences (or sum of negative differences in absolute)
    # because each move fixes one surplus element to one deficit element
    ans = 0
    # We can sum positive differences of zeros and ones separately
    # but since total zero_diff and one_diff are zero, sum of positive zero_diff == sum of negative zero_diff (abs)
    # minimal moves = max of total surplus zeros and total surplus ones
    # but since total zero_diff and one_diff are zero, sum of positive zero_diff == sum of positive one_diff
    # so minimal moves = sum of positive zero_diff (or sum of positive one_diff)
    # Let's compute sum of positive zero_diff and sum of positive one_diff
    # Actually, since total zero_diff and one_diff are zero, sum of positive zero_diff == sum of negative zero_diff (abs)
    # So minimal moves = sum of positive zero_diff + sum of positive one_diff
    # But each move moves one element, so total moves = sum of positive zero_diff + sum of positive one_diff
    # However, since total zero_diff + total one_diff = 0, sum of positive zero_diff == sum of negative zero_diff (abs)
    # So minimal moves = sum of positive zero_diff + sum of positive one_diff
    # But the problem states the sequence exists, so zero_diff and one_diff sums are zero.
    # So minimal moves = sum of positive zero_diff + sum of positive one_diff
    # Let's do that:
    zero_pos = 0
    one_pos = 0
    # We need to re-iterate or store diffs
    # Let's store diffs in a list first
    # To avoid re-reading input, let's store diffs in a list
    # But we already read input, so let's do it in one pass:
    # So let's read input again for each test case
    # To avoid complexity, let's store diffs in a list first
    # Let's redo the approach:
    # We'll store diffs in arrays and then compute sums
    # Let's implement this cleanly:

# Re-implement with storing diffs per test case
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    zero_diffs = []
    one_diffs = []
    for __ in range(n):
        a, b, c, d = map(int, input().split())
        zero_diffs.append(c - a)
        one_diffs.append(d - b)
    zero_pos = sum(x for x in zero_diffs if x > 0)
    one_pos = sum(x for x in one_diffs if x > 0)
    print(zero_pos + one_pos)