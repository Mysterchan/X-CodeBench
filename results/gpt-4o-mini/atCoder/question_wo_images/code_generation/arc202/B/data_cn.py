def compute_tours(H, W):
    MOD = 998244353
    if H % 2 == 0 and W % 2 == 0:
        return 0
    if H % 2 == 1 and W % 2 == 1:
        return 2
    return 6

H, W = map(int, input().split())
print(compute_tours(H, W))