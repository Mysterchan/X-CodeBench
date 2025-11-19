def count_knight_tours(H, W):
    MOD = 998244353
    if H % 2 == 1 and W % 2 == 1:
        return 0
    else:
        # Calculate the number of tours
        total_moves = H * W
        res = 1
        for i in range(total_moves - 1):
            res = res * 2 % MOD
        return res

# Read input
H, W = map(int, input().split())
# Output the result
print(count_knight_tours(H, W))