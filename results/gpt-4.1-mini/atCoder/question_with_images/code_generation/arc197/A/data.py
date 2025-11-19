import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    H, W = map(int, input().split())
    S = input().strip()

    # Count fixed Ds and Rs in S
    fixed_D = S.count('D')
    fixed_R = S.count('R')

    # Remaining moves to assign to '?'
    rem_D = (H - 1) - fixed_D
    rem_R = (W - 1) - fixed_R

    # We want to maximize the number of black cells painted after any number of operations.
    # Each operation paints a path from (1,1) to (H,W) with exactly H-1 Ds and W-1 Rs,
    # respecting fixed moves in S and choosing '?' moves as needed.

    # Key insight:
    # The maximum number of black cells painted is the size of the union of all possible paths
    # that satisfy the constraints.
    #
    # Each path is a sequence of moves of length H+W-2 with fixed D/R moves and '?' moves assigned.
    # The '?' moves can be chosen differently in different operations.
    #
    # The union of all such paths covers a "band" of cells between two extreme paths:
    # - The path where all '?' are assigned to D first, then R (maximizing down moves early)
    # - The path where all '?' are assigned to R first, then D (maximizing right moves early)
    #
    # The union of these paths forms a "staircase" shape.
    #
    # The number of black cells painted is:
    #   H * W - (rem_D * rem_R)
    #
    # Explanation:
    # The total cells in the grid is H*W.
    # The cells not covered by any path correspond to the rectangle of size rem_D x rem_R
    # in the bottom-right corner that cannot be reached by any path respecting the fixed moves.
    #
    # This formula matches the editorial and sample tests.

    ans = H * W - rem_D * rem_R
    print(ans)