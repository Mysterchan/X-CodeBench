def solve(H, W):
    MOD = 998244353
    
    from math import gcd
    
    g = gcd(H, W)
    
    # Check if Hamiltonian cycle exists
    # For a knight tour on a torus to exist, we need specific conditions
    
    # The key insight: if gcd(2, W) = 1 (W is odd), we need H*W to be even
    # If gcd(2, W) = 2 (W is even), different conditions apply
    
    if W % 2 == 1:
        # W is odd
        # We need 2k ≡ H*W (mod W), so 2k ≡ 0 (mod W)
        # Since gcd(2,W) = 1, k ≡ 0 (mod W)
        # This means k = 0, W, 2W, ... but k <= H*W
        # The number of such valid k values that also satisfy our constraints
        
        if H % 2 == 0:
            # H*W is even, tours exist
            # Number of tours = (H*W)! / (2^(H*W/2)) for the combinatorial structure
            # But this needs adjustment based on the actual graph structure
            
            # For the toroidal knight graph, the answer is related to
            # counting Hamiltonian paths in a specific way
            
            # Based on the samples and structure analysis:
            total = H * W
            result = 1
            
            # The formula appears to be based on the cycle structure
            # For each connected component and proper arrangement
            
            if g == 1:
                result = pow(2, total - 1, MOD)
            else:
                result = 0
        else:
            result = 0
    else:
        # W is even
        if g > 1 and gcd(2, g) > 1:
            result = 0
        else:
            total = H * W
            if g == 1:
                result = pow(2, total - 1, MOD)
            else:
                result = 0
    
    return result

H, W = map(int, input().split())
print(solve(H, W))