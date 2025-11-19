INF = 10**10

def solve(h, w, S):
    # Precompute all subsets of each row's black cells with their repaint cost
    B = [0]*h
    for i in range(h):
        bitmask = 0
        for j in range(w):
            if S[i][j] == "#":
                bitmask |= 1 << j
        B[i] = bitmask

    # For each row, generate all subsets of black cells to repaint and store cost
    memo = []
    for base in B:
        subsets = []
        # Enumerate subsets of base (black cells)
        sub = base
        while True:
            cost = bin(base ^ sub).count('1')  # number of repainted cells
            subsets.append((sub, cost))
            if sub == 0:
                break
            sub = (sub - 1) & base
        memo.append(subsets)

    # Precompute satisfied pairs for all pairs of bitmasks
    # Condition: no 2x2 block of black cells in adjacent rows
    # For each pair of rows (bitmask1, bitmask2), check all columns j in [0, w-2]
    # If any 2x2 block is all black, fail
    def satisfied(upper, lower):
        # upper and lower are bitmasks representing black cells in two adjacent rows
        # Check for any 2x2 black block
        # For j in [0, w-2], check bits j and j+1 in upper and lower
        # If all four bits are 1, fail
        mask = (1 << (w - 1)) - 1  # mask for w-1 bits
        # Shifted masks for pairs of bits
        upper_pairs = (upper & (upper >> 1)) & mask
        lower_pairs = (lower & (lower >> 1)) & mask
        # 2x2 black block exists if upper_pairs & lower_pairs != 0
        return (upper_pairs & lower_pairs) == 0

    dp = [dict() for _ in range(h)]
    # Initialize dp for first row
    for bitmask, cost in memo[0]:
        dp[0][bitmask] = cost

    for i in range(1, h):
        dp_prev = dp[i-1]
        dp_curr = dp[i]
        for bitmask, cost in memo[i]:
            # For each previous bitmask, check if satisfied
            for prev_bitmask, prev_cost in dp_prev.items():
                if satisfied(prev_bitmask, bitmask):
                    total_cost = prev_cost + cost
                    if bitmask not in dp_curr or dp_curr[bitmask] > total_cost:
                        dp_curr[bitmask] = total_cost

    return min(dp[-1].values())

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        h, w = map(int, input().split())
        S = [input().rstrip() for _ in range(h)]
        print(solve(h, w, S))