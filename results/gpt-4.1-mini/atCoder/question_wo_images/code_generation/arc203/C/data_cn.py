import sys
input = sys.stdin.readline

MOD = 998244353

# Precompute factorials and inverse factorials for combinations up to max_n
max_n = 400000  # max H+W from constraints
fact = [1] * (max_n + 1)
inv_fact = [1] * (max_n + 1)

for i in range(2, max_n + 1):
    fact[i] = fact[i-1] * i % MOD

# Fermat's little theorem for inverse factorial
inv_fact[max_n] = pow(fact[max_n], MOD-2, MOD)
for i in range(max_n-1, 0, -1):
    inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

def comb(n, r):
    if r > n or r < 0:
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n-r] % MOD

T = int(input())
for _ in range(T):
    H, W, K = map(int, input().split())
    total_walls = 2 * H * W - H - W
    # Minimum walls to remove to connect top-left to bottom-right:
    # The shortest path length is (H-1)+(W-1) edges = H+W-2 edges
    # So minimal walls to remove = H+W-2
    min_remove = H + W - 2

    # If K < min_remove, no way to connect start to end
    if K < min_remove:
        print(0)
        continue

    # If K > total_walls, no such selection
    if K > total_walls:
        print(0)
        continue

    # The number of ways to choose K walls so that the path is connected from start to end
    # equals the number of ways to choose K walls that include at least one shortest path.
    # The shortest path edges are fixed: length = min_remove
    # We must choose all edges of a shortest path (H+W-2 edges) plus any other walls to reach K.

    # Number of ways = number of ways to choose K walls that include the shortest path edges
    # = number of ways to choose (K - min_remove) walls from (total_walls - min_remove) walls
    ans = comb(total_walls - min_remove, K - min_remove)
    print(ans % MOD)