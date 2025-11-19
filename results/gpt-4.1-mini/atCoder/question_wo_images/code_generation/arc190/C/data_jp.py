import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 998244353

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
Q, sh, sw = map(int, input().split())
sh -= 1
sw -= 1

# Precompute factorials and inverse factorials for combinations
N = H + W + 10
fact = [1] * N
inv_fact = [1] * N
for i in range(2, N):
    fact[i] = fact[i-1] * i % MOD
inv_fact[-1] = pow(fact[-1], MOD-2, MOD)
for i in reversed(range(1, N-1)):
    inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

def comb(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n-r] % MOD

# Number of paths = comb(H+W-2, H-1)
# For each cell (h,w), number of paths passing through it:
# = comb(h+w-2, h-1) * comb((H - h) + (W - w), H - h)
# 0-based indexing: h,w from 0
# so paths_through[h][w] = comb(h+w, h) * comb((H-1 - h)+(W-1 - w), H-1 - h)

paths_through = [0]*(H*W)
for h in range(H):
    for w in range(W):
        c1 = comb(h + w, h)
        c2 = comb((H - 1 - h) + (W - 1 - w), H - 1 - h)
        paths_through[h*W + w] = c1 * c2 % MOD

# Initial total sum of f(P)
# sum over all paths P of product of A_{h,w} on P
# = sum over all cells of A[h][w] * paths_through[h][w]
total = 0
for h in range(H):
    for w in range(W):
        total += A[h][w] * paths_through[h*W + w]
total %= MOD

# Current position of Takahashi
cur_h, cur_w = sh, sw

for _ in range(Q):
    d, a = input().split()
    a = int(a)
    # Move Takahashi
    if d == 'L':
        cur_w -= 1
    elif d == 'R':
        cur_w += 1
    elif d == 'U':
        cur_h -= 1
    else:  # 'D'
        cur_h += 1

    idx = cur_h * W + cur_w
    old_val = A[cur_h][cur_w]
    A[cur_h][cur_w] = a

    # Update total
    total -= old_val * paths_through[idx]
    total += a * paths_through[idx]
    total %= MOD

    print(total)