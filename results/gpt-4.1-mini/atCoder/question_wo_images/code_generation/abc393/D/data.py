def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    S = input().strip()

    # Extract positions of all '1's (0-based indexing)
    ones = [i for i, ch in enumerate(S) if ch == '1']
    k = len(ones)

    # If all 1s are already contiguous, no swaps needed
    # But we will handle this naturally by the calculation below

    # The idea:
    # We want to move all 1s to a contiguous block.
    # The minimal cost is achieved by aligning the 1s around the median position.
    # The cost is sum of absolute differences between current positions and target positions.
    #
    # Let ones = [p0, p1, ..., p_{k-1}]
    # We want to place them at positions x, x+1, ..., x+k-1 for some x.
    # The cost = sum |p_i - (x + i)|
    #
    # To minimize cost, choose x so that p_i - i is as close as possible to a constant.
    # The minimal sum of absolute differences is achieved by choosing x so that
    # the sequence (p_i - i) is centered around its median.
    #
    # So:
    # Define adjusted = [p_i - i for i in range(k)]
    # Find median m of adjusted
    # cost = sum |adjusted[i] - m|

    adjusted = [ones[i] - i for i in range(k)]
    adjusted.sort()
    median = adjusted[k // 2]

    cost = sum(abs(x - median) for x in adjusted)
    print(cost)

if __name__ == "__main__":
    main()