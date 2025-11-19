def count_winning_ways(N, X, Y, bags):
    MOD = 998244353
    total_ways = 0

    for mask in range(1 << N):
        takashi_gold = 0
        takashi_silver = 0
        aoki_gold = 0
        aoki_silver = 0
        
        for i in range(N):
            if mask & (1 << i):
                takashi_gold += bags[i][0]
                takashi_silver += bags[i][1]
            else:
                aoki_gold += bags[i][0]
                aoki_silver += bags[i][1]

        if (takashi_gold > 0 or takashi_silver > 0) and (aoki_gold > 0 or aoki_silver > 0):
            # Check if Takashi can win
            if (takashi_gold > 0 and (takashi_silver + X) > aoki_silver) or (aoki_gold > 0 and (aoki_silver + Y) > takashi_silver):
                total_ways += 1
                total_ways %= MOD

    return total_ways

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

N, X, Y = map(int, data[0].split())
bags = [tuple(map(int, line.split())) for line in data[1:N+1]]

# Calculate and print the result
result = count_winning_ways(N, X, Y, bags)
print(result)