import sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

# dp(pos, length, target) := minimal flips to make the majority of segment A[pos:pos+length]
# after applying the operation (length = 3^k) equal to target (0 or 1)
# We will build this bottom-up from length=1 (leaf) to length=3^N (root)

# length = 3^k
# For length=1, dp(pos,1,target) = 0 if A[pos] == target else 1

# For length>1:
# The segment is divided into 3 parts of length//3 each.
# The majority of the 3 parts determines the target.
# To get target, at least 2 of the 3 parts must be target.
# So we try all combinations of which 2 or 3 parts are target,
# and sum their dp costs.

# We want to find minimal flips to change the final majority value at the root.
# First, find the original final value by applying the operation N times.
# Then, find minimal flips to get the opposite value.

# Precompute powers of 3
pow3 = [1]
for _ in range(N):
    pow3.append(pow3[-1]*3)

# dp cache: key = (pos, length, target), value = minimal flips
# length is always 3^k, so we can store dp in a dict or list indexed by (pos, k, target)
# k = log3(length)
from functools import lru_cache

@lru_cache(None)
def dp(pos, k, target):
    # segment length = 3^k
    if k == 0:
        # length=1
        return 0 if A[pos] == target else 1
    length = pow3[k]
    part_len = length // 3
    # We have 3 parts: indices pos, pos+part_len, pos+2*part_len
    # For each part, dp(part_pos, k-1, 0) and dp(part_pos, k-1, 1)
    # To get majority = target, at least 2 parts must be target
    # So we try all combinations of which parts are target and which are not,
    # but only those with majority target (2 or 3 parts target)
    # For each combination, sum dp costs and take minimal

    # For each part, cost to make it 0 or 1
    costs = []
    for i in range(3):
        p = pos + i*part_len
        cost0 = dp(p, k-1, 0)
        cost1 = dp(p, k-1, 1)
        costs.append((cost0, cost1))

    res = 10**15
    # There are 8 combinations of (target or not) for 3 parts
    # We only consider those with majority target (at least 2 parts target)
    # target=0 or 1
    # For each combination, count how many parts are target
    # If count >= 2, sum costs accordingly
    for mask in range(8):
        # mask bit i: 0 means part i target=0, 1 means target=1
        # We want parts with value == target
        # So for each part i:
        # if bit i == target: part is target
        # else: part is not target
        # Actually, we want to assign each part to target or not target
        # But we want majority target, so count how many parts assigned target
        # So we try all assignments of parts to target or not target,
        # but only those with majority target

        # For target=0:
        # parts assigned 0 if bit i == 0
        # For target=1:
        # parts assigned 1 if bit i == 1

        # So for target t:
        # part i assigned target if bit i == t
        # count how many parts assigned target
        count_target = 0
        cost_sum = 0
        for i in range(3):
            bit = (mask >> i) & 1
            if bit == target:
                count_target += 1
                cost_sum += costs[i][target]
            else:
                cost_sum += costs[i][1 - target]
        if count_target >= 2:
            if cost_sum < res:
                res = cost_sum
    return res

# First find original final value
def get_final_value(pos, k):
    if k == 0:
        return A[pos]
    length = pow3[k]
    part_len = length // 3
    vals = [get_final_value(pos + i*part_len, k-1) for i in range(3)]
    # majority
    s = sum(vals)
    return 1 if s >= 2 else 0

orig_val = get_final_value(0, N)
# minimal flips to get opposite value
ans = dp(0, N, 1 - orig_val)
print(ans)