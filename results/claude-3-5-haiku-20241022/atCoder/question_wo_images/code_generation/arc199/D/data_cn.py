MOD = 998244353

H, W = map(int, input().split())

# dp[r_profile] = (count, sum_of_sums)
# r_profile represents the current row configuration
# We process row by row

dp = {tuple([0]*W): (1, 0)}

for i in range(1, H+1):
    new_dp = {}
    for r_profile, (cnt, total_sum) in dp.items():
        # Try all possible values for r[i] (0 to W)
        for r_i in range(W+1):
            # Calculate minimum c values needed
            new_profile = list(r_profile)
            for j in range(r_i):
                new_profile[j] = max(new_profile[j], i)
            new_profile = tuple(new_profile)
            
            # Calculate contribution
            row_contrib = r_i
            col_contrib = sum(new_profile)
            overlap = sum(min(r_i, new_profile[j]) for j in range(W))
            contrib = row_contrib + col_contrib - overlap
            
            # Count ways to extend c values above minimum
            ways = 1
            for j in range(W):
                ways = (ways * (H - new_profile[j] + 1)) % MOD
            
            new_sum = (total_sum + cnt * contrib) % MOD
            
            if new_profile not in new_dp:
                new_dp[new_profile] = (0, 0)
            new_dp[new_profile] = ((new_dp[new_profile][0] + cnt) % MOD, 
                                   (new_dp[new_profile][1] + new_sum) % MOD)
    dp = new_dp

result = sum(total_sum for cnt, total_sum in dp.values()) % MOD
print(result)