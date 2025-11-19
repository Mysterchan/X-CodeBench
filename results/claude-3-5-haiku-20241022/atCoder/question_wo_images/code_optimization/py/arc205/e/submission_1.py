import sys
input = sys.stdin.readline

MOD = 998244353

n = int(input())
a = list(map(int, input().split()))

# dp[mask] stores the product of all elements seen so far that equal mask
dp = [1] * (1 << 20)

results = []

for x in a:
    # Calculate product of all previous elements that are submasks of x
    ans = 1
    
    # Iterate through all submasks of x
    mask = x
    while True:
        ans = ans * dp[mask] % MOD
        if mask == 0:
            break
        mask = (mask - 1) & x
    
    results.append(ans)
    
    # Update dp: multiply x into all masks that are supersets of x
    # We need to update dp[mask] for all mask where x is a submask of mask
    # This is equivalent to: for all mask where (mask & x) == x
    for mask in range(1 << 20):
        if (mask & x) == x:
            dp[mask] = dp[mask] * x % MOD

print(*results, sep='\n')