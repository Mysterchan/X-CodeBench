def solve(H, W):
    MOD = 998244353
    
    from math import gcd
    
    g = gcd(H, W)
    
    # Check if Hamiltonian cycle is possible
    # For knight tour on torus with move (-2, ±1)
    # We need H and W to satisfy certain conditions
    
    if H % 2 == 1 and W % 2 == 0:
        return 0
    
    if H % 2 == 0 and W % 2 == 1:
        # Check divisibility
        if (H * W) % 2 != 0:
            return 0
    
    # For valid cases, compute the number of tours
    # The formula is 2^(HW/g - 1) for certain configurations
    
    if H % 2 == 1 and W % 2 == 1:
        # Both odd - special case
        n = H * W // g
        result = pow(2, n - 1, MOD)
        return result
    else:
        # At least one is even
        n = H * W // g
        result = pow(2, n - 1, MOD)
        return result

H, W = map(int, input().split())
print(solve(H, W))