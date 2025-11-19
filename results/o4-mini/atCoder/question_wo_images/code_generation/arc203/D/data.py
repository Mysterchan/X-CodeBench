import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

# The problem reduces to:
# Given A, find minimal |B| such that by repeatedly inserting B_i XOR B_{i+1} between B_i and B_{i+1},
# we can get A.
#
# It can be shown that the minimal |B| = number_of_runs_in_A + 1
# where a run is a maximal consecutive segment of equal bits.
#
# Why?
# Each insertion doubles the length minus 1, and the sequence A can be seen as a "derived" sequence
# from B by repeated insertions of XORs.
#
# The minimal B corresponds to the "run boundaries" in A.
#
# So minimal |B| = number_of_runs_in_A + 1
#
# We need to maintain the number of runs in A efficiently after each flip query.
#
# A run boundary is at position i if A[i] != A[i-1].
# Number of runs = 1 + number_of_boundaries
#
# We will maintain the count of boundaries and update it after each flip.

# Precompute initial boundaries count
boundaries = 0
for i in range(1, N):
    if A[i] != A[i-1]:
        boundaries += 1

for _ in range(Q):
    i = int(input()) - 1
    old_val = A[i]
    new_val = 1 - old_val
    A[i] = new_val

    # Check boundaries at i and i+1 (if valid)
    # Positions to check: i (boundary between i-1 and i), i+1 (boundary between i and i+1)
    # For i > 0, boundary at i means A[i] != A[i-1]
    if i > 0:
        # Before flip
        old_boundary = (old_val != A[i-1])
        new_boundary = (new_val != A[i-1])
        if old_boundary != new_boundary:
            boundaries += 1 if new_boundary else -1

    if i < N - 1:
        # boundary at i+1 means A[i+1] != A[i]
        old_boundary = (A[i+1] != old_val)
        new_boundary = (A[i+1] != new_val)
        if old_boundary != new_boundary:
            boundaries += 1 if new_boundary else -1

    # minimal |B| = boundaries + 1
    print(boundaries + 1)