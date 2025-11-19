def max_value_per_case(N, W, items):
    dp = [0] * (W + 1)
    
    for x, y in items:
        weight = 1 << x  # 2^X_i
        if weight > W:
            continue
        for j in range(W, weight - 1, -1):
            dp[j] = max(dp[j], dp[j - weight] + y)
    
    return max(dp)

import sys
input = sys.stdin.read

def main():
    data = input().split()
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        W = int(data[index + 1])
        index += 2
        
        items = []
        for _ in range(N):
            X = int(data[index])
            Y = int(data[index + 1])
            items.append((X, Y))
            index += 2
            
        results.append(max_value_per_case(N, W, items))
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

main()