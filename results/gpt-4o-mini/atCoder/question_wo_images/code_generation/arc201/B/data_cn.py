import sys
from collections import defaultdict

input = sys.stdin.read
data = input().splitlines()

def solve():
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        N, W = map(int, data[index].split())
        index += 1
        
        items = defaultdict(int)
        
        for __ in range(N):
            X, Y = map(int, data[index].split())
            weight = 1 << X  # 2 ** X is equivalent to 1 << X
            if weight <= W:
                items[weight] = max(items[weight], Y)  # Keep the max value for the same weight
            index += 1
        
        # Extract weights and their max values, then apply 0/1 knapsack algorithm
        weights = list(items.keys())
        values = list(items.values())
        
        dp = [0] * (W + 1)
        
        for i in range(len(weights)):
            weight = weights[i]
            value = values[i]
            for w in range(W, weight - 1, -1):
                dp[w] = max(dp[w], dp[w - weight] + value)
        
        results.append(dp[W])
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

solve()