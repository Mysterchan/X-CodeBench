import sys
sys.setrecursionlimit(1 << 25)
input = sys.stdin.readline

MOD = 998244353

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

Q, sh, sw = map(int, input().split())
sh -= 1
sw -= 1

# Because H*W <= 200000, we can store the grid as a flat array
# and precompute factorials and inverse factorials for combinations.

N = H + W - 2  # total steps in path (excluding start)
max_n = N

# Precompute factorials and inverse factorials for combinations
fact = [1] * (max_n + 2)
inv_fact = [1] * (max_n + 2)
for i in range(1, max_n + 2):
    fact[i] = fact[i - 1] * i % MOD

inv_fact[max_n + 1] = pow(fact[max_n + 1], MOD - 2, MOD)
for i in range(max_n, 0, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

def comb(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

# The number of paths from (1,1) to (h,w) is comb(h-1 + w-1, h-1)
# The number of paths from (h,w) to (H,W) is comb(H - h + W - w, H - h)

# The sum over all paths of product of A_{h,w} can be expressed as:
# sum over all cells (h,w) of A[h][w] * ways_from_start[h][w] * ways_to_end[h][w]

# Precompute ways_from_start and ways_to_end for each cell
ways_from_start = [0] * (H * W)
ways_to_end = [0] * (H * W)

def idx(h, w):
    return h * W + w

for h in range(H):
    for w in range(W):
        ways_from_start[idx(h, w)] = comb(h + w, h)
        ways_to_end[idx(h, w)] = comb((H - 1 - h) + (W - 1 - w), H - 1 - h)

# Compute initial answer
ans = 0
for h in range(H):
    for w in range(W):
        val = A[h][w]
        if val != 0:
            ans += val * ways_from_start[idx(h, w)] % MOD * ways_to_end[idx(h, w)] % MOD
ans %= MOD

# Process queries
x, y = sh, sw

for _ in range(Q):
    d, p = input().split()
    p = int(p)
    if d == 'L':
        y -= 1
    elif d == 'R':
        y += 1
    elif d == 'U':
        x -= 1
    else:  # d == 'D'
        x += 1

    pos = idx(x, y)
    old_val = A[x][y]
    A[x][y] = p

    # Update answer
    diff = (p - old_val) % MOD
    add = diff * ways_from_start[pos] % MOD * ways_to_end[pos] % MOD
    ans = (ans + add) % MOD

    print(ans)