def count_ways(N, H, W):
    MOD = 998244353
    if H < N or W < N:
        return 0
    if H > 2 * N and W > 2 * N:
        return 0
    if H == N and W == N:
        return 1
    
    # Calculate the number of ways to place the tiles
    ways = 0
    for h in range(0, H - N + 1):
        for w in range(0, W - N + 1):
            if (h // N) * (w // N) >= 4:
                ways += 1
    
    return ways % MOD

import sys
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
results = []
for i in range(1, T + 1):
    N, H, W = map(int, data[i].split())
    results.append(count_ways(N, H, W))

print('\n'.join(map(str, results)))