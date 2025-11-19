import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# The problem reduces to counting, for each subarray A[L:R], the minimal number of operations f(L,R).
# f(L,R) equals the number of contiguous segments in the set of distinct elements in A[L:R].
# Each operation erases a contiguous range of integers that appear in the subarray.
# So f(L,R) = number of contiguous segments in the set of distinct elements in A[L:R].

# Key insight:
# For each subarray, the distinct elements form some subset of [1..N].
# The minimal number of operations = number of contiguous segments in that subset.
# Number of segments = 1 + number_of_gaps, where a gap is a pair of consecutive integers (x, x+1) where x is in the subset but x+1 is not.

# So:
# f(L,R) = 1 + number_of_gaps_in_subarray(L,R)
# sum over all subarrays f(L,R) = sum over all subarrays (1 + number_of_gaps)
# = total number of subarrays + sum over all subarrays of number_of_gaps

# total number of subarrays = N*(N+1)//2

# We need to compute sum over all subarrays of number_of_gaps.
# Each gap corresponds to a pair (x, x+1).
# For each pair (x, x+1), count how many subarrays contain x but not x+1, or x+1 but not x.
# The sum over all pairs of these counts is sum of number_of_gaps over all subarrays.

# Approach:
# For each integer v in [1..N], store sorted positions of v in A.
# For each pair (x, x+1), compute:
#   - number of subarrays containing x but not x+1
#   - number of subarrays containing x+1 but not x
# Sum these counts for all pairs.

# To count subarrays containing x but not x+1:
# - Positions of x: Px
# - Positions of x+1: Px1
# - Subarrays containing x: intervals covering at least one position in Px
# - Subarrays containing x+1: intervals covering at least one position in Px1
# - Subarrays containing x but not x+1 = subarrays containing x - subarrays containing both x and x+1

# Similarly for x+1 but not x.

# We can compute:
# total_subarrays = N*(N+1)//2
# For each v:
#   count_v = number of subarrays containing v = total_subarrays - number of subarrays containing no v
# number of subarrays containing no v can be computed from gaps between occurrences of v.

# For each pair (x,x+1):
#   count_x = subarrays containing x
#   count_x1 = subarrays containing x+1
#   count_both = subarrays containing both x and x+1
#   gaps_for_pair = (count_x - count_both) + (count_x1 - count_both) = count_x + count_x1 - 2*count_both

# sum over all pairs of gaps_for_pair = sum over all subarrays of number_of_gaps

# Finally:
# answer = total_subarrays + sum_of_all_gaps

# Implementation details:
# - For each v, compute count_v
# - For each pair (x,x+1), compute count_both
# - sum gaps_for_pair over all pairs

def count_subarrays_no_v(pos_list):
    # pos_list: sorted positions of v
    # count subarrays with no v = sum of subarrays in gaps between occurrences
    # positions are 0-based
    prev = -1
    res = 0
    for p in pos_list:
        length = p - prev -1
        res += length*(length+1)//2
        prev = p
    length = N - prev -1
    res += length*(length+1)//2
    return res

def count_subarrays_both(pos_x, pos_y):
    # count subarrays containing both x and y
    # Use two pointers to count intervals containing at least one occurrence of x and y
    # We can use the formula:
    # total_subarrays - subarrays_no_x - subarrays_no_y + subarrays_no_x_or_y
    # But subarrays_no_x_or_y is subarrays containing neither x nor y
    # We can compute subarrays_no_x_or_y by merging pos_x and pos_y and counting gaps

    # Compute subarrays_no_x
    no_x = count_subarrays_no_v(pos_x)
    # Compute subarrays_no_y
    no_y = count_subarrays_no_v(pos_y)

    # Merge pos_x and pos_y
    merged = sorted(pos_x + pos_y)
    no_x_or_y = count_subarrays_no_v(merged)

    return total_subarrays - no_x - no_y + no_x_or_y

positions = [[] for _ in range(N+2)]
for i, v in enumerate(A):
    positions[v].append(i)

total_subarrays = N*(N+1)//2

count_v = [0]*(N+2)
for v in range(1, N+1):
    if positions[v]:
        no_v = count_subarrays_no_v(positions[v])
        count_v[v] = total_subarrays - no_v
    else:
        count_v[v] = 0

sum_gaps = 0
for x in range(1, N):
    pos_x = positions[x]
    pos_x1 = positions[x+1]
    if not pos_x and not pos_x1:
        continue
    count_both = count_subarrays_both(pos_x, pos_x1)
    gaps_for_pair = count_v[x] + count_v[x+1] - 2*count_both
    sum_gaps += gaps_for_pair

answer = total_subarrays + sum_gaps
print(answer)