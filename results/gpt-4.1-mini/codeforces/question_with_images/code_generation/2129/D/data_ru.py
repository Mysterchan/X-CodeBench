import sys
input = sys.stdin.readline

MOD = 998244353

# Precompute factorials and inverse factorials for n up to 100
MAXN = 100
fact = [1] * (MAXN + 1)
inv_fact = [1] * (MAXN + 1)

def modinv(a, m=MOD):
    # Fermat's little theorem for prime m
    return pow(a, m - 2, m)

for i in range(2, MAXN + 1):
    fact[i] = fact[i-1] * i % MOD
inv_fact[MAXN] = modinv(fact[MAXN], MOD)
for i in reversed(range(1, MAXN)):
    inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

def comb(n, k):
    if k > n or k < 0:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n-k] % MOD

# Explanation of the problem and approach:
# The problem describes a process of painting cells in order p_1,...,p_n.
# At step i, if i>1, we find the closest black cell to p_i and increment its score by 1.
# Then paint p_i black.
# After all steps, s_i is the score of cell i.
#
# Given partial s (some s_i fixed, some -1), count how many permutations p produce s.
#
# Key observations:
# - The first painted cell p_1 has s_{p_1} = 0 (no increments).
# - For i>1, s_{p_i} counts how many times this cell was the closest black cell to some future painted cell.
# - The sum of all s_i is n-1 (since each step i>1 increments exactly one black cell's score).
#
# The problem is equivalent to counting permutations p such that the "score" s matches the increments distribution.
#
# Approach:
# 1) Check feasibility:
#    - sum of known s_i must be <= n-1
#    - s_i >= 0 or -1 (unknown)
#    - s_i <= n-1
# 2) The first painted cell p_1 must have s_{p_1} = 0.
#    So at least one cell with s_i=0 (or unknown) must be chosen as p_1.
# 3) The painting order p is a permutation of [1..n].
#    The painting order induces a tree structure:
#    - p_1 is root (score 0)
#    - For i>1, p_i's score counts how many times it was closest black cell to future painted cells.
#    - This corresponds to a rooted tree with edges from parent to children.
#    - s_i = number of children of node i in this tree.
#
# So s_i is the outdegree of node i in the tree.
# The sum of s_i = n-1 (number of edges in tree).
#
# The problem reduces to:
# Given partial outdegree sequence s (some known, some unknown),
# count the number of rooted trees on n nodes with outdegree sequence s,
# where the root is the node with s_i=0 chosen as p_1.
#
# But the root must have s_root=0.
# If multiple nodes have s_i=0 or unknown, root can be any of them.
#
# The number of rooted trees with given outdegree sequence s is:
#   number of ways to arrange children for each node,
#   but since nodes are distinct, the count is:
#   number of ways to assign children to nodes respecting outdegree s.
#
# The number of trees with given outdegree sequence s is:
#   n! / (product of s_i!),
#   if sum s_i = n-1 and s_i >= 0.
#
# But we have unknown s_i = -1.
#
# So the problem is:
# - Assign values to unknown s_i >= 0,
# - sum s_i = n-1,
# - s_i fixed for known,
# - s_root = 0 (root node),
# - count number of such assignments,
# - for each assignment, number of trees = n! / product(s_i!),
# - sum over all assignments.
#
# Also, root must be chosen among nodes with s_i=0 or unknown.
#
# So the algorithm:
# For each candidate root r (s_r=0 or s_r=-1):
#   Fix s_r=0 (if unknown)
#   Let known sum = sum of fixed s_i (excluding s_r)
#   Let unknown positions = positions with s_i=-1 except r
#   Let total unknown sum = n-1 - known sum
#   Count number of integer solutions to:
#       sum of unknown s_i = total unknown sum
#       s_i >= 0
#   For each solution:
#       compute product of factorials of s_i
#       add n! * inv(product of factorials) to answer
#
# Since n <= 100, and number of unknowns <= n,
# we can do DP over unknowns and sum.
#
# Finally sum over all possible roots.
#
# Implementation details:
# - For each test:
#   - Identify candidate roots
#   - For each root:
#       - Fix s_r=0 if unknown
#       - Compute known sum
#       - unknown positions = unknown except root
#       - DP over unknown positions to count sum of n! / product(s_i!)
# - Sum over roots
#
# Edge cases:
# - If no candidate root, answer = 0
# - If sum known s_i > n-1, answer = 0
# - If any fixed s_i < 0 or > n-1, answer = 0
#
# DP:
# dp[pos][sum] = number of ways to assign s_i to unknown positions up to pos with sum = sum,
# weighted by product of inv_fact[s_i] (to handle division by factorial)
#
# At the end:
# answer += n! * dp[len_unknown][total_unknown_sum] mod MOD
#
# Because:
# number of trees = n! / product(s_i!)
# and dp stores sum over assignments of product(1/s_i!) = product(inv_fact[s_i])
#
# So multiply by n! to get count.

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = list(map(int, input().split()))
        
        # Validate s_i
        if any(x < -1 or x > n-1 for x in s):
            print(0)
            continue
        
        # sum of known s_i (excluding unknown)
        known_sum = 0
        unknown_positions = []
        for i, val in enumerate(s):
            if val == -1:
                unknown_positions.append(i)
            else:
                known_sum += val
        
        # sum s_i must be n-1
        if known_sum > n-1:
            print(0)
            continue
        
        # Candidate roots: positions with s_i=0 or s_i=-1 (unknown)
        candidate_roots = []
        for i in range(n):
            if s[i] == 0 or s[i] == -1:
                candidate_roots.append(i)
        
        if not candidate_roots:
            print(0)
            continue
        
        ans = 0
        
        # Precompute factorials and inverse factorials already done
        
        # For each candidate root
        for root in candidate_roots:
            # Fix s_root = 0
            # Check if s_root fixed and != 0 => invalid
            if s[root] != -1 and s[root] != 0:
                continue
            
            # sum of known s_i excluding root
            known_sum_ex_root = 0
            unknown_pos_ex_root = []
            for i in range(n):
                if i == root:
                    continue
                if s[i] == -1:
                    unknown_pos_ex_root.append(i)
                else:
                    known_sum_ex_root += s[i]
            
            total_unknown_sum = n - 1 - known_sum_ex_root
            if total_unknown_sum < 0:
                continue
            
            # DP over unknown_pos_ex_root
            # dp[pos][sum] = number of ways * product(inv_fact[s_i])
            # Initialize dp
            dp = [0] * (total_unknown_sum + 1)
            dp[0] = 1
            
            for _ in unknown_pos_ex_root:
                ndp = [0] * (total_unknown_sum + 1)
                for curr_sum in range(total_unknown_sum + 1):
                    ways = dp[curr_sum]
                    if ways == 0:
                        continue
                    # s_i can be from 0 to total_unknown_sum - curr_sum
                    max_val = total_unknown_sum - curr_sum
                    # To optimize, we can do prefix sums
                    # But n and total_unknown_sum <= n-1 <= 99, so direct loop is fine
                    for val in range(max_val + 1):
                        ndp[curr_sum + val] = (ndp[curr_sum + val] + ways * inv_fact[val]) % MOD
                dp = ndp
            
            # Now dp[total_unknown_sum] = sum over assignments of product(inv_fact[s_i])
            # Multiply by n! and inv_fact[0] for root (which is 0! = 1)
            # Also multiply by inv_fact[s_root=0] = 1
            ways = dp[total_unknown_sum]
            ways = ways * fact[n] % MOD
            
            ans = (ans + ways) % MOD
        
        print(ans)

if __name__ == "__main__":
    solve()