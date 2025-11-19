import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# Explanation of the problem and approach:
# For each subarray A[L:R], f(L,R) is the minimum number of operations to erase all elements.
# Each operation chooses a contiguous integer range [l,r] such that all integers in [l,r] appear at least once on the blackboard,
# and erases all occurrences of these integers.
#
# The problem asks for sum of f(L,R) over all subarrays.
#
# Key insight:
# f(L,R) = number of connected components in the "integer adjacency graph" formed by the distinct integers in A[L:R].
# Two integers x and y are connected if they appear together in some operation's chosen range.
#
# The problem reduces to counting how many connected components the distinct integers in A[L:R] form,
# where edges exist between consecutive integers if both appear in A[L:R].
#
# So f(L,R) = (#distinct integers in A[L:R]) - (#edges between consecutive integers present in A[L:R])
#
# We want sum over all subarrays of f(L,R).
#
# Let:
#   D(L,R) = number of distinct integers in A[L:R]
#   E(L,R) = number of edges between consecutive integers present in A[L:R]
#
# Then:
#   f(L,R) = D(L,R) - E(L,R)
#
# So sum f(L,R) = sum D(L,R) - sum E(L,R)
#
# sum D(L,R) is a classic problem: sum over all subarrays of number of distinct elements.
# sum E(L,R) is sum over all subarrays of number of edges between consecutive integers present.
#
# We can compute sum D(L,R) using a two-pointer approach.
#
# For sum E(L,R):
# Each edge corresponds to a pair of consecutive integers (x, x+1).
# For each such pair, we find all positions of x and x+1 in A.
# The edge is present in subarray A[L:R] iff both x and x+1 appear in A[L:R].
#
# So sum E(L,R) = sum over all edges of number of subarrays containing both x and x+1.
#
# To count number of subarrays containing both x and x+1:
# Let pos_x = sorted positions of x in A
# Let pos_y = sorted positions of x+1 in A
#
# Number of subarrays containing both x and x+1 =
# total subarrays - subarrays missing x - subarrays missing x+1
#
# total subarrays = N*(N+1)/2
#
# subarrays missing x = sum over gaps between occurrences of x of number of subarrays in that gap
# similarly for x+1
#
# We compute these and sum over all edges.
#
# Finally, answer = sum D(L,R) - sum E(L,R)

# Step 1: sum D(L,R) - sum of distinct elements over all subarrays
last_occ = [-1]*(N+1)
res_distinct = 0
left = 0
count = 0
freq = [0]*(N+1)

j = 0
for i in range(N):
    x = A[i]
    freq[x] += 1
    if freq[x] == 1:
        count += 1
    # For each i, number of subarrays ending at i with distinct count = count
    # We want sum over all subarrays, so we accumulate count for each i
    # But we need sum of distinct counts over all subarrays, not just ending at i.
    # We'll use a two-pointer approach:
    # Actually, we can do a standard approach:
    # sum of distinct elements over all subarrays = sum over i of (number of subarrays ending at i) * distinct count at i
    # But distinct count changes as we move i.
    # Instead, we use a known approach:
    # We'll use a two-pointer approach to count sum of distinct elements over all subarrays:
    # We'll move right pointer i, and maintain left pointer to keep track of distinct elements.
    # But distinct elements can only increase or stay same as we move right.
    # Actually, the problem is to sum distinct counts over all subarrays.
    # We can do it by:
    # For each position i, the number of subarrays ending at i is i+1.
    # The distinct count for subarrays ending at i varies.
    # So we use a two-pointer approach:
    # We'll keep track of the last occurrence of each element.
    # For each i, the number of subarrays ending at i with distinct count = count.
    # So sum over i of count*(i - left + 1) is sum of distinct counts over all subarrays.
    # But this is complicated.
    # Instead, we use a known approach from AtCoder editorial for sum of distinct elements over all subarrays:
    # We'll use a two-pointer approach:
    # For each right pointer i, move left pointer to maintain distinct count.
    # Actually, we can do a simpler approach:
    # We'll use a sliding window to count number of subarrays with at most k distinct elements for all k,
    # but here we want sum of distinct counts.
    # So we do the following:
    # For each element, we add (i - last_occ[x]) to the answer.
    # This counts the contribution of x to subarrays ending at i.
    # Summing over all i gives sum of distinct elements over all subarrays.
    res_distinct += (i - last_occ[x])
    last_occ[x] = i

# Step 2: sum E(L,R) - sum over all edges of number of subarrays containing both x and x+1
# For each integer from 1 to N-1, if both x and x+1 appear, compute number of subarrays containing both.

pos = [[] for _ in range(N+2)]
for i, v in enumerate(A):
    pos[v].append(i)

total_subarrays = N*(N+1)//2

def subarrays_missing_positions(positions):
    # positions are sorted
    # count subarrays that do NOT contain any occurrence of the element
    # gaps between occurrences + edges
    res = 0
    prev = -1
    for p in positions:
        length = p - prev - 1
        res += length*(length+1)//2
        prev = p
    length = N - prev - 1
    res += length*(length+1)//2
    return res

res_edges = 0
for x in range(1, N):
    if not pos[x] or not pos[x+1]:
        continue
    missing_x = subarrays_missing_positions(pos[x])
    missing_y = subarrays_missing_positions(pos[x+1])
    # subarrays containing both = total - missing_x - missing_y
    both = total_subarrays - missing_x - missing_y
    if both > 0:
        res_edges += both

# Final answer
ans = res_distinct - res_edges
print(ans)