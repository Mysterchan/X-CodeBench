def compute_grundy(a, b, x, y):
    memo = {}
    
    def grundy(gold, silver, is_takahashi):
        if gold == 0 and silver == 0:
            return 0
        
        key = (gold, silver, is_takahashi)
        if key in memo:
            return memo[key]
        
        moves = set()
        add_silver = x if is_takahashi else y
        
        # Convert gold to silver
        if gold > 0:
            new_silver = silver + add_silver
            moves.add(grundy(gold - 1, new_silver, not is_takahashi))
        
        # Remove silver
        if silver > 0:
            moves.add(grundy(gold, silver - 1, not is_takahashi))
        
        # Find mex
        mex = 0
        while mex in moves:
            mex += 1
        
        memo[key] = mex
        return mex
    
    return grundy(a, b, True)

def solve():
    MOD = 998244353
    n, x, y = map(int, input().split())
    bags = []
    for _ in range(n):
        a, b = map(int, input().split())
        bags.append((a, b))
    
    # Compute Grundy number for each bag
    grundy_values = []
    for a, b in bags:
        g = compute_grundy(a, b, x, y)
        grundy_values.append(g)
    
    # Count subsets with XOR = 0
    # dp[xor_value] = count of subsets with that XOR
    dp = {0: 1}
    
    for g in grundy_values:
        new_dp = {}
        for xor_val, count in dp.items():
            # Don't take this bag
            new_dp[xor_val] = new_dp.get(xor_val, 0) + count
            new_dp[xor_val] %= MOD
            # Take this bag
            new_xor = xor_val ^ g
            new_dp[new_xor] = new_dp.get(new_xor, 0) + count
            new_dp[new_xor] %= MOD
        dp = new_dp
    
    print(dp.get(0, 0) % MOD)

solve()