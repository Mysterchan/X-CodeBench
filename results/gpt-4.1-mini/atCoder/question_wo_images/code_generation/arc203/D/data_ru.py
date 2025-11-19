import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

# The problem reduces to:
# minimal |B| = number_of_runs_in_A + 1
# where a run is a maximal consecutive segment of equal bits.
#
# Each query flips A[i], so we need to update the number of runs efficiently.
#
# When flipping A[i], only the boundaries at i-1 and i can change runs count.
#
# Let's maintain the number of runs:
# runs = 1 + number_of_positions j in [1..N-1] where A[j] != A[j-1]
#
# After flipping A[i], update runs accordingly.

runs = 1
for j in range(1, N):
    if A[j] != A[j-1]:
        runs += 1

for _ in range(Q):
    i = int(input()) - 1
    old_val = A[i]
    new_val = 1 - old_val
    A[i] = new_val

    # Check left boundary (i-1, i)
    if i > 0:
        before = (old_val != A[i-1])
        after = (new_val != A[i-1])
        if before and not after:
            runs -= 1
        elif not before and after:
            runs += 1

    # Check right boundary (i, i+1)
    if i < N - 1:
        before = (old_val != A[i+1])
        after = (new_val != A[i+1])
        if before and not after:
            runs -= 1
        elif not before and after:
            runs += 1

    print(runs + 1)