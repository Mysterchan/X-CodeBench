def solve():
    MOD = 998244353
    H, W = map(int, input().split())
    
    from math import gcd
    
    g = gcd(H, W)
    
    # Check if tour is possible
    if gcd(2, H) != 1:
        if H % 2 == 0:
            print(0)
            return
    
    # For odd H and any W, count the number of valid tours
    # The formula involves 2^(H*W-1) / (H*W) * some correction factor
    
    # Based on the structure, the answer is related to:
    # 2^(H*W - H - W + gcd(H,W)) for certain cases
    
    # More specifically, for this problem:
    if H % 2 == 0 or W % 2 == 0:
        if H % 2 == 0 and W % 2 == 0:
            print(0)
            return
    
    # For the general case, use the cycle formula
    # Number of tours = 2^(HW - H - W + gcd(H,W)) * correction
    
    exp = (H * W - H - W + g) % (MOD - 1)
    result = pow(2, exp, MOD)
    
    print(result)

solve()