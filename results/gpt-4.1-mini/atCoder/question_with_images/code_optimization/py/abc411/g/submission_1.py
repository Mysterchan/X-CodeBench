import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mod = 998244353

graph = [[0]*N for _ in range(N)]
for _ in range(M):
    U, V = map(lambda x: int(x)-1, input().split())
    graph[U][V] += 1
    graph[V][U] += 1

ans = 0

# Precompute popcount for all subsets up to size N
popcount = [0]*(1<<N)
for i in range(1, 1<<N):
    popcount[i] = popcount[i>>1] + (i&1)

# For each s from 2 to N-1, count cycles involving vertex s and vertices < s
for s in range(2, N):
    size = s + 1
    full_mask = 1 << size
    DP = [ [0]*(size) for _ in range(full_mask) ]
    DP[1 << s][s] = 1

    # Iterate over subsets containing s
    for bit in range(1 << s, full_mask):
        # Skip subsets not containing s
        if (bit & (1 << s)) == 0:
            continue
        for i in range(size):
            if (bit >> i) & 1 == 0 or DP[bit][i] == 0:
                continue
            val = DP[bit][i]
            # Try to add vertex j < s not in bit
            for j in range(s):
                if (bit >> j) & 1:
                    continue
                w = graph[i][j]
                if w:
                    DP[bit | (1 << j)][j] = (DP[bit | (1 << j)][j] + val * w) % mod

    # Subtract paths that directly close cycle at s to avoid counting paths of length 1
    for i in range(s):
        DP[(1 << s) | (1 << i)][i] = (DP[(1 << s) | (1 << i)][i] - graph[i][s]) % mod

    # Sum up cycles closing at s
    for bit in range(1 << s, full_mask):
        if (bit & (1 << s)) == 0:
            continue
        for i in range(s):
            if (bit >> i) & 1:
                w = graph[i][s]
                if w:
                    ans = (ans + DP[bit][i] * w) % mod

# Each cycle counted twice (once in each direction), so divide by 2 modulo
inv2 = (mod + 1) // 2
ans = (ans * inv2) % mod

# Add cycles of length 2 (multi-edges)
for i in range(N):
    for j in range(i+1, N):
        c = graph[i][j]
        if c >= 2:
            ans = (ans + c * (c - 1) // 2) % mod

print(ans)