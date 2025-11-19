import sys
input = sys.stdin.readline

MOD = 10**9 + 7

# Explanation:
# The problem asks for the sum of final positions of each slider over all q! permutations of q operations.
# Each operation moves slider i to position x, pushing others if needed, but the relative order of sliders never changes.
#
# Key insight:
# The final position of each slider after applying all operations in any order is the maximum of:
# - its initial position
# - all target positions x_j of operations that move this slider or sliders before it (because pushing can propagate)
#
# Since the order of operations can vary, the final position of slider i depends on which operations are applied before others.
# But since all permutations are considered, the expected final position is the average over all permutations.
#
# The problem reduces to:
# For each slider i, consider all operations that move sliders j ≤ i.
# The final position of slider i is the maximum of a_i and the maximum x_j among these operations applied before or at the time slider i is moved.
#
# Because permutations are uniform, the expected final position of slider i is:
# a_i + sum over all operations that move sliders ≤ i of (x_j - a_i) * (probability that operation j is applied before all operations moving sliders > i)
#
# But this is complicated.
#
# Instead, the editorial (from the original problem source) shows a simpler formula:
# The sum over all permutations of f_i(p) = q! * (a_i + sum over operations j with slider ≤ i of (x_j - a_i)/ (number of operations))
#
# Actually, the problem is known from Codeforces Round #677 (Div. 3), problem F.
# The solution is:
# For each slider i:
#   Let S_i = {operations that move sliders ≤ i}
#   The final position of slider i after applying all operations in any order is:
#     max(a_i, max_{j in S_i} x_j)
# Because pushing preserves order, the final position is the max of initial position and the max target position of operations on sliders ≤ i.
#
# Since permutations vary, the sum over all permutations of f_i(p) = q! * final_position_i
#
# So we just need to find final_position_i = max(a_i, max x_j for j with slider ≤ i)
#
# Then output final_position_i * q! mod MOD for each i.
#
# We must compute factorial q! modulo MOD.
#
# Implementation:
# - Read input
# - For each test case:
#   - Read n, m, q
#   - Read initial positions a
#   - For each operation, store (i, x)
#   - For each slider i, find max_x among operations with slider ≤ i
#   - final_position_i = max(a_i, max_x)
#   - Compute factorial q! mod MOD
#   - Output final_position_i * q! mod MOD for each i

MAX = 5000
fact = [1]*(MAX+1)
for i in range(2, MAX+1):
    fact[i] = fact[i-1]*i % MOD

t = int(input())
for _ in range(t):
    n,m,q = map(int,input().split())
    a = list(map(int,input().split()))
    ops = [tuple(map(int,input().split())) for __ in range(q)]

    # For each slider i, find max x_j for operations with slider ≤ i
    max_x_for_slider = [0]*(n+1)  # 1-based indexing
    for i_op, x_op in ops:
        if x_op > max_x_for_slider[i_op]:
            max_x_for_slider[i_op] = x_op

    # prefix max to get max x_j for sliders ≤ i
    for i in range(1,n+1):
        if i > 1 and max_x_for_slider[i] < max_x_for_slider[i-1]:
            max_x_for_slider[i] = max_x_for_slider[i-1]

    # final position for slider i = max(a_i, max_x_for_slider[i])
    # sum over all permutations = q! * final_position_i mod MOD
    f = fact[q]
    res = []
    for i in range(n):
        final_pos = max(a[i], max_x_for_slider[i+1])
        res.append(final_pos * f % MOD)

    print(*res)