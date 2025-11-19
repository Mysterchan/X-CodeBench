def count_permutations(t, test_cases):
    MOD = 998244353
    results = []
    
    for n, m, parents, colors, depths in test_cases:
        color_count = [[0, 0] for _ in range(n + 1)]

        # Count chips by color at each depth
        for idx in range(m):
            color_count[depths[idx]][colors[idx]] += 1

        # DP table to count permutations
        dp = [1]  # Starting with 1 way to arrange 0 elements
        
        # Calculating the number of ways to arrange chips
        for depth in range(1, n + 1):
            b_count = color_count[depth][0]  # Number of black chips
            w_count = color_count[depth][1]  # Number of white chips
            
            total_chips = b_count + w_count
            if total_chips == 0:
                dp.append(dp[-1])  # No new chips, same as before
            else:
                # Update number of permutations using factorials
                ways = dp[-1]
                for i in range(total_chips):
                    ways = (ways * (total_chips - i)) % MOD
                
                # Divide by factorial of counts to account for duplications
                if b_count > 1:
                    for i in range(1, b_count + 1):
                        ways = (ways * pow(i, MOD - 2, MOD)) % MOD
                if w_count > 1:
                    for i in range(1, w_count + 1):
                        ways = (ways * pow(i, MOD - 2, MOD)) % MOD

                dp.append(ways)

        results.append(dp[n])  # The result for this test case

    return results

# Read input
t = int(input())
test_cases = []

for _ in range(t):
    n, m = map(int, input().split())
    parents = list(map(int, input().split()))
    colors = list(map(int, input().split()))
    depths = list(map(int, input().split()))
    test_cases.append((n, m, parents, colors, depths))

# Output results
results = count_permutations(t, test_cases)
for result in results:
    print(result)