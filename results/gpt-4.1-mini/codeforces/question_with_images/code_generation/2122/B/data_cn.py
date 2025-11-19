import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    zero_diff = 0
    one_diff = 0
    for __ in range(n):
        a, b, c, d = map(int, input().split())
        zero_diff += a - c
        one_diff += b - d
    # The minimal operations is the sum of positive differences in zeros and ones
    # Because we can move elements between heaps arbitrarily,
    # the minimal moves equals the total number of elements that need to be moved.
    # zero_diff and one_diff should be zero sum overall (guaranteed by problem)
    # So minimal moves = sum of positive zero_diff + sum of positive one_diff
    # But since zero_diff + one_diff = 0, positive zero_diff = negative one_diff in magnitude
    # So minimal moves = max(sum of positive zero_diff, sum of positive one_diff)
    # Actually, since zero_diff + one_diff = 0, sum of positive zero_diff = sum of negative one_diff (abs)
    # So minimal moves = sum of positive zero_diff (or sum of positive one_diff)
    # We can just sum positive zero_diff and positive one_diff and take max.
    pos_zero = 0
    pos_one = 0
    # Recalculate per heap to get positive sums
    # But we only have total zero_diff and one_diff, not per heap here.
    # So we need to accumulate positive and negative separately while reading input.
    # Let's do it in one pass:
    # So we redo the loop with storing all a,b,c,d first.
    # To avoid complexity, we do it in one pass:
    # Actually, minimal moves = sum over i of abs(a_i - c_i) + abs(b_i - d_i) divided by 2
    # Because each move fixes one zero or one difference.
    # But since total zeros and ones are conserved, minimal moves = sum of positive differences in zeros or ones.
    # Let's do it directly:
    # minimal moves = sum over i of max(a_i - c_i, 0) + max(b_i - d_i, 0)
    # Because we only need to move out the surplus zeros and ones.
    # So we redo the reading loop:
    # Let's store all inputs first.
    pass

# Re-implement with above logic:
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    zero_surplus = 0
    one_surplus = 0
    for __ in range(n):
        a, b, c, d = map(int, input().split())
        if a > c:
            zero_surplus += a - c
        if b > d:
            one_surplus += b - d
    print(max(zero_surplus, one_surplus))