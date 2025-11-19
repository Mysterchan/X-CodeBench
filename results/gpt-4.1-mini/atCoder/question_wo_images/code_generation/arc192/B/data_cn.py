N = int(input())
A = list(map(int, input().split()))

# Fennec picks indices from the left (1 to N)
# Snuke picks indices from the right (N to 1)
# Each player tries to add indices to S by decrementing A_i at that index at least once.
# The game ends when S = {1,2,...,N}, i.e., all indices have been chosen at least once.
# The player who makes the last move (adding the last missing index to S) wins.

# The key insight:
# - Each index must be chosen at least once to be added to S.
# - Players alternate turns, starting with Fennec.
# - Fennec will try to add indices from the left.
# - Snuke will try to add indices from the right.
# - The game ends when the sets chosen by both players cover all indices.
# - The player who adds the last index to S wins.

# We find the smallest prefix from the left where Fennec can add all indices (A_i > 0)
# and the smallest suffix from the right where Snuke can add all indices (A_i > 0).
# The intersection point determines who gets the last index.

l = 0
while l < N and A[l] > 0:
    l += 1

r = N - 1
while r >= 0 and A[r] > 0:
    r -= 1

# If l > r, it means the sets chosen by Fennec and Snuke overlap or meet,
# so Fennec gets the last index and wins.
# Otherwise, Snuke wins.

if l > r:
    print("Fennec")
else:
    print("Snuke")