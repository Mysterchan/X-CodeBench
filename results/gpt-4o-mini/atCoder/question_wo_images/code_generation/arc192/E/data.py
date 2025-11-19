def count_paths(W, H, L, R, D, U):
    MOD = 998244353

    # Calculate the number of blocks in each region
    # Region 1: (0, 0) to (L-1, H) and (0, 0) to (W, D-1)
    count1 = L * (H + 1) + (W + 1) * D - L * D

    # Region 2: (R+1, 0) to (W, H) and (R+1, D) to (W, U)
    count2 = (W - R) * (H + 1) + (W + 1) * (U - D) - (W - R) * (U - D)

    # Region 3: (0, U+1) to (L-1, H) and (0, U+1) to (R, H)
    count3 = L * (H - U) + (R + 1) * (H - U)

    # Region 4: (R+1, U+1) to (W, H)
    count4 = (W - R) * (H - U)

    # Total blocks
    total_blocks = (count1 + count2 + count3 + count4) % MOD

    # Calculate the number of paths
    # Each block can be a starting point, and from each block, we can move to the right or up
    # The number of paths from a block (x, y) to (W, H) is (W - x) + (H - y)
    # The total number of paths is the sum of paths from all blocks

    total_paths = 0
    for x in range(W + 1):
        for y in range(H + 1):
            if (x < L or x > R) and (y < D or y > U):
                total_paths += (W - x + H - y) % MOD
                total_paths %= MOD

    return total_paths

# Read input
W, H, L, R, D, U = map(int, input().split())
# Print the result
print(count_paths(W, H, L, R, D, U))