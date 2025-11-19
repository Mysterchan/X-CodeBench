import sys
input = sys.stdin.readline

# Explanation:
# The game can be analyzed using Sprague-Grundy theorem (Nimbers).
# Each token is like an independent pile.
# The moves allow moving tokens from column j to column j-1 along some path.
# The key insight (from editorial and problem analysis) is:
# The Grundy number of a token at (x, y) is (y - 1).
# Because from column y, the token can be moved to column y-1, y-2, ..., 1,
# and the moves correspond to decreasing the column number by at least 1.
# The row coordinate does not affect the Grundy number.
#
# So the nimber of the whole position is XOR of (y_i - 1) for all tokens.
# If XOR != 0, first player (Mimo) wins, else second player (Yuyu) wins.

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    xor_sum = 0
    for __ in range(k):
        x, y = map(int, input().split())
        xor_sum ^= (y - 1)
    print("Mimo" if xor_sum != 0 else "Yuyu")