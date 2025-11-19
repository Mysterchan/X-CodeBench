MOD = 998244353

def solve():
    H, W, K = map(int, input().split())
    
    # Total number of walls
    # Horizontal walls: H-1 rows, each with W walls
    # Vertical walls: H rows, each with W-1 walls
    total_walls = (H - 1) * W + H * (W - 1)
    
    # Minimum walls needed to connect top-left to bottom-right
    min_walls = H + W - 2
    
    # If K < min_walls, impossible to connect
    if K < min_walls:
        print(0)
        return
    
    # If K > total_walls, impossible
    if K > total_walls:
        print(0)
        return
    
    # Precompute factorials and inverse factorials
    max_n = total_walls + 1
    fact = [1] * max_n
    for i in range(1, max_n):
        fact[i] = fact[i-1] * i % MOD
    
    inv_fact = [1] * max_n
    inv_fact[max_n - 1] = pow(fact[max_n - 1], MOD - 2, MOD)
    for i in range(max_n - 2, -1, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
    
    def comb(n, r):
        if r < 0 or r > n:
            return 0
        return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD
    
    # Number of paths from top-left to bottom-right using exactly min_walls walls
    num_paths = comb(H + W - 2, H - 1)
    
    # Extra walls we can choose
    extra = K - min_walls
    
    # Number of walls not on any shortest path
    walls_not_on_path = total_walls - min_walls
    
    # Answer: num_paths * C(walls_not_on_path, extra)
    answer = num_paths * comb(walls_not_on_path, extra) % MOD
    
    print(answer)

T = int(input())
for _ in range(T):
    solve()