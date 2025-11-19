def mod_inv(a, p):
    return pow(a, p - 2, p)

def count_paths(W, H, L, R, D, U):
    MOD = 998244353

    # Calculate the number of blocks in each region
    total_blocks = (W + 1) * (H + 1)
    blocked_blocks = (R - L) * (U - D) if R > L and U > D else 0
    valid_blocks = total_blocks - blocked_blocks

    # Calculate the number of paths from each valid block
    paths = 0
    for x in range(W + 1):
        for y in range(H + 1):
            if (x < L or R < x or y < D or U < y):
                # Calculate the number of paths from (0, 0) to (x, y)
                paths_from_origin = (mod_inv(x + y + 1, MOD) * (x + y) % MOD) % MOD
                paths = (paths + paths_from_origin) % MOD

    return paths

W, H, L, R, D, U = map(int, input().split())
print(count_paths(W, H, L, R, D, U))