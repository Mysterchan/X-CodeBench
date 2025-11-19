def solve():
    MOD = 998244353
    N, X, Y = map(int, input().split())
    bags = []
    for _ in range(N):
        a, b = map(int, input().split())
        bags.append((a, b))
    
    # Compute Grundy number for each bag
    memo = {}
    
    def grundy(g, s, player):
        # player: 0 = Takahashi, 1 = Aoki
        if (g, s, player) in memo:
            return memo[(g, s, player)]
        
        if g == 0 and s == 0:
            return 0
        
        moves = set()
        
        # Remove 1 gold, add X/Y silver
        if g > 0:
            add = X if player == 0 else Y
            # After this move, it becomes opponent's turn
            moves.add(grundy(g - 1, s + add, 1 - player))
        
        # Remove 1 silver
        if s > 0:
            moves.add(grundy(g, s - 1, 1 - player))
        
        # MEX
        mex = 0
        while mex in moves:
            mex += 1
        
        memo[(g, s, player)] = mex
        return mex
    
    # For large values, we need to optimize
    # Key observation: Grundy values stabilize after some point
    bag_grundy = []
    for a, b in bags:
        # Compute Grundy for this bag when Takahashi starts with it
        g = grundy(a, b, 0)
        bag_grundy.append(g)
    
    # Count subsets where XOR is non-zero
    # Use DP: dp[xor_val] = count of subsets with that XOR
    dp = {0: 1}
    
    for g in bag_grundy:
        new_dp = {}
        for xor_val, cnt in dp.items():
            # Don't take this bag
            new_dp[xor_val] = (new_dp.get(xor_val, 0) + cnt) % MOD
            # Take this bag
            new_xor = xor_val ^ g
            new_dp[new_xor] = (new_dp.get(new_xor, 0) + cnt) % MOD
        dp = new_dp
    
    # Sum all non-zero XOR values
    result = sum(cnt for xor_val, cnt in dp.items() if xor_val != 0) % MOD
    print(result)

solve()