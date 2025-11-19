import sys
input = sys.stdin.readline

MOD = 998244353

# Explanation:
# We want sequences A of length N with elements in [0, 2^M),
# such that for any i<j, popcount(A_i XOR A_j) ≤ 2.
#
# This means the Hamming distance between any two elements is at most 2.
#
# Let's analyze the structure of such sets:
#
# - If all elements are the same, condition holds trivially.
# - If elements differ, their pairwise XOR has popcount ≤ 2.
#
# The set of elements forms a code with max pairwise distance 2.
#
# Possible structures:
# 1) All elements equal: size N ≤ 2^M (trivial)
# 2) Elements differ by at most 2 bits.
#
# Let's consider the maximum size of such a set:
#
# The maximum size of a set of binary strings of length M with pairwise Hamming distance ≤ 2
# is at most 1 + M + M*(M-1)/2.
#
# Why?
# Because:
# - The center element (call it c)
# - All elements differing from c in exactly 1 bit: M elements
# - All elements differing from c in exactly 2 bits: C(M,2) elements
#
# Any other element differing in 3 or more bits from c would have distance > 2.
#
# Also, any two elements in this set differ by at most 2 bits:
# - Between two 1-bit difference elements: differ in at most 2 bits
# - Between 1-bit and 2-bit difference elements: differ in at most 2 bits
# - Between two 2-bit difference elements: differ in at most 2 bits
#
# So the maximum size of such a set is S = 1 + M + M*(M-1)/2.
#
# If N > S, answer is 0.
#
# If N ≤ S, how many sequences of length N can we form from this set?
#
# The set size is S.
# We want sequences of length N from these S elements.
# The only condition is that all elements are from this set.
#
# So the answer is S^N mod MOD.
#
# But we must confirm that any sequence of length N from this set satisfies the condition.
#
# Since the set is constructed so that any two elements differ in at most 2 bits,
# any pair in the sequence satisfies popcount(A_i XOR A_j) ≤ 2.
#
# So the answer is:
# - If N > S: 0
# - Else: S^N mod MOD
#
# Note: 2^M can be very large, but we only need S = 1 + M + M*(M-1)//2.
#
# Implementation:
# For each test case:
#   Compute S = 1 + M + M*(M-1)//2
#   If N > S: print 0
#   Else: print pow(S, N, MOD)

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    S = 1 + M + (M * (M - 1) // 2)
    if N > S:
        print(0)
    else:
        print(pow(S, N, MOD))